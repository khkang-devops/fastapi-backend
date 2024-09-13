from app.api.sample import sample_router
from app.common.utils.auth_util import check_api_token, insert_log
from app.common.utils.db_util import db_util
from app.common.utils.log_util import get_logger
from fastapi import Depends, FastAPI, Request

# logger
logger = get_logger(__name__)

# fastapi
app = FastAPI(
    title="FastAPI Backend API Server",
    description="FastAPI Sample code",
    version="1.0.0"
)

# sample router
app.include_router(
    sample_router.router,
    prefix="/api/v1/sample",
    tags=["sample"],
    dependencies=[
        Depends(check_api_token), # 토큰체크
        Depends(insert_log) # 사용이력로그저장 (백그라운드실행)
    ]
)

# startup
@app.on_event("startup")
async def startup_event():
    await db_util.select_one("select 1", {}, await db_util.get_session("read"))
    await db_util.select_one("select 1", {}, await db_util.get_session("write"))

# middleware
@app.middleware("http")
async def managing_db_session(request: Request, call_next):
    if "docs" in str(request.url) or "openapi" in str(request.url):
        return await call_next(request)
    else:
        # session inject
        request.state.db_session = {
            "read": await db_util.get_session("read"),
            "write": await db_util.get_session("write")
        }

        # 요청처리
        response = await call_next(request)

        # session commit
        await request.state.db_session["write"].commit()

        # return
        return response