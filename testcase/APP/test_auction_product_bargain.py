import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_add_bargain(get_token_fixture):
    """新增议价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,  #	状态,0:关闭,1:开启
        "auctionProductId": 2,
        "price": 56,  #价格
        "remark": "议价", #备注
        "fromUserId": 7,  #消息发送人id
        "fromUserNickName": 0, #消息发送人名称
        "toUserId": 1, #消息接受人id
        "toUserNickName": 0, #消息发送人名称
        "toUserHeadimg": 0, #消息发送人头像
        "state": 1  #状态：0-议价中，1-议价成功 ，2-议价失败
    }
    url = URL + "/v1/negotiated/agree"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_client_bargain_list(get_token_fixture):
    """客户议价列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 2,
        "fromUserId": 7,  #消息发送人id
        "limit": 10,
        "page": 1
    }
    url = URL + "/v1/negotiated/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


















if __name__ == '__main__':
    pytest.main()