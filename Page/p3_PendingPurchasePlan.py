# -*- coding:utf-8 -*-

from l1_LoginPage import LoginPage
import Constant.base_constant
import time

class PendingPurchasePlan(LoginPage):

    pendingpp_lct = ('ID', "extdd-48")
    starttime_lct = ('ID', "txtDateStart")
    endtime_lct = ('ID', "txtDateEnd")
    ordercode_lct = ('ID', "txtPlanNumber")
    operator_lct = ('ID', "txtOperateName")
    plantype_lct = ('ID', "ddlPlanType")
    orderstatus_lct = ('ID', "ddlStatus")
    warehouse_lct = ('ID', "ddlWarehouse")
    productname_lct = ('ID', "txtProductName")
    status_0_lct = ('ID', "rblIsCreate_0")
    status_1_lct = ('ID', "rblIsCreate_1")
    status_2_lct = ('ID', "rblIsCreate_2")
    searchbtn_lct = ('ID', "btnSearch")
    editbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[8]/a[1]")
    stopbtn_lct = ('ID', "RptPurchaseOrderFormList_btnStop_0")
    planoutside_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[1]")
    mergebtn_lct = ('ID', "btnMerge")
    planinside_lct = ('ID', "chk_1")
    createpurchseorder_lct = ('ID', "btnSumbit")
    assertinfo_lct = ('ID', "lbNumber")

    # 打开待处理采购计划页面
    def click_purbtn(self):
        purchasebtn = self.findElement(Constant.base_constant.purbtn_lct)
        self.click(purchasebtn)

    def click_purordermngbtn(self):
        puchaseMenubtn = self.findElement(Constant.base_constant.purordermngbtn_lct)
        self.click(puchaseMenubtn)

    def click_pendingpp(self):
        pendingpp = self.findElement(self.pendingpp_lct)
        self.click(pendingpp)

    # 输入查询条件
    def choose_starttime(self, starttime):
        stime = self.findElement(self.starttime_lct)
        self.clear(stime)
        time.sleep(1)
        self.send_key(stime, starttime)
        print 'input time success'

    def choose_endtime(self, endtime):
        etime = self.findElement(self.endtime_lct)
        self.clear(etime)
        time.sleep(1)
        self.send_key(etime, endtime)
        print 'input endtime success'

    def input_ordercode(self, ordercode):
        oc = self.findElement(self.ordercode_lct)
        self.send_key(oc, ordercode)

    def input_productname(self, productname):
        pn = self.findElement(self.productname_lct)
        self.send_key(pn, productname)

    def choose_warehouse(self, warehouse):
        wh = self.findElement(self.warehouse_lct)
        self.select_value(wh, warehouse)

    def input_operator(self, operatorname):
        oper = self.findElement(self.operator_lct)
        self.send_key(oper, operatorname)

    def choose_plantype(self, plantype):
        pt = self.findElement(self.plantype_lct)
        self.select_value(pt, plantype)
        print 'input plantype success'

    def choose_orderstatus(self, orderstatus):
        os = self.findElement(self.orderstatus_lct)
        self.select_value(os, orderstatus)
        print 'input plantype success'

    def click_all(self):
        the_all = self.findElement(self.status_0_lct)
        self.click(the_all)

    def click_finished(self):
        finish = self.findElement(self.status_1_lct)
        self.click(finish)

    def click_notfinished(self):
        notfinish = self.findElement(self.status_2_lct)
        self.click(notfinish)

    # 点击搜索
    def click_search(self):
        sc = self.findElement(self.searchbtn_lct)
        self.click(sc)

    # 勾选采购计划
    def choose_planoutside(self):
        po = self.findElement(self.planoutside_lct)
        self.click(po)

    # 点击编辑
    def click_edit(self):
        et = self.findElement(self.editbtn_lct)
        self.click(et)

    # 点击中止
    def click_stop(self):
        sp = self.findElement(self.stopbtn_lct)
        self.click(sp)

    # 点击合并采购计划
    def click_merge(self):
        mg = self.findElement(self.mergebtn_lct)
        self.click(mg)

    # 勾选采购明细
    def choose_planinside(self):
        pi = self.findElement(self.planinside_lct)
        self.click(pi)

    # 点击生成采购订单
    def click_createorder(self):
        co = self.findElement(self.createpurchseorder_lct)
        self.click(co)

    def get_assertinfo(self):
        assertinfo = self.findElement(self.assertinfo_lct)
        info = assertinfo.text
        return info





