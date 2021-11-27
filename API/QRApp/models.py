from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field


class FileObject(BaseModel):
    name: str
    size: str
    content_type:str