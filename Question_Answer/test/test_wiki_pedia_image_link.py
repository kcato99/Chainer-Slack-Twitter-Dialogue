#!/usr/bin/env python
#coding: utf8
import unittest
import sys
import os
from os import path
sys.path.append(os.path.join(os.path.dirname("__file__"), "./../"))
sys.path.append(os.path.join(os.path.dirname("__file__"), "."))
APP_ROOT = path.dirname(path.abspath(__file__))
from wiki_pedia_image_link import WikiPediaImageLink
import filecmp


class Test_WikiPediaImageLink(unittest.TestCase):
    """
    Check contents similarity
    """

    def setUp(self):
        self.wiki_pedia_image_link = WikiPediaImageLink()
        self.wiki_pedia_image_link.start_mysql()

    def test_get_like_search(self):
        test_word = "Zundert"
        answer_list = [
            "Zundert-City_Hall.JPG",
            "Zundert_church.JPG",
            "Zundert_gravestone_van_Gogh.JPG"
        ]
        self.wiki_pedia_image_link.search_like(test_word)
        self.assertListEqual(self.wiki_pedia_image_link.image_data_list, answer_list)

if __name__ == '__main__':
    unittest.main()