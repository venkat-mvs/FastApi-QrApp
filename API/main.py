''' Framework Level Modules '''
from imp import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

''' API level modules '''
import API.logger as logger 
import API.startup as startup
import API.middleware as middleware

def main():
    app = FastAPI(title="QRCode Generator",
                version="0.1.1",
                docs_url="/api/swagger")    

    origins = [
        "http://0.0.0.0:8000",
        "http://localhost:8080",
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    middleware.add_request_logger(app, log=logger.log)

    startup.configure(app, log=logger.log)

    return app

app = main()

if __name__ == "__main__":
    uvicorn.run("main:app",
                host = "0.0.0.0",
                port = 80,
                reload = True,
                use_colors = True,
                reload_includes= ["./*","./QRApp"],
                reload_excludes = ["*/__pycache__"],
                server_header = True,
                log_level = "critical"
                )