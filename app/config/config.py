
import os
from pydantic import BaseSettings

# environ
environ = os.environ.get("DEVEL_ENV", "LOCAL")

# config_file
config_file = {
    "LOCAL": "app/config/.env_local",
    "DEV": "app/config/.env_dev",
    "STG": "app/config/.env_stg",
    "PRD": "app/config/.env_prd",
}

# api_response
api_response = {
    200: {"status": 200, "code": "S00000", "message": "요청 성공하였습니다."},
    201: {"status": 201, "code": "S00001", "message": "요청 등록되었습니다."},
    203: {"status": 203, "code": "S00002", "message": "요청자의 권한이 맞지 않습니다."},
    400: {"status": 400, "code": "F00000", "message": "요청 형식이 맞지 않습니다"},
    401: {"status": 401, "code": "F00001", "message": "시스템 접근 권한이 없습니다"},
    404: {"status": 404, "code": "E00005", "message": "요청한 정보가 존재하지 않습니다."},
    406: {
        "status": 406,
        "code": "E00006",
        "message": "Not Acceptable, refer to description.",
        "description": None,
    },
    409: {"status": 409, "code": "E00005", "message": "이미 요청한 정보가 있습니다"},
    500: {"status": 500, "code": "E00000", "message": "시스템 오류입니다", "description": None},
}

# APIConfig
class APIConfig(BaseSettings):
    svc_cd: str = os.environ.get("svc_cd")
    log_level: str = os.environ.get("log_level")

    class Config:
        case_sensitive = True
        env_file = config_file[environ]
        env_file_encoding = "utf-8"

# ReadDatabaseConfig
class ReadDatabaseConfig(BaseSettings):
    read_charset: str = os.environ.get("read_charset")
    read_driver: str = os.environ.get("read_driver")
    read_user: str = os.environ.get("read_user")
    read_passwd: str = os.environ.get("read_passwd")
    read_host: str = os.environ.get("read_host")
    read_port: str = os.environ.get("read_port")
    read_database: str = os.environ.get("read_database")
    read_pool_size: int = os.environ.get("read_pool_size")
    read_pool_recycle: int = os.environ.get("read_pool_recycle")
    read_max_overflow: int = os.environ.get("read_max_overflow")
    read_pool_timeout: int = os.environ.get("read_pool_timeout")

    class Config:
        case_sensitive = True
        env_file = config_file[environ]
        env_file_encoding = "utf-8"

# WriteDatabaseConfig
class WriteDatabaseConfig(BaseSettings):
    write_charset: str = os.environ.get("write_charset")
    write_driver: str = os.environ.get("write_driver")
    write_user: str = os.environ.get("write_user")
    write_passwd: str = os.environ.get("write_passwd")
    write_host: str = os.environ.get("write_host")
    write_port: str = os.environ.get("write_port")
    write_database: str = os.environ.get("write_database")
    write_pool_size: int = os.environ.get("write_pool_size")
    write_pool_recycle: int = os.environ.get("write_pool_recycle")
    write_max_overflow: int = os.environ.get("write_max_overflow")
    write_pool_timeout: int = os.environ.get("write_pool_timeout")

    class Config:
        case_sensitive = True
        env_file = config_file[environ]
        env_file_encoding = "utf-8"