import pytest,requests,json
URL = "http://192.168.110.173:8885"

def test_1_group_product_delete(get_token_fixture):
    """文章新增"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        [1]
    }
    url = URL + "/v1/news/addColumn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200