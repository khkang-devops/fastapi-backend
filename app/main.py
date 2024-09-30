from app.api.sample import sample_router
from app.common.utils.auth_util import check_api_token, insert_log
from app.common.utils.db_util import read_db, write_db
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
    await read_db.select_one("select 1", {})
    await write_db.select_one("select 1", {})

# # middleware
# @app.middleware("http")
# async def managing_db_session(request: Request, call_next):
#     if "docs" in str(request.url) or "openapi" in str(request.url):
#         return await call_next(request)
#     else:
#         # 요청처리
#         response = await call_next(request)

#         # commit
#         await write_db.session().commit()

#         # init
#         await read_db.init_session()
#         await write_db.init_session()

#         # return
#         return response