import re
import requests

if __name__ == '__main__':
    url = "https://www.gushimi.org/"
    header={
        'authority': 'googleads.g.doubleclick.net',
        'method': 'GET',
        'path': '/pagead/adview?ai=CiWWaGmEjYrGgAovi8gXlsLqYCMax1r5or9mLt5wPv_-549cCEAEgya_XBmCdAaABh8a0kQHIAQaoAwHIA8sEqgTLAU_Qbv8Q9c2dkrEVq89jjZiW5-nkkkSb-SabG9-XHe9wxPnATxtr1UGhI6le0b1EtX-19AuCkm_epNvs5p3spFWyt-M_KaxH8FlfuuabrR-oSloASH_S0TOLviDLisGs0maypWiaJplSO3ER3Krz6zakJlWwUqrW3ha5ZOeR3TVIOybMCebCo_mD3xLmxpYCpZ2zE5ql2sqNHIimK93VIZfO7imOSChmvdCK0X8BLqkyaLn5LTkSXrLq6Yb2LwItjW71lWPVPxv8w5YMwASC2L7I6AOgBjeAB-G5y-4CqAeOzhuoB5PYG6gH7paxAqgH_p6xAqgHpKOxAqgH1ckbqAemvhvYBwHyBwQQl54B0ggHCIhhEAEYH4AKAcgLAdgTA4gUBdAVAZgWAYAXAbIXHAoaCAASFHB1Yi01ODEyNTM1NTA0NTYwNjE1GAA&sigh=E89ywrHUonQ&uach_m=[UACH]&template_id=492',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': '''https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-5812535504560615&output=html&h=158&slotname=6317671460&adk=755450550&adf=3503317802&pi=t.ma~as.6317671460&w=553&lmt=1638873775&rafmt=11&psa=1&format=553x158&url=https%3A%2F%2Fwww.gushimi.org%2Fshiren%2F4009.html&flash=32.0.0&wgl=1&uach=WyJXaW5kb3dzIiwiMTAuMC4wIiwieDg2IiwiIiwiOTguMC4xMTA4LjYyIixbXSxudWxsLG51bGwsIjY0IixbWyIgTm90IEE7QnJhbmQiLCI5OS4wLjAuMCJdLFsiQ2hyb21pdW0iLCI5OC4wLjExMDguNjIiXSxbIk1pY3Jvc29mdCBFZGdlIiwiOTguMC4xMTA4LjYyIl1dXQ..&dt=1646485788045&bpp=3&bdt=139&idt=100&shv=r20220302&mjsv=m202203020101&ptt=9&saldr=aa&abxe=1&cookie=ID%3D0faf2797b7552b90-22985d76c4d0003c%3AT%3D1646142046%3ART%3D1646142046%3AS%3DALNI_MZZUeaCw0VszbZ6QuyGIeaozbmOWQ&correlator=6201086216373&frm=20&pv=2&ga_vid=1046799716.1646485788&ga_sid=1646485788&ga_hid=610333578&ga_fc=0&u_tz=480&u_his=3&u_h=960&u_w=1440&u_ah=920&u_aw=1440&u_cd=24&u_sd=1.5&dmc=8&adx=0&ady=514&biw=553&bih=849&scr_x=0&scr_y=0&eid=42531398%2C44750773%2C31065507%2C31060566%2C31063246&oid=2&pvsid=3597187553254413&pem=276&tmod=1732927488&wsm=1&uas=0&nvt=1&ref=https%3A%2F%2Fwww.gushimi.org%2F&eae=0&fc=640&brdim=0%2C0%2C0%2C0%2C1440%2C0%2C1440%2C920%2C570%2C849&vis=1&rsz=%7C%7CoeE%7C&abl=CS&pfx=0&fu=128&bc=31&ifi=1&uci=a!1&fsb=1&xpc=s54GhXllud&p=https%3A//www.gushimi.org&dtd=136''',
        'sec-ch-ua': '''" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"''',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '''"Windows"''',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    }
    response=requests.get(url,headers=header)
    response.raise_for_status()
    response.encoding='utf-8'  #传输的时候按照另一种密码格式进行，虽然显示的是utf-8但可能并不是，所以需要再次修改解码格式为utf-8
    regex=re.compile(r'''<dd><a href="(.*?)" title="(.*?)"><img src=".*?" width="105" height="130" alt=".*?"/></a></dd>''')
    message=regex.findall(response.text)
    i=0
    url_2=url+message[i][0]
    response_2=requests.get(url_2,headers=header)
    response_2.raise_for_status()
    response_2.encoding='utf-8'
    regex_2=re.compile(r'''<li>(.*?). 古诗《<a href="(.*?)" title="(.*?)">''')
    message_2=regex_2.findall(response_2.text)
    print(message_2)
    j=0
    url_3=url+message_2[j][1]
    response_3=requests.get(url_3,headers=header)
    response_3.raise_for_status()
    response_3.encoding='utf-8'
    regex_3=re.compile(r'''<div class="newstext" id="(.*?)">
(.*)</div>
<div class="newstext">''')
    message_3=regex_3.findall(response_3.text)
    print(message_3)