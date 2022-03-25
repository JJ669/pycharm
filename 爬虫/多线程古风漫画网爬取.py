import requests
import os
import re
import threading
manhua_1=input("请输入你想下载的漫画\n")
manhua_2=input("请输入漫画的拼音，比如戒魔人：jiemoren\n")
regex1 = re.compile(r'var chapterPath = "(.*?)"')
regex2 = re.compile(r'var chapterImages = \[(.*)\]')
regex3 = re.compile(r'"(.*?)",?')
def findname():
    list_name=[]
    url_x= 'https://www.gufengmh8.com/manhua/'
    url_x=url_x + manhua_2+'/'
    regex_1 = re.compile(rf'''<a href="(.*?)"
                                           class="">
                                            <span>(.*?)</span>
                                        </a>
                                    </li>''')
    response=requests.get(url_x)
    response.raise_for_status()
    list=regex_1.findall(response.text)
    for i in range(0,len(list)):
        list_name.append(list[i][1])
    for k in range(0,len(list)):
        print(f'{k+1}:{list_name[k]}')
    return url_x
def f2(list_html,num,os_name):
    url_1 = 'https://www.gufengmh8.com'
    url_1 = url_1 + list_html[num - 1][0]
    name = list_html[num - 1][1]
    response_1 = requests.get(url_1)
    response_1.raise_for_status()
    list1 = regex1.findall(response_1.text)
    list2 = regex2.findall(response_1.text)
    list3 = regex3.findall(list2[0])
    for i in range(0, len(list3)):
        url_map = 'https://res.xiaoqinre.com/'
        url_map = url_map + list1[0] + list3[i]
        message = requests.get(url_map)
        try:
            message.raise_for_status()
        except requests.exceptions.HTTPError:
            continue
        except requests.exceptions.ChunkedEncodingError:
            continue
        else:
            with open(f'{os_name}\\{num}-{name}话-{i + 1}张.jpg', 'wb') as f1:
                f1.write(message.content)
                print(f'{name}话,第{i + 1}张漫画已下载')
def f3(list_html,k1,k2,os_name):
    for num in range(k1,k2+1):
        f2(list_html,num,os_name)
def fk(list_html,k1,k2,os_name):
    t=threading.Thread(target=f3,args=(list_html,k1,k2,os_name))
    t.start()
def double(list_html,key_f,key_l,os_name):
    key_cha=key_l-key_f+1
    p=key_cha/100
    p=int(p)
    l=key_cha%100
    if p>0:
        for i in range(0,p):
            fk(list_html,key_f+i*100,key_f+i*100+100,os_name)
        if l >0:
            fk(list_html,key_f+p*100,key_l,os_name)
    else:
        fk(list_html,key_f,key_l,os_name)
def main(url):
    print(f"请输入你要下载从多少话到多少话的{manhua_1}")
    key_f = input('开始:')
    key_f = int(key_f)
    key_l = input('结束:')
    key_l = int(key_l)
    response = requests.get(url)
    response.raise_for_status()
    os_name = f'{manhua_1}\\{key_f}-{key_l}话\\'
    if os.path.exists(f'{os_name}'):
        True
    else:
        os.makedirs(f'{os_name}')
    regex_1 = re.compile(rf'''<a href="(.*?)"
                                           class="">
                                            <span>(.*?)</span>
                                        </a>
                                    </li>''')
    list_html = regex_1.findall(response.text)
    #方法一
    #for num in range(key_f,key_l+1):
        #f2(list_num,num,os_name)
    #方法二
    double(list_html,key_f,key_l,os_name)
if __name__ =='__main__':
    url=findname()
    main(url)