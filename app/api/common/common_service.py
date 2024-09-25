from app.api.common import common_dao
from app.api.common.common_model import InsertUserHistory
from app.common.utils.common_util import get_exception
from app.common.utils.db_util import write_db
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
        await common_dao.insert_user_history(insertUserHistory)
        await write_db.commit()
    except Exception as ex:
        return get_exception(ex)
    finally:
        await write_db.init_session()