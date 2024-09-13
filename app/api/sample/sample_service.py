from app.api.sample import sample_dao
from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, TransactionSample, UpdateSample
from app.common.utils.common_util import return_exception
from app.common.utils.log_util import get_logger

# logger
logger = get_logger(__name__)

# ----------------------------------------------------------------------
# get sample_info
# ----------------------------------------------------------------------
async def get_sample_info(
    searchSample: SearchSample,
    db_session: dict
):
    try:
        return await sample_dao.get_sample_info(searchSample, db_session["read"])
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
async def get_sample_list(
    db_session: dict
):
    try:
        return await sample_dao.get_sample_list(db_session["read"])
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# insert sample
# ----------------------------------------------------------------------
async def insert_sample(
    insertSample: InsertSample,
    db_session: dict
):
    try:
        return await sample_dao.insert_sample(insertSample, db_session["write"])
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# update sample
# ----------------------------------------------------------------------
async def update_sample(
    updateSample: UpdateSample,
    db_session: dict
):
    try:
        return await sample_dao.update_sample(updateSample, db_session["write"])
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# delete sample
# ----------------------------------------------------------------------
async def delete_sample(
    deleteSample: DeleteSample,
    db_session: dict
):
    try:
        return await sample_dao.delete_sample(deleteSample, db_session["write"])
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# transaction sample
# ----------------------------------------------------------------------
async def transaction_sample(
    transactionSample: TransactionSample,
    db_session: dict
):
    try:
        # delete
        deleteSample = DeleteSample()
        deleteSample.sp_id = transactionSample.sp_id
        await sample_dao.delete_sample(deleteSample, db_session["write"])

        # insert
        insertSample = InsertSample()
        insertSample.sp_id = transactionSample.sp_id
        insertSample.sp_nm = transactionSample.sp_nm
        insertSample.crt_usr = transactionSample.crt_usr
        response = await sample_dao.insert_sample(insertSample, db_session["write"])

        # return
        return response
    except Exception as ex:
        return return_exception(ex)