from pydantic import BaseModel

class SearchSample(BaseModel):
    sp_id: str = ""

class InsertSample(BaseModel):
    sp_id: str = ""
    sp_nm: str = ""
    crt_usr: str = ""

class UpdateSample(BaseModel):
    sp_id: str = ""
    sp_nm: str = ""
    crt_usr: str = ""

class DeleteSample(BaseModel):
    sp_id: str = ""

class TransactionSample(BaseModel):
    sp_id: str = ""
    sp_nm: str = ""
    crt_usr: str = ""