import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_add_business(get_token_fixture):
    """新增商家"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "status": 1,
            "userId": 6,
            "shopName": "球卡店铺",
            "areaCode": "12345678",
            "area": "意大利",
            "address": "米兰",
            "headimg": "梅西头像",
            "frontidcard": "身份证正面",
            "backidcard": "身份证反面",
            "business": "营业执照123456",
            "contact": "球卡商家",
            "contactNumber": "18875272518",
            "sysUserId": 1,
            "username": "qiukashangjia1",
            "password": "123456"
    }
    url = URL + "/v1/businessConfig/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_page_select_business(get_token_fixture):
    """商家审核"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": 1,
        "startTime": "",
        "endTime": "",
        "status": "",
        "name": "",
        "phone": ""
    }
    url = URL + "/v1/businessConfig/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_1_business_audit(get_token_fixture):
    """商家审核"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": "43",
        "state": 1,
        "remark": "haha"
    }
    url = URL + "/v1/webBusniess/updateBusinessApply"
    res = requests.put(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_business_audit_list(get_token_fixture):
    """商家审核列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":"10",
        "page":"1",
        "startTime":"",
        "endTime":"",
        "shopName":"",
        "phone":"",
        "state":"1" #状态（1：审核中；2：已通过；3：已拒绝）
    }
    url = URL + "/v1/webBusniess/businessApplyList"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()