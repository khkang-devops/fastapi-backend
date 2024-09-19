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
            r_session = db_util.get_session("read")
            w_session = db_util.get_session("write")

            async with r_session() as read_session:
                async with w_session() as write_session:
                    # session inject
                    request.state.db_session = {
                        "read": read_session,
                        "write": write_session
                    }

                    # 요청처리
                    response = await original_route_handler(request)

                    # session commit
                    await request.state.db_session["write"].commit()

                    # return
                    return response
        return custom_route_handler