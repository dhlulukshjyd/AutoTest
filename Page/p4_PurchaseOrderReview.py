# -*- coding:utf-8 -*-
from Page.l1_LoginPage import LoginPage
import Constant.base_constant


class PurchaseOrderReview(LoginPage):
    reviewpurchaseorder_lct = ('ID', 'extdd-57')
    ordercode_lct = ('ID', 'txtFormNumber')
    productname_lct = ('ID', 'txtProductName')
    warehouse_lct = ('ID', 'ddlWarehouse')
    supplier_lct = ('ID', 'txtSupplier')
    operator_lct = ('ID', 'txtOperateName')
    producttype_lct = ('ID', 'ddlProductCategory')
    ordertype_lct = ('ID', 'ddlPurchaseOrderFormType')
    starttime_lct = ('ID', 'txtDateStart')
    endtime_lct = ('ID', 'txtDateEnd')
    confirm_lct = ('ID', 'rblIsSupplierConfirming_0')
    isconfirm_lct = ('ID','rblIsSupplierConfirming_1')
    notconfirm_lct = ('ID', 'rblIsSupplierConfirming_2')
    searchbtn_lct = ('ID', 'btnSearch')
    orderdata_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[1]/input")
    reviewbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[8]/a[1]")
    editbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[8]/a[2]")
    logbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[8]/a[3]")
    confitmbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[8]/a[4]")
    mergebtn_lct = ('ID', "btnMerge")
    review_productname = ('ID', "txtProductName")
    review_producttype = ('ID', "ddlProductCategory")
    review_searchbtn = ('ID', "btnSearch")
    review_outexcel = ('ID', "btn_OutExcel")
    review_pass = ('ID', "btnPass")
    review_failed = ('ID', "btnRefuse")
    assertinfo_lct = ('ID', "lbTitle")

    # 打开审核采购订单页面
    def click_purbtn(self):
        pb = self.findElement(Constant.base_constant.purbtn_lct)
        self.click(pb)

    def click_purordermg(self):
        pm = self.findElement(Constant.base_constant.purordermngbtn_lct)
        self.click(pm)

    def click_revieworder(self):
        ro = self.findElement(self.reviewpurchaseorder_lct)
        self.click(ro)

    # 输入搜索条件
    def input_ordercode(self, ordercode):
        oc = self.findElement(self.ordercode_lct)
        self.send_key(oc, ordercode)

    def input_productname(self,productname):
        pn = self.findElement(self.productname_lct)
        self.send_key(pn, productname)

    def choose_warehouse(self, warehouse):
        wh = self.findElement(self.warehouse_lct)
        self.select_value(wh, warehouse)

    def input_supplier(self, supplier):
        sp = self.findElement(self.supplier_lct)
        self.send_key(sp, supplier)

    def input_operator(self, operator):
        op = self.findElement(self.operator_lct)
        self.send_key(op, operator)

    def choose_producttype(self, producttype):
        pt = self.findElement(self.producttype_lct)
        self.select_value(pt, producttype)

    def choose_ordertype(self, ordertype):
        ot = self.findElement(self.ordertype_lct)
        self.select_value(ot, ordertype)

    def click_all(self):
        ac = self.findElement(self.confirm_lct)
        self.click(ac)

    def click_isconfirm(self):
        ic = self.findElement(self.isconfirm_lct)
        self.click(ic)

    def click_notconfirm(self):
        nc = self.findElement(self.notconfirm_lct)
        self.click(nc)

    def choose_starttime(self, starttime):
        st = self.findElement(self.starttime_lct)
        self.send_key(st, starttime)

    def choose_endtime(self, endtime):
        et = self.findElement(self.endtime_lct)
        self.send_key(et, endtime)

    # 点击搜索
    def click_searchbtn(self):
        sb = self.findElement(self.searchbtn_lct)
        self.click(sb)

    # 点击合并
    def click_mergebtn(self):
        mb = self.findElement(self.mergebtn_lct)
        self.click(mb)

    # 点击审核
    def click_reviewbtn(self):
        rb = self.findElement(self.reviewbtn_lct)
        self.click(rb)

    # 点击编辑
    def click_editbtn(self):
        eb = self.findElement(self.editbtn_lct)
        self.click(eb)

    # 点击日志
    def click_logbtn(self):
        lb = self.findElement(self.logbtn_lct)
        self.click(lb)

    # 点击确认
    def click_confirmbtn(self):
        cb = self.findElement(self.confitmbtn_lct)
        self.click(cb)

    # 点击审核通过
    def click_reviewpass(self):
        rp = self.findElement(self.review_pass)
        self.click(rp)

    # 点击审核失败
    def click_reviewfail(self):
        rf = self.findElement(self.review_failed)
        self.click(rf)

    # 断言
    def assertinfo(self):
        af = self.findElement(self.assertinfo_lct)
        info = af.text
        return info


