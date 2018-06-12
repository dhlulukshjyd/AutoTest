# -*- coding: utf-8 -*-


from l1_LoginPage import LoginPage
import Constant.base_constant


class addPurchasePlan(LoginPage):
    prchsPlanApply_lct = ('XPATH', ".//*[@id='extdd-42']")
    warehouse_lct = ('ID', "ddlWareHouse")
    choosefile_lct = ('ID', "QuoteFileUpload")
    importfilebtn_lct = ('ID', "btnImport")
    chooseproductbtn_lct = ('XPATH', ".//*[@id='form1']/table[2]/tbody/tr/td[1]/input[1]")
    inputproductname_lct = ('ID',"tbProductName")
    selectproductclass_lct = ('ID', "ddlProductCategory")
    inputpacking_lct = ('ID', "tbPacking")
    inputfactory_lct = ('ID', "tbManufacturer")
    searchbtn_lct = ('ID', "btn_Sc")
    chooseproduct_lct = ('XPATH', ".//*[@id='form1']/table[3]/tbody/tr[2]/td[3]")
    confirmbtn_lct = ('XPATH', ".//*[@id='form1']/table[1]/tbody/tr/td/input[1]")
    productamount_lct = ('ID', "rptList_tbQuantity_0")
    choosereason_lct = ('ID', "rptList_purchaseReason_0")
    submitbtn_lct = ('ID', "btnSumbitSave")
    purchaseprice_lct = ('ID', "rptList_tbPrice_0")
    supplier_lct = ('ID', "rptList_tbSupplierName_0")
    suppliername_lct = ('ID', "txtSupplier")
    suppliersearchbtn_lct = ('ID', "btnSearch")
    choosesupplier_lct = ('XPATH', ".//*[@id='Form1']/table[2]/tbody/tr[2]/td[3]")

    # 打开申请页面
    def click_purbtn(self):
        applyMenubtn = self.findElement(Constant.base_constant.purbtn_lct)
        self.click(applyMenubtn)

    def click_purmngbtn(self):
        applyMenubtn = self.findElement(Constant.base_constant.purmngbtn_lct)
        self.click(applyMenubtn)

    def click_prchsPlanApply(self):
        applyMenubtn = self.findElement(self.prchsPlanApply_lct)
        self.click(applyMenubtn)

    # 选择仓库
    def choose_warehouse(self, wrhsvalue):
        choose_warehouse = self.findElement(self.warehouse_lct)
        self.select_value(choose_warehouse, wrhsvalue)

    # 选择文件
    def chooseFile(self, path):
        chooseFile = self.findElement(self.choosefile_lct)
        self.clear(chooseFile)
        self.send_key(chooseFile, path)

    # 导入文件
    def importfile(self):
        importfile = self.findElement(self.importfilebtn_lct)
        self.click(importfile)

    # 点击选择商品按钮
    def click_chooseProductbtn(self):
        chooseproductbbtn = self.findElement(self.chooseproductbtn_lct)
        self.click(chooseproductbbtn)

    # 搜索商品
    def productname(self, product):
        productname = self.findElement(self.inputproductname_lct)
        self.clear(productname)
        self.send_key(productname, product)

    def productclass(self, classvalue):
        productclass = self.findElement(self.selectproductclass_lct)
        self.select_value(productclass, classvalue)

    def productpacking(self, packing):
        productpacking = self.findElement(self.inputpacking_lct)
        self.send_key(productpacking, packing)

    def productfactoy(self, factory):
        productfactoy = self.findElement(self.inputfactory_lct)
        self.send_key(productfactoy, factory)

    def click_search(self):
        searchbtn = self.findElement(self.searchbtn_lct)
        self.click(searchbtn)

    # 选择商品
    def chooseproduct(self):
        chooseprouct = self.findElement(self.chooseproduct_lct)
        self.click(chooseprouct)

    # 点击确认按钮
    def click_confirm(self):
        confirm = self.findElement(self.confirmbtn_lct)
        self.click(confirm)

    #输入采购价格
    def purchaseprice(self,price):
        purchaseprice = self.findElement(self.purchaseprice_lct)
        self.clear(purchaseprice)
        self.send_key(purchaseprice, price)


    # 点击供应商按钮
    def click_supplierbtn(self):
        supplierbtn = self.findElement(self.supplier_lct)
        self.click(supplierbtn)

    # 搜索供应商
    def inputsuppliername(self, name):
        suppliername = self.findElement(self.suppliername_lct)
        self.send_key(suppliername, name)

    def click_suppliersearch(self):
        suppliersearchbth = self.findElement(self.suppliersearchbtn_lct)
        self.click(suppliersearchbth)

    def choosesupplier(self):
        choosesuplier = self.findElement(self.choosesupplier_lct)
        self.double_click(choosesuplier)


    # 输入产品数量
    def productamount(self, amount):
        productamount = self.findElement(self.productamount_lct)
        self.clear(productamount)
        self.send_key(productamount, amount)

    # 选择原因
    def choosereason(self, reasonvalue):
        choosereasonbtn = self.findElement(self.choosereason_lct)
        self.select_value(choosereasonbtn, reasonvalue)

    # 点击提交
    def submit(self):
        submit = self.findElement(self.submitbtn_lct)
        self.click(submit)



