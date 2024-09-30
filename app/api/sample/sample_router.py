from app.api.sample import sample_service
from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, TransactionSample, UpdateSample
from app.common.utils.common_util import get_exception
from app.common.utils.log_util import get_logger
from app.common.utils.route_util import SessionManagingRoute
from fastapi import APIRouter

# logger
logger = get_logger(__name__)

# router
router = APIRouter(route_class=SessionManagingRoute)
# router = APIRouter()

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
        return get_exception(ex)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
@router.post("/list")
async def get_sample_list():
    try:
        return await sample_service.get_sample_list()
    except Exception as ex:
        return get_exception(ex)

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
        return get_exception(ex)

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
        return get_exception(ex)

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
        return get_exception(ex)

# ----------------------------------------------------------------------
# transaction sample
# ----------------------------------------------------------------------
@router.post("/transaction")
async def transaction_sample(
    transactionSample: TransactionSample
):
    try:
        return await sample_service.transaction_sample(transactionSample)
    except Exception as ex:
        return get_exception(ex)