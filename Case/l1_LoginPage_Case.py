# -*- coding: utf-8 -*-

import Data.l1_Login_Data
from Page.l1_LoginPage import LoginPage
import Utils.TestCaseLog
import time


class LoginPage_Case(LoginPage):
    # 登录SRM
    def login(self):
        Utils.TestCaseLog.Log("Login SRM System")
        login_page = LoginPage(self.driver)
        login_page.set_username(Data.l1_Login_Data.username())
        login_page.set_password(Data.l1_Login_Data.password())
        time.sleep(1)
        login_page.click_SignIn()

    # 获取断言信息
    def getassertinfo(self):
        Utils.TestCaseLog.Log("Check whether sign in dialog exists or not")
        login_page = LoginPage(self.driver)
        return login_page.get_assertinfo()







