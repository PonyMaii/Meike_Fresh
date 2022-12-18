import json

from core.ResultBase import ResultResponse
from utils.my_logging import logger


def process_response(response):
    if response.status_code in [200, 201, 400]:
        ResultResponse.success = True
        ResultResponse.body = response.json()
    else:
        ResultResponse.success = False
        logger.error("接口状态码不是2开头，请检查")
    logger.info("接口的返回内容>>>：" + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse
