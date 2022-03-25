from seleniumrequests import Edge
def F1():
    webdriver=Edge(executable_path="D:\#python编程文件\pycharm文件夹\爬虫\模拟真实爬虫\msedgedriver.exe")
    reponse=webdriver.request('POST','https://cas.bjtu.edu.cn/auth/login/?next=/o/authorize/%3Fresponse_type%3Dcode%26client_id%3DaGex8GLTLueDZ0nW2tD3DwXnSA3F9xeFimirvhfo%26state%3D1634139580%26redirect_uri%3Dhttps%3A//mis.bjtu.edu.cn/auth/callback/%3Fredirect_to%3D/cms/')
    print(reponse)

if __name__ == '__main__':
    F1()