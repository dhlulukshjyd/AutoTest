# -*- coding: utf-8 -*-
# Author: jiangchunxiao
import time, sys
from Page.p1_PurchacePlanApply import addPurchasePlan
import Data.l1_Login_Data
import Data.p1_PurchasePlanApply_Data
import Utils.TestCaseLog

reload(sys)
sys.setdefaultencoding('utf8')

class PurchaseApply_Case(addPurchasePlan):
    # 打开申请页面
    def open_apply_page(self):
        self.click_purbtn()
        time.sleep(1)
        self.click_purmngbtn()
        time.sleep(1)
        self.click_prchsPlanApply()
        print "Success to open the PurchasePlanApply page"
        Utils.TestCaseLog.Log("open the PurchasePlanApply page")


    # 选择仓库、商品
    def choose_apply_wh_good(self):
        time.sleep(2)
        self.switchframe(Data.p1_PurchasePlanApply_Data.frameid())
        # 选择仓库
        self.choose_warehouse(Data.p1_PurchasePlanApply_Data.warehousevalue())
        self.click_chooseProductbtn()
        # 切换窗口frame
        self.switchframe(Data.p1_PurchasePlanApply_Data.windowframeid())
        time.sleep(2)
        # 选择商品
        self.productname(Data.p1_PurchasePlanApply_Data.productcode())
        self.click_search()
        time.sleep(1)
        self.chooseproduct()
        self.click_confirm()
        print "Start to choose the purchase-product"
        Utils.TestCaseLog.Log("Choose the purchase-product")
        # 切换回主frame
        self.switchframe(Data.p1_PurchasePlanApply_Data.frameid())

    # 选择价格、供应商、数量、原因
    def choose_apply_price_num(self):
        # 输入采购价格
        time.sleep(2)
        self.purchaseprice(Data.p1_PurchasePlanApply_Data.purchaseprice())
        print "Start to input the purchaseprice"
        Utils.TestCaseLog.Log("Input the purchaseprice")
        time.sleep(1)
        # 输入采购数量
        self.productamount(Data.p1_PurchasePlanApply_Data.productamount())
        # 选择采购原因
        self.choosereason(Data.p1_PurchasePlanApply_Data.reasonvalue())
        # 选择供应商
        self.click_supplierbtn()
        time.sleep(2)
        self.switchframe(Data.p1_PurchasePlanApply_Data.windowframeid())
        self.inputsuppliername(Data.p1_PurchasePlanApply_Data.suppliername())
        self.click_suppliersearch()
        time.sleep(1)
        self.choosesupplier()
        self.driver.switch_to.parent_frame()
        # pplanapply.supplier(Data.PurchasePlanApply_Data.suppliername())
        time.sleep(2)

    # 提交采购单
    def submit_apply(self):
        self.submit()
        time.sleep(1)
        self.accept_alert()
        Utils.TestCaseLog.Log("Test Success")


