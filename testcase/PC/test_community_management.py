import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_dynamic_state_alter(get_token_fixture):
    """动态状态修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id": 2, #动态id
            "status": 1  #状态,0:关闭,1:开启
    }
    url = URL + "/v1/dynamic/updateDynamicStatus"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_2_dynamic_audit_state_alter(get_token_fixture):
    """动态审核状态修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "ids": 2, #动态id
            "state": 2  #1：审核中；2：审核通过；3：审核不通过
    }
    url = URL + "/v1/dynamic/updateDynamicState"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_3_dynamic_delete(get_token_fixture):
    """动态删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [8,9,10]
    url = URL + "/v1/dynamic/delDynamic"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_4_dynamic_list(get_token_fixture):
    """动态列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "page": 1,
            "limit": 10,
            "name": "", #用户昵称
            "startTime": "",
            "endTime": "",
            "state": 2, #1：审核中；2：审核通过；3：审核不通过
            "status": 1 #状态,0:关闭,1:开启
    }
    url = URL + "/v1/dynamic/pageDynamicList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_5_comment_state_alter(get_token_fixture):
    """评论状态修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id": 2, #动态id
            "status": 0 #状态,0:关闭,1:开启
    }
    url = URL + "/v1/dynamic/updateDynamicCommentStatus"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_6_dynamic_comment_list(get_token_fixture):
    """动态评论列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "id": 2, #动态id
            "limit": 10,
            "page":  1
    }
    url = URL + "/v1/dynamic/dynamicCommentList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_7_community_classity_add(get_token_fixture):
    """社区分类新增、修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "status": 1, #状态,0:关闭,1:开启
            "name": "9199测试社区"
    }
    url = URL + "/v1/dynamic/addColumn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_8_community_classity_select_page(get_token_fixture):
    """社区分类分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "page": 1,
            "limit": 10,
            "name": "", #社区名称
            "startTime": "",
            "endTime": ""
    }
    url = URL + "/v1/dynamic/pageColumn"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_9_community_classfty_delete(get_token_fixture):
    """社区分类删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [5]
    url = URL + "/v1/dynamic/delColumn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()


