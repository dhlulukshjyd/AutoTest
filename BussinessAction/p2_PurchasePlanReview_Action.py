# -*- coding: utf-8 -*-
from Case.p2_PurchasePlanReview_Case import PurchaseReview_Case
import unittest, time, sys
from selenium import webdriver
from  Utils.TestCaseInfo import TestCaseInfo
from Utils.CommonMethod import CommonMethod
from Utils.TestResult import TestReport
import Data.l1_Login_Data
import Data.p2_PurchasePlanReview_Data as rppd
import Utils.TestCaseLog
import Constant.base_constant as constant

reload(sys)
sys.setdefaultencoding('utf8')

class PurchasePlanReview_Test_Case(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(constant.chromedriverpath())
        self.baseurl = constant.baseurl()
        self.testcaseinfo = TestCaseInfo(3, "PurchasePlanReview-test", "jiangchunxiao")
        self.testResult = TestReport()
        Utils.TestCaseLog.CreateLoggerFile("Test_PurchasePlanReview")

    def test_purchaseplanreview(self):
        cm = CommonMethod(self.driver)
        try:
            self.testcaseinfo.starttime = cm.getCurrentTime()
            Utils.TestCaseLog.Log("Open the Base Site " + self.baseurl)

            # 打开SRM网页
            self.driver.get(self.baseurl)
            # 放大网页
            self.driver.maximize_window()

            # 登录SRM
            ppreview = PurchaseReview_Case(self.driver)
            ppreview.set_username(Data.l1_Login_Data.username())
            ppreview.set_password(Data.l1_Login_Data.password())
            ppreview.click_SignIn()
            ppreview.accept_alert()
            time.sleep(1)
            self.driver.get(self.baseurl)

            # 打开页面
            time.sleep(5)
            ppreview.open_apply_page()

            # 搜索
            sql_sentence = 'SELECT Number FROM Latent_Export.dbo.CustomizePurchasePlanForm WHERE FormStatus = 3 '
            '''planorder = cm.connect_db(constant.dbhost(),constant.db(),constant.dbuser(),constant.dbpwd(),sql_sentence)
            ppreview.searchplan(planorder, rppd.warehouse(), rppd.productname(), rppd.operator())'''
            ppreview.searchplan(rppd.planorder(), rppd.warehouse(), rppd.productname(), rppd.operator())

            # 审核通过
            ppreview.reviewpass()

            # 写入报告Pass
            time.sleep(3)
            text = ppreview.get_assertinfo()
            self.assertEqual(text, "自定义采购计划审批")
            self.testcaseinfo.result = 'Pass'

        except Exception as err:
            self.testcaseinfo.errorInfo = str(err)
            Utils.TestCaseLog.Log(("Got error: " + str(err)))
            self.testcaseinfo.result = "Failed"
            Utils.TestCaseLog.Log("Test Failed")
        finally:
            self.testcaseinfo.endtime = cm.getCurrentTime()
            self.testcaseinfo.secondsDuration = cm.timeDiff(self.testcaseinfo.starttime, self.testcaseinfo.endtime)
            Utils.TestCaseLog.Log("Ran 1 test in %s" % self.testcaseinfo.secondsDuration)

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
        self.testResult.WriteHTML(self.testcaseinfo)


if __name__ == '__main__':
        unittest.main()

