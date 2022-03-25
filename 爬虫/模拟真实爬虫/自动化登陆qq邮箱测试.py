from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
def F1():
    user=input("请输入qq账号")
    password=input("请输入qq密码")

    driver=webdriver.Edge(executable_path="D:\#python编程文件\pycharm文件夹\爬虫\模拟真实爬虫\msedgedriver.exe")
    driver.get("https://mail.qq.com/cgi-bin/loginpage?autologin=n&errtype=1&clientuin=893203813&param=&sp=&tfcont=22%20serialization%3A%3Aarchive%2010%200%200%203%200%200%200%208%20authtype%201%206%209%20clientuin%209%20893203813%206%20domain%206%20qq.com&r=425d97a74510b857121cb670fe023885")
    driver.set_window_size(1200,1000)

    element3= driver.find_element_by_xpath('//*[@id="qqLoginTab"]')
    ActionChains(driver).move_to_element(element3).perform()
    element3.click()
    sleep(1)

    #进入iframe
    driver.switch_to.frame(driver.find_element_by_id('login_frame'))


    element1 = driver.find_element_by_id("u")
    ActionChains(driver).move_to_element(element1).perform()
    element1.click()
    element1.clear()
    element1.send_keys(user)
    sleep(1)

    element2 = driver.find_element_by_id("p")
    ActionChains(driver).move_to_element(element2).perform()
    element2.click()
    element2.clear()
    element2.send_keys(password)
    sleep(1)


    element3 = driver.find_element_by_id('login_button')
    element3.click()
    sleep(1)

     #退出iframe
    driver.switch_to.default_content()

    driver.switch_to.window(driver.current_window_handle[1])
    sleep(10)


if __name__ == '__main__':
    F1()