from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, UpdateSample
from app.common.utils.db_util import write_db, read_db
from app.common.utils.log_util import get_logger

# logger
logger = get_logger(__name__)

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
    return await read_db.select_one(sql, param)

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

    # parameter
    param = {}

    # execute sql
    return await read_db.select_list(sql, param)

# ----------------------------------------------------------------------
# insert sample
# ----------------------------------------------------------------------
async def insert_sample(
    insertSample: InsertSample
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
    await write_db.insert(sql, param)

# ----------------------------------------------------------------------
# update sample
# ----------------------------------------------------------------------
async def update_sample(
    updateSample: UpdateSample
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
    await write_db.update(sql, param)

# ----------------------------------------------------------------------
# delete sample
# ----------------------------------------------------------------------
async def delete_sample(
    deleteSample: DeleteSample
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
    await write_db.delete(sql, param)