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
    ❏DChars❏ : dchars/tests/languages/hbo/hbo_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_HBO = new_dstring(language="עִבְֿרִיתֿ מִקְרָאִיתֿ",
                          options = {"anonymize the unknown characters" : 'no'},
                          )
DSTRING_HBO__UNKNOWNCHAR = new_dstring(language="עִבְֿרִיתֿ מִקְרָאִיתֿ",
                                       options = {"anonymize the unknown characters" : 'yes'},
                                      )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringHBO(unittest.TestCase):
    """
        class TESTSDStringHBO

        We test dchars.languages.hbo.dchars::DStringHBO
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringHBO.test_base_char
        """

        # oבּo and oבo have the same base character :
        string = DSTRING_HBO("בּ")
        self.assertEqual( string[0].base_char, "ב" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ב")
        self.assertEqual( string[0].base_char, "ב" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        # (kaf/final kaf) oכo and oךo have the same base character :
        string = DSTRING_HBO("כ")
        self.assertEqual( string[0].base_char, "כ" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ך")
        self.assertEqual( string[0].base_char, "כ" )
        self.assertEqual( string[0].contextual_form, "final" )

        # (mem/final mem) oמo and oםo have the same base character :
        string = DSTRING_HBO("מ")
        self.assertEqual( string[0].base_char, "מ" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ם")
        self.assertEqual( string[0].base_char, "מ" )
        self.assertEqual( string[0].contextual_form, "final" )

        # (nun/final nun) oנo and oןo have the same base character :
        string = DSTRING_HBO("נ")
        self.assertEqual( string[0].base_char, "נ" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ן")
        self.assertEqual( string[0].base_char, "נ" )
        self.assertEqual( string[0].contextual_form, "final" )

        # (pe/final pe) oפo and oףo have the same base character :
        string = DSTRING_HBO("פ")
        self.assertEqual( string[0].base_char, "פ" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ף")
        self.assertEqual( string[0].base_char, "פ" )
        self.assertEqual( string[0].contextual_form, "final" )

        # (tsadi/final tsadi) oצo and oץo have the same base character :
        string = DSTRING_HBO("צ")
        self.assertEqual( string[0].base_char, "צ" )
        self.assertEqual( string[0].contextual_form, "initial+medium+final" )

        string = DSTRING_HBO("ץ")
        self.assertEqual( string[0].base_char, "צ" )
        self.assertEqual( string[0].contextual_form, "final" )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringHBO.test_clone
        """
        string0 = DSTRING_HBO("קּ")
        string1 = DSTRING_HBO("קּ")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].base_char = "מַֽ"
        string1[0].methegh = False

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringHBO.test_emptystring
        """
        string = DSTRING_HBO("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringHBO.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     "א",
                     "מּם",     # with/without daghesh
                     "אטלפבקּק", # letters
                     "כֻּכֹּכִּכַּכּככַ",  # vowels
                     "כַּֿ",       # + "HEBREW POINT RAFE" 0x05BF
                     "א׃",      # + "HEBREW PUNCTUATION SOF PASUQ" 0x05C3
                     "מַֽ",       # + "HEBREW POINT METEG" 0x05BD
                     "לֻ֑",       # + "HEBREW ACCENT ETNAHTA" 0x0591
                     "מ֑ׄ",       # + "HEBREW MARK UPPER DOT"(05C4) + "HEBREW ACCENT ETNAHTA"
                     "מׅ֑",       # + "HEBREW MARK UPPER DOT"(05C5) + "HEBREW ACCENT ETNAHTA"
                     ):

            string = DSTRING_HBO(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_HBO(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringHBO.test_get_sourcestr_repr
        """

        txt1 = "א"
        string1 = DSTRING_HBO(txt1)
        txt2 = string1.get_sourcestr_representation()+"א"
        string2 = DSTRING_HBO(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_HBO(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_HBO(txt2)
        self.assertEqual( string1, string2 )

        for txt1 in (
                     "",
                     "א",
                     "מּם",     # with/without daghesh
                     "אטלפבקּק", # letters
                     "כֻּכֹּכִּכַּכּככַ",  # vowels
                     "כַּֿ",       # + "HEBREW POINT RAFE" 0x05BF
                     "א׃",      # + "HEBREW PUNCTUATION SOF PASUQ" 0x05C3
                     "מַֽ",       # + "HEBREW POINT METEG" 0x05BD
                     "לֻ֑",       # + "HEBREW ACCENT ETNAHTA" 0x0591
                     "מ֑ׄ",       # + "HEBREW MARK UPPER DOT"(05C4) + "HEBREW ACCENT ETNAHTA"
                     "מׅ֑",       # + "HEBREW MARK UPPER DOT"(05C5) + "HEBREW ACCENT ETNAHTA"
                     ):

            string1 = DSTRING_HBO(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_HBO(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr2(self):
        """
                TESTSDStringHBO.test_get_sourcestr_repr2
        """

        for srcfilename in (
                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text001_Genesis_I.txt"),

                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text002_Psalms_18.txt"),

                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text003_Jonah_I.txt"),
                           ):

            with open( srcfilename, 'r') as src:

                txt1 = src.read()
                string1 = DSTRING_HBO(txt1)
                txt2 = string1.get_sourcestr_representation()
                string2 = DSTRING_HBO(txt2)
                self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_alternative_characters(self):
        """
                TESTSDStringHBO.test_alternative_characters
        """

        txt1 = "ℵ" # 0x2135
        string1 = DSTRING_HBO(txt1)
        txt2 = "א" # x05D0
        string2 = DSTRING_HBO(txt2)
        self.assertEqual( string1, string2 )
        self.assertEqual( string1[0].base_char, chr(0x05D0) )

        txt1 = chr(0x05C3) # 0x05C3 (original "HEBREW PUNCTUATION SOF PASUQ")
        string1 = DSTRING_HBO(txt1)
        txt2 = ":"
        string2 = DSTRING_HBO(txt2)
        self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringHBO.test_normalstring
        """

        #.......................................................................
        src = "ABCת012הָאָֽxmyzארֶץab"
        string = DSTRING_HBO(src)

        self.assertEqual( len(string), 18 )

        for index in range(17):
            # "ABC" is unknown
            # "ab" is unknown
            # "wxyz" is unknown :
            if index in (0, 1, 2,  9, 10, 11, 12,  16, 17):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( str(string), "ABCת012הָאָֽxmyzארֶץab")

        #.......................................................................
        src = "ABCת012הָאָֽxmyzארֶץab"
        string = DSTRING_HBO__UNKNOWNCHAR(src)

        self.assertEqual( len(string), 18 )

        for index in range(18):
            # "ABC" is unknown
            # "ab" is unknown
            # "wxyz" is unknown :
            if index in (0, 1, 2,  9, 10, 11, 12,  16, 17):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( str(string),
                          "{0}{0}{0}ת012הָאָֽ{0}{0}{0}{0}ארֶץ{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_HBO("ABCת012 הָאָֽרֶץ׃ab")

        self.assertEqual( len(string), 15 )

        for index in range(15):
            # "ABC" is unknown
            # "ab" is unknown
            if index in (0, 1, 2,   13, 14,):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( str(string), "ABCת012 הָאָֽרֶץ׃ab".format( UNKNOWN_CHAR_SYMBOL) )

        # letter "ת" :
        self.assertEqual( string[3].base_char, "ת" )
        self.assertEqual( string[6].shin_sin_dot, None )

        # letter "אָֽ" :
        self.assertEqual( string[9].base_char, 'א' )
        self.assertEqual( string[9].vowel, 'HEBREW POINT QAMATS' )

        #.......................................................................
        string = DSTRING_HBO__UNKNOWNCHAR("ABCת012 הָאָֽרֶץ׃ab")

        self.assertEqual( len(string), 15 )

        for index in range(15):
            # "ABC" is unknown
            # "ab" is unknown
            if index in (0, 1, 2,   13, 14,):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( str(string), "{0}{0}{0}ת012 הָאָֽרֶץ׃{0}{0}".format( UNKNOWN_CHAR_SYMBOL) )

        # letter "ת" :
        self.assertEqual( string[3].base_char, "ת" )
        self.assertEqual( string[6].shin_sin_dot, None )

        # letter "אָֽ" :
        self.assertEqual( string[9].base_char, 'א' )
        self.assertEqual( string[9].vowel, 'HEBREW POINT QAMATS' )

        #.......................................................................
        string = DSTRING_HBO("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_HBO__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringHBO.test_problematicstring
        """

        for src in ("אְְ",       # two "HEBREW POINT SHEVA" 0x05B0
                    "אֽֽ",         # two "HEBREW POINT METEG" 0x05BD
                    "שׂׂ",         # two "HEBREW POINT SIN DOT" 0x05C2
                    "אֿֿ",         # two "HEBREW POINT RAFE" 0x05BF
                    ):

            with self.assertRaises( DCharsError ):
                string = DSTRING_HBO(src)
                string.get_transliteration()

    #///////////////////////////////////////////////////////////////////////////
    def test_punctuation(self):
        """
                TESTSDStringHBO.test_punctuation
        """

        string = DSTRING_HBO("׃1ת")
        self.assertEqual( string[0].punctuation, True )
        self.assertEqual( string[1].punctuation, False )
        self.assertEqual( string[2].punctuation, False )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringHBO.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        str1 = "בּ"
        str2 = "בּ"
        self.assertTrue( DSTRING_HBO(str1)[0] == DSTRING_HBO(str2)[0] )
        self.assertFalse( DSTRING_HBO(str1)[0] != DSTRING_HBO(str2)[0] )

        str1 = "בּ"
        str2 = "גּ"
        self.assertTrue( DSTRING_HBO(str1)[0] < DSTRING_HBO(str2)[0] )
        self.assertFalse( DSTRING_HBO(str1)[0] > DSTRING_HBO(str2)[0] )

        str1 = "ב"
        str2 = "בּ"
        self.assertTrue( DSTRING_HBO(str1)[0] < DSTRING_HBO(str2)[0] )
        self.assertFalse( DSTRING_HBO(str1)[0] > DSTRING_HBO(str2)[0] )

        str1 = "בַּ"
        str2 = "בַּֿ"
        self.assertTrue( DSTRING_HBO(str1)[0] < DSTRING_HBO(str2)[0] )
        self.assertFalse( DSTRING_HBO(str1)[0] > DSTRING_HBO(str2)[0] )

        str1 = "בַּ"
        str2 = "בִּ"
        self.assertTrue( DSTRING_HBO(str1)[0] < DSTRING_HBO(str2)[0] )
        self.assertFalse( DSTRING_HBO(str1)[0] > DSTRING_HBO(str2)[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        str1 = "בּ"
        str2 = "בּ"
        self.assertTrue( DSTRING_HBO(str1) == DSTRING_HBO(str2) )
        self.assertFalse( DSTRING_HBO(str1) != DSTRING_HBO(str2) )

        str1 = "עִבְֿרִיתֿ מִקְרָאִיתֿ"
        str2 = "עִבְֿרִיתֿ מִקְרָאִיתֿ"
        self.assertTrue( DSTRING_HBO(str1) == DSTRING_HBO(str2) )
        self.assertFalse( DSTRING_HBO(str1) != DSTRING_HBO(str2) )

        str1 = "חֹפֶשׁ"
        str2 = "תָּכְנִית"
        self.assertTrue( DSTRING_HBO(str1) < DSTRING_HBO(str2) )
        self.assertFalse( DSTRING_HBO(str1) > DSTRING_HBO(str2) )

        # with unknown characters :
        self.assertTrue( DSTRING_HBO("מִקְרָאִיתֿ") < DSTRING_HBO("מִקְרָאִ²תֿ") )
        self.assertFalse( DSTRING_HBO("מִקְרָאִיתֿ") > DSTRING_HBO("מִקְרָאִ²תֿ") )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue2(self):
        """
                TESTSDStringHBO.test_sortingvalue2

                We try to compute the "sorting value" of many words.
        """
        for srcfilename in (
                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text001_Genesis_I.txt"),

                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text002_Psalms_18.txt"),

                                os.path.join("tests",
                                             "languages",
                                             "hbo",
                                             "text003_Jonah_I.txt"),
                           ):

            with open( srcfilename, 'r') as src:

                for line in src.readlines():
                    for word in line.split():
                        DSTRING_HBO(word).sortingvalue()

