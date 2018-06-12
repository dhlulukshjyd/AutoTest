# -*- coding:utf-8 -*-

from selenium import webdriver
from Utils.CommonMethod import CommonMethod
from Case.p4_PurchaseOrderReview_Case import PurchaseOrderReview_Case
import Utils.TestCaseLog
from Utils.TestCaseInfo import TestCaseInfo
from Utils.TestResult import TestReport
import time, unittest, sys
import Constant.base_constant as constant
import Data.l1_Login_Data
import Data.p4_PurchaseOrderReview_Data as pord

reload(sys)
sys.setdefaultencoding('utf8')

class PurchaseOrderReview_Test_Case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(constant.chromedriverpath())
        self.baseurl = constant.baseurl()
        self.testcaseinfo = TestCaseInfo(5,"PurchaseOrderReview-test","jiangchunxiao")
        self.testResult = TestReport()
        Utils.TestCaseLog.CreateLoggerFile("Test_PurchaseOrderReview")

    def test_PurchaseOrderReview(self):
        cm = CommonMethod(self.driver)
        purchaseorder = PurchaseOrderReview_Case(self.driver)
        try:
            self.testcaseinfo.starttime = cm.getCurrentTime()
            Utils.TestCaseLog.Log("Open the Base Site " + self.baseurl)

            # 打开SRM网页
            self.driver.get(self.baseurl)
            # 放大网页
            self.driver.maximize_window()

            # 登录SRM
            purchaseorder.set_username(Data.l1_Login_Data.username())
            purchaseorder.set_password(Data.l1_Login_Data.password())
            purchaseorder.click_SignIn()
            purchaseorder.accept_alert()
            time.sleep(1)
            self.driver.get(self.baseurl)

            # 打开审核采购订单页面
            time.sleep(5)
            purchaseorder.open_review_page()

            # 搜索采购订单
            purchaseorder.searchorder(pord.ordercode(), pord.productname(), pord.warehouse(), pord.supplier(),
                                 pord.operator(), pord.prodcuttype(), pord.ordertype(), pord.starttime(),
                                 pord.endtime())

            # 审核通过
            purchaseorder.reviewpass()

            # 写入报告Pass
            time.sleep(3)
            text = purchaseorder.get_assertinfo()
            self.assertEqual(text, "审核采购订单")
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
