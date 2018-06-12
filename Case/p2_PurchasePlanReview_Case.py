# -*- coding: utf-8 -*-
# Author: jiangchunxiao
import time, sys
from Page.p2_ReviewPurchasePlan import ReviewPlan
import Data.l1_Login_Data
import Data.p2_PurchasePlanReview_Data
import Utils.TestCaseLog

reload(sys)
sys.setdefaultencoding('utf8')

class PurchaseReview_Case(ReviewPlan):

    # 打开申请页面
    def open_apply_page(self):
        self.click_purbtn()
        time.sleep(1)
        self.click_purmngbtn()
        time.sleep(1)
        self.click_prchsPlanReview()
        print "Success to open the PurchasePlanReview page"
        Utils.TestCaseLog.Log("open the PurchasePlanApply page")

    # 采购单号搜索
    def searchplan(self, planorder, warehouse, productname, operator):
        time.sleep(2)
        self.switchframe(Data.p2_PurchasePlanReview_Data.frameid())
        self.input_planorder(planorder)
        self.choose_warehouse(warehouse)
        self.input_productname(productname)
        self.input_operator(operator)
        self.click_search()
        time.sleep(2)

    # 审核通过
    def reviewpass(self):
        self.click_review()
        self.switchframe(Data.p2_PurchasePlanReview_Data.windowframeid())
        self.click_pass()
        time.sleep(3)
        self.accept_alert()
        time.sleep(3)
        self.accept_alert()
        self.switchframe(Data.p2_PurchasePlanReview_Data.frameid())

    # 审核不通过
    def reviewfailed(self):
        self.click_review()
        self.switchframe(Data.p2_PurchasePlanReview_Data.windowframeid())
        self.choose_rp(Data.p2_PurchasePlanReview_Data.reviewopinion())
        self.click_fail()
        time.sleep(3)
        self.accept_alert()
        time.sleep(3)
        self.accept_alert()
        self.switchframe(Data.p2_PurchasePlanReview_Data.frameid())

