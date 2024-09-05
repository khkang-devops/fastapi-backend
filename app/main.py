from app.api.sample import sample_router
from app.common.utils.auth_util import check_api_token, insert_log
from app.common.utils.db_util import select_read_db, select_write_db
from app.common.utils.log_util import get_logger
from fastapi import Depends, FastAPI

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
    # select_test
    await select_read_db()
    await select_write_db()

"""
# middleware
@app.middleware("http")
async def pre_post_process(request: Request, call_next):
    # 요청전처리
    await check_api_token(request)

    # 요청처리
    response = await call_next(request)

    # 요청후처리

    # return
    return response
"""