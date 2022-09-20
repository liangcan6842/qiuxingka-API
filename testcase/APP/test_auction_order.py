import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_add_order(get_token_fixture):
    """添加订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 0,  #拍卖产品id
        "contact": "",          #收货人姓名
        "address": "",
        "phone": "",
        "remark": "",
        "orderType": 0          #订单类型
    }
    url = URL + "/v1/a/dynamic/addReplyComment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
