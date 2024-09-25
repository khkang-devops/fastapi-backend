
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