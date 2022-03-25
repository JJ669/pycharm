import requests
import re
def reptile():
    url = 'https://tieba.baidu.com'
    name = input('请输入你感兴趣的主题\n')
    num = input('请输入你要查看贴吧条数\n')
    num = int(num)
    num_s = int(num / 50)
    num_y = num % 50
    if num_y != 0:
        num_s = num_s + 1
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'bdshare_firstime=1601522697786; BIDUPSID=548BCE575FD3A41F1C17A5E2D4E19A04; PSTM=1598793158; BDUSS=UZPMUlvQTRYZGtscGpJQnV-NXdyWGhDc1R-UkFtQ3N2OXFYSXlLUERVSUpVczlmRVFBQUFBJCQAAAAAAQAAAAEAAAAr1GchAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnFp18JxadfS; BDUSS_BFESS=UZPMUlvQTRYZGtscGpJQnV-NXdyWGhDc1R-UkFtQ3N2OXFYSXlLUERVSUpVczlmRVFBQUFBJCQAAAAAAQAAAAEAAAAr1GchAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnFp18JxadfS; __yjs_duid=1_f4f140d1aa71113f65faef21bb2affa21620627542304; BAIDUID=327608345EB7F6D990A5609C3B579804:FG=1; STOKEN=eb71e29990bd06dc8262b3f657b24cd4337a01e331225e2badf0668ea7087fde; NO_UNAME=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=4747AF49534FDD06B13A41758B8715E0:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=34442_34537_34496_31253_34004_34092_34106_26350_34471; BA_HECTOR=aga02k852l8k2kahmt1gj9be70r; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1630395948,1630555418,1630768637,1630842314; BAIDU_WISE_UID=wapp_1630842312302_618; USER_JUMP=-1; st_key_id=17; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1630842324; ab_sr=1.0.1_OWVkNDU0ZDQwYTNmNGQ0MGRhY2RjNTMxYjRhNGNlMjgxZWM4ZDZmOTU5YjU3NWZiMWQ0NjM5NTViMDM4ZmQ0YzFhMTJmNTk0NTIzNjNiNWE1NzQyM2Q4ZmU5NzAxZGMxZjAwYzViOTUyYTRhYTkzODFmNTE1ODEyNTY3MWM1NmU1MmYxYjU3MjJiYjY2OGM2NTMxM2E5NWQ0OTBhN2MyNThmOTE1MjQ5MWMyZWQyYWM5Njk2MjFjYjAzYTU3NDIy; st_data=ca621798299b8479c83c0612e76ec4ca4e60fe74f1b3f40116f0c44a5c481a9730ca883897c497de93f9eeeff7ee8926a65191ae3d0c51390cc831ec3c9490e2a43966942e30dffb0d9c10494dede7d180a3f72ba0c4583e83f64e36ef92fb6b57af841343eb62a247bf00568d5b9948d8deb6accc17e7c9e657b06f7699069d3364d95a0798399ec2e700fed1dba9c0; st_sign=9d465837',
        'Host': 'tieba.baidu.com',
        'Referer': 'https://tieba.baidu.com/index.html',
        'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
    }
    proxy = {
        'https': '103.103.3.6:8080'
    }
    for r in range(0, num_s):
        keyword = {
            'ie': 'utf-8',
            'kw': f'{name}',
            'fr': 'search',
            'pn': f'{r * 50}'
        }
        url = url + '/f?'
        response = requests.get(url, headers=header, params=keyword)
        response.raise_for_status()
        regex1 = re.compile(
            r'<a rel="noreferrer" href="(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">(.*?)</a>')
        list_1 = regex1.findall(response.text)
        for i in range(0, len(list_1)):
            url_2 = "https://tieba.baidu.com/" + list_1[i][0]
            print(f'{r * 50 + i + 1}:{list_1[i][1]},{url_2}')
if __name__ =='__main__':
    reptile()