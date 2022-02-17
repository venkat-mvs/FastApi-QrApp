from logging import Logger
from fastapi import FastAPI

from API.QRApp import QRApp

def configure(app:FastAPI, log: Logger):

    @app.on_event("startup")
    async def on_start():

        log.info("Configuring Server...")
        qrapp = QRApp(log)
        log.info(f"Adding {QRApp.__name__} Routers... ")
        app.include_router(qrapp,prefix="/api")
        log.info(f"Adding {QRApp.__name__} Routers...done")
        log.info("Configuring Server...done")



    @app.on_event("shutdown")
    async def on_shutdown():
        
        log.info("Server shutdown")


