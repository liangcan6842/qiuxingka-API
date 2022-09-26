import requests,json,pytest,allure,os
URL = "http://192.168.110.173:8885"
@allure.feature("app组团测试")
@allure.story("组团产品测试用例")
@allure.description("生成组团订单")
def test_1_add_group_order(get_token_fixture):
    """添加组团订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 3, #商品id
        "addressId": 1, #地址id
        "couponId": 1,  #优惠券id
        "remark": "924组团订单",  #备注
        "num": 10,  #数量（不需要自选队伍的订单必传）
        "soldModelList": [  #选择的售卖信息（只有选队随机、买队随机需要传此信息）
            {
                "soldinfoId": 3, #售卖信息id
                "num": 1  #数量（买队随机数量只能为1）
            }
        ]
    }
    url = URL + "/v1/a/product/addOrder"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_pay_order(get_token_fixture):
    """订单支付"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 0, #订单id
        "type": 2 #1-微信，2-支付宝
    }
    url = URL + "/v1/a/product/payment"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_order_coupon_list(get_token_fixture):
    """订单可用优惠券列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 0, #订单产品id
        "price": 2 #订单总金额
    }
    url = URL + "/v1/a/product/couponListByOrder"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_group_list(get_token_fixture):
    """组团列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10, #订单产品id
        "page": 1, #订单总金额
        # "name": "", #筛选条件
        # "classId": 0, #产品分类id（全部不传）
        # "userId": 7 #商家app端id
    }
    url = URL + "/v1/a/product/nlogin/getPage"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_type_list(get_token_fixture):
    """分类列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/a/product/nlogin/getClassList"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_group_detail(get_token_fixture):
    """组团详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 3, #组团id
    }
    url = URL + "/v1/a/product/nlogin/productDetails"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_7_card_key_list_detail(get_token_fixture):
    """卡密列表详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 2,
        "page": 2,
        "id": 1, #组团id
        # "name": 2, #筛选条件
    }
    url = URL + "/v1/a/product/nlogin/getCamilePageByProduct"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_8_get_sale_message(get_token_fixture):
    """获取售卖信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 1 #订单id
    }
    url = URL + "/v1/a/product/nlogin/productSoldinfo"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_9_send_tear_card_report(get_token_fixture):
    """上传拆卡报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "productId": 3,
        "camileReportModels": [
            {
                "productId": 3,  #组团产品id
                "camileReportModels": [11,22,55]  #卡密
            }
        ]
    }
    url = URL + "/v1/a/product/addProductCamileReport"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_10_query_tear_card_report(get_token_fixture):
    """查询拆卡报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1 ,
        "id": 3 #组团id
    }
    url = URL + "/v1/a/product/getProductCamileReport"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200