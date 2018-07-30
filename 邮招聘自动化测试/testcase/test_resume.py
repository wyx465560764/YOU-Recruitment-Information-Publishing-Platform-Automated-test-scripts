import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class resume(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome();
        self.driver.get("http://localhost:8080")
        self.driver.add_cookie({'name':'username','value':'学生'})
        self.driver.get("http://localhost:8080")
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_addresume(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[2]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[7]/a').click()
        self.driver.find_element_by_name('realName').send_keys('面试者')
        self.driver.find_element_by_name('phone').send_keys('12345678901')
        self.driver.find_element_by_name('email').send_keys('test@123.com')
        self.driver.find_element_by_name('skill').send_keys(u'python+selenium+webdriver自动化测试')
        self.driver.find_element_by_name('school').send_keys('重庆邮电大学')
        self.driver.find_element_by_id("input_select").click()
        Select(self.driver.find_element_by_id("input_select")).select_by_visible_text(u"本科")
        self.driver.find_element_by_name('major').send_keys('软件工程')
        self.driver.find_element_by_name('endDate').send_keys('0020180701')
        self.driver.find_element_by_name('project').send_keys('邮招聘测试工程师')
        self.driver.find_element_by_name('award').send_keys('测试比赛奖项')
        self.driver.find_element_by_name('compusExperise').send_keys('学生会部长')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input[1]').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[1]').text,'面试者')
    def test_changeresumename(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[1]').click()
        self.driver.find_element_by_name('realname').clear()
        self.driver.find_element_by_name('realname').send_keys('修改后的面试者')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[1]').text,'修改后的面试者')
    def test_changeresumephone(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[1]').click()
        self.driver.find_element_by_name('phone').clear()
        self.driver.find_element_by_name('phone').send_keys('18875141272')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[2]').text,'18875141272')
    def test_changeresumeskill(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[1]').click()
        self.driver.find_element_by_name('skill').clear()
        self.driver.find_element_by_name('skill').send_keys('python+selenium')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[4]').text,'python+selenium')
    def test_changeresumeschool(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[1]').click()
        self.driver.find_element_by_name('school').clear()
        self.driver.find_element_by_name('school').send_keys('cqupt')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[5]').text,'cqupt')
    def test_changeresumemaxeducation(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[1]').click()
        self.driver.find_element_by_id("input_select").click()
        Select(self.driver.find_element_by_id("input_select")).select_by_visible_text(u"博士")
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/section[4]/div/dl/dd[4]/input').click()
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[6]').text,'博士')
    def test_deleteresume(self):
        self.driver.find_element_by_xpath('//*[@id="information"]/div/div/div[3]/div[2]/ul/li[4]/div/a/i').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr/td[7]/a[2]').click()
        time.sleep(1)
        self.assertNotEqual(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr[1]/td[1]').text,'修改后的面试者')