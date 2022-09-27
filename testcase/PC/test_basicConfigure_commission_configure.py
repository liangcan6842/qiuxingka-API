import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_commission_configure(get_token_fixture):
    """新增、修改分佣配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,  #	状态,0:关闭,1:开启
        "groupProdct": 10, #组团佣金
        "auctionProduct": 20 #拍卖佣金
    }
    url = URL + "/v1/commission/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_query_configure(get_token_fixture):
    """配置查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/commission/getCommission"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
