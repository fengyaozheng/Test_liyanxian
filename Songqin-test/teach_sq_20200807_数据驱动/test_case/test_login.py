#自动化执行excel用例
#1- 先获取对应的用例数据
from tools.excelMethod import get_excelData,set_excelData
from lib.apiLib.login import Login
import json,os
import pytest
# testData = get_excelData('1-登录接口',2,5)#列表[(bdoy,repsData),(),(),()]
#测试类--登录模块
class TestLogin:
    #数据驱动
    @pytest.mark.parametrize('body,repsData',get_excelData('1-登录接口',2,5))
    def test_login(self,body,repsData):
        res = Login().login(body,flag=True)#获取登录的响应数据
        assert res['retcode']== json.loads(repsData)['retcode']#断言

if __name__ == '__main__':
    #使用pytest框架，执行对应的模块，生成报告需要的数据文件  放到../report/tmp
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])

    #方案一：直接生成报告
    #os.system('allure generate ../report/tmp -o  ../report/report --clean')
    #方案二：直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')
