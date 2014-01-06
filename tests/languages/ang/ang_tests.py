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
    ❏DChars❏ : dchars/tests/languages/ang/ang_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_ANG = new_dstring(language = "Ænglisc",
                          options = {"anonymize the unknown characters" : "no",
                                     "sorting method" : "default"},
                          )
DSTRING_ANG__UNKNOWNCHAR = new_dstring(language = "Ænglisc",
                                       options = {"anonymize the unknown characters" : "yes"},
                                      )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringANG(unittest.TestCase):
    """
        class TESTSDStringANG

        We test dchars.languages.ang.dchars::DStringANG
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTSDStringANG.test_add
        """
        string1 = DSTRING_ANG("p")
        string2 = DSTRING_ANG("e")
        string3 = string1 + string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_ANG )
        string1[0].base_char = "c"
        self.assertEqual( DSTRING_ANG("p") + DSTRING_ANG("e"), string3 )

        string1 = DSTRING_ANG("p")
        string2 = DSTRING_ANG("e")
        string3 = string1 + string2
        string1 += string2
        self.assertEqual( string1, string3 )
        self.assertEqual( type(string1), DSTRING_ANG )

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringANG.test_base_char
        """

        # 'a' and 'A' have the same "base_char" representation :
        string = DSTRING_ANG("a")
        self.assertEqual( string[0].base_char, "a" )

        string = DSTRING_ANG("A")
        self.assertEqual( string[0].base_char, "a" )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringANG.test_clone
        """
        string0 = DSTRING_ANG("a")
        string1 = DSTRING_ANG("a")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].capital_letter = True
        string1[0].stress = True
        string1[0].makron = True

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringANG.test_emptystring
        """

        string = DSTRING_ANG("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_endswith(self):
        """
                TESTSDStringANG.test_endswith
        """
        string = DSTRING_ANG("mōdgeþanc")
        self.assertEqual( string.endswith( DSTRING_ANG("þanc") ), True )
        self.assertEqual( string.endswith( DSTRING_ANG("") ), True )
        self.assertEqual( string.endswith( DSTRING_ANG("mōdgeþanc") ), True )
        self.assertEqual( string.endswith( DSTRING_ANG("a") ), False )

    ## #///////////////////////////////////////////////////////////////////////////
    ## def test_equivalences(self):
    ##     """
    ##             TESTSDStringANG.test_equivalences
    ##     """

    ##     for txt1, txt2 in ( ('', ''),
    ##                         ('Á', 'Á'), # 00C1 / 0041 0301
    ##                         ('ā́', 'ā́'),   # 0101 0301 / 0061 0304 0301
    ##                        ):

    ##         string = DSTRING_ANG(txt1)
    ##         txt2 = string.get_sourcestr_representation()
    ##         self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringANG.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     'a',
                     'p',
                     'à',
                     'ā́', # 0101 0301
                     "Q",
                     "ō",
                     "mōdgeþanc, ...",
                     "N",
                     " ",
                     "iài",
                     ):

            string = DSTRING_ANG(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_ANG(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringANG.test_get_sourcestr_repr
        """

        txt1 = "a"
        string1 = DSTRING_ANG(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_ANG(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "a"
        string1 = DSTRING_ANG__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_ANG__UNKNOWNCHAR(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_ANG(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_ANG(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_ANG__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_ANG__UNKNOWNCHAR(txt2)
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
                     "iài",
                     ):
            string1 = DSTRING_ANG(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_ANG(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_ANG__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_ANG__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_str(self):
        """
                TESTSDStringANG.test_init_from_str
        """

        for txt in ('ceosan',
                    'ċēosan'):

            string = DSTRING_ANG(txt)
            txt2 = str(string)

            self.assertEqual( len(txt2), 6 )
            self.assertEqual(txt, txt2)

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringANG.test_normalstring
        """

        #.......................................................................
        string = DSTRING_ANG("*ā́*bebiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, 2 )
        self.assertEqual( string[1].makron, True )

        self.assertEqual( str(string), "*ā́*bebiB**" )

        #.......................................................................
        string = DSTRING_ANG__UNKNOWNCHAR("*ā́*bebiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, 2 )
        self.assertEqual( string[1].makron, True )

        self.assertEqual( str(string), "{0}ā́{0}bebiB{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_ANG("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_ANG__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringANG.test_problematicstring
        """

        # e with two "stress(es)" :
        with self.assertRaises( DCharsError ):
            DSTRING_ANG("é́")

        # i with two "makron/makra" :
        with self.assertRaises( DCharsError ):
            DSTRING_ANG("ī̄")


    #///////////////////////////////////////////////////////////////////////////
    def test_modify_character(self):
        """
                TESTSDStringANG.test_modify_character
        """

        string1 = DSTRING_ANG("a")
        string1[0].stress = 2
        string2 = DSTRING_ANG("á")
        self.assertEqual( string1, string2)

        string1 = DSTRING_ANG("a")
        string1[0].stress = 2
        string1[0].makron = True
        string2 = DSTRING_ANG("ā́")
        self.assertEqual( string1, string2)

        string1 = DSTRING_ANG("c")
        string1[0].upperdot = True
        string2 = DSTRING_ANG("ċ")
        self.assertEqual( string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringANG.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_ANG("a")[0] == DSTRING_ANG("a")[0] )

        self.assertTrue( DSTRING_ANG("a")[0] < DSTRING_ANG("b")[0] )
        self.assertFalse( DSTRING_ANG("a")[0] > DSTRING_ANG("b")[0] )

        self.assertFalse( DSTRING_ANG("a")[0] < DSTRING_ANG("A")[0] )
        self.assertFalse( DSTRING_ANG("a")[0] > DSTRING_ANG("A")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        self.assertTrue( DSTRING_ANG("abc") == DSTRING_ANG("abc") )

        self.assertTrue( DSTRING_ANG("abc") < DSTRING_ANG("abd") )
        self.assertFalse( DSTRING_ANG("abc") > DSTRING_ANG("abd") )

        self.assertTrue( DSTRING_ANG("a") < DSTRING_ANG("b") )
        self.assertFalse( DSTRING_ANG("a") > DSTRING_ANG("b") )

        self.assertTrue( DSTRING_ANG("mam") < DSTRING_ANG("mām") )
        self.assertFalse( DSTRING_ANG("mam") > DSTRING_ANG("mām") )

        self.assertFalse( DSTRING_ANG("romam") < DSTRING_ANG("Romam") )
        self.assertFalse( DSTRING_ANG("romam") > DSTRING_ANG("Romam") )

        self.assertTrue( DSTRING_ANG("Rō") < DSTRING_ANG("Romam") )
        self.assertFalse( DSTRING_ANG("Rō") > DSTRING_ANG("Romam") )

        # with unknown characters :
        self.assertTrue( DSTRING_ANG("ab") < DSTRING_ANG("a²") )
        self.assertFalse( DSTRING_ANG("ab") > DSTRING_ANG("a²") )

        self.assertTrue( DSTRING_ANG("abc") < DSTRING_ANG("a²c") )
        self.assertFalse( DSTRING_ANG("abc") > DSTRING_ANG("a²c") )

    #///////////////////////////////////////////////////////////////////////////
    def test_startswith(self):
        """
                TESTSDStringANG.test_startswith
        """
        string = DSTRING_ANG("ġē")
        self.assertEqual( string.startswith( DSTRING_ANG("ġ") ), True )
        self.assertEqual( string.startswith( DSTRING_ANG("") ), True )
        self.assertEqual( string.startswith( DSTRING_ANG("ġē") ), True )
        self.assertEqual( string.startswith( DSTRING_ANG("S") ), False )
