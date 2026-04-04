from api.credit import credit
from core.result_base import ResultBase

def post_apply_credit(json):
    result = ResultBase()
    res = credit.apply_credit(json=json)
    result.success = False
    if res.json()['retStatus'] == '111111':
        result.success = True
    else:
        result.error = "接口返回码是【{}】，返回信息是：{}".format(res.json()['retStatus'], res.json()['retMsg'])
    result.message = res.json()['retMsg']
    result.response = res
    return result