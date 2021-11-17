from fastapi import FastAPI


from API import QRApp

app = FastAPI(title="QRCode Generator",
              version="0.1.1",
              docs_url="/api/swagger")             

@app.on_event("startup")
async def on_start():
    #import webbrowser
    #created = webbrowser.open_new_tab("http://localhost:8000/swagger")
    # for application, endpoint, name in installed_apps
    # app.mount(path = endpoint, app=application, name=)
    app.include_router(QRApp.router,prefix="/api")

    # use_route_names_as_operation_ids(app)

@app.on_event("shutdown")
async def on_shutdown():
    print("ended..")

