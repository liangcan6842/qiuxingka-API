import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_group_product_rack_up_down(get_token_fixture):
    """组团产品上下架"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data ={
        "ids":3,
        "frameState":1 #1：上架；2：下架
    }
    url = URL + "/v1/product/frameState"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_group_product_rack_up_audit(get_token_fixture):
    """组团产品上架审核"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "ids": 3,
        "state": 2,  # 2：已通过；3：拒绝
        "reason": ""  # 拒绝原因
    }
    url = URL + "/v1/product/checkState"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_group_product_detail(get_token_fixture):
    """组团详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 3
    }
    url = URL + "/v1/product/productDetails"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_group_list(get_token_fixture):
    """组团列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "shopName":"qiukashangjia",  #商家名称
        # "code": 3,  #组团编码
        # "title":"",  #组团名称
        # "state": 3,  #状态（1：待审核；2：已通过；3：已拒绝；4：组团中；5：组团成功；6：组团失败（超时未组满））
        # "startTime":"",
        # "endTime":""
    }
    url = URL + "/v1/product/getPage"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200