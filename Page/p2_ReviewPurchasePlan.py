# -*- coding:utf-8 -*-

from l1_LoginPage import LoginPage
import Constant.base_constant


class ReviewPlan(LoginPage):
    reviewpage_lct = ('ID', "extdd-48")
    starttime_lct = ('ID', "txtDateStart")
    endtime_lct = ('ID', "txtDateEnd")
    planorder_lct = ('ID', "txtPlanNumber")
    warehouse_lct = ('ID', "ddlWarehouse")
    productname_lct = ('ID', "txtProductName")
    operator_lct = ('ID', "txtOperateName")
    searchbtn_lct = ('ID', "btnSearch")
    reviewbtn_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[6]/a[1]")
    log_lct = ('XPATH',".//*[@id='form1']/table[3]/tbody/tr[2]/td[6]/a[2]")
    reviewopinion_lct = ('ID', "ddlOpinion")
    passbtn_lct = ('ID', "btnSumbit")
    failbtn_lct = ('ID', "btnStop")
    assertinfo_lct = ('ID',"lbTitle")

    # 打开申请页面
    def click_purbtn(self):
        purchasebtn = self.findElement(Constant.base_constant.purbtn_lct)
        self.click(purchasebtn)

    def click_purmngbtn(self):
        puchaseMenubtn = self.findElement(Constant.base_constant.purmngbtn_lct)
        self.click(puchaseMenubtn)

    def click_prchsPlanReview(self):
        reviewbtn = self.findElement(self.reviewpage_lct)
        self.click(reviewbtn)

    # 输入查询条件
    def choose_starttime(self, starttime):
        stime = self.findElement(self.starttime_lct)
        self.send_key(stime, starttime)

    def choose_endtime(self, endtime):
        etime = self.findElement(self.endtime_lct)
        self.send_key(etime, endtime)

    def input_planorder(self, planorder):
        porder = self.findElement(self.planorder_lct)
        self.send_key(porder, planorder)

    def input_productname(self, prodcutname):
        pn = self.findElement(self.productname_lct)
        self.send_key(pn, prodcutname)

    def choose_warehouse(self, warehouse):
        wh = self.findElement(self.warehouse_lct)
        self.select_value(wh, warehouse)

    def input_operator(self, operatorname):
        oper = self.findElement(self.operator_lct)
        self.send_key(oper, operatorname)

    # 点击搜索
    def click_search(self):
        searchbtn = self.findElement(self.searchbtn_lct)
        self.click(searchbtn)

    # 点击审核
    def click_review(self):
        review = self.findElement(self.reviewbtn_lct)
        self.click(review)

    # 点击日志
    def click_log(self):
        log = self.findElement(self.log_lct)
        self.click(log)

    # 选择审批意见
    def choose_rp(self, value):
        review_opinion = self.findElement(self.reviewopinion_lct)
        self.select_value(review_opinion, value)

    # 点击通过
    def click_pass(self):
        clickpass = self.findElement(self.passbtn_lct)
        self.click(clickpass)

    # 点击打回
    def click_fail(self):
        clickfail = self.findElement(self.failbtn_lct)
        self.click(clickfail)

    # 断言是否审核成功
    def get_assertinfo(self):
        assertinfo = self.findElement(self.assertinfo_lct)
        info = assertinfo.text
        return info













