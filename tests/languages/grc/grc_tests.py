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
    ❏DChars❏ : dchars/tests/languages/grc/grc_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_GRC = new_dstring(language="Ἑλληνικὴ γλῶττα",
                          options = {"anonymize the unknown characters" : 'no'},
                          )

DSTRING_GRC__UNKNOWNCHAR = new_dstring(language="Ἑλληνικὴ γλῶττα",
                                       options = {"anonymize the unknown characters" : 'yes'},
                                      )


# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).

################################################################################
class TESTSDStringGRC(unittest.TestCase):
    """
        class TESTSDStringGRC

        We test  dchars.languages.grc.dchars::DStringGRC
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTSDStringGRC.test_add
        """
        string1 = DSTRING_GRC("α")
        string2 = DSTRING_GRC("ι")
        string3 = string1 + string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_GRC )
        string1[0].tonos = "ὀξεῖα"
        self.assertEqual( DSTRING_GRC("α") + DSTRING_GRC("ι"), string3 )

        string1 = DSTRING_GRC("α")
        string2 = DSTRING_GRC("ι")
        string1 += string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_GRC )

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringGRC.test_base_char
        """

        # 'α' and 'Α' have the same "base_char" representation :
        string = DSTRING_GRC("α")
        self.assertEqual( string[0].base_char, "α" )

        string = DSTRING_GRC("Α")
        self.assertEqual( string[0].base_char, "α" )

        string = DSTRING_GRC("Ἰ")
        self.assertEqual( string[0].base_char, "ι" )
        self.assertEqual( string[0].capital_letter, True )
        self.assertEqual( string[0].pneuma, "ψιλὸν" )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringGRC.test_clone
        """
        string0 = DSTRING_GRC("α")
        string1 = DSTRING_GRC("α")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].base_char = "ω"
        string1[0].capital_letter = True
        string1[0].tonos = "ὀξεῖα"
        string1[0].pneuma = "δασὺ"

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_alternative_characters(self):
        """
                TESTSDStringGRC.test_alternative_characters
        """

        txt1 = "ά" # 1F71
        string1 = DSTRING_GRC(txt1)
        txt2 = "α̍" # 03B1+030D
        string2 = DSTRING_GRC(txt2)
        self.assertEqual( string1, string2 )

        txt1 = "άέίόύώή" # 1F71, 1F73, 1F77, 1F79, 1F7B, 1F7D, 1F75
        string1 = DSTRING_GRC(txt1)
        # 03B1+030D, 03B5+030D, 03B9+030D, 03BF+030D, 03C5+030D, 03C9+030D, 03B7+030D
        txt2 = "α̍ε̍ι̍ο̍υ̍ω̍η̍"
        string2 = DSTRING_GRC(txt2)
        self.assertEqual( string1, string2 )

        txt1 = "ᾄ" # 1F84 (=1F04 + 0345)
        string1 = DSTRING_GRC(txt1)
        txt2 = "ᾀ̍" # 1F80 (=1F00 + 030D)
        string2 = DSTRING_GRC(txt2)
        self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_beta_and_sigma(self):
        """
                TESTSDStringGRC.test_beta_and_sigma
        """

        txt = DSTRING_GRC("βϐσς")

        self.assertEqual( txt[0].base_char, "β" )
        self.assertEqual( txt[0].contextual_form, "initial" )

        self.assertEqual( txt[1].base_char, "β" )
        self.assertEqual( txt[1].contextual_form, "medium+final" )

        self.assertEqual( txt[2].base_char, "σ" )
        self.assertEqual( txt[2].contextual_form, "initial+medium" )

        self.assertEqual( txt[3].base_char, "σ" )
        self.assertEqual( txt[3].contextual_form, "final" )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringGRC.test_emptystring
        """

        string = DSTRING_GRC("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_equivalences(self):
        """
                TESTSDStringGRC.test_equivalences
        """

        for txt1, txt2 in ( ('', ''),
                            ('ά', 'ά'), # 1F71 / 03AC
                            ('ᾄ', 'ά'), # 1F71 / 03B1 0301
                            ("ϋ", 'ϋ'),   # 03CB / 03C5 0308
                            ("ῧ", 'ῧ'),   # 1FE7 / 03CB 0342
                           ):

            string = DSTRING_GRC(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringGRC.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     'α',
                     'ά',
                     'ᾄ',
                     "ᾄ ἕ",
                     "δὲ ὅτι μὲν καθ' ἕνα πάντων ἀμείνων καὶ ἰσχυρό",
                     "ὅτι. μὲν",
                     "ϋ",       # 03CB
                     "ῧ",       # 1FE7
                     "ῤ",
                     "ῧͅ",       # 1FE7 + 0345
                     "ᾎ̈",
                     "Ἰ",       # 1F38
                     "βϐσς",
                     ):

            string = DSTRING_GRC(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_GRC(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringGRC.test_get_sourcestr_repr
        """

        txt1 = "α"
        string1 = DSTRING_GRC(txt1)
        txt2 = string1.get_sourcestr_representation()+"β"
        string2 = DSTRING_GRC(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "α"
        string1 = DSTRING_GRC__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"β"
        string2 = DSTRING_GRC__UNKNOWNCHAR(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_GRC(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_GRC(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_GRC__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_GRC__UNKNOWNCHAR(txt2)
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
            string1 = DSTRING_GRC(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_GRC(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_GRC__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_GRC__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr2(self):
        """
                TESTSDStringGRC.test_get_sourcestr_repr2
        """

        for src in (
                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text001_Lucian_Dialogues_of_the_Gods.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text002_Iliad_I_v1_205.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text003_Euripides_Bacchae_1_104.txt"), 'r')
                ):

            txt1 = src.read()
            string1 = DSTRING_GRC(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_GRC(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringGRC.test_normalstring
        """

        #.......................................................................
        string = DSTRING_GRC("*ά̄*βάϐά̄Β**")
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
        string = DSTRING_GRC__UNKNOWNCHAR("*ά̄*βάϐά̄Β**")
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
        string = DSTRING_GRC("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_GRC__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringGRC.test_problematicstring
        """

        # α with two "tonos" :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("ά̀")

        # α with two "pneuma" :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("ἀ̔")

        # α with one makron and one brakhu :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("ᾱ̆")

        # α with two dialytika :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("α̈̈")

        # α (lower case) with two hypogegrammene :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("ᾳͅ")

        # α (upper case) with two hypogegrammene :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("ᾼͅ")

        # ρ (upper case) with one pneuma :
        DSTRING_GRC("Ῥ")

        # ρ (upper case) with two pneuma :
        with self.assertRaises( DCharsError ):
            DSTRING_GRC("Ῥ̔")

        # normal α (lower case) with tonos, pneuma, makron, dialutika :
        DSTRING_GRC("ᾆ̈")

        # normal α (upper case) with tonos, pneuma, makron, dialutika :
        DSTRING_GRC("ᾎ̈")

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringGRC.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_GRC("α")[0] == DSTRING_GRC("α")[0] )

        self.assertTrue( DSTRING_GRC("α")[0] < DSTRING_GRC("β")[0] )
        self.assertFalse( DSTRING_GRC("α")[0] > DSTRING_GRC("β")[0] )

        self.assertFalse( DSTRING_GRC("α")[0] < DSTRING_GRC("Α")[0] )
        self.assertFalse( DSTRING_GRC("α")[0] > DSTRING_GRC("Β")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        self.assertTrue( DSTRING_GRC("αβγ") == DSTRING_GRC("αβγ") )

        self.assertTrue( DSTRING_GRC("αβγ") < DSTRING_GRC("αβδ") )
        self.assertFalse( DSTRING_GRC("αβγ") > DSTRING_GRC("αβδ") )

        self.assertTrue( DSTRING_GRC("α") < DSTRING_GRC("β") )
        self.assertFalse( DSTRING_GRC("α") > DSTRING_GRC("β") )

        self.assertTrue( DSTRING_GRC("μαμ") < DSTRING_GRC("μάμ") )
        self.assertFalse( DSTRING_GRC("μαμ") > DSTRING_GRC("μάμ") )

        self.assertTrue( DSTRING_GRC("μάμ") < DSTRING_GRC("μᾶμ") )
        self.assertFalse( DSTRING_GRC("μάμ") > DSTRING_GRC("μᾶμ") )

        self.assertFalse( DSTRING_GRC("Πλάτων") < DSTRING_GRC("πλάτων") )
        self.assertFalse( DSTRING_GRC("Πλάτων") > DSTRING_GRC("πλάτων") )

        self.assertTrue( DSTRING_GRC("ἂν") < DSTRING_GRC("ἀνακλαίομαι") < DSTRING_GRC("ἀνήρ") )

        # with unknown characters :
        self.assertTrue( DSTRING_GRC("ᾶμ") < DSTRING_GRC("ᾶ²") )
        self.assertTrue( DSTRING_GRC("ᾶμω") < DSTRING_GRC("ᾶ²ω") )
        self.assertFalse( DSTRING_GRC("ᾶμω") > DSTRING_GRC("ᾶ²ω") )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue2(self):
        """
                TESTSDStringGRC.test_sortingvalue2

                We try to compute the "sorting value" of many words.
        """
        for src in (
                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text001_Lucian_Dialogues_of_the_Gods.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text002_Iliad_I_v1_205.txt"), 'r'),

                        open( os.path.join("tests",
                                "languages",
                                "grc",
                                "text003_Euripides_Bacchae_1_104.txt"), 'r')
                ):

            for line in src.readlines():
                for word in line.split():
                    DSTRING_GRC(word).sortingvalue()

