#coding=utf-8
'''
@author: Jinglong Yi
'''
import requests
import re
import string
import time

tieba_name = '宝妈微信群'
tiezi_names = []
store_file_path = 'C:\\Users\\user\\Desktop\\贴吧爬取数据%s.txt' % str(int(time.time()))

def special_print(print_str, store_file=None):
    print('★★★★★★★★    ' + str(print_str), flush=True)
    if store_file:
        store_file.write('★★★★★★★★    ' + str(print_str)+'\n')

def tiezi_check(tiezi_names, tieba_title_line):
    if not tiezi_names:
        return True
    for tiezi_name in tiezi_names:
        if tiezi_name in tieba_title_line:
            return True
    return False

def word_check(word, check_words):
    for check_word in check_words:
        if check_word in word:
            return False
    if re.match('..\:..', word):
        return False
    num_or_letter = False
    for one_char in word:
        if one_char in [str(x) for x in string.digits] or one_char in [str(x) for x in string.ascii_letters]:
            num_or_letter = True
            break
    if not num_or_letter:
        return False
    return True
    
def get_resp_line(resp):
    resp_html = resp.content.decode('utf-8')
    resp_lines = resp_html.split('\n')
    return resp_lines

tieba_index_url = 'https://m.zaixiaoyuan.com/p/home?cid=hit'
tieba_detail_url = 'https://tieba.baidu.com'
tieba_index_params = {'kw': tieba_name,
                      'ie': 'utf-8',
                      }
detail_link_mapping = {}
check_words = ['该楼层疑似违规已被系统折叠',
               '送TA礼物',
               '收起回复',
               'function']

# 将目标贴吧首页的所有主题帖链接存下来
special_print('正在获取帖子列表')
tieba_index_resp = requests.get(tieba_index_url, tieba_index_params)
tieba_index_lines = get_resp_line(tieba_index_resp)
for tieba_index_line in tieba_index_lines:
    if 'j_th_tit' in tieba_index_line and 'threadlist_title' not in tieba_index_line and tiezi_check(tiezi_names, tieba_index_line):
        title_line = tieba_index_line.strip()
        title_name = title_line.split(' ')[3][7:-1]
        title_link_tail = title_line.split(' ')[2][6:-1]
        title_link = tieba_detail_url + title_link_tail
        detail_link_mapping[title_link] = title_name
for detail_link in detail_link_mapping:
    print('标题:'+detail_link_mapping[detail_link])
    print('链接:'+detail_link)

# 遍历所有主题帖，爬取主题帖所有回复
with open(store_file_path, 'a', encoding='utf-8') as store_file:
    for detail_link in detail_link_mapping:
        title_name = detail_link_mapping[detail_link]
        special_print('正在爬取帖子:'+title_name, store_file)
        last_page = 0
        current_page = 1
        try:
            while(True):
                special_print('正在爬取第'+str(last_page+1)+'页', store_file)
                detail_link_resp = requests.get(detail_link+'?pn='+str(last_page+1))
                detail_link_lines = get_resp_line(detail_link_resp)
                more_page = False
                for detail_link_line in detail_link_lines:
                    detail_line = detail_link_line.strip()
                    detail_line_fix = re.sub(u"\\<.*?\\>", "", detail_line)
                    if 'class="tP"' in detail_link_line:
                        more_page = True
                        current_page = int(detail_line_fix.strip())
                        if current_page == last_page:
                            special_print('没有更多页了', store_file)
                            raise IndexError
                    if 'd_post_content j_d_post_content' in detail_link_line and 'topic_name' not in detail_link_line:
                        if 'void' in detail_line_fix:
                            detail_line_fix = detail_line_fix[:detail_line_fix.index('void')]
                        detail_line_words = [x for x in detail_line_fix.split(' ') if x]
                        for detail_line_word in detail_line_words:
                            if word_check(detail_line_word, check_words):
                                print(detail_line_word)
                                store_file.write(detail_line_word+'\n')
                if not more_page:
                    special_print('没有更多页了', store_file)
                    raise IndexError
                last_page = current_page
        except IndexError:
            continue

