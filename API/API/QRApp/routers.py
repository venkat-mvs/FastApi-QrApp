import io
from logging import Logger
from typing import Dict
from dotenv import Any
from fastapi.datastructures import UploadFile
from fastapi.params import Depends, File, Query
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRoute, APIRouter

''' APP level imports '''
from .QRGenerator import QRGenerator
from .services import QRGeneratorService
from .models import FileObject


def QRApp(log:Logger) -> APIRouter:
    
    router = APIRouter(
        prefix= "/qrcode",
        tags = ["QR Generator"]
    )

    @router.get("/", name="App Details", include_in_schema=False)
    async def Init():
        return {"QRGenerator":True}

    @router.get("/generate", responses= {
                200:{"content":{"image/png":{}}}
            },
            name="QR code Generator")
    async def q_r_code_generator(data:str= Query(..., max_length=150),
                                service:QRGenerator = Depends(QRGeneratorService)):
        '''
        Takes input as text and convert them into a QRcode png image
        '''
        log.debug(f"QR Code Generator: {data}")
        image_bytes = await service.generate(data)

        return StreamingResponse(io.BytesIO(image_bytes), status_code=200, media_type="image/png")
        

    @router.post("/file-details", name="Get File Details")
    async def image_echo(file:UploadFile= File(...)):

        file_name:str = file.filename
        file_size:str = str(file.spool_max_size)+" bytes"
        file_type:str = file.content_type

        return FileObject(name = file_name, size=file_size, content_type=file_type)  

    @router.post("/logo-qrcode", name="Get QrCode having logo", 
                responses={
                    200:{"content":{"image/png":{} }},
                    400:{"content":{"application/json":{}}}
                    })
    async def qrcode_logoed(file:UploadFile = File(...),
                            data:str=Query(..., max_length=150), 
                            service:QRGenerator = Depends(QRGeneratorService)) -> StreamingResponse:

        if file.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
            raise ValueError(f"File type: {file.content_type} not allowed")
        
        response = await file.read()
        serviceResponse = await service.generate_with_logo(data,response)
        return StreamingResponse(io.BytesIO(serviceResponse), status_code=200, media_type="image/png")

    return router