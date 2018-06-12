# -*- coding:utf-8 -*-

from selenium import webdriver
from Utils.CommonMethod import CommonMethod
from Case.p3_PendingPurchasePlan_Case import PendingPurchasePlan_Case
import Utils.TestCaseLog
from Utils.TestCaseInfo import TestCaseInfo
from Utils.TestResult import TestReport
import time,unittest, sys
import Constant.base_constant as constant
import Data.l1_Login_Data
import Data.p3_PendingPurchasePlan_Data as pppd

reload(sys)
sys.setdefaultencoding('utf8')

class PendingPurchasePlan_Test_Case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(constant.chromedriverpath())
        self.baseurl = constant.baseurl()
        self.testcaseinfo = TestCaseInfo(4,"PendingPurchasePlan-test","jiangchunxiao")
        self.testResult = TestReport()
        Utils.TestCaseLog.CreateLoggerFile("Test_PendingPurchasePlan")

    def test_pendingpurchaseplan(self):
        cm = CommonMethod(self.driver)
        pendingplan = PendingPurchasePlan_Case(self.driver)
        try:
            self.testcaseinfo.starttime = cm.getCurrentTime()
            Utils.TestCaseLog.Log("Open the Base Site " + self.baseurl)

            # 打开SRM网页
            self.driver.get(self.baseurl)
            # 放大网页
            self.driver.maximize_window()

            # 登录SRM
            pendingplan.set_username(Data.l1_Login_Data.username())
            pendingplan.set_password(Data.l1_Login_Data.password())
            pendingplan.click_SignIn()
            pendingplan.accept_alert()
            time.sleep(1)
            self.driver.get(self.baseurl)

            # 打开待处理采购计划页面
            time.sleep(5)
            pendingplan.open_pending_page()

            # 搜索计划
            pendingplan.searchplan(pppd.starttime(), pppd.endtime(), pppd.ordercode(),pppd.productname(),
                                   pppd.warehouse(), pppd.operatorname(), pppd.plantype(), pppd.orderstatus())
            #pendingplan.searchplan(pppd.ordercode())
            # 编辑采购计划，生成采购订单
            pendingplan.editplan()
            cm.accept_alert()
            time.sleep(1)
            cm.accept_alert()

            # 写入报告Pass
            time.sleep(3)
            text = pendingplan.get_assertinfo()
            self.assertEqual(text, Data.p3_PendingPurchasePlan_Data.ordercode())
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
