from api.credit import credit
from core.result_base import ResultBase

def post_apply_credit(json):
    result = ResultBase()
    res = credit.apply_credit(json=json)

    # 1. 检查 HTTP 状态码
    if res.status_code != 200:
        result.success = False
        result.error = f"HTTP 请求失败，状态码：{res.status_code}"
        result.response = res
        return result

    result.success = False
    if res.json()['retStatus'] == '111111':
        result.success = True
    else:
        result.error = "接口返回码是【{}】，返回信息是：{}".format(res.json()['retStatus'], res.json()['retMsg'])
    result.message = res.json()['retMsg']
    result.response = res
    return result

def post_query_credit(json):
    result = ResultBase()
    res = credit.query_credit(json=json)

    if res.status_code != 200:
        result.success = False
        result.error = f"HTTP 请求失败，状态码：{res.status_code}"
        result.response = res
        return result

    result.success = False
    if res.json()['retStatus'] == '000000':
        result.success = True
    else:
        result.error = "接口返回码是【{}】，返回信息是：{}".format(res.json()['retStatus'], res.json()['retMsg'])
    result.message = res.json()['retMsg']
    result.response = res
    return result