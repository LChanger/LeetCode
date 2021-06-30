"""
Author: yijinglong
Email: yijinglong@corp.netease.com
Create Time: 16:35
"""

# coding:utf-8
import json
import codecs
filename = "/project/datasets/baike_graph/entity_dict.json"
resultname="./baike_graph/entity_attribute.txt"
linenums = 0

def generate_unique_name():
    with codecs.open(filename, 'r', encoding='utf-8') as fr:
        with codecs.open(resultname, 'w', encoding='utf-8') as fw:
            graph=json.load(fr)
            for v in graph.values():
                for probs in v.values():
                    if "name_unique" in probs:
                        fw.write(probs["name_unique"]+'\n')
    print(linenums)

def is_chinese(string):
    """
    检查整个字符串是否为中文
    Args:
        string (str): 需要检查的字符串,包含空格也是False
    Return
        bool
    """
    for chart in string:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False

    return True

def generate_name_attribute():
    pre='0000年的母系氏族'
    with codecs.open(filename, 'r', encoding='utf-8') as fr:
        with codecs.open(resultname, 'w', encoding='utf-8') as fw:
            graph=json.load(fr)
            for v in graph.values():
                for probs in v.values():
                    if probs["name_unique"]!=pre:
                        fw.write('\n')
                        pre=probs["name_unique"]
                    for att_k in probs:
                        if is_chinese(att_k):
                            fw.write(probs["name_unique"] + '\t'+ att_k +'\n')
if __name__ == "__main__":
    # generate_unique_name()
    generate_name_attribute()



