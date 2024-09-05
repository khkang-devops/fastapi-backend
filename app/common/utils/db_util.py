from app.common.utils.common_util import decrypt
from app.common.utils.log_util import get_logger
from app.config.config import api_response, ReadDatabaseConfig, WriteDatabaseConfig
from asyncio import current_task
from decimal import Decimal
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
# get write db
# ------------------------------------------------------------------------------------------
async def get_write_db():
    db = write_session()
    try:
        yield db
    finally:
        await db.close()

# ------------------------------------------------------------------------------------------
# read db util
# ------------------------------------------------------------------------------------------
async def select_read_db():
    # log
    logger.debug("select 1")

    # execute sql
    async with read_session() as session:
        try:
            row = await session.execute("select 1")
            result = dict(row.fetchone())
            return result
        except Exception as ex:
            logger.error(repr(ex))
            return None

async def select_count(
    sql: str = "",
    param: dict = {}
):
    # log
    logger.debug(param)
    logger.debug(sql)

    # execute sql
    async with read_session() as session:
        try:
            result = await session.execute(sql, param)
            return result.scalar()
        except Exception as ex:
            logger.error(repr(ex))
            return 0

async def select_one(
    sql: str = "",
    param: dict = {}
):
    # log
    logger.debug(param)
    logger.debug(sql)

    # execute sql
    async with read_session() as session:
        try:
            result = await session.execute(sql, param)
            row = result.first()
            row_dict = {}

            # row to dict
            if (row is not None):
                for column in row._fields:
                    # decimal to float (because type_error)
                    if isinstance(getattr(row, column), Decimal):
                        row_dict[column] = float(getattr(row, column))
                    else:
                        row_dict[column] = getattr(row, column)

            return row_dict
        except Exception as ex:
            logger.error(repr(ex))
            return None

async def select_list(
    sql: str = "",
    param: dict = {}
):
    # log
    logger.debug(param)
    logger.debug(sql)

    # execute sql
    async with read_session() as session:
        try:
            result = []
            rows = await session.execute(sql, param)

            # row to dict
            for row in rows:
                row_dict = {}
                for column in row._fields:
                    # decimal to float (because type_error)
                    if isinstance(getattr(row, column), Decimal):
                        row_dict[column] = float(getattr(row, column))
                    else:
                        row_dict[column] = getattr(row, column)
                result.append(row_dict)

            return result
        except Exception as ex:
            logger.error(repr(ex))
            return None

# ------------------------------------------------------------------------------------------
# write db util
# ------------------------------------------------------------------------------------------
async def select_write_db():
    # log
    logger.debug("select 1")

    # execute sql
    async with write_session() as session:
        try:
            row = await session.execute("select 1")
            result = dict(row.fetchone())
            return result
        except Exception as ex:
            logger.error(repr(ex))
            return None

async def insert(
    sql: str = "",
    param: dict = {},
    session: async_scoped_session = None
):
    # log
    logger.debug(param)
    logger.debug(sql)

    try:
        # not transaction
        if session is None:
            async with write_session() as session:
                await session.execute(sql, param)
                await session.commit()
        # transaction
        else:
            await session.execute(sql, param)

        # return
        status_code = status.HTTP_201_CREATED
        response_body = api_response.get(status_code)
        return JSONResponse(status_code=status_code, content=response_body)
    except Exception as ex:
        logger.error(repr(ex))
        raise Exception(ex)

async def update(
    sql: str = "",
    param: dict = {},
    session: async_scoped_session = None
):
    # log
    logger.debug(param)
    logger.debug(sql)

    try:
        # not transaction
        if session is None:
            async with write_session() as session:
                await session.execute(sql, param)
                await session.commit()
        # transaction
        else:
            await session.execute(sql, param)

        # return
        status_code = status.HTTP_201_CREATED
        response_body = api_response.get(status_code)
        return JSONResponse(status_code=status_code, content=response_body)
    except Exception as ex:
        logger.error(repr(ex))
        raise Exception(ex)

async def delete(
    sql: str = "",
    param: dict = {},
    session: async_scoped_session = None
):
    # log
    logger.debug(param)
    logger.debug(sql)

    try:
        # not transaction
        if session is None:
            async with write_session() as session:
                await session.execute(sql, param)
                await session.commit()
        # transaction
        else:
            await session.execute(sql, param)

        # return
        status_code = status.HTTP_200_OK
        response_body = api_response.get(status_code)
        return JSONResponse(status_code=status_code, content=response_body)
    except Exception as ex:
        logger.error(repr(ex))
        raise Exception(ex)