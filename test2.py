from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('https://www.taobao.com/')
input = browser.find_element_by_id('q')
input.send_keys('火影忍者')
time.sleep(2)
input.clear()
input.send_keys('海贼王')
time.sleep(2)
button = browser.find_element_by_class_name('btn-search')
button.click()
