from app.common.utils.db_util import db_util
from fastapi import Request
from fastapi.routing import APIRoute

# ----------------------------------------------------------------------
# db session 관리
# custom route handler
# ----------------------------------------------------------------------
class SessionManagingRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()
        async def custom_route_handler(request: Request):
            # session inject
            request.state.db_session = {
                "read": await db_util.get_session("read"),
                "write": await db_util.get_session("write")
            }

            # 요청처리
            response = await original_route_handler(request)

            # session commit
            await request.state.db_session["write"].commit()

            # return
            return response
        return custom_route_handler