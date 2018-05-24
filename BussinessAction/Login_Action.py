# -*- coding: utf-8 -*-
from selenium import webdriver
import Constant.base_constant as constant
from Utils.TestCaseInfo import TestCaseInfo
from Utils.TestResult import TestReport
from Utils.CommonMethod import CommonMethod
from Case.LoginPage_Case import LoginPage_Case
import Utils.TestCaseLog
import unittest, time, sys

reload(sys)
sys.setdefaultencoding('utf8')



class LoginPage_Test_Case(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(constant.chromedriverpath())
        self.base_url = constant.baseurl()
        self.testcaseinfo = TestCaseInfo(1, "Login-test", 'jiangchunxiao')
        self.testResult = TestReport()
        Utils.TestCaseLog.CreateLoggerFile("Test_Login")

    def test_login(self):
        cm = CommonMethod(self.driver)
        lg = LoginPage_Case(self.driver)
        try:
            self.testcaseinfo.starttime = cm.getCurrentTime()
            # 打开SRM网页
            Utils.TestCaseLog.Log("Open Base Site " + self.base_url)
            self.driver.get(self.base_url)
            self.driver.maximize_window()

            # 登录SRM
            lg.login()
            # 确认弹窗
            lg.accept_alert()
            # 重新访问该网页
            self.driver.get(self.base_url)
            time.sleep(5)

            # 断言是否登录成功
            text = lg.getassertinfo()
            self.assertEqual(text, "运维部报障电话：33331254")
            self.testcaseinfo.result = "Pass"
            Utils.TestCaseLog.Log("Test Pass")

        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
            Utils.TestCaseLog.Log(("Got error: " + str(err)))
            self.testcaseinfo.result = "Failed"
            Utils.TestCaseLog.Log("Test Failed")

        finally:
            self.testcaseinfo.endtime = cm.getCurrentTime()
            self.testcaseinfo.secondsDuration = cm.timeDiff(self.testcaseinfo.starttime, self.testcaseinfo.endtime)
            Utils.TestCaseLog.Log("Ran 1 test in %s" % self.testcaseinfo.secondsDuration)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()
        self.testResult.WriteHTML(self.testcaseinfo)


if __name__ == '__main__':
    unittest.main()








