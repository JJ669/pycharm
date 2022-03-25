from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
def F1():
    browser=webdriver.Edge(executable_path="D:\#python编程文件\pycharm文件夹\爬虫\模拟真实爬虫\msedgedriver.exe")
    browser.get("https://image.baidu.com/")
    browser.set_window_size(1200,1000)

    element1=browser.find_element_by_link_text("城市建筑摄影专题")
    element1.click()
    sleep(1)

    element2=browser.find_element_by_link_text('渐变风格插画')
    element2.click()
    sleep(1)

    element4=browser.find_element_by_link_text('皮影')
    element4.click()
    sleep(1)

    browser.switch_to.window(browser.window_handles[1])
    # window_handles中存储的列表是以0：首页，1：最新页面，2，3，4，。。。按打开顺序排列最后一个最先打开
    element3=browser.find_elements_by_class_name('albumsdetail-item')
    element3[0].click()
    sleep(1)

    browser.switch_to.window(browser.window_handles[0])

    element1_1=browser.find_element_by_class_name('s_ipt')
    e1=ActionChains(browser).move_to_element(element1_1).perform()
    element1_1.click()
    element1_1.send_keys('跑车')
    element1_1.send_keys(Keys.ENTER)
    sleep(1)


    sleep(10)



if __name__ == '__main__':
    F1()