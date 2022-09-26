import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"
@allure.feature("平台客服")
@allure.story("总后台查询列表用例")
@allure.description("总后台查询列表")
def test_1_pc_query_list(get_token_fixture):
    """总后台查询列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }

    url = URL + "/v1/platform/total/messageList"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("举报管理")
@allure.story("举报详情用例")
@allure.description("举报详情")
def test_2_report_detail(get_token_fixture):
    """举报详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id" : 1
    }
    url = URL + "/v1/report/reportDetails"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()