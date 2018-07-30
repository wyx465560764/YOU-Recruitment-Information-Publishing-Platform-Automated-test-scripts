
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Login(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("http://localhost:8080")
        #self.driver.find_element_by_xpath('//*[@id="show"]/a').click()
        elem = self.driver.find_element_by_id('login')
        ActionChains(self.driver).move_to_element(elem).perform()
        time.sleep(2)
        #self.driver.find_element_by_xpath('//*[@id="show"]/a').click()
        self.driver.find_element_by_link_text(u"请登录").click()
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        self.driver.find_element_by_id('account').send_keys('12')
        self.driver.find_element_by_id('password').send_keys('12')
        self.driver.find_element_by_id('submitLogin').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.title,u'邮招聘信息发布平台')
        # print('登录成功')
        #self.driver.find_element_by_xpath('//*[@id="head"]/div/div[2]/div[2]/a').click()
        #time.sleep(3)
    def test_loginUsernull(self):
        self.driver.find_element_by_id('account').clear()
        self.driver.find_element_by_id('password').send_keys('12')
        self.driver.find_element_by_id('submitLogin').click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.title,"登录界面")
    def test_findPasswordNotSame(self):
        self.driver.find_element_by_id("resetPassword").click()
        self.driver.find_element_by_id("employeeName").send_keys('12')
        self.driver.find_element_by_id("phone").send_keys('12')
        self.driver.find_element_by_id("answer").send_keys('12')
        self.driver.find_element_by_id("password").send_keys('12')
        self.driver.find_element_by_id("rePassword").send_keys('123')
        self.driver.find_element_by_id("personRegister").click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual('找回密码',self.driver.title)
    def test_findPassword(self):
        self.driver.find_element_by_id("resetPassword").click()
        self.driver.find_element_by_id("employeeName").send_keys('12')
        self.driver.find_element_by_id("phone").send_keys('12')
        self.driver.find_element_by_id("answer").send_keys('12')
        self.driver.find_element_by_id("password").send_keys('12')
        self.driver.find_element_by_id("rePassword").send_keys('12')
        self.driver.find_element_by_id("personRegister").click()
        self.driver.switch_to_alert().accept()
        self.assertNotEqual(self.driver.title,'找回密码')
    def test_findPasswordError(self):
        self.driver.find_element_by_id("resetPassword").click()
        self.driver.find_element_by_id("employeeName").send_keys('12')
        self.driver.find_element_by_id("phone").send_keys('123')
        self.driver.find_element_by_id("answer").send_keys('123')
        self.driver.find_element_by_id("password").send_keys('12')
        self.driver.find_element_by_id("rePassword").send_keys('12')
        self.driver.find_element_by_id("personRegister").click()
        self.driver.switch_to_alert().accept()
        self.assertNotEqual(self.driver.title,'登录密码')
