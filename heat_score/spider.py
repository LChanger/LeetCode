"""
Author: yijinglong
Email: yijinglong@corp.netease.com
Create Time: 17:50
"""

# -*- coding: utf-8 -*-
import requests
import re
import codecs
import urllib.parse
header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
def get_html(url,retry=3,timeout=10): # 获取serp源代码函数
    try:
       r = requests.get(url,headers=header,timeout=10)
    except requests.exceptions.RequestException:
       r = ''
       if retry > 0:
         get_html(url,retry-1)
    else:
        return r.content

def res_count(url):         #采集结果数函数
    html = get_html(url)
    if html:
        html = html.decode('utf-8')
        # html=str(html, encoding="utf-8")
        # html = html.decode('utf-8')
        count = re.search('百度为您找到相关结果约(.+?)个',html,re.S)
    return count.group(1)
if __name__ == "__main__":
    with codecs.open('./baike_graph/entity_attribute.txt', 'r', encoding='utf-8') as fr:
        with codecs.open('./baike_graph/count_quotes.txt', 'w', encoding='utf-8') as fw:
            for i in fr: #待查询的词放在kwd.txt里
                    kwd = i.strip()
                    if kwd=='':
                        fw.write('\n')
                        continue
                    kwd=kwd.split('\t')
                    kwd[0]='"'+kwd[0]+'"'
                    kwd=" ".join(kwd)
                    url = 'https://www.baidu.com/s?wd={0}'.format(urllib.parse.quote(kwd))+'&usm=3&rsv_idx=2&rsv_page=1'
                    res = res_count(url)
                    print(kwd+ ' '+res)
                    fw.write(kwd+ ' '+res+'\n')
    print('完毕,结果保存在文件')