import requests
import re
import xlwt
import os
def reptile_tao():
    name=input('请输入你想要查看的商品名称\n')
    num=input('请输入你想要查看的几页\n')
    num=int(num)
    t_1=num
    regex1=re.compile(r'"raw_title":"(.*?)",(.*?),"view_price":"(.*?)",(.*?),"view_sales":"(.*?)人付款"')
    header={
        'authority': 'uland.taobao.com',
        'method': 'GET',
        'path': '/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E4%B9%A6&clk1=3958570d9b423b3030575295f5d9ea29&upsId=3958570d9b423b3030575295f5d9ea29&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.179.152.249_10885757_1631273307531%3Bprepvid%3A201_11.27.24.10_10894675_1631273324632',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '__wpkreporterwid_=78f28c72-50aa-4e3f-8315-89284132f717; thw=cn; miid=298845211863614740; cna=7wHZF5s1b2oCAXWl125Js0gB; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E100HluKnTu96KV6HgvD3ExrSXDAqKsv2EXJ1W2X7ag8tbldzT3%2BgIDdlq0QV48vWJOjW1%2B6RFTeqcD%2Bj6JgdDSihg%3D%3D; tracknick=tb410860503; _cc_=Vq8l%2BKCLiw%3D%3D; enc=%2FPZsv%2BUZoDII7HCopTViVIJ4t7uQQrxy0%2FT0zVy%2FpSb7xo5UjWSEeSi7WTdgSp7GeYxO7xDJ27LhDHci7xdkwELZIjJnkgvGwFwPhRi0QoE%3D; lego2_cna=8HD2XTTM4U0H002WK1UCUX12; xlly_s=1; ctoken=V8cRNdOgw4Xcv6I8tDbmhSq7; _m_h5_tk=a1d2aaa509e81240bc71f9da235cc384_1631280507890; _m_h5_tk_enc=1eae98d8ae26e2d3e33d659800a706d8; tfstk=cNWNB_O4KReamwpbwd94CeH6a-TOam9De2-Xs6ER1sMT2RdkzsqZkHfqKBRWVhAG.; l=eBjqfWpeO2zwB3IzBO5Courza77T2IRb8qVzaNbMiInca6ZhTFwyKN1KSPOW7dtxgtfEAetPgw_puReB5i4dgmyD-JluBKW9pxJ6-; isg=BD09y1zAAGep9pqRYszDzdErTJk32nEshDFO4f-CwhTDNlxoxyij_E6k4Wpwionk',
        'referer': 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E4%B9%A6&clk1=3958570d9b423b3030575295f5d9ea29&upsId=3958570d9b423b3030575295f5d9ea29&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.179.152.249_10885757_1631273307531%3Bprepvid%3A201_11.8.106.4_10897201_1631273311215',
        'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    }
    work = xlwt.Workbook()
    w1 = work.add_sheet(f'{name}')
    w1.write(0,0,'名称')
    w1.write(0,1,'价格')
    w1.write(0,2,'销量')
    for i in range(0,t_1):
        url=f'https://s.taobao.com/search?q={name}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210909&ie=utf8&p4ppushleft=2%2C48&s={i*44}'
        response=requests.get(url,headers=header)
        response.raise_for_status()
        list_1=regex1.findall(response.text)
        for k in range(0,len(list_1)):
            print(f'{i*48+k+1}:商品名称:{list_1[k][0]},价格：{list_1[k][2]},销量：{list_1[k][4]}')
            w1.write(i*48+k+1,0,list_1[k][0])
            w1.write(i*48+k+1,1,float(list_1[k][2]))
            if "万+" in list_1[k][4]:
                message=list_1[k][4][0:-2]
                t1=int(float(message))
                t1=t1*10000
                w1.write(i*48+k+1,2,t1)
            elif '+' in list_1[k][4]:
                message=list_1[k][4][0:-2]
                message=int(message)
                w1.write(i*48+k+1,2,message)
            else:
                w1.write(i*48+k+1,2,int(list_1[k][4]))
    work.save(f'.\\{name}.xls')
if __name__ == '__main__':
    reptile_tao()