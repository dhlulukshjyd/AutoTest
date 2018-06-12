# -*- coding:utf-8 -*-

from Page.p3_PendingPurchasePlan import PendingPurchasePlan
import Data.p3_PendingPurchasePlan_Data
import time
import Utils.TestCaseLog



class PendingPurchasePlan_Case(PendingPurchasePlan):
    # 打开申请页面
    def open_pending_page(self):
        self.click_purbtn()
        time.sleep(1)
        self.click_purordermngbtn()
        time.sleep(1)
        self.click_pendingpp()
        print "Success to open the PendingPurchasePlan page"
        Utils.TestCaseLog.Log("open the PendingPurchasePlan page")

    # 搜索
    def searchplan(self, starttime, endtime, ordercode, productname, warehouse, operatorname, plantype, orderstatus):
        self.switchframe(Data.p3_PendingPurchasePlan_Data.frameid())
        self.choose_starttime(starttime)
        self.choose_endtime(endtime)
        self.input_ordercode(ordercode)
        self.input_productname(productname)
        self.choose_warehouse(warehouse)
        self.input_operator(operatorname)
        self.choose_plantype(plantype)
        self.choose_orderstatus(orderstatus)
        self.click_search()
        time.sleep(2)

    # 编辑采购计划
    def editplan(self):
        self.click_edit()
        self.driver.switch_to.parent_frame()
        self.switchframe(Data.p3_PendingPurchasePlan_Data.createpoframeid())
        time.sleep(2)
        self.choose_planinside()
        self.click_createorder()








