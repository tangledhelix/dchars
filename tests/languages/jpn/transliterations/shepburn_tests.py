#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
#    DChars Copyright (C) 2012 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of DChars.
#    DChars is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DChars is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DChars.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    ❏DChars❏ : dchars/tests/languages/jpn/transliterations/shepburn_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
DSTRING_JPN = new_dstring(language="jpn",
                          transliteration_method="shepburn",
                          options = {"anonymize the unknown characters" : "yes",
                                     "long vowels written with circumflex" : "no",
                                     "katakanas written with upper case letters" : "yes",
                                     "ou becomes ō" : "no",
                                     },
                         )

LIST_OF_RECIPROCAL_EXAMPLES = (
    ('',                ''    ),
    ('か',              'ka'  ),
    ('きゃ',            'kya'),
    ('びゅ',            'byu'),
    ('じゃあく',        'jaaku'),
    ('おねえさん',      'oneesan'),
    ('ゑ',              'we'),
    ('あんない',        'annai'),
    ('ぐんま',          'gunma'),
    ('しんよう',        "shin'you"),
    ('かんい',          "kan'i"),
    ("けっか",          "kekka",),
    ("さっさと",        "sassato"),
    ("ずっと",          "zutto"),
    ("きっぷ",          "kippu"),
    ("ざっし",          "zasshi"),
    ("いっしょ",        "issho"),
    ("こっち",          "kotchi"),
    ("まっちゃ",        "matcha"),
    ("みっつ",          "mittsu"),
    ("じゃ",            "ja"),
        
    ('カ',              'KA'),
    ('ニャ',            'NYA'),
    ('ピュ',            'PYU'),
    ('ヱ',            'WE'),
    ('トウキョウ',      'TOUKYOU'),
    ('フリー',          'FURĪ'),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringJPN(unittest.TestCase):
    """
        class TESTSDStringJPN

        We test dchars.languages.jpn.transliterations.shepburn.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringJPN.test_from_srcstr_2_srcstr()
        """

        for jpn, jpn_shepburn in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_JPN().init_from_transliteration(jpn_shepburn)
            self.assertEqual( jpn, str(string) )
            jpn_shepburn2 = string.get_transliteration()
            self.assertEqual( jpn_shepburn, jpn_shepburn2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration(self):
        """
                TESTSDStringJPN.test_get_transliteration
        """
        for jpn, jpn_shepburn in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_JPN(jpn)
            jpn_shepburn2 = string.get_transliteration()
            self.assertEqual( jpn_shepburn, jpn_shepburn2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringJPN.test_init_from_transliteration1
        """

        for jpn, jpn_shepburn in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_JPN().init_from_transliteration(jpn_shepburn)
            jpn2 = str(string)
            self.assertEqual( jpn, jpn2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringJPN.test_unknown_characters
        """
        string = DSTRING_JPN("²か²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"か"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_JPN().init_from_transliteration("²ka²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"か"+UNKNOWN_CHAR_SYMBOL )

