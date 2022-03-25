from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumrequests import Edge
import time

def F1():
    driver=webdriver.Edge(executable_path="D:\#python编程文件\pycharm文件夹\爬虫\模拟真实爬虫\msedgedriver.exe")
    driver.get("http://www.shousuceshi.com/")

    element1=driver.find_element_by_xpath('//*[@id="box-text"]')
    time1=time.time()
    for i in range(0,10000):
        time2 = time.time()
        if time2-time1>=10:
            break
        else:
            element1.click()


    time.sleep(10)





if __name__ =="__main__":
    F1()