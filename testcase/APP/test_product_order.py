import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_select_auction_product_detail(get_token_fixture):
    """查看拍卖产品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "productOrderId": 2, #产品id
        "type": 0  #支付方式 1-微信，2-支付宝
    }
    url = URL + "/v1/mailingOrder"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_select_auction_product_list(get_token_fixture):
    """查看拍卖产品列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "state": 0  #产品状态 0-待支付，1-已支付,2-待发货，3-待收货,4-已收货
    }
    url = URL + "/productOrder/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200