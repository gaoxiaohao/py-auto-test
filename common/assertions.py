from common.logger import logger


def assert_api_response(result, expect,test_data):
    """
    统一断言接口响应
    :param test_data:
    :param result: 操作层返回的 ResultBase 对象（包含 success, response, error, message 等）
    :param expect: 预期结果字典，应包含 success, retStatus, retMsg
    """
    # 1. 断言接口调用成功（HTTP 200 + JSON 可解析）
    assert result.success ==expect["success"], f"接口调用失败: {result.error}"

    # 2. 获取响应 JSON
    resp = result.response.json()

    # 3. 断言业务状态码
    actual_ret_status = resp.get("retStatus")
    assert actual_ret_status == expect["retStatus"], \
        f"期望 retStatus={expect['retStatus']}，实际 {actual_ret_status}"

    # 4. 断言业务消息（可选，如果 expect 中有 retMsg）
    if "retMsg" in expect:
        actual_ret_msg = resp.get("retMsg")
        assert actual_ret_msg == expect["retMsg"], \
            f"期望 retMsg={expect['retMsg']}，实际 {actual_ret_msg}"

    # 5. 可选：记录日志
    logger.info(f"用例 {test_data['name']} 符合预期")
    logger.info(f"断言通过: success=True, retStatus={actual_ret_status}, retMsg={actual_ret_msg}")