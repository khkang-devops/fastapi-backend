from pydantic import BaseModel

class InsertUserHistory(BaseModel):
    usr_id: str = "" # 사용자id
    usr_ip: str = "" # 사용자ip
    usr_dept: str = "" # 사용자부서
    usr_url: str = "" # 사용자접근url
    usr_param: str = "" # 사용자파라미터