import asyncio
import logging
import os
import sys
from contextlib import asynccontextmanager
from typing import Any, Dict, Union

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from cogito.api.handlers import (
    health_check_handler,
    metrics_handler,
)
from cogito.api.responses import ErrorResponse
from cogito.core.config import ConfigFile
from cogito.core.exceptioin_handlers import (
    too_many_requests_exception_handler,
    validation_exception_handler,
)
from cogito.core.exceptions import (
    ConfigFileNotFoundError,
    NoThreadsAvailableError,
    SetupError,
)
from cogito.core.logging import get_logger
from cogito.core.models import BasePredictor
from cogito.core.utils import (
    create_routes_semaphores,
    get_predictor_handler_return_type,
    load_predictor,
    wrap_handler,
    readiness_context,
)


class Application:
    _logger: logging.Logger
    ready: bool

    def __init__(
        self,
        config_file_path: str = ".",
        logger: Union[Any, logging.Logger] = None,
    ):

        self._logger = logger or Application._get_default_logger()

        try:
            self.config = ConfigFile.load_from_file(
                os.path.join(f"{config_file_path}/cogito.yaml")
            )
        except ConfigFileNotFoundError as e:
            self._logger.warning(
                "config file does not exist. Using default configuration.",
                extra={"error": str(e), "config_file_path": config_file_path},
            )
            self.config = ConfigFile.default()

        if self.config.cogito.server.cache_dir:
            os.environ["HF_HOME"] = self.config.cogito.server.cache_dir
            os.environ["COGITO_HOME"] = self.config.cogito.server.cache_dir
        else:
            os.environ["HF_HOME"] = os.path.expanduser("/.cogito/models")
            os.environ["COGITO_HOME"] = os.path.expanduser("/.cogito/models")

        @asynccontextmanager
        async def lifespan(app: FastAPI):

            try:
                await self.setup(app)
            except SetupError as e:
                self._logger.critical(
                    "Unable to start application",
                    extra={"error": e},
                )
                sys.exit(1)

            with readiness_context(self.config.cogito.server.readiness_file):
                yield

        self.app = FastAPI(
            title=self.config.cogito.server.name,
            version=self.config.cogito.server.version,
            description=self.config.cogito.server.description,
            access_log=self.config.cogito.server.fastapi.access_log,
            debug=self.config.cogito.server.fastapi.debug,
            lifespan=lifespan,
        )

        # FastAPIInstrumentor.instrument_app(self.app, excluded_urls=",".join(
        #        ["/health-check", "/metrics", "/docs", "/openapi.json"]))

        self.app.logger = self._logger

        self._set_default_routes()

        map_route_to_model: Dict[str, str] = {}
        self.map_model_to_instance: Dict[str, BasePredictor] = {}
        semaphores = create_routes_semaphores(self.config.cogito)

        route = self.config.cogito.server.route

        self._logger.info("Adding route", extra={"route": route})
        map_route_to_model[route.path] = route.predictor
        if route.predictor not in self.map_model_to_instance:
            predictor = load_predictor(route.predictor)
            self.map_model_to_instance[route.predictor] = predictor
        else:
            self._logger.info(
                "Predictor class already loaded",
                extra={"predictor": route.predictor},
            )

        model = self.map_model_to_instance.get(route.predictor)
        response_model = get_predictor_handler_return_type(model)

        handler = wrap_handler(
            descriptor=route.predictor,
            original_handler=getattr(
                self.map_model_to_instance.get(route.predictor), "predict"
            ),
            semaphore=semaphores[route.predictor],
            response_model=response_model,
        )

        self.app.add_api_route(
            route.path,
            handler,
            methods=["POST"],
            name=route.name,
            description=route.description,
            tags=route.tags,
            response_model=response_model,
            responses={500: {"model": ErrorResponse}},
        )

        self.app.add_exception_handler(
            RequestValidationError, validation_exception_handler
        )
        self.app.add_exception_handler(
            NoThreadsAvailableError, too_many_requests_exception_handler
        )

    def _set_default_routes(self) -> None:
        """Include default routes"""
        self.app.add_api_route(
            "/health-check",
            health_check_handler,
            methods=["GET"],
            name="health_check",
            description="Health check endpoint",
            tags=["health"],
        )

        self.app.add_api_route(
            "/metrics",
            metrics_handler,
            methods=["GET"],
            name="metrics",
            description="Metrics endpoint",
            tags=["metrics"],
        )

    async def setup(self, app: FastAPI):
        self._logger.info("Setting up application", extra={})
        for predictor in self.map_model_to_instance.values():
            try:
                self._logger.debug(
                    "Setting up predictor",
                    extra={"predictor": predictor.__class__.__name__},
                )
                # if is courutine
                if asyncio.iscoroutinefunction(predictor.setup):
                    await predictor.setup()
                else:
                    predictor.setup()
            except Exception as e:
                self._logger.critical(
                    "Unable to setting up predictor",
                    extra={"predictor": predictor.__class__.__name__, "error": e},
                )
                raise SetupError(predictor.__class__.__name__, e)

    def run(self):
        uvicorn.run(
            self.app,
            host=self.config.cogito.server.fastapi.host,
            port=self.config.cogito.server.fastapi.port,
        )

    @classmethod
    def _get_default_logger(cls):
        return get_logger("cogito.app")
