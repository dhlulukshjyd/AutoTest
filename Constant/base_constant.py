# coding:utf-8

# 采购模块
purbtn_lct = ('XPATH', ".//*[@id='ext-gen46']/em/span/span")
# 采购-采购订单管理
purordermngbtn_lct = ('XPATH',".//*[@id='extdd-13']/img[1]")
# 采购-自定义计划管理
purmngbtn_lct = ('XPATH', ".//*[@id='extdd-19']/img[1]")


def chromedriverpath():
    return r'C:\Python27\chromedriver2.28.exe'

def baseurl():
    return "http://cs-srm.jianke.com"

def dbhost():
    return '**'

def dbuser():
    return '**'

def dbpwd():
    return '***'

def db():
    return 'Latent_Export'

