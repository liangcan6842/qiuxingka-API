import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"
@allure.feature("消息列表")
@allure.story("公用接口消息测试用例")
@allure.description("添加消息窗口")
def test_1_alter_user_disable_information(get_token_fixture):
    """添加消息窗口"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1, #状态,0:关闭,1:开启
        "fromUserId": 7, #消息发送人
        "toUserId": 8,  #消息接收人
        "remarkName": "普通消息", #备注名称
        "type": 1,     #消息类型：1-普通消息，2-系统消息，3-订单通知,4-互动消息
        "msg": "最新通知！，国庆活动球卡优惠福利上线，请各位卖家关注活动内容",     #最新消息
        "nickName": "lucky",  #昵称
        "headimg": "lucky头像"  #头像
    }
    url = URL + "/v1/app/send/msg"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200