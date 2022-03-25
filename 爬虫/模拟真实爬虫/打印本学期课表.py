from selenium import webdriver
from time import sleep
import xlwt
def F1():
    #user=input("请输入学号\n")
    #password=input("请输入密码\n")
    user="20211058"
    password="54xl2L60Q913$!"
    driver=webdriver.Edge(executable_path="D:\#python编程文件\pycharm文件夹\爬虫\模拟真实爬虫\msedgedriver.exe")
    driver.get('https://mis.bjtu.edu.cn/home/')
    driver.set_window_size(1200,1000)
    sleep(1)

    element1=driver.find_element_by_xpath('//*[@id="id_loginname"]')
    #ActionChains(driver).move_to_element(element1).perform()   悬停（没必要）
    element1.click()
    element1.clear()
    element1.send_keys(user)
    sleep(1)

    element2=driver.find_element_by_xpath('//*[@id="id_password"]')
    #ActionChains(driver).move_to_element(element2).perform()    悬停（没必要）
    element2.click()
    element2.clear()
    element2.send_keys(password)
    sleep(1)

    element3=driver.find_element_by_xpath('//*[@id="login"]/dl/dd[2]/div/div[3]/button')
    element3.click()
    sleep(1)
    #登陆成功

    #进入教务系统
    element4=driver.find_element_by_link_text("32.教务系统")
    element4.click()
    sleep(1)
    #进入教务系统页
    driver.switch_to.window(driver.window_handles[1])
    return driver
if __name__=='__main__':
    driver=F1()
    element1=driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/ul/li[4]/a')
    element1.click()
    sleep(1)
    element2=driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[1]/ul/li[3]/a')
    element2.click()
    sleep(1)
    work=xlwt.Workbook(encoding='utf-8')
    sheet=work.add_sheet('本学期课本')
    for i in range(1,9):
        element4=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/th[{i}]')
        sheet.write(0,i-1,element4.text)
    for i in range(2,9):
        for j in range(1,9):
            element5=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[{j}]')
            sheet.write(i-1,j-1,element5.text)
    work.save('本学期课表.xlsx')
