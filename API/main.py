from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from API import QRApp

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
         

@app.on_event("startup")
async def on_start():
    #import webbrowser
    #created = webbrowser.open_new_tab("http://localhost:8000/swagger")
    app.include_router(QRApp.router,prefix="/api")


@app.on_event("shutdown")
async def on_shutdown():
    print("ended..")

