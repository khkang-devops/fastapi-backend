import json
import ssl
from app.common.utils.log_util import get_logger
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from decimal import Decimal
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.engine.cursor import CursorResult
from tornado.httpclient import AsyncHTTPClient

# logger
logger = get_logger(__name__)

# async_http_client
async_http_client = AsyncHTTPClient()

# key
key = b'5\xe7t\xd3\xeaF]\xf6\tw\xed\r\xc7\xa7\x17\xf7'
nonce = b'\xfb\x1d\xb4\t\xe7*\xf6F6\x9e\xa3C'

# ----------------------------------------------------------------------
# encrypt (AES-128 -> base64)
# pycryptodome.ipynb 암복호화 소스 참조
# ----------------------------------------------------------------------
def encrypt(raw: str):
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    cipher.update("header".encode("utf-8"))
    enc = cipher.encrypt(raw.encode("utf-8"))
    enc = b64encode(enc)
    return enc.decode('ascii')

# ----------------------------------------------------------------------
# decrypt (base64 -> AES-128)
# pycryptodome.ipynb 암복호화 소스 참조
# ----------------------------------------------------------------------
def decrypt(raw: str, tag: bytes):
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    cipher.update("header".encode("utf-8"))
    dec = b64decode(raw.encode('ascii'))
    dec = cipher.decrypt_and_verify(dec, tag)
    return dec.decode('utf-8')

# ----------------------------------------------------------------------
# 비동기API호출
# ----------------------------------------------------------------------
async def async_api_call(url, data):
    # context
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # call
    response = await async_http_client.fetch(
        url,
        method="POST",
        headers={"Content-Type": "application/json"},
        body=json.dumps(data).encode("utf-8"),
        ssl_options=context,
        connect_timeout=60.0,
        request_timeout=60.0
    )

    return response

# ----------------------------------------------------------------------
# DB조회결과 -> list
# ----------------------------------------------------------------------
def get_list(rows: CursorResult):
    result = []

    for row in rows:
        row_dict = {}
        for column in row._fields:
            # decimal to float (because type_error)
            if isinstance(getattr(row, column), Decimal):
                row_dict[column] = float(getattr(row, column))
            else:
                row_dict[column] = getattr(row, column)
        result.append(row_dict)

    return result

# ----------------------------------------------------------------------
# DB조회결과 -> dict
# ----------------------------------------------------------------------
def get_dict(rows: CursorResult):
    row = rows.first()
    result = {}

    if (row is not None):
        for column in row._fields:
            # decimal to float (because type_error)
            if isinstance(getattr(row, column), Decimal):
                result[column] = float(getattr(row, column))
            else:
                result[column] = getattr(row, column)

    return result

# ----------------------------------------------------------------------
# get_response
# ----------------------------------------------------------------------
def get_response(
    status_code: int = None,
    result: object = None
):
    if status_code == status.HTTP_200_OK:
        message = "요청 성공하였습니다."
    elif status_code == status.HTTP_201_CREATED:
        message = "정상 처리되었습니다."
    elif status_code == status.HTTP_400_BAD_REQUEST:
        message = "요청 형식이 맞지 않습니다."
    elif status_code == status.HTTP_401_UNAUTHORIZED:
        message = "시스템 접근 권한이 없습니다."
    elif status_code == status.HTTP_404_NOT_FOUND:
        message = "요청한 정보가 존재하지 않습니다."
    elif status_code == status.HTTP_409_CONFLICT:
        message = "이미 요청한 정보가 있습니다."
    elif status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
        message = "시스템 오류입니다."

    content = {
        "message": message
    }

    if result is not None:
        content["result"] = result

    return JSONResponse(status_code=status_code, content=content)

# ----------------------------------------------------------------------
# get_exception
# ----------------------------------------------------------------------
def get_exception(ex: Exception):
    logger.error(repr(ex))

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    if hasattr(ex, "status_code"):
        status_code = ex.status_code

    return JSONResponse(status_code=status_code, content={"message": repr(ex)})