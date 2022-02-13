import io
from logging import Logger
from fastapi.datastructures import UploadFile
from fastapi.params import Depends, File, Query
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRoute, APIRouter

''' API level imports '''
from API.settings import ENV
from API.logger import log

''' APP level imports '''
from .QRGenerator import QRGenerator
from .services import QRGeneratorService
from .models import FileObject

router = APIRouter(
    prefix= "/qrcode",
    tags = ["QR Generator"]
)

@router.get("/", name="App Details")
def Init():
    return {"QRCodeGeneratorAPI":True}

@router.get("/generate", responses= {
            200:{
                "content":"image/png"
            }
        },
        name="QR code Generator")
async def q_r_code_generator(data:str= Query(..., max_length=150),
                             service:QRGenerator = Depends(QRGeneratorService)):
    '''
    Takes input as text and convert them into a QRcode png image
    '''
    log.info(f"QR Code Generator: {data}")
    env = ENV.values()
    image_bytes = await service.generate(data)

    return StreamingResponse(io.BytesIO(image_bytes), status_code=200, media_type="image/png")
    

@router.post("/get-file-details", name="Get File Details")
async def image_echo(file:UploadFile= File(...)):

    file_name:str = file.filename
    file_size:str = str(file.spool_max_size)+" bytes"
    file_type:str = file.content_type

    return FileObject(name = file_name, size=file_size, content_type=file_type)  

    # return StreamingResponse(io.BytesIO(None),status_code=200,media_type="image/png")