# -*- coding:utf-8 -*-
from Utils.CommonMethod import CommonMethod

class LoginPage(CommonMethod):
    """description of class"""
    # page element identifier
    username_lct = ('ID', 'username')
    pwd_lct = ('ID', 'pwd')
    login_lct = ('ID', 'submit_login')
    assertinfo_lct = ('XPATH', ".//*[@id='form1']/div[4]/table/tbody/tr/td[2]/b")

    # 输入用户
    def set_username(self, username):
        name = self.findElement(self.username_lct)
        self.send_key(name, username)

    # 输入密码
    def set_password(self, password):
        pwd = self.findElement(self.pwd_lct)
        self.send_key(pwd, password)

    # 点击登录
    def click_SignIn(self):
        submitbtn = self.findElement(self.login_lct)
        self.click(submitbtn)

    # 检查是否登录成功
    def get_assertinfo(self):
        infolct = self.findElement(self.assertinfo_lct)
        info = infolct.text
        return info

#login_page = LoginPage(webdriver.Chrome('C:\Python27\chromedriver2.28.exe'))
#login_page.driver.get('http://cs-srm.jianke.com')
#login_page.set_username('jiangchunxiao')
#login_page.set_password('xiao19940415')
#login_page.click_SignIn()
#time.sleep(5)
#print login_page.get_assertinfo()