from pydantic import BaseModel

class RequestName1(BaseModel):
    message: str

class RequestName2(BaseModel):
    response: str