import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_add_order(get_token_fixture):
    """添加订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 2,  #拍卖产品id
        "contact": "lucky",          #收货人姓名
        "address": "四川成都",
        "phone": "18875272518",
        "remark": "议价订单",
        "orderType": 4          #订单类型 1-保证金，2-一口价，3-竞价，4-议价
    }
    url = URL + "/v1/auctionOrder"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_order(get_token_fixture):
    """删除订单id"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionOrderId": 3,  # 订单id
    }
    url = URL + "/v1/auctionOrder/del"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_select_order(get_token_fixture):
    """查询订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 3,  # 拍卖产品id
        "orderType": 3  # 订单类型 1-保证金，2-一口价，3-竞价，4-议价
    }
    url = URL + "/v1/auctionOrder/orderType"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_auction_user_paid_orderMessage(get_token_fixture):
    """从查询拍卖用户已支付订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 3,  # 拍卖产品id
        "orderType": 3  # 订单类型 1-保证金，2-一口价，3-竞价，4-议价
    }
    url = URL + "/v1/auctionOrder/orderType"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_order_pay_operate(get_token_fixture):
    """订单支付操作"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionOrderId": 3,  # 订单id
        "type": 1  # 1-微信，2-支付宝
    }
    url = URL + "/v1/auctionOrder/payment"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_wechat_auction_product_pay(get_token_fixture):
    """微信拍卖产品回调"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/auctionOrder/wv_notify"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_7_alipay_auction_product_pay(get_token_fixture):
    """支付宝拍卖产品回调"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/auctionOrder/alipay_notify"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_8_select_auction_product_detail(get_token_fixture):
    """查询拍卖产品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 3  # 拍卖产品id
    }
    url = URL + "/v1/auctionOrder/auctionProduct/details"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_9_buyer_sure_receipt(get_token_fixture):
    """查询拍卖产品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 3  # 拍卖产品id
    }
    url = URL + "/v1/auctionOrder/auctionProduct/details"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200