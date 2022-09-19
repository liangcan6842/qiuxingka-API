import requests,json,pytest
URL = "http://192.168.110.244:8885"

def test_1_send_dynamic(get_token_fixture):
    """发动态"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,  #状态,0:关闭,1:开启
        "userId": 7,
        "columnId": 1,  #所属栏目id
        "type": 1,   #	动态类型（1：文字；2：图片；3：视频）
        "content": "今天买了很多球卡，运气很好，都是喜欢的球星",
        "address": "中国重庆",
        "label": "球星",
        "views": 50,
        "comments": 235,
        "likes": 3256,
        "collects": 256,
        "state": 1  #1：审核中；2：审核通过；3：审核不通过
    }
    url = URL + "/v1/a/dynamic/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_dynamic_detail(get_token_fixture):
    """动态详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": "2", #动态id
    }
    url = URL + "/v1/a/dynamic/nlogin/dynamicDetails"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_dynamic_list(get_token_fixture):
    """动态列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        "content": "", #内容查询
        "columnId": ""  #栏目类型id（全部：不传）
    }
    url = URL + "/v1/a/dynamic/nlogin/dynamicList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_usr_dynamic_list(get_token_fixture):
    """用户动态列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        "userId": "7",
        "content": "", #内容查询
        "columnId": ""  #栏目类型id（全部：不传）
    }
    url = URL + "/v1/a/dynamic/nlogin/userDynamicList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_dynamic_likes(get_token_fixture):
    """动态点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": "2", #动态id
    }
    url = URL + "/v1/a/dynamic/addLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_dynamic_cancel_likes(get_token_fixture):
    """动态取消点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": "2", #动态id
    }
    url = URL + "/v1/a/dynamic/cancelLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_7_user_likes_list(get_token_fixture):
    """用户喜欢列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        "userId": "7",
        "content": "今天买了很多球卡，运气很好，都是喜欢的球星", #内容查询
        "columnId": ""  #栏目类型id（全部：不传）
    }
    url = URL + "/v1/a/dynamic/nlogin/userLikeDynamicList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_8_dynamic_comment(get_token_fixture):
    """动态评论"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "dynamicId": 2, #动态id
        "content": "你这动态发的内容太好了!" #评论内容
    }
    url = URL + "/v1/a/dynamic/addComment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_9_comment_reply(get_token_fixture):
    """评论回复"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "type": 2,  #1：直接回复；2：回复某个用户
        "commentId": 8,
        "content": "嗯，对对对，他这动态是发的真好"
    }
    url = URL + "/v1/a/dynamic/addReplyComment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_10_comment_reply_list(get_token_fixture):
    """评论回复列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,  #容量
        "page": 1,
        "commentId": 8,
    }
    url = URL + "/v1/a/dynamic/nlogin/dynamicReplyCommentList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_11_dynamic_collect(get_token_fixture):
    """动态收藏"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 2, #动态id
    }
    url = URL + "/v1/a/dynamic/addCollect"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_12_dynamic_cancel_collect(get_token_fixture):
    """动态取消收藏"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":  2 #动态id
    }
    url = URL + "/v1/a/dynamic/cancelCollect"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_13_dynamic_comment_likes(get_token_fixture):
    """动态评论点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 8 #评论id
    }
    url = URL + "/v1/a/dynamic/addCommentLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_14_comment_cancel_likes(get_token_fixture):
    """动态评论取消点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": "8", #评论id
    }
    url = URL + "/v1/a/dynamic/cancelCommentLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_15_dynamic_comment_list(get_token_fixture):
    """动态评论列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1 ,
        "id":  2 #动态id
    }
    url = URL + "/v1/a/dynamic/nlogin/dynamicCommentList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_16_colum_type_list(get_token_fixture):
    """栏目类型列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "name": ""
    }
    url = URL + "/v1/a/dynamic/nlogin/columnList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()