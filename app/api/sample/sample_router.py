from app.api.sample import sample_service
from app.api.sample.sample_model import DeleteSample, InsertSample, SearchSample, TransactionSample, UpdateSample
from app.common.utils.common_util import return_exception
from app.common.utils.log_util import get_logger
from app.common.utils.route_util import SessionManagingRoute
from fastapi import APIRouter, Request

# logger
logger = get_logger(__name__)

# router
# router = APIRouter(route_class=SessionManagingRoute)
router = APIRouter()

# ----------------------------------------------------------------------
# get sample_info
# ----------------------------------------------------------------------
@router.post("/info")
async def get_sample_info(
    searchSample: SearchSample,
    request: Request
):
    try:
        return await sample_service.get_sample_info(searchSample, request.state.db_session)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# get sample_list
# ----------------------------------------------------------------------
@router.post("/list")
async def get_sample_list(
    request: Request
):
    try:
        return await sample_service.get_sample_list(request.state.db_session)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# insert sample
# ----------------------------------------------------------------------
@router.post("/insert")
async def insert_sample(
    insertSample: InsertSample,
    request: Request
):
    try:
        return await sample_service.insert_sample(insertSample, request.state.db_session)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# update sample
# ----------------------------------------------------------------------
@router.post("/update")
async def update_sample(
    updateSample: UpdateSample,
    request: Request
):
    try:
        return await sample_service.update_sample(updateSample, request.state.db_session)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# delete sample
# ----------------------------------------------------------------------
@router.post("/delete")
async def delete_sample(
    deleteSample: DeleteSample,
    request: Request
):
    try:
        return await sample_service.delete_sample(deleteSample, request.state.db_session)
    except Exception as ex:
        return return_exception(ex)

# ----------------------------------------------------------------------
# transaction sample
# ----------------------------------------------------------------------
@router.post("/transaction")
async def transaction_sample(
    transactionSample: TransactionSample,
    request: Request
):
    try:
        return await sample_service.transaction_sample(transactionSample, request.state.db_session)
    except Exception as ex:
        return return_exception(ex)