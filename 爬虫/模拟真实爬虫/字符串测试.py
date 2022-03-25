import re
message='''M201040B [09]
模拟电子技术 [本]
第01-12周 王晓轩
逸夫教学楼 YF208
A101031B [01]
工程与社会系列讲座 [本]
第19-22周 陶丹
第九教学楼 中心报告厅'''
message=message.replace('\n','')
print(message)
regex1=re.compile(rf'(.*?)第(.*?)-(.*?)周(.*?)')
print(regex1.findall(message))
