# -*- coding: utf-8 -*-
# Author: jiangchunxiao
import unittest, time, sys
from selenium import webdriver
from Case.PurchaseApply_Case import PurchaseApply_Case
from Page.AddPurchacePlan import addPurchasePlan
from Utils.TestCaseInfo import TestCaseInfo
from Utils.TestResult import TestReport
from Utils.CommonMethod import CommonMethod
import Data.Login_Data
import Data.PurchasePlanApply_Data
import Constant.base_constant as constant
import Utils.TestCaseLog

reload(sys)
sys.setdefaultencoding('utf8')

class PurchaseApply_Test_Case(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(constant.chromedriverpath())
        self.baseurl = constant.baseurl()
        self.testcaseinfo = TestCaseInfo(2,"PurchasePlanApply-test","jiangchunxiao")
        self.testResult = TestReport()
        Utils.TestCaseLog.CreateLoggerFile("Test_PurchasePlanApply")

    def test_purchaseplanapply(self):
        cm = CommonMethod(self.driver)
        pplanapply = PurchaseApply_Case(self.driver)
        try:
            self.testcaseinfo.starttime = cm.getCurrentTime()
            Utils.TestCaseLog.Log("Open the Base Site " + self.baseurl)
            # 打开SRM网页
            self.driver.get(self.baseurl)
            # 放大网页
            self.driver.maximize_window()

            # 登录SRM系统

            pplanapply.set_username(Data.Login_Data.username())
            pplanapply.set_password(Data.Login_Data.password())
            pplanapply.click_SignIn()
            pplanapply.accept_alert()
            time.sleep(3)
            self.driver.get(self.baseurl)

            #判断是否登录成功
            time.sleep(3)
            self.assertEqual(pplanapply.get_assertinfo(),"运维部报障电话：33331254")
            self.testcaseinfo.result = 'Pass'
            print "Login Success！"
            Utils.TestCaseLog.Log("Login Success！")

            # 打开申请页面
            pplanapply.open_apply_page()
            # 选择仓库、商品
            pplanapply.choose_apply_wh_good()
            # 选择价格、供应商、数量、原因
            pplanapply.choose_apply_price_num()
            # 提交采购单
            pplanapply.submit_apply()

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
        time.sleep(10)
        self.driver.close()
        self.testResult.WriteHTML(self.testcaseinfo)

if __name__ == '__main__':
        unittest.main()


