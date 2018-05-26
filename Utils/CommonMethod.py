# coding:utf-8
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import pymssql

class CommonMethod(object):
    """description of class"""

    def __init__(self, driver):
        self.driver = driver

    # 连接sql server数据库
    def connect_db(self, host, database, user, pwd, sql_sentence):
        conn = pymssql.connect(host=host, database=database, user=user, password=pwd)
        cur = conn.cursor()
        try:
            cur.execute(sql_sentence)
            resultdata = cur.fetchone()
            return resultdata
        except Exception as e:
            print e
        finally:
            cur.close()
            conn.close()

    # 查找元素
    def findElement(self, element):
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    # 单击
    def click(self, element):
        element.click()

    # 清除
    def clear(self, element):
        element.clear()

    # 输入值
    def send_key(self, element, value):
        element.send_keys(value)

    # 选择下拉框
    def select_value(self, element, value):
        s1 = Select(element)
        s1.select_by_value(value)

    # 双击
    def double_click(self, element):
        a1 = ActionChains(self.driver)
        a1.double_click(element).perform()

    # 确定alert
    def accept_alert(self):
        alert = self.driver.switch_to_alert()
        time.sleep(2)
        alert.accept()

    # 切换iframe
    def switchframe(self, frameid):
        self.driver.switch_to.frame(frameid)

    # 切换window
    def switchwindow(self):
        currentWindowhandle =self.driver.current_window_handle
        print currentWindowhandle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != currentWindowhandle:
                self.driver.close()
                self.driver.switch_to.window(handle)

    # 当前时间转为字符串
    def getCurrentTime(self):
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.now().strftime(format)

    # 时间差
    def timeDiff(self, starttime, endtime):
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)




