
from pydantic import BaseModel

class FileObject(BaseModel):
    name: str
    size: str
    content_type:str