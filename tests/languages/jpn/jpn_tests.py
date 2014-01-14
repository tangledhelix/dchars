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
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringJPN.test_get_sourcestr_repr
        """

        txt1 = "α"
        string1 = DSTRING_JPN(txt1)
        txt2 = string1.get_sourcestr_representation()+"β"
        string2 = DSTRING_JPN(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "α"
        string1 = DSTRING_JPN__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"β"
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
                     'α',
                     'ά',
                     'ᾄ',
                     "ᾄ ἕ",
                     "δὲ ὅτι μὲν καθ' ἕνα πάντων ἀμείνων καὶ ἰσχυρό",
                     "ὅτι. μὲν",
                     "ϋ" # 03CB=(03C5+0308),
                     "ῧ" # (1FE7) 03CB+0342
                     "ῧͅ" # (1FE7) 03CB+0342; 0345
                     "μῧͅμ" # μ + (1FE7) 03CB+0342; 0345 + μ
                     "ᾎ̈",
                     "Ἰ",       # 1F38
                     "βϐσς",
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
    def test_get_sourcestr_repr2(self):
        """
                TESTSDStringJPN.test_get_sourcestr_repr2
        """

        for src in (
                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text001_Lucian_Dialogues_of_the_Gods.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text002_Iliad_I_v1_205.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text003_Euripides_Bacchae_1_104.txt"), 'r')
                ):

            txt1 = src.read()
            string1 = DSTRING_JPN(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_JPN(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr3(self):
        """
                TESTSDStringJPN.test_get_sourcestr_repr3

                Testing the 'ignore_makron' parameter.
        """

        #.......................................................................
        string1 = DSTRING_JPN("ί̄")
        string2 = DSTRING_JPN("ί")
        self.assertEqual( string1.get_sourcestr_representation(ignore_makron = True),
                          string2.get_sourcestr_representation(ignore_makron = False) )

        #.......................................................................
        string1 = DSTRING_JPN("ί̄")
        string2 = DSTRING_JPN("ί̄")
        self.assertNotEqual( string1.get_sourcestr_representation(ignore_makron = True),
                             string2.get_sourcestr_representation(ignore_makron = False) )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringJPN.test_normalstring
        """

        #.......................................................................
        string = DSTRING_JPN("*ά̄*βάϐά̄Β**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "α" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].tonos, 'ὀξεῖα' )
        self.assertEqual( string[1].mekos, 'μακρόν' )
        self.assertEqual( string[1].pneuma, None )

        self.assertEqual( str(string), "*ά̄*βάϐά̄Β**" )

        #.......................................................................
        string = DSTRING_JPN__UNKNOWNCHAR("*ά̄*βάϐά̄Β**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "α" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].tonos, 'ὀξεῖα' )
        self.assertEqual( string[1].mekos, 'μακρόν' )
        self.assertEqual( string[1].pneuma, None )

        self.assertEqual( str(string), "{0}ά̄{0}βάϐά̄Β{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

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

        # α with two "tonos" :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ά̀")

        # α with two "pneuma" :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ἀ̔")

        # α with one makron and one brakhu :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ᾱ̆")

        # α with two dialytika :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("α̈̈")

        # α (lower case) with two hypogegrammene :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ᾳͅ")

        # α (upper case) with two hypogegrammene :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("ᾼͅ")

        # ρ (upper case) with one pneuma :
        DSTRING_JPN("Ῥ")

        # ρ (upper case) with two pneuma :
        with self.assertRaises( DCharsError ):
            DSTRING_JPN("Ῥ̔")

        # normal α (lower case) with tonos, pneuma, makron, dialutika :
        DSTRING_JPN("ᾆ̈")

        # normal α (upper case) with tonos, pneuma, makron, dialutika :
        DSTRING_JPN("ᾎ̈")

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringJPN.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_JPN("α")[0] == DSTRING_JPN("α")[0] )

        self.assertTrue( DSTRING_JPN("α")[0] < DSTRING_JPN("β")[0] )
        self.assertFalse( DSTRING_JPN("α")[0] > DSTRING_JPN("β")[0] )

        self.assertFalse( DSTRING_JPN("α")[0] < DSTRING_JPN("Α")[0] )
        self.assertFalse( DSTRING_JPN("α")[0] > DSTRING_JPN("Β")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        self.assertTrue( DSTRING_JPN("αβγ") == DSTRING_JPN("αβγ") )

        self.assertTrue( DSTRING_JPN("αβγ") < DSTRING_JPN("αβδ") )
        self.assertFalse( DSTRING_JPN("αβγ") > DSTRING_JPN("αβδ") )

        self.assertTrue( DSTRING_JPN("α") < DSTRING_JPN("β") )
        self.assertFalse( DSTRING_JPN("α") > DSTRING_JPN("β") )

        self.assertTrue( DSTRING_JPN("μαμ") < DSTRING_JPN("μάμ") )
        self.assertFalse( DSTRING_JPN("μαμ") > DSTRING_JPN("μάμ") )

        self.assertTrue( DSTRING_JPN("μάμ") < DSTRING_JPN("μᾶμ") )
        self.assertFalse( DSTRING_JPN("μάμ") > DSTRING_JPN("μᾶμ") )

        self.assertFalse( DSTRING_JPN("Πλάτων") < DSTRING_JPN("πλάτων") )
        self.assertFalse( DSTRING_JPN("Πλάτων") > DSTRING_JPN("πλάτων") )

        self.assertTrue( DSTRING_JPN("ἂν") < DSTRING_JPN("ἀνακλαίομαι") < DSTRING_JPN("ἀνήρ") )

        # with unknown characters :
        self.assertTrue( DSTRING_JPN("ᾶμ") < DSTRING_JPN("ᾶ²") )
        self.assertTrue( DSTRING_JPN("ᾶμω") < DSTRING_JPN("ᾶ²ω") )
        self.assertFalse( DSTRING_JPN("ᾶμω") > DSTRING_JPN("ᾶ²ω") )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue2(self):
        """
                TESTSDStringJPN.test_sortingvalue2

                We try to compute the "sorting value" of many words.
        """
        for src in (
                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text001_Lucian_Dialogues_of_the_Gods.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text002_Iliad_I_v1_205.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "jpn",
                                "text003_Euripides_Bacchae_1_104.txt"), 'r')
                ):

            for line in src.readlines():
                for word in line.split():
                    DSTRING_JPN(word).sortingvalue()

    #///////////////////////////////////////////////////////////////////////////
    def test_startswith(self):
        """
                TESTSDStringJPN.test_startswith
        """
        string = DSTRING_JPN("ἀμείνων")
        self.assertEqual( string.startswith( DSTRING_JPN("ἀμεί") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("ἀμείνων") ), True )
        self.assertEqual( string.startswith( DSTRING_JPN("μείνων") ), False )
