import json
import ssl
from app.common.utils.log_util import get_logger
from app.config.config import api_response
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from fastapi import status
from fastapi.responses import JSONResponse
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
# exception
# ----------------------------------------------------------------------
def return_exception(ex: Exception):
    logger.error(repr(ex))

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    if hasattr(ex, "status_code"):
        status_code = ex.status_code

    response_body = api_response.get(status_code)
    response_body["description"] = repr(ex)
    return JSONResponse(status_code=status_code, content=response_body)