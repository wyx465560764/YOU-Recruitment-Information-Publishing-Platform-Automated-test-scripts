import unittest
import time
from selenium import webdriver

class studentright(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080")
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
        #self.driver.find_element_by_xpath('//*[@id="show"]/a').click()
       # self.driver.find_element_by_id('account').send_keys('学生')
       # self.driver.find_element_by_id('password').send_keys('123')
        #self.driver.find_element_by_id('submitLogin').click()
        #self.driver.switch_to_alert().accept()
        self.driver.add_cookie({'name':'username','value':'学生'})
        self.driver.refresh()
    def tearDown(self):
        self.driver.quit()
    def test_studentToAddRecruit(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[3]/div/a/i').click()
        text1=self.driver.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(text1,'没有权限发布招聘信息')
    def test_studentToChangeRecuit(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[1]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[7]/a[1]').click()
        text2=self.driver.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(text2,'没有修改权限')
    def test_studentToDeleteRecuit(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[1]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[7]/a[2]').click()
        self.driver.switch_to_alert().accept()
        text3=self.driver.switch_to_alert().text
        time.sleep(1)
        self.assertEqual(text3,'没有删除权限')