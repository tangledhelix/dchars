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
    ❏DChars❏ : dchars/tests/languages/lat/transliterations/basic_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
DSTRING_LAT = new_dstring(language="latīna",
                          transliteration_method="basic",
                          options = {"anonymize the unknown characters" : "yes",
                                     },
                         )

LIST_OF_RECIPROCAL_EXAMPLES = (
    ('',        ''      ),
    ('a',       'a'     ),
    ('p',       'p'     ),
    ('ï',       'i+'    ),
    ("Q",       'Q'     ),
    ("ō",       'o_'    ),
    ("Quōēre,", 'Quo_e_re,'),
    ("N",       'N'     ),
    (" ",       ' '     ),
    ("iïi",     'ii+i'  ),
    ("a",       'a'     ),
    ("A",       'A'     ),
    ("á",       "a/"    ),
    ("ā́",       "a/_"   ),
    ("ï",       "i+"    ),
    ("ā́̈",       "a/_+"  ),
    ("A",       'A'     ),
    ("abcedefg",'abcedefg'),
    ("WXYZ",    'WXYZ'  ),
    ("Á̄̈",       "A/_+"  ),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringLAT(unittest.TestCase):
    """
        class TESTSDStringLAT

        We test dchars.languages.lat.transliterations.basic.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_alternative_characters(self):
        """
                TESTSDStringLAT.test_alternative_characters
        """

        for txt1, txt2 in (
                ("ä́̄", "ā́̈"),     # 00E4 0301 304 / # 0101 0301 0308
                ("ǟ́", "ā́̈"),     # 00E4 0304 301 / # 0101 0301 0308
                ("Ǟ́", "Á̄̈"),     # 00C4 0304 0301 / # 00C1 0304 0308
                ):

            string1 = DSTRING_LAT(txt1)
            string2 = DSTRING_LAT(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringLAT.test_from_srcstr_2_srcstr()
        """

        for lat, lat_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_LAT().init_from_transliteration(lat_basic)
            self.assertEqual( lat, str(string) )
            lat_basic2 = string.get_transliteration()
            self.assertEqual( lat_basic, lat_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration1(self):
        """
                TESTSDStringLAT.test_get_transliteration1
        """
        for lat, lat_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_LAT(lat)
            lat_basic2 = string.get_transliteration()
            self.assertEqual( lat_basic, lat_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration2(self):
        """
                TESTSDStringLAT.test_get_transliteration

                This function uses non-reciprocal characters.
        """
        for txt, trans in (
                            # 00E4 + 0301
                            ("ä́",    'a/+'          ),
                            # 00C4 0304 0301
                            ("Ǟ́",    'A/_+'          ),
                          ):
            string = DSTRING_LAT(txt)
            self.assertEqual( string.get_transliteration(), trans )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringLAT.test_init_from_transliteration1
        """

        for lat, lat_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_LAT().init_from_transliteration(lat_basic)
            lat2 = str(string)
            self.assertEqual( lat, lat2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration2(self):
        """
                TESTSDStringLAT.test_init_from_transliteration2
        """
        for filename in ( os.path.join("tests", "languages", "lat",
                                       "text001_Cicero_In_Pisonem.txt"),

                          os.path.join("tests", "languages", "lat",
                                       "text002_Virgil_Aeneid_I.txt"),

                          os.path.join("tests", "languages", "lat",
                                       "text003_Cicero_In_Catilinam_I.txt")
                        ):

            with open( filename, 'r' ) as src:

                txt = src.read()

                trans1 = DSTRING_LAT(txt).get_transliteration()
                string = DSTRING_LAT().init_from_transliteration(trans1)
                trans2 = string.get_transliteration()
                self.assertEqual(trans1, trans2)

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringLAT.test_unknown_characters
        """
        string = DSTRING_LAT("²Quōēre²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"Quōēre"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_LAT().init_from_transliteration("²Quo_e_re²Quo_e_re²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"Quōēre"+UNKNOWN_CHAR_SYMBOL+ \
                          "Quōēre"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_LAT().init_from_transliteration("²Quo_e_re²Quo_e_re²")
        self.assertEqual( string.get_transliteration(),
                          UNKNOWN_CHAR_SYMBOL+"Quo_e_re"+UNKNOWN_CHAR_SYMBOL+ \
                          "Quo_e_re"+UNKNOWN_CHAR_SYMBOL )


