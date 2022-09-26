import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_cardKey(get_token_fixture):
    """新增、修改卡密"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "seriesId": 3, #系列id
        "ballTeamId": 3, #球队id
        "playerId": 11, #球员id
        "code": "2022ru0924", #编号
        "cardType": "92465yu至ytu尊球卡", #卡种
        "xcode": "2022092423450578"
    }
    url = URL + "/v1/cardCamille/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_cardKey(get_token_fixture):
    """删除卡密"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [7]
    url = URL + "/v1/cardCamille/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_cardKey(get_token_fixture):
    """分页查询卡密"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "code": 2,  #编号
        # "cardType": 1,  #卡种
        # "ballTeamId": "", #球队
        # "playerId": "", #球员
        # "seriesId": "" #系列id
    }
    url = URL + "/v1/cardCamille/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
