import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_bid_markup(get_token_fixture):
    """新增竞拍加价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1, #状态,0:关闭,1:开启
        "startPrice": 20, #开始价格
        "endPrice": 80,  #结束价格
        "raisePrice": 60 #最低价格
    }
    url = URL + "/v1/auctionRaisePrice/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_edit_bid_markup(get_token_fixture):
    """编辑竞拍加价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":1,
        "status": 1, #状态,0:关闭,1:开启
        "startPrice": 10, #开始价格
        "endPrice": 98,  #结束价格
        "raisePrice": 90 #最低价格
    }
    url = URL + "/v1/auctionRaisePrice/edit"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_delete_bid_markup(get_token_fixture):
    """删除竞拍加价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = []
    url = URL + "/v1/auctionRaisePrice/del"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_select_bid_markup_list(get_token_fixture):
    """列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1
    }
    url = URL + "/v1/auctionRaisePrice/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200