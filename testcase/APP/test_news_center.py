import requests,json,pytest,allure,os
URL = "http://192.168.110.173:8885"
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻列表")
def test_1_news_list(get_token_fixture):
    """新闻列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "content": "" #内容查询
    }
    url = URL + "/v1/a/news/nlogin/newsList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻详情")
def test_2_news_detail(get_token_fixture):
    """新闻详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/nlogin/newsDetails"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻评论")
def test_3_news_comment(get_token_fixture):
    """新闻评论"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "newsId": 4, #新闻id
        "content": "10.9新闻测试评论" #评论内容
    }
    url = URL + "/v1/a/news/addComment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻评论列表")
def test_4_news_comment_list(get_token_fixture):
    """新闻评论列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/nlogin/dynamicCommentList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("评论回复")
def test_5_comment_reply(get_token_fixture):
    """评论回复"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "type": 2,     #1：直接回复；2：回复某个用户
        "commentId": 7,
        "content": "测试评论回复"
    }
    url = URL + "/v1/a/news/addReplyComment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("评论回复列表")
def test_6_comment_reply_list(get_token_fixture):
    """评论回复列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "commentId": 7 #评论id
    }
    url = URL + "/v1/a/news/nlogin/dynamicReplyCommentList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻点赞")
def test_7_news_like(get_token_fixture):
    """新闻点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/addLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻取消点赞")
def test_8_news_cancle_like(get_token_fixture):
    """新闻取消点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/cancelLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("评论点赞")
def test_9_comment_like(get_token_fixture):
    """评论点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 7 #评论id
    }
    url = URL + "/v1/a/news/addCommentLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("评论取消点赞")
def test_10_comment_cancle_like(get_token_fixture):
    """评论取消点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 7 #评论id
    }
    url = URL + "/v1/a/news/cancelCommentLike"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻收藏")
def test_11_news_collect(get_token_fixture):
    """评论点赞"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/addCollect"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("新闻中心")
@allure.story("新闻中心测试用例")
@allure.description("新闻取消收藏")
def test_12_news_cancle_collect(get_token_fixture):
    """新闻取消收藏"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4 #新闻id
    }
    url = URL + "/v1/a/news/cancelCollect"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200





















