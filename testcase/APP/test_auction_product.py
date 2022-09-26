import requests,json,pytest
URL = "http://192.168.110.173:8885"

def test_1_add_auction_product(get_token_fixture):
    """添加新的拍卖产品"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1, #状态,0:关闭,1:开启
        "cardPictureUrl": "920拍卖产品1", #产品、卡片图片
        "cardDescribe": "该球卡属于珍贵卡片，购买后请妥善保管",  #卡片描述
        "blemishExplain": "完好无损", #瑕疵说明
        "startingPrice": 23,   #起拍价
        "fixedPrice": 70,      #一口价
        "earnestMoney": 6,    #保证金
        "auctionCardTypeConfigId": 1, #拍卖卡类型配置id
        "regionId": "500000,500100,500112",       #地区id
        "postageType": 1,     #邮费类型 1-包邮，2-到付
        "auctionStartTime": "2022-09-20 18:00:00",  #开拍时间
        "auctionEndTime": "2022-10-05 18:00:00",  #拍卖结束时间（拍卖时间最多14天）
        "paymentDay": 1,  #支付结束时间（几天）
        "state": 1,  #状态：0-下架，1-待拍卖，2-拍卖中，3-待支付，4-待发货，5待收货，6-已收货
        "type": 1,   #0-竞价，1-议价，2-一口价
        "userId": 7,  #竞价或议价成功用户id
        "webUserId":7 ,
        "role": 2,   #用户角色（1：普通用户；2：商家）
        "headimg": "920商家头像", #头像
        "nickName": "测试拍卖产品1", #昵称
        "isMerchant": "true", #是否是卖家用户 true: 是，false 否
        "fixPrice": 68, #定价
        "version": 0,  #版本
        "reason": "拍卖失败，没有人买"   #拍卖取消 理由
    }
    url = URL + "/v1/auctionProduct"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_2_query_auction_product_detail_businessMessage(get_token_fixture):
    """查看拍卖产品详情，商家信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"auctionProductId":1 }
    url = URL + "/v1/auctionProduct/user"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_3_query_auction_product_list(get_token_fixture):
    """查看拍卖产品列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        # "cardDescribe": "珍贵卡片", #关键字搜索
        # "cardTypeId	": 1 , #卡片类型查询后台拍卖卡片类型配置下拉框
        # "forSale": 1,  #是否在售 1是，0否
        # "price":1 , #价格排序： 1 价格升序 2价格降序
        # "progress": 1,   #进度： 1正序，0-降序
        # "endAuction": 0,      #结拍： 1查询结束拍卖的产品
    }
    url = URL + "/v1/auctionProduct/page"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_4_query_my_auction_list(get_token_fixture):
    """查看我的拍卖列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": 10,
        "page": 1,
        "state": 2 #产品状态 1-待拍卖，2-拍卖中，3-待支付，4-待发货，5-待收货
    }
    url = URL + "/v1/auctionProduct/myPage"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_5_get_latest_price_message(get_token_fixture):
    """获取产品最新价格"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId": 2
    }
    url = URL + "/v1/auctionProduct/newBiddingPrice"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_6_query_auction_productDetail(get_token_fixture):
    """查看拍卖产品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"auctionProductId":1 }
    url = URL + "/v1/auctionProduct/details"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_7_whether_pay_margin(get_token_fixture):
    """是否缴纳保证金"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"auctionProductId":3 }
    url = URL + "/v1/auctionProduct/isPayEarnest"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

def test_8_cancel_auction(get_token_fixture):
    """取消拍卖"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "auctionProductId":1,
        "status": 1, #状态,0:关闭,1:开启
        "reason": "未达到预期目标",
        "state": 1,  #0-申请中，1-通过，2不通过
        "checkUserId": 45, #审核人
        "checkTime": "2022-09-20 16:00:00",  #审核时间
        "remark": "取消拍卖" #备注
    }
    url = URL + "/v1/auctionProduct/cancelTheAuction"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200




if __name__ == '__main__':
    pytest.main()

























































