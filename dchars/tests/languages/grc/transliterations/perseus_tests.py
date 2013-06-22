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
    ❏DChars❏ : dchars/tests/languages/grc/transliterations/perseus_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.symbols.symbols import UNKNOWN_CHAR_SYMBOL

DSTRING_GRC = new_dstring(language="Ἑλληνικὴ γλῶττα",
                          transliteration_method = "perseus",
                          options = {"anonymize the unknown characters" : False},
                          )

DSTRING_GRC__UNKNOWNCHAR = new_dstring(language="Ἑλληνικὴ γλῶττα",
                                       transliteration_method = "perseus",
                                       options = {"anonymize the unknown characters" : True},
                                      )

LIST_OF_RECIPROCAL_EXAMPLES = (
    ("",        ''),
    ("ά",       'a/'),
    ("ἁ",       'a('),
    ("ἅ",       "a(/"),
    ("ἆ",       "a)="),
    ("ᾇ",       "a(=|"),
    ('ϋᾱᾱ̈',     "u+a&a+&"),
    ('ἆ ἆ',     "a)= a)="),
    ("ὁ, οἱ",   "o(, oi("),
    ('ᾯ',       "*(=w|"),
    ('Ἢ',       "*)\\h"),
    ("ξ",       "c"),
    ("Ξ",       "*c"),
    ("ἐν",      "e)n"),
    ("πρόσ",    "pro/s"),
    ("τῶν",     "tw=n"),
    ("πρὸσ",    "pro\\s"),
    ("προϊέναι","proi+e/nai"),
    ("τῷ",      "tw=|"),
    ("μαχαίρᾱσ","maxai/ra&s"),
    ("μάχαιρᾰ", "ma/xaira'"),
    ('βἆ',      "ba)="),
    ('ΠΛΑΤΩΝ',  "*p*l*a*t*w*n"),
    ('Ἀγαμέμνων',"*)agame/mnwn"),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringGRC(unittest.TestCase):
    """
        class TESTSDStringGRC

        We test dchars.languages.grc.transliterations.perseus.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringGRC.test_from_srcstr_2_srcstr()
        """

        for grc, grc_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_GRC().init_from_transliteration(grc_basic)
            self.assertEqual( grc, str(string) )
            grc_basic2 = string.get_transliteration()
            self.assertEqual( grc_basic, grc_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration1(self):
        """
                TESTSDStringGRC.test_get_transliteration1
        """
        for grc, grc_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_GRC(grc)
            grc_basic2 = string.get_transliteration()
            self.assertEqual( grc_basic, grc_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration2(self):
        """
                TESTSDStringGRC.test_get_transliteration2

                This function uses non-reciprocal characters.
        """
        for txt, trans in ( ("",          ""             ),
                            ("ξ",         "c"            ),
                            ("Ξ",         "*c"           ),
                            ("ἐν",        'e)n'          ),
                            ("ὁ, οἱ",     'o(, oi('      ),
                            ("πρός",      "pro/s"        ),
                            ("τῶν",       "tw=n"         ),
                            ("πρὸς",      "pro\\s"       ),
                            ("προϊέναι",  "proi+e/nai"   ),
                            ("τῷ",        "tw=|"         ),
                            ("μαχαίρᾱς",  "maxai/ra&s"   ),
                            ("μάχαιρᾰ",   "ma/xaira'"    ),
                            ("ᾧ",         "w(=|"         ),
                            ("ᾯ",         "*(=w|"        ),
                            ("ΠΛΑΤΩΝ",    "*p*l*a*t*w*n" ),
                            ("Πλάτων",    "*pla/twn"     ),
                            ("(12Πλάτων)","(12*pla/twn)" ),
                            ("(9 Πλάτων}","(9 *pla/twn}" ),
                            ("[9 Πλάτων]","[9 *pla/twn]" ),
                            (".;!Πλάτων]",".?!*pla/twn]" ),
                            ("²Πλάτων²",  "²*pla/twn²"   ),
                          ):
            string = DSTRING_GRC(txt)
            self.assertEqual( string.get_transliteration(), trans )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringGRC.test_init_from_transliteration1
        """

        for grc, grc_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_GRC().init_from_transliteration(grc_basic)
            grc2 = str(string)
            self.assertEqual( grc, grc2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration2(self):
        """
                TESTSDStringGRC.test_init_from_transliteration2
        """
        for txt in ( "",
                     "ξ",
                     "Ξ",
                     "ἐν",
                     "ὁ, οἱ",
                     "πρός",
                     "τῶν",
                     "πρὸς",
                     "προϊέναι",
                     "τῷ",
                     "μαχαίρᾱς",
                     "μάχαιρᾰ",
                     'βἆ',
                     'βϐ',
                     'ϋᾱᾱ̈',
                     'ἆ ἆ',
                     'ἆ ἆ '
                     '[ἆ ἆ]'
                     '{ἆ ἆ}'
                     '{0ἆ ἆ2}'
                     'σς',
                     'ΠΛΑΤΩΝ',
                     'Ἀγαμέμνων',
                     '"ᾯ"',
                     'Ἢ',
                     ):

            trans1 = DSTRING_GRC(txt).get_transliteration()
            string1 = DSTRING_GRC().init_from_transliteration(trans1)
            trans2 = string1.get_transliteration()
            self.assertEqual(trans1, trans2)
            string2 = DSTRING_GRC().init_from_transliteration(trans2)
            self.assertEqual(string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration3(self):
        """
                TESTSDStringGRC.test_init_from_transliteration3
        """
        for filename in ( os.path.join("dchars",
                                       "tests",
                                       "languages",
                                       "grc",
                                       "text001_Lucian_Dialogues_of_the_Gods.txt"),

                          os.path.join("dchars",
                                       "tests",
                                       "languages",
                                       "grc",
                                       "text002_Iliad_I_v1_205.txt"),

                          os.path.join("dchars",
                                       "tests",
                                       "languages",
                                       "grc",
                                       "text003_Euripides_Bacchae_1_104.txt")
                        ):

            with open( filename, 'r' ) as src:

                txt = src.read()

                trans1 = DSTRING_GRC(txt).get_transliteration()
                string = DSTRING_GRC().init_from_transliteration(trans1)
                trans2 = string.get_transliteration()
                self.assertEqual(trans1, trans2)

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringGRC.test_unknown_characters
        """
        string = DSTRING_GRC("²ἆ²")
        self.assertEqual( str(string), "²ἆ²" )

        string = DSTRING_GRC().init_from_transliteration("²a)=²a)=²")
        self.assertEqual( str(string), "²ἆ²ἆ²" )

        string = DSTRING_GRC().init_from_transliteration("²a)=²a)=²")
        self.assertEqual( string.get_transliteration(), "²a)=²a)=²" )


        string = DSTRING_GRC__UNKNOWNCHAR("²ἆ²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"ἆ"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_GRC__UNKNOWNCHAR().init_from_transliteration("²a)=²a)=²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"ἆ"+UNKNOWN_CHAR_SYMBOL+ \
                          "ἆ"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_GRC__UNKNOWNCHAR().init_from_transliteration("²a)=²a)=²")
        self.assertEqual( string.get_transliteration(),
                          UNKNOWN_CHAR_SYMBOL+"a)="+UNKNOWN_CHAR_SYMBOL+ \
                          "a)="+UNKNOWN_CHAR_SYMBOL )
