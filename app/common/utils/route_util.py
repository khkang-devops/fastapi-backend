from app.common.utils.db_util import write_db, read_db
from app.common.utils.log_util import get_logger
from fastapi import Request
from fastapi.routing import APIRoute

# logger
logger = get_logger(__name__)

# ----------------------------------------------------------------------
# db session 관리
# custom route handler
# ----------------------------------------------------------------------
class SessionManagingRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request):
            # 요청처리
            response = await original_route_handler(request)

            # 후처리_세션관리
            if (read_db.session().in_transaction()):
                await read_db.init_session()
            if (write_db.session().in_transaction()):
                await write_db.commit()
                await write_db.init_session()

            # return
            return response
        return custom_route_handler