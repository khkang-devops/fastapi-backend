from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, UpdateSample
from app.common.utils.db_util import delete, insert, select_list, select_one, update
from sqlalchemy.ext.asyncio import async_scoped_session

# ----------------------------------------------------------------------
# get sample_info
# ----------------------------------------------------------------------
async def get_sample_info(
    searchSample: SearchSample
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
    return await select_one(sql, param)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
async def get_sample_list():
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

    # execute sql
    return await select_list(sql)

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
    return await insert(sql, param, session)

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
    return await update(sql, param, session)

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
    return await delete(sql, param, session)