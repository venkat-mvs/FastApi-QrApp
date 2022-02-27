from logging import Logger
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

''' API level imports '''
import middleware
import utils
from settings import ENV, Env

''' APP level imports '''
from QRApp import QRApp

def configure(app:FastAPI, log: Logger, settings:Env = Depends(ENV.values)):
    ''' 
    Configuring API
        - Adding Routers
        - Adding Middelwares
        - Adding Exception handlers
        - Can be used to add other important things
    '''

    @app.on_event("startup")
    async def on_start():

        log.info("Configuring Server...")

        origins = [
            "*"
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["GET","POST"],
            allow_headers=["*"],
        )
        
        middleware.add_request_logger(app, log=log)

        utils.add_root_redirecter_for(app, to="api/docs")

        utils.add_exception_handlers(app, log=log)

        qrapp = QRApp(log)
        log.info(f"Adding {QRApp.__name__} Routers... ")
        app.include_router(qrapp,prefix="/api")
        log.info(f"Adding {QRApp.__name__} Routers...done")


        log.info("Configuring Server...done")



    @app.on_event("shutdown")
    async def on_shutdown():
        
        log.info("Server shutdown")


