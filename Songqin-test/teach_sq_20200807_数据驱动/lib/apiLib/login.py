#1- 使用请求库 requests
import requests,json
#2- url---考虑可维护性--
from config import HOST
import json
class Login:
    def login(self,inData,flag=False):#登录方法
        url = f'{HOST}/api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = json.loads(inData)#字符串---变成----字典
        reps = requests.post(url, data=payload)
        if flag == False:#这个登录的接口会作为后续接口的前置条件
            return reps.cookies['sessionid']
        else:#本身这个登录接口需要调用
            return reps.json()

if __name__ == '__main__':#   ctrl+j
    res = Login().login({'username':'auto','password':'sdfsdfsdf'},True)
    print(res)