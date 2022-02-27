import io
from qrcode import QRCode
from PIL import Image
import qrcode

class QRGenerator():

    def __init__(self) -> None:
        self.qr:QRCode = qrcode.QRCode(
            version= 1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5
        )

    def __clear(self) -> None:
        self.qr.clear()

    def __generate(self, data: str) -> Image.Image:
        self.__clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)

        return self.qr.make_image(fill='black', back_color='white')

    def _imageToBytes(self, img:Image.Image, format:str='PNG'):
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=format)

        return img_byte_arr.getvalue()

    async def generate(self, data:str, format:str="PNG") -> bytes:
        
        img = self.__generate(data)
        
        return self._imageToBytes(img,format=format)

    async def generate_with_logo(self, data:str, logo:bytes, format:str="PNG") -> bytes:
        

        img = self.__generate(data).convert('RGB')

        width,height = img.size

        logo_img = Image.open(io.BytesIO(logo)).resize((width//8,height//8))

        pos = ((img.size[0] - logo_img.size[0]) // 2, (img.size[1] - logo_img.size[1]) // 2)

        img.paste(logo_img, pos)

        return self._imageToBytes(img,format=format)
