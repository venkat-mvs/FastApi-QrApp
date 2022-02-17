''' Framework Level Modules '''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import uvicorn

''' API level modules '''
import API.logger as logger 
import API.startup as startup
import API.middleware as middleware

HOST = "localhost"
PORT = 8000
API_TITLE = "QRCode Generator"
API_VERSION = "0.1.1"

def main():

    app = FastAPI(
                title=API_TITLE,
                version=API_VERSION,
                docs_url="/api/swagger",
                redoc_url="/api/docs"
        )    

    origins = [
        "http://0.0.0.0:8000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET","POST"],
        allow_headers=["*"],
    )
    
    @app.get("/", include_in_schema=False)
    def redirect():
        return RedirectResponse("api/docs")
    
    middleware.add_request_logger(app, log=logger.log)

    startup.configure(app, log=logger.log)

    return app

app = main()

if __name__ == "__main__":
    logger.log.info(f"Starting Server at http://{HOST}:{PORT}")
    uvicorn.run("main:app",
                host = HOST,
                port = PORT,
                reload = True,
                use_colors = True,
                reload_includes= ["*","./QRApp"],
                reload_excludes = ["*/__pycache__"],
                server_header = True,
                log_level = "debug"
    )