# import requests,json
# def get_token():
#     '''
#     请求登录接口，获取token
#     :return:
#     '''
#     headers = {"Content-Type": "application/json;charset=utf8"}
#     url = "http://jiecheng.api.sauou.com/doc.html#/home "
#     data = {
#         "username": "admin",
#         "password": "123456"
#     }
#     res = requests.post(url=url, headers=headers, json=data).text
#     res = json.loads(res)
#     print(res)
#     token = res["data"]
#     return token
#
# if __name__ == '__main__':
#    token = get_token() # 获取token

