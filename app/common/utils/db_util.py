from app.common.utils.common_util import decrypt, get_dict, get_list
from app.common.utils.log_util import get_logger
from app.config.config import api_response, ReadDatabaseConfig, WriteDatabaseConfig
from asyncio import current_task
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

# logger
logger = get_logger(__name__)

# read_config
read_config = ReadDatabaseConfig()

# write_config
write_config = WriteDatabaseConfig()

# tag
tag = b'^\x07\x8a.\xa9\xd7\xdc\xfb\x88fiBa}(\x1d'

# ------------------------------------------------------------------------------------------
# read database
# ------------------------------------------------------------------------------------------
read_connection_string = "{driver}://{user}:{passwd}@{host}:{port}/{database}".format(
    driver=read_config.read_driver,
    user=read_config.read_user,
    passwd=decrypt(read_config.read_passwd, tag), # pycryptodome.ipynb 암복호화 소스 참조
    host=read_config.read_host,
    port=read_config.read_port,
    database=read_config.read_database
)

# create async engine
read_engine = create_async_engine(
    read_connection_string,
    encoding=read_config.read_charset,
    poolclass=QueuePool,
    pool_size=read_config.read_pool_size,
    pool_recycle=read_config.read_pool_recycle,
    max_overflow=read_config.read_max_overflow,
    pool_timeout=read_config.read_pool_timeout
)

# create async session
read_async_session_factory = sessionmaker(read_engine, class_=AsyncSession)
read_session = async_scoped_session(read_async_session_factory, scopefunc=current_task)

# ------------------------------------------------------------------------------------------
# write database
# ------------------------------------------------------------------------------------------
write_connection_string = "{driver}://{user}:{passwd}@{host}:{port}/{database}".format(
    driver=write_config.write_driver,
    user=write_config.write_user,
    passwd=decrypt(write_config.write_passwd, tag), # pycryptodome.ipynb 암복호화 소스 참조
    host=write_config.write_host,
    port=write_config.write_port,
    database=write_config.write_database
)

# create async engine
write_engine = create_async_engine(
    write_connection_string,
    encoding=write_config.write_charset,
    poolclass=QueuePool,
    pool_size=write_config.write_pool_size,
    pool_recycle=write_config.write_pool_recycle,
    max_overflow=write_config.write_max_overflow,
    pool_timeout=write_config.write_pool_timeout
)

# create async session
write_async_session_factory = sessionmaker(write_engine, class_=AsyncSession)
write_session = async_scoped_session(write_async_session_factory, scopefunc=current_task)

# ------------------------------------------------------------------------------------------
# database util
# ------------------------------------------------------------------------------------------
class DatabaseUtil:
    # get_session
    async def get_session(
        self,
        type: str = ""
    ):
        session = None

        if type == "read":
            session = read_session()
        else:
            session = write_session()

        try:
            return session
        finally:
            await session.close()

    # select_count
    async def select_count(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        # execute sql
        try:
            result = await session.execute(sql, param)
            return result.scalar()
        except Exception as ex:
            logger.error(repr(ex))
            return 0

    # select_one
    async def select_one(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        # execute sql
        try:
            return get_dict(await session.execute(sql, param))
        except Exception as ex:
            logger.error(repr(ex))
            return None

    # select_list
    async def select_list(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        # execute sql
        try:
            return get_list(await session.execute(sql, param))
        except Exception as ex:
            logger.error(repr(ex))
            return None

    # insert
    async def insert(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        try:
            # execute sql
            await session.execute(sql, param)

            # return
            status_code = status.HTTP_201_CREATED
            response_body = api_response.get(status_code)
            return JSONResponse(status_code=status_code, content=response_body)
        except Exception as ex:
            logger.error(repr(ex))
            raise Exception(ex)

    # update
    async def update(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        try:
            # execute sql
            await session.execute(sql, param)

            # return
            status_code = status.HTTP_200_OK
            response_body = api_response.get(status_code)
            return JSONResponse(status_code=status_code, content=response_body)
        except Exception as ex:
            logger.error(repr(ex))
            raise Exception(ex)

    # delete
    async def delete(
        self,
        sql: str = "",
        param: dict = {},
        session: async_scoped_session = None
    ):
        # log
        logger.debug(param)
        logger.debug(sql)

        try:
            # execute sql
            await session.execute(sql, param)

            # return
            status_code = status.HTTP_200_OK
            response_body = api_response.get(status_code)
            return JSONResponse(status_code=status_code, content=response_body)
        except Exception as ex:
            logger.error(repr(ex))
            raise Exception(ex)

# ------------------------------------------------------------------------------------------
# create db_util
# ------------------------------------------------------------------------------------------
db_util = DatabaseUtil()