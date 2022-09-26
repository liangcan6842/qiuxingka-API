import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_group_add(get_token_fixture):
    """添加、修团组队"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id":0 , #修改时必传
        "activityName": "923分组购买球卡，享组团优惠福利", #活动名称
        "searchKey": "组团优惠", #搜索关键词
        "reminder": "组团购买比单独购买优惠、划算得多哦！", #温馨提示
        "coverImg": "梅西、C罗、贝克汉姆", #封面图
        "bannerImg": "各种分组球卡", #轮播图
        "boxVideo": "923视频", #原箱视频
        "boxWeigh": "2kg", #原箱称重
        "openTimesId": 1, #开卡时间配置id
        "seriesIds": "3", #系列ids
        "random": 1, #随机方式（1：即买即随）
        "whichGroup":3, #同系列第几组
        "title": "随即球队组团", #组团标题(所选系列名称的拼接)
        "specs": "923规格", #规格
        "collageForm": 1, #拼团形式（1：随机球队；2：选队随机；3：买队随机）
        "itemPrice": 80, #商品单价
        "itemNum": 82, #商品份数
        "isQuota": 1, #是否限购（1：是；2：否）
        "quotaNum": 2, #限购份数
        "itemTotalPrice":6560 , #商品总价
        "releaseTime": "", #发布时间（审核后立即发布）
        "salesCycle": 1, #销售周期配置id
        "soldinfoAddModels": [
            {
                "productId": 0, #商品id（不传）
                "ballTeamId": 3, #球队id
                "ballTeamName": "923旋风球队", #球队名称
                "ballTeamImg": "923旋风球队图片", #球队图片
                "num": 50, #数量
                "soldNum": 0, #已售数量（不传）
                "price": 68 #价格
            }
        ],
        "activityAddModels": [
            {
                "productId": 0, #商品id（不传）
                "name": "组团优惠活动", #名称
                "start": "2022-09-24 09:00:00", #区间开始
                "end": "2022-10-08 23:00:00", #区间结束
                "price": 60 #价格
            }
        ]
    }
    url = URL + "/v1/merchanProduct/add"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_group_list(get_token_fixture):
    """组团列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "code": "",  #组团编码
        # "title": "",  #组团名称
        # "state": 2,  #状态（1：待审核；2：已通过；3：已拒绝；4：组团中；5：组团成功；6：组团失败（超时未组满））
        # "startTime": "",
        # "endTime": ""
    }
    url = URL + "/v1/merchanProduct/getPage"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_detail(get_token_fixture):
    """详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":3
    }
    url = URL + "/v1/merchanProduct/productDetails"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
def test_4_detail_card_key_list(get_token_fixture):
    """详情卡密列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "id": 3 #组团id
    }
    url = URL + "/v1/merchanProduct/getCamilePageByProduct"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_seriesId_get_team_list(get_token_fixture):
    """根据系列id获取球队列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [3]
    url = URL + "/v1/merchanProduct/getListBySeriesIds"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_seriesId_get_card_key_list(get_token_fixture):
    """根据系列id获取卡密列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit":10,
        "page":1,
        "collageForm":1, #组团方式
        "ids":3 #系列id
    }
    url = URL + "/v1/merchanProduct/getCamileListBySeriesIds"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_storage_card(get_token_fixture):
    """存储卡"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "userCamileId":6 #用户卡密id
    }
    url = URL + "/v1/merchanProduct/storageCamile"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_rack_up_down(get_token_fixture):
    """上下架"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "ids":3 ,
        "frameState":1 #1：上架；2：下架
    }
    url = URL + "/v1/merchanProduct/frameState"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_ship(get_token_fixture):
    """发货"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "userCamileIds": [6], #用户卡密ids
        "courierNumber": "2022092446030929069",  #快递单号
        "courierServicesCompany": "圆通速递"  #快递公司
    }
    url = URL + "/v1/merchanProduct/deliverCamile"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



