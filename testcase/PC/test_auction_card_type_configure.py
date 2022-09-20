import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_auction_card_type(get_token_fixture):
    """新增拍卖卡类型"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1, #状态,0:关闭,1:开启
        "name": "shhj球卡" #拍卖类型名称
    }
    url = URL + "/v1/auctionCardType/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_auction_card_edit(get_token_fixture):
    """拍卖卡编辑"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":3,
        "status": 1, #状态,0:关闭,1:开启
        "name": "shhj球卡dfg" #拍卖卡类型名称
    }
    url = URL + "/v1/auctionCardType/edit"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_auction_card_alter_state(get_token_fixture):
    """拍卖卡修改状态"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 3, #拍卖卡类型id
        "status":0   #状态, 0: 关闭, 1: 开启
    }
    url = URL + "/v1/auctionCardType/update"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_auction_card_type_delete(get_token_fixture):
    """拍卖卡类型删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [3]
    url = URL + "/v1/auctionCardType/del"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_auction_card_type_list_select(get_token_fixture):
    """拍卖球卡类型列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":"10",
        "page":"1",
        "name":"", #玩法名称
    }
    url = URL + "/v1/auctionCardType/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200