#这个模块，有没有前置：先登录  cookie
from config import HOST
import requests
# from login import Login
# import json
class Lesson:
    def __init__(self,sessionId):#
        self.cookie = {'sessionid':sessionId}#cookie
        self.url = f'{HOST}/api/mgr/sq_mgr/'#url
    #1- 课程-新增
    def lesson_add(self,inBody):
        payload = {
                    'action':'add_course',
                    'data':inBody
        }
        reps = requests.post(self.url,data=payload,cookies = self.cookie)
        reps.encoding = 'unicode_escape'
        return reps.json()
    #2- 课程-列出
    def lesson_list(self,inBody):
        payload = inBody
        reps = requests.get(self.url,params=payload,cookies = self.cookie)
        reps.encoding = 'unicode_escape'
        return reps.json()
    #3- 课程-删除
    def lesson_delete(self,inBody):
        payload = {
                    'action':'delete_course',
                    'id':int(inBody)
        }
        reps = requests.delete(self.url,data=payload,cookies = self.cookie)
        reps.encoding = 'unicode_escape'
        return reps.json()
    #4- 课程-修改
    def lesson_delete(self):
        pass

#1-课程新增操作--验证
# testData = '''{ "name":"初中化学", "desc":"初中化学课程", "display_idx":"4" }'''
# sessionId = Login().login(json.dumps({'username':'auto','password':'sdfsdfsdf'}))
# # print(Lesson(sessiona).lesson_add(testData))
# 2- 列出课程--验证
# testData2 = { "action":"list_course", "pagenum":1,"pagesize":20 }
# import pprint
# pprint.pprint(Lesson(sessionId).lesson_list(testData2))


#删除课程---可以作为环境初始化
#1- 列出所有的
#2- 执行删除的id
# for one in Lesson(sessionId).lesson_list(testData2)['retlist']:#返回是list
#     Lesson(sessionId).lesson_delete(one['id'])
#
# #创建一批测试数据---新增课程
# testData3 = '''{ "name":"初中化学", "desc":"初中化学课程", "display_idx":"4" }'''
# Lesson(sessionId).lesson_add(testData3)

