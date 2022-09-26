import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_add_bid(get_token_fixture):
    """新增竞价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId":3 ,
        "price": 59
    }
    url = URL + "/v1/bidding"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_2_query_bid_list(get_token_fixture):
    """竞价列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10 ,
        "page": 1
    }
    url = URL + "/v1/bidding/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

