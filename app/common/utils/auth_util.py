import json
from app.api.common.common_model import InsertUserHistory
from app.api.common.common_service import insert_user_history
from app.common.utils.log_util import get_logger
from fastapi import Header, HTTPException, Request, status, BackgroundTasks

# logger
logger = get_logger(__name__)

# ----------------------------------------------------------------------
# check api token
# ----------------------------------------------------------------------
async def check_api_token(
    api_token: str = Header(None)
):
    if api_token != "123":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

# ----------------------------------------------------------------------
# insert user history log (백그라운드저장처리)
# ----------------------------------------------------------------------
async def insert_log(
    request: Request,
    background_tasks: BackgroundTasks
):
    # request_body
    request_body = await request.body()

    # usr_param
    usr_param = ""
    if request_body and (request.method == "POST" or request.method == "PUT" or request.method == "DELETE"):
        usr_param = await request.json()
        usr_param = json.dumps(usr_param)

    # parameter
    insertUserHistory = InsertUserHistory()
    insertUserHistory.usr_id = "usr_id"
    insertUserHistory.usr_ip = "usr_ip"
    insertUserHistory.usr_dept = "usr_dept"
    insertUserHistory.usr_url = str(request.url)
    insertUserHistory.usr_param = usr_param

    # insert user_log (background_task)
    background_tasks.add_task(insert_user_history, insertUserHistory)