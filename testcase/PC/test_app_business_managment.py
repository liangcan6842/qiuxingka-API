import pytest,requests,json
URL = "http://192.168.110.173:8885"
def test_1_business_audit_list(get_token_fixture):
    """app商家审核列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        "startTime": "",
        "endTime": "",
        "shopName": "", #店铺名称
        "phone": "",
        "state": ""   #1：审核中；2：已通过；3：已拒绝
    }
    url = URL + "/v1/webBusniess/businessApplyList"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_business_audit(get_token_fixture):
    """app商家审核"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 1,
        "remark": "审核通过",
        "state": 2  #1：审核中；2：已通过；3：已拒绝
    }
    url = URL + "/v1/webBusniess/updateBusinessApply"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
