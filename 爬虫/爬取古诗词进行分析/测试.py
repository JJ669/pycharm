import re
import requests
regex_3=re.compile(r'''<div class="newstext" id="(.*?)">
(.*?)</div>
<div class="newstext">''')
message='''<div class="content_box">
<div class="box_title"><H2>声声慢·寻寻觅觅</H2></div>
<div class="news_content">
<div class="old_h1">朝代：<a href="/shiren/songdai/" title="宋代">宋代</a>作者：<a href="/shiren/4009.html" title="李清照">李清照</a>更新时间：2018-03-26</div>
<div class="clear"></div>
<div class="newstext" id="212152">
寻寻觅觅，冷冷清清，凄凄惨惨戚戚。乍暖还寒时候，最难将息。三杯两盏淡酒，怎敌他、晚来风急！雁过也，正伤心，却是旧时相识。<br/>满地黄花堆积，憔悴损，如今有谁堪摘？守着窗儿，独自怎生得黑！梧桐更兼细雨，到黄昏、点点滴滴。这次第，怎一个愁字了得！<br/></div>
<div class="newstext">
<a href="/gushi/gaozhongernianji/" title="高中二年级">高中二年级</a>&nbsp;<a href="/gushi/gaozhong/" title="高中古诗大全">高中古诗大全</a>&nbsp;<a href="/gushi/songcisanbaishou/" title="宋词三百首">宋词三百首</a>&nbsp;<a href="/gushi/gaoershangce/" title="高二上册">高二上册</a>&nbsp;</div>



<div class="clear h10"></div>
</div>
<div class="clear"></div>
</div>
'''
meg=regex_3.findall(message)
print(meg)