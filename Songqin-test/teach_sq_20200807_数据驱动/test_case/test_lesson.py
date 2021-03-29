#课程模块--测试类
import pytest
from lib.apiLib.login import Login
from lib.apiLib.lesson import Lesson
from tools.excelMethod import get_excelData
import json
import os
class TestLesson:
    def setup_class(self):
        print('----类级别，只要调用这个测试类，我就第一个执行')
        self.session = Login().login(json.dumps({'username':'auto','password':'sdfsdfsdf'}))

    #1- 课程新增
    @pytest.mark.parametrize('body,repsData',get_excelData('2-课程模块',2,3))
    def test_lesson_add(self,body,repsData):
        res = Lesson(self.session).lesson_add(body)
        assert res['retcode']== json.loads(repsData)['retcode']

if __name__ == '__main__':
    #使用pytest框架，执行对应的模块，生成报告需要的数据文件  放到../report/tmp
    pytest.main(['test_lesson.py','-s','--alluredir','../report/tmp'])
    # pytest.main(['test_lesson.py', '-s'])
    #方案一：直接生成报告
    #os.system('allure generate ../report/tmp -o  ../report/report --clean')
    #方案二：直接启动一个服务，自动打开浏览器
    os.system('allure serve ../report/tmp')