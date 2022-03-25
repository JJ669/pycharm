import requests
import re
import os
import easygui

def F1(name, num):
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1630461674908_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid='
    num = int(num)
    t = int(num / 30)
    leave_num = num % 30
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'BIDUPSID=548BCE575FD3A41F1C17A5E2D4E19A04; PSTM=1598793158; BDUSS=UZPMUlvQTRYZGtscGpJQnV-NXdyWGhDc1R-UkFtQ3N2OXFYSXlLUERVSUpVczlmRVFBQUFBJCQAAAAAAQAAAAEAAAAr1GchAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnFp18JxadfS; BDUSS_BFESS=UZPMUlvQTRYZGtscGpJQnV-NXdyWGhDc1R-UkFtQ3N2OXFYSXlLUERVSUpVczlmRVFBQUFBJCQAAAAAAQAAAAEAAAAr1GchAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnFp18JxadfS; __yjs_duid=1_f4f140d1aa71113f65faef21bb2affa21620627542304; BAIDUID=327608345EB7F6D990A5609C3B579804:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=E1EBEADA4D4646B3FAC96A78CBA74B91:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=3; H_PS_PSSID=34442_34496_31253_34004_34524_34092_34106_26350_34319; BA_HECTOR=20048485800g2501vq1gitkls0q; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_NTJhNDlkYTRiOWM0ZWYzZWIyMDMxZTljY2JjYzBiMjcyYjU3ZGQ0NDQ5MTRiODIwNWM2NGY5MGZlZjRkZGViODQ1Y2NhNmM1ODJlYmIzNTFhNTdhY2E1NGFmNWFhYWMwN2M4YTU3YjY0ZmMwZjc3Yzk2ZDJmNGZhMmU5ZTU1MTQ4ZWU0YWRiMGE4YTEyOWM2ZGFjZjdiZWM2MDY4ZDc5NDQ0MmYzZTAwYmE2OWU3NTYxOGEyNjY4NzAxOTlhOGY1; indexPageSugList=%5B%22%E6%98%9F%E7%A9%BA%22%2C%22%E7%8C%AB%22%2C%22%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%22%2C%22%E5%8A%A0%E9%80%9F%20%E6%8A%80%E8%83%BD%E5%9B%BE%E6%A0%87%20%E5%9B%BE%E7%89%87%22%2C%22%E6%B8%B8%E6%88%8F%20%E5%B0%8F%E6%95%8C%E6%9C%BA%20%E5%BE%80%E4%B8%8B%E9%A3%9E%20%E5%9B%BE%E7%89%87%22%2C%22%E6%B8%B8%E6%88%8F%20%E6%95%8C%E6%9C%BA%20%E5%BE%80%E4%B8%8B%E9%A3%9E%20%E5%9B%BE%E7%89%87%22%2C%22%E5%8A%A8%E7%94%BB%20%E6%95%8C%E6%9C%BA%20%E5%BE%80%E4%B8%8B%E9%A3%9E%20%E5%9B%BE%E7%89%87%22%2C%22%E7%AE%80%E7%AC%94%E7%94%BB%20%E6%95%8C%E6%9C%BA%20%E5%BE%80%E4%B8%8B%E9%A3%9E%20%E5%9B%BE%E7%89%87%20%22%2C%22%E6%B8%B8%E6%88%8F%E9%A3%9E%E6%9C%BA%E5%AD%90%E5%BC%B9%20%E5%9B%BE%E7%89%87%22%5D',
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu.com/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
        }
    regex1 = re.compile(r'"thumbURL":"(.*?)"')
    os_name = f'{name}图片'
    try:
        for r in range(0, t + 1):
            if r < t:
                p = 30
            else:
                p = leave_num
            keyword = {'word': f'{name}',
                       'pn': r * 30}
            response = requests.get(url, headers=header, params=keyword)
            response.raise_for_status()
            text1 = response.text
            list1 = regex1.findall(text1)
            if os.path.exists(f'{os_name}'):
                True
            else:
                os.makedirs(f'{os_name}')
            for i in range(0, p):
                message = requests.get(list1[i])
                message.raise_for_status()
                k = i + 1
                with open(f'{os_name}\\{name}{k + r * 30}.jpg', 'wb') as f1:
                    f1.write(message.content)
        easygui.msgbox(msg=f'{num}张照片已下载完成', title='提醒', ok_button='朕已阅')
    except requests.exceptions.ConnectionError:
        easygui.msgbox(msg=f'您的网络不顺畅，请连接好网络后再此尝试',title='警报',ok_button='好的')
    except:
        easygui.msgbox(msg=f'出现了一些问题，请重试',title='警报',ok_button='好的')
if __name__ == '__main__':
    Fields = ['名称：', '数量：']
    list = easygui.multenterbox(msg='请输入你要下载的图片名称/种类(请先联网),如果数量多的话可能时间较久', title='自动从百度图库中下载图片', fields=Fields)
    try:
        F1(list[0], list[1])
    except:
        True