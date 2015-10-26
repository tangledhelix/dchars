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
    ❏DChars❏ : dchars/tests/languages/ang/transliterations/basic_tests.py
"""

import unittest

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
DSTRING_ANG = new_dstring(language="Ænglisc",
                          transliteration_method="basic",
                          options = {"anonymize the unknown characters" : "yes",
                                     },
                         )

LIST_OF_RECIPROCAL_EXAMPLES = (
    ('',        ''      ),
    ('a',       'a'     ),
    ('p',       'p'     ),
    ("Q",       'Q'     ),
    ("ō",       'o_'    ),
    ("Quōēre,", 'Quo_e_re,'),
    ("N",       'N'     ),
    (" ",       ' '     ),
    ("è",       'e\\'   ),
    ("a",       'a'     ),
    ("A",       'A'     ),
    ("á",       "a/"    ),
    ("ā́",       "a/_"   ),
    ("A",       'A'     ),
    ("abcedefg",'abcedefg'),
    ("WXYZ",    'WXYZ'  ),
    ("ǣ",       'a+e_'  ),
    ("Æ",       "A+E"   ),
    ("a̽",       "a*"    ),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringANG(unittest.TestCase):
    """
        class TESTSDStringANG

        We test dchars.languages.ang.transliterations.basic.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringANG.test_from_srcstr_2_srcstr()
        """

        for ang, ang_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_ANG().init_from_transliteration(ang_basic)
            self.assertEqual( ang, str(string) )
            ang_basic2 = string.get_transliteration()
            self.assertEqual( ang_basic, ang_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration1(self):
        """
                TESTSDStringANG.test_get_transliteration1
        """
        for ang, ang_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_ANG(ang)
            ang_basic2 = string.get_transliteration()
            self.assertEqual( ang_basic, ang_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringANG.test_init_from_transliteration1
        """

        for ang, ang_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_ANG().init_from_transliteration(ang_basic)
            ang2 = str(string)
            self.assertEqual( ang, ang2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringANG.test_unknown_characters
        """
        string = DSTRING_ANG("²Quōēre²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"Quōēre"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_ANG().init_from_transliteration("²Quo_e_re²Quo_e_re²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"Quōēre"+UNKNOWN_CHAR_SYMBOL+ \
                          "Quōēre"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_ANG().init_from_transliteration("²Quo_e_re²Quo_e_re²")
        self.assertEqual( string.get_transliteration(),
                          UNKNOWN_CHAR_SYMBOL+"Quo_e_re"+UNKNOWN_CHAR_SYMBOL+ \
                          "Quo_e_re"+UNKNOWN_CHAR_SYMBOL )


