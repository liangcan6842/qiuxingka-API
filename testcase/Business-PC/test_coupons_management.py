import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_add_coupons(get_token_fixture):
    """添加、修改优惠券"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "type": 1, #优惠券类型（1：平台优惠券；2：商家优惠券）
        "mold": 1, #1：无门槛；2：满减
        "name": "9.8折", #优惠券名称
        "info": "凡是到店买球卡，都享有9.8折优惠", #优惠券信息
        # "fullMoney": 100,  #满减需要满足的金额
        # "money": 10, #优惠券金额
        "startTime": "",
        "endTime": "",
        "amount": 100, #数量
        "remark": "须知：数量有限，先买先得，用完为止", #备注
        "status": 1  #状态,0:关闭,1:开启
    }
    url = URL + "/v1/merchanCoupon/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_coupons_list(get_token_fixture):
    """优惠券列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "startTime": "",
        # "endTime": "",
        # "name": "", #优惠券名称
        # "mold": 2, #优惠券类型（1：无门槛；2：满减；3：折扣）
        # "status": 1,  #状态,0:关闭,1:开启
        # "state":0  #审核状态（1：申请中；2：审核通过；3：拒绝）
    }
    url = URL + "/v1/merchanCoupon/couponList"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_coupons_receive_record(get_token_fixture):
    """优惠券领取记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "startTime": "",
        "endTime": "",
        "name": "", #优惠券名称
        "nickName": "", #用户昵称
        "mold": 10, #优惠券类型（1：无门槛；2：满减；3：折扣）
        "state":0  #审核状态（1：申请中；2：审核通过；3：拒绝）
    }
    url = URL + "/v1/merchanCoupon/receiveCouponList"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200