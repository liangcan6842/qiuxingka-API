import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_register(get_token_fixture):
    """注册"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "phone": "18875272518",
        "code": "12345678", #短信验证码
        "password": "123456",
        "wechatOpenid": "",
        "qqOpenid": "",
        "nickName": "",
        "headimg": ""
    }
    url = URL + "/v1/a/user/register"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_alter_personal_information(get_token_fixture):
    """修改个人资料"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "headimg": "lucky的头像", #头像
        "nickName": "测试用户lucky",
        "synopsis": "一个资深球迷",  #简介
        "gender": 1,   #1:男,2:女；3：不展示
        "address": "中国重庆"
    }
    url = URL + "/v1/a/user/updateUserInfo"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_get_user_message(get_token_fixture):
    """获取登录用户基本信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/getHomeUser"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_homePage(get_token_fixture):
    """我的主页"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/myHomePage"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_other_homePage(get_token_fixture):
    """他人主页"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"userId":8}
    url = URL + "/v1/a/user/nlogin/othersHomePage"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_integral(get_token_fixture):
    """我的积分"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/myIntegral"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_integral_detail(get_token_fixture):
    """积分明细"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10,
        "page":1
    }
    url = URL + "/v1/a/user/integralList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_integral_leaderboard(get_token_fixture):
    """积分排行榜"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10,
        "page":1
    }
    url = URL + "/v1/a/user/integralRankingList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_balance(get_token_fixture):
    """我的余额"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/myBalance"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_withdrawal(get_token_fixture):
    """提现"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "name": "",  #姓名
        "account": "",  #支付宝账号
        "money": 0    #金额
    }
    url = URL + "/v1/a/user/putforword"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_withdrawal_record(get_token_fixture):
    """提现记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10 ,
        "page":1 ,
        "year":2022,
        "month":9    #年份和月份都要传
    }
    url = URL + "/v1/a/user/putforwordList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_coupon(get_token_fixture):
    """我的优惠券"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10 ,
        "page":1 ,
        "state":0  #状态（0：全部；1：待使用；2：已使用；3：已过期）
    }
    url = URL + "/v1/a/user/userCoupon"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_coupon_code_receive(get_token_fixture):
    """优惠券兑换码领取"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "code":400  #兑换码
    }
    url = URL + "/v1/a/user/receiveCoupon"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_integration(get_token_fixture):
    """我的积分"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/myIntegral"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_integration_detail(get_token_fixture):
    """积分明细"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1
    }
    url = URL + "/v1/a/user/integralList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_2_business_settled(get_token_fixture):
    """商家入驻"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,
        "userId": 7,
        "shopName": "全球球卡销售中心",
        "areaCode": "400000000", #地区码
        "area": "中国重庆",
        "address": "重庆市渝北",
        "headimg": "lucky商家头像",
        "frontidcard": "lucky身份信息",
        "backidcard": "lucky鉴发机关",
        "business": "lucky营业执照",
        "state": 1,          #1：审核中；2：已通过；3：已拒绝
        "checkUserId": 0,
        "checkTime": "",
        "remark": "申请商家",
        "reason": "资料齐全"
    }
    url = URL + "/v1/a/user/userBusinessApply"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_acount_detail(get_token_fixture):
    """账户明细"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10,
        "page":1,
        "year":2022,
        "month":9
    }
    url = URL + "/v1/a/user/accountDetailsList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_add_alter_address(get_token_fixture):
    """添加、修改地址"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1, #状态,0:关闭,1:开启
        "userId": 7,
        "name": "测试用户地址",
        "phone": "18875272518",
        "areaCode": "400000000",
        "area": "中国重庆",
        "address": "重庆市南岸区",
        "isDefault": 1 #是否默认（1：是；2：否）
    }
    url = URL + "/v1/a/user/addReceive"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_alter_default_address(get_token_fixture):
    """修改默认地址"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 1, #地址id
        "isDefault": 2  #是否默认（1：是；2：否）
    }
    url = URL + "/v1/a/user/updateReceiveIsDefault"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_delete_address(get_token_fixture):
    """删除地址"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 1 #地址id
    }
    url = URL + "/v1/a/user/deleteReceive"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_my_receipt_address(get_token_fixture):
    """我的收货地址"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 11,
        "page": 1,
    }
    url = URL + "/v1/a/user/myReceive"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_setting_detail(get_token_fixture):
    """设置详情"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/user/setDetails"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_focus_on(get_token_fixture):
    """关注"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"userId":8}
    url = URL + "/v1/a/user/addFollow"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_cancel_focus_on(get_token_fixture):
    """取消关注"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"userId":8}
    url = URL + "/v1/a/user/cancelFollow"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_focus_on_list(get_token_fixture):
    """关注列表"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":8,
        "page":1,
        "userId":7,
        "nickName":""
    }
    url = URL + "/v1/a/user/nlogin/concerns"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_pull_black(get_token_fixture):
    """拉黑"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"userId":8}
    url = URL + "/v1/a/user/addBlack"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_cancel_pull_black(get_token_fixture):
    """取消拉黑"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"userId":8}
    url = URL + "/v1/a/user/cancelBlack"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_fans_list(get_token_fixture):
    """粉丝列表"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":8,
        "page":1,
        "userId":8,
        "nickName":""
    }
    url = URL + "/v1/a/user/nlogin/fans"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_1_column_list(get_token_fixture):
    """栏目列表"""
    # 通过Fixture函数获取get_token_ fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "name":"919测试社区"
    }
    url = URL + "/v1/a/user/nlogin/dynamicColumnList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()
