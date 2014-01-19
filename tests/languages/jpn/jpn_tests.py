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
    ❏DChars❏ : dchars/tests/languages/jpn/jpn_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.symbols.symbols import UNKNOWN_CHAR_SYMBOL

DSTRING_JPN = new_dstring(language="日本語",
                          options = {"anonymize the unknown characters" : 'no'},
                          )

DSTRING_JPN__UNKNOWNCHAR = new_dstring(language="日本語",
                                       options = {"anonymize the unknown characters" : 'yes'},
                                      )


# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).

################################################################################
class TESTSDStringJPN(unittest.TestCase):
    """
        class TESTSDStringJPN

        We test  dchars.languages.jpn.dchars::DStringJPN
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTSDStringJPN.test_add
        """
        string1 = DSTRING_JPN("日本")
        string2 = DSTRING_JPN("語")
        string3 = string1 + string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_JPN )
        string1[0].base_char = "kanji"
        self.assertEqual( DSTRING_JPN("日本") + DSTRING_JPN("語"), string3 )

        string1 = DSTRING_JPN("日本")
        string2 = DSTRING_JPN("語")
        string3 = string1 + string2
        string1 += string2
        self.assertEqual( string1, string3 )
        self.assertEqual( type(string1), DSTRING_JPN )

    #///////////////////////////////////////////////////////////////////////////
    def test_alternative_characters(self):
        """
                TESTSDStringJPN.test_alternative_characters
        """

        txt1 = "が" # 304C
        string1 = DSTRING_JPN(txt1)
        txt2 = "が" # 304B+3099
        string2 = DSTRING_JPN(txt2)
        self.assertEqual( string1, string2 )

        txt1 = "ぷ" # 3075
        string1 = DSTRING_JPN(txt1)
        txt2 = "ぷ" # 3075+309A
        string2 = DSTRING_JPN(txt2)
        self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringJPN.test_base_char
        """

        # 'ふ' and 'ぷ' have the same "base_char" representation :
        string = DSTRING_JPN("ぷ")
        self.assertEqual( string[0].base_char, "ふ" )

        # 'ぶ' and 'ふ' have the same "base_char" representation :
        string = DSTRING_JPN("ぶ")
        self.assertEqual( string[0].base_char, "ふ" )

        # 'フ' and 'ふ' have the same "base_char" representation :
        string = DSTRING_JPN("フ")
        self.assertEqual( string[0].base_char, "ふ" )

        string = DSTRING_JPN("ヅ")
        self.assertEqual( string[0].base_char, "つ" )
        self.assertEqual( string[0].diacritic, "dakuten" )
        self.assertEqual( string[0].chartype, "katakana" )
        self.assertEqual( string[0].smallsize, False )

        string = DSTRING_JPN("きゃ")
        self.assertEqual( string[1].base_char, "や" )
        self.assertEqual( string[1].diacritic, None )
        self.assertEqual( string[1].chartype, "hiragana" )
        self.assertEqual( string[1].smallsize, True )

        string = DSTRING_JPN("ヒー")
        self.assertEqual( string[1].base_char, "ー" )
        self.assertEqual( string[1].diacritic, None )
        self.assertEqual( string[1].chartype, "choonpu" )
        self.assertEqual( string[1].smallsize, False )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringJPN.test_clone
        """
        string0 = DSTRING_JPN("きゃヒー日本")
        string1 = DSTRING_JPN("きゃヒー日本")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].base_char = "す"
        string1[0].chartype = "katakana"

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringJPN.test_emptystring
        """
        string = DSTRING_JPN("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_endswith(self):
        """
                TESTSDStringJPN.test_endswith
        """
        string = DSTRING_JPN("きゃヒー日本")
        self.assertEqual( string.endswith( DSTRING_JPN("日本") ), True )
        self.assertEqual( string.endswith( DSTRING_JPN("") ), True )
        self.assertEqual( string.endswith( DSTRING_JPN("きゃヒー日本") ), True )
        self.assertEqual( string.endswith( DSTRING_JPN("き") ), False )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringJPN.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     'きゃヒー日本',
                     "ほお",
                     "市長選、またも「基地」の重し　名護「本土はひとごと」",
                     "「日本」という漢字による国号の表記は、",
                     "(1) 第一説は、天武天皇の治世（672年 - 686年）に成立したとする説である。"
                     ):

            string = DSTRING_JPN(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_JPN(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringJPN.test_get_sourcestr_repr
        """

        txt1 = "日"
        string1 = DSTRING_JPN(txt1)
        txt2 = string1.get_sourcestr_representation()+"本"
        string2 = DSTRING_JPN(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "日"
        string1 = DSTRING_JPN__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"本"
        string2 = DSTRING_JPN__UNKNOWNCHAR(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_JPN(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_JPN(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_JPN__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_JPN__UNKNOWNCHAR(txt2)
        self.assertEqual( string1, string2 )

        for txt1 in ('',
                     'きゃヒー日本',
                     "ほお",
                     "市長選、またも「基地」の重し　名護「本土はひとごと」",
                     "「日本」という漢字による国号の表記は、",
                     "(1) 第一説は、天武天皇の治世（672年 - 686年）に成立したとする説である。",
                     "首と頭が長く、長い四肢をもつ。角はない。各脚とも第3指を残し他の指は退化している。",
                     "よく発達した蹄（ひづめ）をもち、硬い土の上を走ることができる。長い尾と、",
                     "頭から首の上部にかけての鬣（たてがみ）を除くと、全身の毛は短いが、",
                     "ある程度の寒冷地での生活にも耐えられる。",
                     "優れた嗅覚をもつが、毒草や血のにおいなどを嗅ぎ分けることはできない。",
                     "顔の両側に目が位置するため視野が広いが、反面、両眼視できる範囲は狭いため、",
                     "距離感をつかむことは苦手とする。走るときに背中が湾曲しないため、",
                     "乗用に用いることができる。",
                     " 一般に、立ったまま寝る事でも知られるが、本当に安全な場所であれば、横になって休むこともある。",
                     ):

            string1 = DSTRING_JPN(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_JPN(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_JPN__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_JPN__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringJPN.test_normalstring
        """

        #.......................................................................
        string = DSTRING_JPN("*き*ー日本は、**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "き" )
        self.assertEqual( string[1].chartype, "hiragana" )

        self.assertEqual( str(string), "*き*ー日本は、**" )

        #.......................................................................
        string = DSTRING_JPN__UNKNOWNCHAR("*き*ー日本は、**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "き" )
        self.assertEqual( string[1].chartype, "hiragana" )

        self.assertEqual( str(string), "{0}き{0}ー日本は、{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_JPN("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_JPN__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringJPN.test_problematicstring
        """

        # き with two "dakuten" :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ぎ゙")

        # は with two "handakuten" :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ぱ゚")

        # は with a "dakuten" and a "handakuten" :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ば゚")

    #///////////////////////////////////////////////////////////////////////////
    def test_punctuation(self):
        """
                TESTSDStringJPN.test_punctuation
        """

        string = DSTRING_JPN("、")
        self.assertEqual( string[0].base_char, "、" )
        self.assertEqual( string[0].smallsize, False )
        self.assertEqual( string[0].unknown_char, False )
        self.assertEqual( string[0].chartype, "other" )
        self.assertEqual( string[0].diacritic, None )
        self.assertEqual( string[0].punctuation, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringJPN.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_JPN("ま")[0] == DSTRING_JPN("ま")[0] )

        self.assertTrue( DSTRING_JPN("か")[0] < DSTRING_JPN("ま")[0] )
        self.assertTrue( DSTRING_JPN("か")[0] < DSTRING_JPN("マ")[0] )
        self.assertTrue( DSTRING_JPN("ま")[0] > DSTRING_JPN("か")[0] )
        self.assertTrue( DSTRING_JPN("マ")[0] > DSTRING_JPN("か")[0] )        

        self.assertTrue( DSTRING_JPN("ら")[0] < DSTRING_JPN("り")[0] )
        self.assertTrue( DSTRING_JPN("り")[0] > DSTRING_JPN("ら")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................

        # from http://en.wikipedia.org/wiki/Goj%C5%ABon

        self.assertTrue( DSTRING_JPN("は") < DSTRING_JPN("ば") < DSTRING_JPN("ぱ") )
        
        self.assertTrue( DSTRING_JPN("まつ") == DSTRING_JPN("まつ") )

        self.assertTrue( DSTRING_JPN("まつ") < DSTRING_JPN("まったく") < \
                         DSTRING_JPN("まつば") < DSTRING_JPN("まとう"))

        self.assertTrue( DSTRING_JPN("きや") < DSTRING_JPN("きゃ") < \
                         DSTRING_JPN("きやく") < DSTRING_JPN("きゃく") < \
                         DSTRING_JPN("きゆ") )

        self.assertTrue( DSTRING_JPN("すず") < DSTRING_JPN("すすいろ") < \
                         DSTRING_JPN("すすき") < DSTRING_JPN("すずき") < \
                         DSTRING_JPN("すずしい") < DSTRING_JPN("すすむ") )

        # with unknown characters :
        self.assertTrue( DSTRING_JPN("まつ") < DSTRING_JPN("ま²") )
        self.assertTrue( DSTRING_JPN("まったく") < DSTRING_JPN("ま²たく") )

        # examples taken from Kanji & Kana, Hadamitzky and Spahn, p. 22
        words = (
                'あ',
                'ア',
                'ああ',
                'アー',
                'アート',
                'ああら',
                'あい',
                'あいか',
                'あいが',
                'あいがえし',
                'あいかぎ',
                'あいき',
                'あいぎ',
                'あいきどう',
                'あいきゃく',
                'アイキャー',
                'あいきょう',
                'あいぎょう',
                'あいきわ',
                'あいきん',
                'あいぎん',
                'あち',
                'あつ',
                'あっ',
                'あつい',
                'あつか',
                'あっか',
                'あつかい',
            )

        previous_word = None
        for word in words:
            if previous_word is not None:
                self.assertTrue( DSTRING_JPN(previous_word) < DSTRING_JPN(word) )

            previous_word = word
            
        

    #///////////////////////////////////////////////////////////////////////////
    def test_startswith(self):
        """
                TESTSDStringJPN.test_startswith
        """
        string = DSTRING_JPN("きゃヒー日本")
        self.assertEqual( string.startswith( DSTRING_JPN("きゃ") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("きゃヒー日本") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("ゃヒー日本") ), False )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_character(self):
        """
                TESTSDStringJPN.test_unknown_character
        """

        string = DSTRING_JPN("*")
        self.assertEqual( string[0].base_char, "*" )
        self.assertEqual( string[0].smallsize, False )
        self.assertEqual( string[0].unknown_char, True )
        self.assertEqual( string[0].chartype, None )
        self.assertEqual( string[0].diacritic, None )
        self.assertEqual( string[0].punctuation, False )
