import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_add_ball_team(get_token_fixture):
    """球队添加、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "name": "923火豹球队", #球队名称
        "englishName": "923-Fire Leopard team ", #球队英文
        "img": "923火豹球队图片" #球队图片
    }
    url = URL + "/v1/cardBall/addTeam"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_add_ball_player(get_token_fixture):
    """球员添加、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "ballTeamId": 5, #球队id
        "name": "9234球员", #球员英文名称
        "img": "9234球员图片" #图片
    }
    url = URL + "/v1/cardBall/addPlayer"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_ball_team(get_token_fixture):
    """删除球队"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[5]
    url = URL + "/v1/cardBall/teamDelete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_delete_ball_player(get_token_fixture):
    """删除球员"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[14]
    url = URL + "/v1/cardBall/playerDelete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_ball_team(get_token_fixture):
    """球队分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "startTime": "",
        "endTime": "",
        "name": "",  # 球队名称
        "status": 1  # 状态,0:关闭,1:开启
    }
    url = URL + "/v1/cardBall/getTeamPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_pagination_query_ball_player(get_token_fixture):
    """球员分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        # "startTime": "",
        # "endTime": "",
        # "ballTeamId": 0,#球队id
        # "name": "",  # 球员名称
        # "status": 1  # 状态,0:关闭,1:开启
    }
    url = URL + "/v1/cardBall/getPlayerPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_ball_team_list(get_token_fixture):
    """球队列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "startTime": "",
        "endTime": "",
        "name": "",  # 厂商名称
        "status": 1  # 状态,0:关闭,1:开启
    }
    url = URL + "/v1/cardBall/getTeamList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_ball_player_list(get_token_fixture):
    """球员列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "startTime": "",
        "endTime": "",
        "ballTeamId": 1,#球队id
        "name": "",  # 厂商名称
        "status": 1  # 状态,0:关闭,1:开启
    }
    url = URL + "/v1/cardBall/getPlayerList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()


