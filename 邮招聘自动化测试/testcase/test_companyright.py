import unittest
import time
from selenium import webdriver

class companyright(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.get("http://localhost:8080")
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
        self.driver.add_cookie({'name':'username','value':'12'})
        self.driver.refresh()
        #self.driver.find_element_by_id('account').send_keys('12')
        #self.driver.find_element_by_id('password').send_keys('12')
        #self.driver.find_element_by_id('submitLogin').click()
        #self.driver.switch_to_alert().accept()
    def tearDown(self):
        self.driver.quit()
    def test_companyToAddRecruit(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[3]/div/a/i').click()  
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="add"]/div/form/div[1]/div[1]/ul/li[1]/div[1]').text,'公司名称：')
    def test_companyToAddResume(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[2]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input[1]').click()
        text=self.driver.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(text,'你的身份不是学生，不能录入信息')
        self.driver.switch_to_alert().accept()
    def test_companyToSeeResume(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        name=self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[1]').text
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[2]/b').text,name+'个人简历信息')
        