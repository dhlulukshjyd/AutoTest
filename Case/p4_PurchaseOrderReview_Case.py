# -*- coding:utf-8 -*-
from Page.p4_PurchaseOrderReview import PurchaseOrderReview
import time
import Utils.TestCaseLog
import Data.p4_PurchaseOrderReview_Data
class PurchaseOrderReview_Case(PurchaseOrderReview):
    # 打开申请页面
    def open_review_page(self):
        self.click_purbtn()
        time.sleep(1)
        self.click_purordermg()
        time.sleep(1)
        self.click_revieworder()
        print "Success to open the PurchaseOrderReview page"
        Utils.TestCaseLog.Log("open the PurchaseOrderReview page")

    # 搜索
    def searchorder(self, ordercode, productname, warehouse, supplier,
                    operator, producttype, ordertype, starttime, endtime):
        time.sleep(3)
        self.switchframe(Data.p4_PurchaseOrderReview_Data.frameid())
        self.input_ordercode(ordercode)
        self.input_productname(productname)
        self.choose_warehouse(warehouse)
        self.input_supplier(supplier)
        self.input_operator(operator)
        self.choose_producttype(producttype)
        self.choose_ordertype(ordertype)
        self.choose_starttime(starttime)
        self.choose_endtime(endtime)
        time.sleep(1)
        self.click_searchbtn()
        time.sleep(2)

    # 点击审核
    def reviewpass(self):
        self.click_reviewbtn()
        self.switchframe(Data.p4_PurchaseOrderReview_Data.windowframeid())
        time.sleep(1)
        self.click_reviewpass()
        self.accept_alert()
        time.sleep(3)
        self.accept_alert()
        time.sleep(1)
        self.driver.switch_to.parent_frame()










