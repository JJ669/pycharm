from selenium import webdriver
from time import sleep
import re
import pyautogui as pa

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
def Match(link):
    key=1
    while(key):
        class_time=input("请输入你想选课的时间段\n如：星期五第2时段，简写为五2\n")
        for i in range(0,len(link[3])):
            if(class_time[0]==link[3][i][8] and class_time[1]==link[3][i][9]):
                print("课程："+link[0][i]+"，老师:"+link[1][i]+"，选课须知："+link[2][i]+"，时间地点："+link[3][i])
        key=input("是否再次搜索(是，输入1；否，输入0)\n")
        key=int(key)
def Change(link):    #link[0]为class_name_link,link[1]为teacher_name_link,link[2]为condition_link,link[3]为class_time_place_link
    i=0
    regex1=re.compile(r'(.*) 星期(.*) 第(.*)节 (.*)')
    while(1):
        try:
            link[3][i]
        except IndexError:
            break
        else:
            list1=regex1.findall(link[3][i])
            link[3][i]=list1[0][0]+' '+list1[0][1]+list1[0][2]+list1[0][3]
            i=i+1
    return link
def F2(driver):    #进行选课课表查询
    element1=driver.find_element_by_link_text("课程选课")
    element1.click()
    sleep(0.5)

    element2 = driver.find_element_by_link_text("选课课堂查询")
    element2.click()
    sleep(0.5)

    element3= driver.find_element_by_id("id_xsh")
    element3.click()
    sleep(0.5)
    print('''4：心理中心\n
             5：团委\n
             6：选培办\n
             7：招生就业\n
             8：电信学院\n
             9：机电学院\n
             10：土建学院\n
             11：建艺学院\n
             12：经管学院\n
             13：运输学院\n
             14：法学院\n
             15：语言学院\n
             16：马克思主义学院\n
             17：体育部\n
             18：理学院\n
             19：计算机学院\n
             20：软件学院\n
             21：电气学院\n
             27：詹天佑学院\n
''')
    key=input("请输入对应的开课学院编号\n")
    element4=driver.find_element_by_xpath(f'//*[@id="id_xsh"]/option[{key}]')
    element4.click()
    sleep(0.5)

    element5=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/form/div[6]/input')
    element5.click()
    sleep(0.5)

    class_name_link=[]
    teacher_name_link=[]
    condition_link=[]
    class_time_place_link=[]
    link=[class_name_link,teacher_name_link,condition_link,class_time_place_link]

    while(1):
        try :
            element_next = driver.find_element_by_link_text('下一页')  # 下一页
        except :
            break
        else:
            for i in range(2,22):
                class_name=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[2]')
                teacher_name=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[11]')
                condition=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[8]')
                class_time_place=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[12]')
                link[0].append(class_name.text)
                link[1].append(teacher_name.text)
                link[2].append(condition.text)
                link[3].append(class_time_place.text)
        element_next.click()
        sleep(0.5)
    for i in range(2, 22):    #最后一页循环中不执行
        try:
            driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[2]')
        except:
            break
        else:
            class_name = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[2]')
            teacher_name = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[11]')
            condition = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[8]')
            class_time_place = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[12]')
            link[0].append(class_name.text)
            link[1].append(teacher_name.text)
            link[2].append(condition.text)
            link[3].append(class_time_place.text)
    link=Change(link)
    print(link)
    Match(link)

def F3(driver):  #进行选课
    element1 = driver.find_element_by_link_text("课程选课")
    element1.click()
    sleep(0.5)

    element2 = driver.find_element_by_link_text("网上选课")
    element2.click()
    sleep(1)

    shoot1 = pa.locateOnScreen('1.bmp')
    pa.click(shoot1[0] + shoot1[2] / 2, shoot1[1] + shoot1[3] / 2)
    sleep(0.5)
    print('''4:体育
    8:科学
    9:美育
    ''')
    shoot2 = pa.locateOnScreen('2.jpg')
    shoot3=pa.locateOnScreen('3.jpg')
    shoot4=pa.locateOnScreen('4.jpg')
    shoot5=pa.locateOnScreen('查询.jpg')
    pa.click(shoot2[0] + shoot2[2] / 2, shoot2[1] + shoot2[3] / 2)
    pa.click(shoot5[0] + shoot5[2] / 2, shoot5[1] + shoot5[3] / 2)

    class_name_link = []
    teacher_name_link = []
    condition_link = []
    class_time_place_link = []
    link = [class_name_link, teacher_name_link, condition_link, class_time_place_link]

    while (1):
        try:
            element_next = driver.find_element_by_link_text('下一页')  # 下一页
        except:
            break
        else:
            for i in range(2, 12):
                class_name = driver.find_element_by_xpath(
                    f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[3]')
                teacher_name = driver.find_element_by_xpath(
                    f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[7]')
                condition = driver.find_element_by_xpath(
                    f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[9]')
                class_time_place = driver.find_element_by_xpath(
                    f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[8]')
                link[0].append(class_name.text)
                link[1].append(teacher_name.text)
                link[2].append(condition.text)
                link[3].append(class_time_place.text)
        element_next.click()
        sleep(0.5)
    for i in range(2, 12):  # 最后一页循环中不执行
        try:
            driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[3]')
        except:
            break
        else:
            class_name = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[3]')
            teacher_name = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[7]')
            condition = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[9]')
            class_time_place = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[{i}]/td[8]')
            link[0].append(class_name.text)
            link[1].append(teacher_name.text)
            link[2].append(condition.text)
            link[3].append(class_time_place.text)
    print(link)


if __name__ == '__main__':
    driver=F1()  #进入教务系统页面
    F2(driver)   #课查询