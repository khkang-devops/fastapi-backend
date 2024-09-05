from app.api.sample import sample_service
from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, TransactionSample, UpdateSample
from app.common.utils.common_util import return_exception
from app.common.utils.db_util import get_write_db
from app.common.utils.log_util import get_logger
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import async_scoped_session

# logger
logger = get_logger(__name__)

# router
router = APIRouter()

# ----------------------------------------------------------------------
# get sample_info
# ----------------------------------------------------------------------
@router.post("/info")
async def get_sample_info(
    searchSample: SearchSample
):
    try:
        return await sample_service.get_sample_info(searchSample)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
@router.post("/list")
async def get_sample_list():
    try:
        return await sample_service.get_sample_list()
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# insert sample
# ----------------------------------------------------------------------
@router.post("/insert")
async def insert_sample(
    insertSample: InsertSample
):
    try:
        return await sample_service.insert_sample(insertSample)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# update sample
# ----------------------------------------------------------------------
@router.post("/update")
async def update_sample(
    updateSample: UpdateSample
):
    try:
        return await sample_service.update_sample(updateSample)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# delete sample
# ----------------------------------------------------------------------
@router.post("/delete")
async def delete_sample(
    deleteSample: DeleteSample
):
    try:
        return await sample_service.delete_sample(deleteSample)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# transaction sample
# ----------------------------------------------------------------------
@router.post("/transaction")
async def transaction_sample(
    transactionSample: TransactionSample,
    session: async_scoped_session = Depends(get_write_db) # db sessiob for transaction
):
    try:
        return await sample_service.transaction_sample(transactionSample, session)
    except Exception as ex:
        return return_exception(ex)