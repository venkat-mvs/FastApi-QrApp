from logging import Logger
from fastapi import FastAPI

from API import QRApp


def configure(app:FastAPI, log: Logger):

    @app.on_event("startup")
    async def on_start():
        log.info(f"Adding {QRApp.NAME} Routers... ")
        app.include_router(QRApp.router,prefix="/api")
        log.info(f"Added {QRApp.NAME} Routers")



    @app.on_event("shutdown")
    async def on_shutdown():
        log.info("ended..")

