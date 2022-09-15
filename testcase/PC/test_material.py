import pytest,requests,json
URL = "http://192.168.110.173:9100"
def test_1_add_material(get_token_fixture):
    """新增材料"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "unitPrice": 0,
            "specs": "",
            "image": "",
            "name": "",
            "unitId": 0,
            "weight": 0,
            "id": 0,
            "type": 0,
            "categoryId": 0
    }
    url = URL + "/erp-admin-api/v1/order"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_select_material(get_token_fixture):
    """分页查询材料"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "limit":"15",
            "page":"1",
            "type":"",
            "name":"",
            "categoryId":""
    }
    url = URL + "/erp-admin-api/v1/material/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_print_material_code(get_token_fixture):
    """打印材料码"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
            "materialId":"2",
            "amount":"1 "
    }
    url = URL + "/erp-admin-api/v1/material/code"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.mian()









