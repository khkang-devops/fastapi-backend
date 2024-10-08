from app.api.common.common_model import InsertUserHistory
from app.common.utils.db_util import write_db
from app.config.config import APIConfig

# config
config = APIConfig()

# svc_cd
svc_cd = config.svc_cd

# ----------------------------------------------------------------------
# insert user history
# ----------------------------------------------------------------------
async def insert_user_history(
    insertUserHistory: InsertUserHistory
):
    # sql
    sql = f"""
        -- insert_history
        insert into tb_sample_history (
            svc_cd,
            usr_id,
            usr_ip,
            usr_dept,
            usr_url,
            usr_param,
            crt_dttm
        ) values (
            :svc_cd,
            :usr_id,
            :usr_ip,
            :usr_dept,
            :usr_url,
            :usr_param,
            now() at time zone 'Asia/Seoul'
        )
    """

    # parameter
    param = {
        "svc_cd": svc_cd,
        "usr_id": insertUserHistory.usr_id,
        "usr_ip": insertUserHistory.usr_ip,
        "usr_dept": insertUserHistory.usr_dept,
        "usr_url": insertUserHistory.usr_url,
        "usr_param": insertUserHistory.usr_param
    }

    # execute sql
    return await write_db.insert(sql, param)