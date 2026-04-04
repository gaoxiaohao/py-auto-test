from datetime import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)


# 授信申请接口
@app.route('/credit/apply', methods=['POST'])
def apply_credit():
    data = request.get_json()
    outer_order_id = data.get('outerOrderId', 'unknown')
    phone = data.get('businessParams', {}).get('phone', 0)

    # 模拟业务逻辑：金额 > 10000 失败
    if phone == '18888888888':
        return jsonify({
            "retStatus": "111111",
            "retMsg": "处理中",
            "outerOrderId": outer_order_id,
            "result": None
        })
    elif phone == '18888888880':
        return jsonify({
            "retStatus": "222222",
            "retMsg": "订单重复",
            "outerOrderId": outer_order_id,
            "result": None
        })
    else:
        return jsonify({
            "retStatus": "999999",
            "retMsg": "失败-其他",
            "outerOrderId": outer_order_id,
            "result": None
        })



# 授信结果查询接口
@app.route('/credit/query', methods=['POST'])
def query_credit():
    data = request.get_json()
    outer_order_id = data.get('outerOrderId', 'unknown')
    if outer_order_id == '88888888':
        return jsonify({
            "retStatus": "000000",
            "retMsg": "成功",
            "result": {
                "creditStartDate": "2026-04-03",
                "creditEndDate": "2027-04-03",
                "amount": 50000.00,
                "creditSuccessTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        })

    elif outer_order_id == '88888882':
        return jsonify({
            "retStatus": "RIS001",
            "retMsg": "风控拒绝",
            "result": None
        })
    elif outer_order_id == '888888883':
        return jsonify({
            "retStatus": "BAS001",
            "retMsg": "联网核查不通过",
            "result": None
        })
    elif outer_order_id == '888888886':
        return jsonify({
            "retStatus": "BAS002",
            "retMsg": "验四不通过",
            "result": None
        })
    elif outer_order_id == '888888884':
        return jsonify({
            "retStatus": "BAS003",
            "retMsg": "客户开立失败",
            "result": None
        })
    elif outer_order_id == '888888885':
        return jsonify({
            "retStatus": "BAS004",
            "retMsg": "重复授信",
            "result": None
        })
    else :
        return jsonify({
            "retStatus": "333333",
            "retMsg": "订单不存在",
            "result": None
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)