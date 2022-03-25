import requests
url="https://apd-16d984d174ac504ca7d3c8c9345a4435.v.smtcdns.com/moviets.tc.qq.com/AJL7oko8fuJ1FOpWyOIWTa6BQiccpf4NK2CcstdPJm0E/uwMROfz2r5zAoaQXGdGnC2df644E7D3uP8M8pmtgwsRK9nEL/dtBKqABcIfRkuDw_OL-Uh_GxWOvcf5tl2B7xqFbS4BS_NGMPdWSLWB0SnXz0OryQsZNUXfTEsuIJp1WPi8zNj_bEhsYnpmBq1mkvpgC6xshBSqcFTa9uQnzDBEcgCkmkXFX6lbb8i8eY82T3VXPemD0Zqz2fEXf6VosQPllqqvF47szVn4Ccmw/034_p0029371vd2.321002.2.ts?index=34&start=337800&end=347967&brs=4104604&bre=5248207&ver=4&token=e65656a1c55e0223a79169bcbbb61027"
requests=requests.get(url)
requests.raise_for_status()
with open('1.avi','wb') as f1:
    f1.write(requests.content)