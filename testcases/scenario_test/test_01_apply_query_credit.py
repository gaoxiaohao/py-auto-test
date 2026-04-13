import allure
import pytest

from common.logger import logger
from operation.credit import post_apply_credit, post_query_credit
from testcases.conftest import scenario_data


class TestApplyQueryCredit:


    @allure.story("授信-授信查询案例")
    @allure.description("场景验证")
    @pytest.mark.multiple
    # @pytest.mark.usefixtures("")
    @pytest.mark.parametrize("case_data", scenario_data["test_apply_query_credit"], ids=lambda x: x["name"])
    def test_apply_query_credit(self, case_data):
        # 提取请求和期望
        request_data = case_data["request"]
        expect = case_data["expect"]
        logger.info("*************** 开始执行用例 ***************")
        credit_result = post_apply_credit(request_data)
        assert credit_result.success is True, credit_result.error
        query_result = post_query_credit(request_data)
        assert query_result.success is True, query_result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(expect["retStatus"], query_result.response.json().get("retStatus")))
        logger.info("*************** 结束执行用例 ***************")

