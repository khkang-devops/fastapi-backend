from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, UpdateSample
from app.common.utils.db_util import db_util
from sqlalchemy.ext.asyncio import async_scoped_session

# ----------------------------------------------------------------------
# get sample_info
# ----------------------------------------------------------------------
async def get_sample_info(
    searchSample: SearchSample,
    session: async_scoped_session = None
):
    # sql
    sql = f"""
        -- get_sample_info
        select
            sp_id,
            sp_nm,
            crt_usr,
            to_char(crt_dttm, 'YYYY-MM-DD HH24:MI:SS') as crt_dttm
        from
            tb_sample
        where
            sp_id = :sp_id
    """

    # parameter
    param = {
        "sp_id": searchSample.sp_id
    }

    # execute sql
    return await db_util.select_one(sql, param, session)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
async def get_sample_list(
    session: async_scoped_session = None
):
    # sql
    sql = f"""
        -- get_sample_list
        select
            sp_id,
            sp_nm,
            crt_usr,
            to_char(crt_dttm, 'YYYY-MM-DD HH24:MI:SS') as crt_dttm
        from
            tb_sample
        order by
            crt_dttm desc
    """

    # parameter
    param = {}

    # execute sql
    return await db_util.select_list(sql, param, session)

# ----------------------------------------------------------------------
# insert sample
# ----------------------------------------------------------------------
async def insert_sample(
    insertSample: InsertSample,
    session: async_scoped_session = None
):
    # sql
    sql = f"""
        -- insert_sample
        insert into tb_sample (
            sp_id,
            sp_nm,
            crt_usr,
            crt_dttm
        ) values (
            :sp_id,
            :sp_nm,
            :crt_usr,
            now() at time zone 'Asia/Seoul'
        )
    """

    # parameter
    param = {
        "sp_id": insertSample.sp_id,
        "sp_nm": insertSample.sp_nm,
        "crt_usr": insertSample.crt_usr
    }

    # execute sql
    return await db_util.insert(sql, param, session)

# ----------------------------------------------------------------------
# update sample
# ----------------------------------------------------------------------
async def update_sample(
    updateSample: UpdateSample,
    session: async_scoped_session = None
):
    # sql
    sql = f"""
        -- update_sample
        update
            tb_sample
        set
            sp_nm = :sp_nm,
            crt_usr = :crt_usr
        where
            sp_id = :sp_id
    """

    # parameter
    param = {
        "sp_id": updateSample.sp_id,
        "sp_nm": updateSample.sp_nm,
        "crt_usr": updateSample.crt_usr
    }

    # execute sql
    return await db_util.update(sql, param, session)

# ----------------------------------------------------------------------
# delete sample
# ----------------------------------------------------------------------
async def delete_sample(
    deleteSample: DeleteSample,
    session: async_scoped_session = None
):
    # sql
    sql = f"""
        -- delete_sample
        delete from
            tb_sample
        where
            sp_id = :sp_id
    """

    # parameter
    param = {
        "sp_id": deleteSample.sp_id
    }

    # execute sql
    return await db_util.delete(sql, param, session)