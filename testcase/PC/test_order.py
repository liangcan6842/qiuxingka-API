import pytest,requests,json
URL = "http://192.168.110.244:8885"
def test_1_add_order(get_token_fixture):
    """新增订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "productId": 15,
            "productCount": 200,
            "customId": 1
    }
    url = URL +"/erp-admin-api/v1/order"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_select_order(get_token_fixture):
    """分页查询订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit":"10",
            "page":"1",
            "customName":"",
            "code":"",
            "state":"",
            "startTime":"",
            "endTime":""
    }
    url = URL + "/erp-admin-api/v1/order/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    # code = res[]
    print(res)
    # assert res["code"] == 200












if __name__ == '__main__':
    pytest.main()