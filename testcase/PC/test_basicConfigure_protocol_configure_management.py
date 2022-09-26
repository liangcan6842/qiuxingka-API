import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"
@allure.feature("基础配置")
@allure.story("协议配置")
@allure.description("添加修改协议")
def test_1_add_protocol(get_token_fixture):
    """新增、修改协议"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,
        "register":"1、本网站服务条款的确认和接纳 本网站各项服务的所有权和运作权归本网站拥有。"
                   "2、用户必须： (1)自行配备上网的所需设备， 包括个人电脑、调制解调器或其他必备上网装置。 (2)自行负担个人上网所支付的与此服务有关的电话费用、 网络费用。"
                   "3、用户在本网站平台上不得发布下列违法信息： (1)反对宪法所确定的基本原则的； ..."
                   "4、有关个人资料 用户同意： ..."
                   "5、电子邮件 用户在注册时应当选择稳定性及安全性相对较好的电子邮箱，并且同意接受并阅读本网站发往用户的各类电子邮件。 ..."
                   "6、服务条款的修改 本网站有权在必要时修改服务条款，本网站服务条款一旦发生变动，将会在重要页面上提示修改内容。 ..."
                   "7、用户的帐号、密码和安全性 你一旦注册成功成为用户，你将得到一个密码和帐号。 ..."
                   "8、拒绝提供担保 用户明确同意信息服务的使用由用户个人承担风险。",
        "purchase": "购买前请仔细阅读注册服务条款"
    }
    url = URL + "/v1/agreement/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("基础配置")
@allure.story("协议配置")
@allure.description("协议查询")
def test_2_query_protocol(get_token_fixture):
    """协议查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/agreement/getCommission"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
