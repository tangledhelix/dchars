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
    ❏DChars❏ : dchars/tests/languages/lat/lat_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_LAT = new_dstring(language = "latīna",
                          options = {"anonymize the unknown characters" : "no",
                                     "sorting method" : "default"},
                          )
DSTRING_LAT__UNKNOWNCHAR = new_dstring(language = "latīna",
                                       options = {"anonymize the unknown characters" : "yes"},
                                      )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringLAT(unittest.TestCase):
    """
        class TESTSDStringLAT

        We test dchars.languages.lat.dchars::DStringLAT
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringLAT.test_base_char
        """

        # 'a' and 'A' have the same "base_char" representation :
        string = DSTRING_LAT("a")
        self.assertEqual( string[0].base_char, "a" )

        string = DSTRING_LAT("A")
        self.assertEqual( string[0].base_char, "a" )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringLAT.test_emptystring
        """

        string = DSTRING_LAT("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_equivalences(self):
        """
                TESTSDStringLAT.test_equivalences
        """

        for txt1, txt2 in ( ('', ''),
                            ('Á', 'Á'), # 00C1 / 0041 0301
                            ('ā́', 'ā́'),   # 0101 0301 / 0061 0304 0301
                           ):

            string = DSTRING_LAT(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringLAT.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     'a',
                     'p',
                     'ï',
                     'ā́', # 0101 0301
                     "Q",
                     "ō",
                     "Quōēre, ...",
                     "N",
                     " ",
                     "iïi",
                     ):

            string = DSTRING_LAT(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_LAT(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringLAT.test_get_sourcestr_repr
        """

        txt1 = "a"
        string1 = DSTRING_LAT(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_LAT(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "a"
        string1 = DSTRING_LAT__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_LAT__UNKNOWNCHAR(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_LAT(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_LAT(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_LAT__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_LAT__UNKNOWNCHAR(txt2)
        self.assertEqual( string1, string2 )

        for txt1 in ('',
                     'a',
                     'á',
                     'ā́',
                     "Quō usque tandem abūtēre",
                     "Quō usque tandem abūtēre, ...",
                     "Á",
                     "N",
                     " ",
                     "iïi",
                     "ǟ",
                     "ǟ́",
                     ):
            string1 = DSTRING_LAT(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_LAT(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_LAT__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_LAT__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr2(self):
        """
                TESTSDStringLAT.test_get_sourcestr_repr2
        """

        for filename in (
                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text001_Cicero_In_Pisonem.txt"),

                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text002_Virgil_Aeneid_I.txt"),

                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text003_Cicero_In_Catilinam_I.txt"),
                ):

            with open( filename, 'r') as src:

                txt1 = src.read()
                string1 = DSTRING_LAT(txt1)
                txt2 = string1.get_sourcestr_representation()
                string2 = DSTRING_LAT(txt2)
                self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_str(self):
        """
                TESTSDStringLAT.test_init_from_str
        """

        for txt in ('Roma',
                    'Rōma'):

            string = DSTRING_LAT(txt)
            txt2 = str(string)

            self.assertEqual( len(txt2), 4 )
            self.assertEqual(txt, txt2)

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringLAT.test_normalstring
        """

        #.......................................................................
        string = DSTRING_LAT("*ā́*bebiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, True )
        self.assertEqual( string[1].length, 'long' )

        self.assertEqual( str(string), "*ā́*bebiB**" )

        #.......................................................................
        string = DSTRING_LAT__UNKNOWNCHAR("*ā́*bebiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, True )
        self.assertEqual( string[1].length, 'long' )

        self.assertEqual( str(string), "{0}ā́{0}bebiB{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_LAT("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_LAT__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringLAT.test_problematicstring
        """

        # e with two "stress(es)" :
        with self.assertRaises( DCharsError ):
            DSTRING_LAT("é́")

        # i with two "long" :
        with self.assertRaises( DCharsError ):
            DSTRING_LAT("ī̄")

        # a with two "short" :
        with self.assertRaises( DCharsError ):
            DSTRING_LAT("ă̆")

        # a with two "diaeresis" :
        with self.assertRaises( DCharsError ):
            DSTRING_LAT("ä̈")

    #///////////////////////////////////////////////////////////////////////////
    def test_modify_character(self):
        """
                TESTSDStringLAT.test_modify_character
        """

        string1 = DSTRING_LAT("a")
        string1[0].stress = True
        string2 = DSTRING_LAT("á")
        self.assertEqual( string1, string2)

        string1 = DSTRING_LAT("a")
        string1[0].stress = True
        string1[0].length = "long"
        string1[0].diaeresis = True
        string2 = DSTRING_LAT("ǟ́")
        self.assertEqual( string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringLAT.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_LAT("a")[0] == DSTRING_LAT("a")[0] )

        self.assertTrue( DSTRING_LAT("a")[0] < DSTRING_LAT("b")[0] )
        self.assertFalse( DSTRING_LAT("a")[0] > DSTRING_LAT("b")[0] )

        self.assertFalse( DSTRING_LAT("a")[0] < DSTRING_LAT("A")[0] )
        self.assertFalse( DSTRING_LAT("a")[0] > DSTRING_LAT("A")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        self.assertTrue( DSTRING_LAT("abc") == DSTRING_LAT("abc") )

        self.assertTrue( DSTRING_LAT("abc") < DSTRING_LAT("abd") )
        self.assertFalse( DSTRING_LAT("abc") > DSTRING_LAT("abd") )

        self.assertTrue( DSTRING_LAT("a") < DSTRING_LAT("b") )
        self.assertFalse( DSTRING_LAT("a") > DSTRING_LAT("b") )

        self.assertTrue( DSTRING_LAT("mam") < DSTRING_LAT("mām") )
        self.assertFalse( DSTRING_LAT("mam") > DSTRING_LAT("mām") )

        self.assertFalse( DSTRING_LAT("romam") < DSTRING_LAT("Romam") )
        self.assertFalse( DSTRING_LAT("romam") > DSTRING_LAT("Romam") )

        self.assertTrue( DSTRING_LAT("Rō") < DSTRING_LAT("Romam") )
        self.assertFalse( DSTRING_LAT("Rō") > DSTRING_LAT("Romam") )

        # with unknown characters :
        self.assertTrue( DSTRING_LAT("ab") < DSTRING_LAT("a²") )
        self.assertFalse( DSTRING_LAT("ab") > DSTRING_LAT("a²") )

        self.assertTrue( DSTRING_LAT("abc") < DSTRING_LAT("a²c") )
        self.assertFalse( DSTRING_LAT("abc") > DSTRING_LAT("a²c") )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue2(self):
        """
                TESTSDStringLAT.test_sortingvalue2

                We try to compute the "sorting value" of many words.
        """
        for srcfilename in (
                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text001_Cicero_In_Pisonem.txt"),

                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text002_Virgil_Aeneid_I.txt"),

                                os.path.join("dchars",
                                             "tests",
                                             "languages",
                                             "lat",
                                             "text003_Cicero_In_Catilinam_I.txt"),
                           ):

            with open( srcfilename, 'r') as src:

                for line in src.readlines():
                    for word in line.split():
                        DSTRING_LAT(word).sortingvalue()

