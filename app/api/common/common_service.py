from app.api.common import common_dao
from app.api.common.common_model import InsertUserHistory
from app.common.utils.common_util import return_exception
from app.common.utils.log_util import get_logger

# logger
logger = get_logger(__name__)

# ----------------------------------------------------------------------
# insert user history
# ----------------------------------------------------------------------
async def insert_user_history(
    insertUserHistory: InsertUserHistory = None
):
    try:
        return await common_dao.insert_user_history(insertUserHistory)
    except Exception as ex:
        return return_exception(ex)