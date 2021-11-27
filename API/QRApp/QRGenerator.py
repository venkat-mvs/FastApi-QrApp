import io
from qrcode import QRCode
import qrcode

class QRGenerator():

    def __init__(self) -> None:
        self.qr:QRCode = qrcode.QRCode(
            version= 1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=4,
        )

    def __clear(self) -> None:
        self.qr.clear()

    async def generate(self, data:str, format:str="PNG") -> bytes:
        self.__clear()

        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill='black', back_color='white')
        
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=format)

        return img_byte_arr.getvalue()