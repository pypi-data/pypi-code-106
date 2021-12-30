# -*- coding: UTF-8 -*-
"""vega FYI word_list中带有term的其他补充信息

    @author: vegaviazhang
    @file:demo_test.py
    @time:2021/12/28
"""
from pprint import pprint

from trie import TrieDict


def main():
    word_list = [
        "立克次氏体属",  # no_term_info
        "糖尿病一型",  # no_term_info
        "小细胞肺癌",  # no_term_info
        "非小细胞肺癌",  # no_term_info
    ]

    words_list = [
        ("糖尿病", {"mesh_code": "AAA-BBB", "mesh_level": "level 1"}),  # term_info
        ("糖尿病一型", {"mesh_code": "AAA-BBB-CCC", "mesh_level": "level 2"}),  # term_info
        ("小细胞肺癌", ['临床表现: 小细胞癌的临床主要表现为刺激性的干咳、咳痰、胸闷气短以及胸痛等症状']),  # term_info
        ("非小细胞肺癌", '病因是什么'),  # term_info
    ]
    vega_trie = TrieDict()
    vega_trie.init_or_insert_dict(words_list)
    # ['糖尿病一型', '糖尿病', '糖尿病二型', '高血压', '焦虑情绪', '慢性肾脏疾病1期']

    # 1.最大前向匹配
    origin_text = "AAA非小细胞肺癌糖尿病一型非小细胞肺癌糖尿病糖尿病糖尿病糖尿病一型小细胞肺癌"  # 8个
    match_list = vega_trie.get_match_words(origin_text)
    pprint(match_list)
    """output
    [
         ['糖尿病一型', {'mesh_code': 'AAA-BBB-CCC', 'mesh_level': 'level 2'}],
         '立克次氏体属',
         ['糖尿病', {'mesh_code': 'AAA-BBB', 'mesh_level': 'level 1'}],
         ['糖尿病', {'mesh_code': 'AAA-BBB', 'mesh_level': 'level 1'}],
         ['糖尿病', {'mesh_code': 'AAA-BBB', 'mesh_level': 'level 1'}]
     ]
    """

    # 2.判断一个词是否在字典树中
    # 2.1 有词在字典树中
    print(vega_trie.check_exist("非和小细胞肺癌"))
    # (True, ['小细胞肺癌', ['临床表现: 小细胞癌的临床主要表现为刺激性的干咳、咳痰、胸闷气短以及胸痛等症状']])

    # 2.2 没有词在字典树中
    print(vega_trie.check_exist("细胞肺癌"))
    # (False, None)


if __name__ == "__main__":
    main()
