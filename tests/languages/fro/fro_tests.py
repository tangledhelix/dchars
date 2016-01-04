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
    ❏DChars❏ : dchars/tests/languages/fro/fro_tests.py
"""

import unittest

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_FRO = new_dstring(language = "romanz",
                          options = {"anonymize the unknown characters" : "no",
                                     "sorting method" : "default"},
                          )
DSTRING_FRO__UNKNOWNCHAR = new_dstring(language = "romanz",
                                       options = {"anonymize the unknown characters" : "yes"},
                                      )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringFRO(unittest.TestCase):
    """
        class TESTSDStringFRO

        We test dchars.languages.fro.dchars::DStringFRO
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTSDStringFRO.test_add
        """
        string1 = DSTRING_FRO("p")
        string2 = DSTRING_FRO("e")
        string3 = string1 + string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_FRO )
        string1[0].base_char = "c"
        self.assertEqual( DSTRING_FRO("p") + DSTRING_FRO("e"), string3 )

        string1 = DSTRING_FRO("p")
        string2 = DSTRING_FRO("e")
        string3 = string1 + string2
        string1 += string2
        self.assertEqual( string1, string3 )
        self.assertEqual( type(string1), DSTRING_FRO )

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringFRO.test_base_char
        """

        # 'a' and 'A' have the same "base_char" representation :
        string = DSTRING_FRO("a")
        self.assertEqual( string[0].base_char, "a" )

        string = DSTRING_FRO("A")
        self.assertEqual( string[0].base_char, "a" )

        string = DSTRING_FRO("ç")
        self.assertEqual( string[0].base_char, "c" )

        string = DSTRING_FRO("Ç")
        self.assertEqual( string[0].base_char, "c" )

        string = DSTRING_FRO("é")
        self.assertEqual( string[0].base_char, "e" )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringFRO.test_clone
        """
        string0 = DSTRING_FRO("e")
        string1 = DSTRING_FRO("e")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].capital_letter = True
        string1[0].stress = 1

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringFRO.test_emptystring
        """
        string = DSTRING_FRO("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_endswith(self):
        """
                TESTSDStringFRO.test_endswith
        """
        string = DSTRING_FRO("Marsilïun")
        self.assertEqual( string.endswith( DSTRING_FRO("un") ), True )
        self.assertEqual( string.endswith( DSTRING_FRO("ïun") ), True )
        self.assertEqual( string.endswith( DSTRING_FRO("Marsilïun") ), True )
        self.assertEqual( string.endswith( DSTRING_FRO("u") ), False )

    #///////////////////////////////////////////////////////////////////////////
    def test_equivalences(self):
        """
                TESTSDStringFRO.test_equivalences
        """

        for txt1, txt2 in ( ('', ''),
                            ('à', 'à'),   # 00E0 / 0061 0300
                            ('â', 'â'),   # 00E2 / 0061 0302
                            ('ä', 'ä'),   # 00E4 / 0061 0308
                            ('é', 'é'),   # 00E1 / 0065 0301
                            ('ç', 'ç'),   # 00E7 / 0063 0327 
                           ):

            string = DSTRING_FRO(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringFRO.test_from_srcstr_2_srcstr
        """

        for txt1 in ('',
                     'a',
                     'p',
                     'à',
                     "Q",
                     "Marsilïun, ...",
                     "N",
                     " ",
                     "iài",
                     "â",
                     "ä",
                     "ç",
                     ):

            string = DSTRING_FRO(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_FRO(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringFRO.test_get_sourcestr_repr
        """

        txt1 = "a"
        string1 = DSTRING_FRO(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_FRO(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "a"
        string1 = DSTRING_FRO__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"b"
        string2 = DSTRING_FRO__UNKNOWNCHAR(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_FRO(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_FRO(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_FRO__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_FRO__UNKNOWNCHAR(txt2)
        self.assertEqual( string1, string2 )

        for txt1 in ('',
                     'a',
                     'á',
                     'à',
                     "N",
                     "ç",
                     " ",
                     "iài",
                     ):
            string1 = DSTRING_FRO(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_FRO(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_FRO__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_FRO__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_str(self):
        """
                TESTSDStringFRO.test_init_from_str
        """

        for txt in ('Marsilïun',
                    "Vint à son proisne sermoner,",
                    "Et dist qu'il fesoit bon doner",
                    "Por Dieu, qui reson entendoit ;",
                    "Que Diex au double li rendoit",
                    "Celui qui le fesoit de cuer.",
                    "« Os, fet li vilains, bele suer,",
                    "Que noz prestres a en couvent :",
                    "Qui por Dieu done à escient,",
                    "Que Diex li fet mouteploier ;",
                    "Miex ne poons-nous emploier",
                    "No vache, se bel te doit estre.",
                    ''):

            string = DSTRING_FRO(txt)
            txt2 = str(string)

            self.assertEqual(txt, txt2)

        for txt in ("Marsilïun",
                    "Vint à so",
                    "Et dist q",):

            string = DSTRING_FRO(txt)
            txt2 = str(string)

            self.assertEqual( len(txt2), 9 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringFRO.test_normalstring
        """

        #.......................................................................
        string = DSTRING_FRO("*â*bebiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, 3 )

        self.assertEqual( str(string), "*â*bebiB**" )

        #.......................................................................
        string = DSTRING_FRO__UNKNOWNCHAR("*â*bïbiB**")
        self.assertEqual( len(string), 10 )

        for index in range(0, 10):
            if index in (0, 2, 8, 9):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "a" )
        self.assertEqual( string[1].capital_letter, False )
        self.assertEqual( string[1].stress, 3 )

        self.assertEqual( str(string), "{0}â{0}bïbiB{0}{0}".format(UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_FRO("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_FRO__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
#    def test_problematicstring(self):
#        """
#                TESTSDStringFRO.test_problematicstring
#        """
#
#        # e with two "stress(es)" :
#        with self.assertRaises( DCharsError ):
#            DSTRING_FRO("é́")
#
#        # i with two "makron/makra" :
#        with self.assertRaises( DCharsError ):
#            DSTRING_FRO("ī̄")
#
#        # i with two "stress(es)" :
#        with self.assertRaises( DCharsError ):
#            DSTRING_FRO("a̽̽")

    #///////////////////////////////////////////////////////////////////////////
    def test_modify_character(self):
        """
                TESTSDStringFRO.test_modify_character
        """

        string1 = DSTRING_FRO("a")
        string1[0].stress = 2
        string2 = DSTRING_FRO("á")
        self.assertEqual( string1, string2)

        string1 = DSTRING_FRO("à")
        string1[0].stress = 0
        string2 = DSTRING_FRO("a")
        self.assertEqual( string1, string2)

        string1 = DSTRING_FRO("a")
        string1[0].stress = 3
        string2 = DSTRING_FRO("â")
        self.assertEqual( string1, string2)

        string1 = DSTRING_FRO("c")
        string1[0].cedilla = True
        string2 = DSTRING_FRO("ç")
        self.assertEqual( string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringFRO.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        self.assertTrue( DSTRING_FRO("a")[0] == DSTRING_FRO("a")[0] )

        self.assertTrue( DSTRING_FRO("a")[0] < DSTRING_FRO("b")[0] )
        self.assertFalse( DSTRING_FRO("a")[0] > DSTRING_FRO("b")[0] )

        self.assertFalse( DSTRING_FRO("a")[0] < DSTRING_FRO("A")[0] )
        self.assertFalse( DSTRING_FRO("a")[0] > DSTRING_FRO("A")[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        self.assertTrue( DSTRING_FRO("abc") == DSTRING_FRO("abc") )

        self.assertTrue( DSTRING_FRO("abc") < DSTRING_FRO("abd") )
        self.assertFalse( DSTRING_FRO("abc") > DSTRING_FRO("abd") )

        self.assertTrue( DSTRING_FRO("a") < DSTRING_FRO("b") )
        self.assertFalse( DSTRING_FRO("a") > DSTRING_FRO("b") )

        self.assertTrue( DSTRING_FRO("mam") < DSTRING_FRO("mām") )
        self.assertFalse( DSTRING_FRO("mam") > DSTRING_FRO("mām") )

        self.assertFalse( DSTRING_FRO("romam") < DSTRING_FRO("Romam") )
        self.assertFalse( DSTRING_FRO("romam") > DSTRING_FRO("Romam") )

        self.assertFalse( DSTRING_FRO("ca") > DSTRING_FRO("ça") )
        self.assertFalse( DSTRING_FRO("ca") < DSTRING_FRO("ça") )
        
        self.assertFalse( DSTRING_FRO("pe") < DSTRING_FRO("pé") )
        self.assertFalse( DSTRING_FRO("pe") > DSTRING_FRO("pé") )

        # with unknown characters :
        self.assertTrue( DSTRING_FRO("ab") < DSTRING_FRO("a²") )
        self.assertFalse( DSTRING_FRO("ab") > DSTRING_FRO("a²") )

        self.assertTrue( DSTRING_FRO("abc") < DSTRING_FRO("a²c") )
        self.assertFalse( DSTRING_FRO("abc") > DSTRING_FRO("a²c") )

    #///////////////////////////////////////////////////////////////////////////
    def test_startswith(self):
        """
                TESTSDStringFRO.test_startswith
        """
        string = DSTRING_FRO("çà")
        self.assertEqual( string.startswith( DSTRING_FRO("ç") ), True )
        self.assertEqual( string.startswith( DSTRING_FRO("") ), True )
        self.assertEqual( string.startswith( DSTRING_FRO("çà") ), True )
        self.assertEqual( string.startswith( DSTRING_FRO("S") ), False )
