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
#    (at your option) any hboer version.
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
    ❏DChars❏ : dchars/tests/languages/hbo/transliterations/basic_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
DSTRING_HBO = new_dstring(language="עִבְֿרִיתֿ מִקְרָאִיתֿ",
                          transliteration_method = "basic",
                          options = {"anonymize the unknown characters" : 'no'},
                          )

DSTRING_HBO__UNKNOWNCHAR = new_dstring(language="עִבְֿרִיתֿ מִקְרָאִיתֿ",
                                       transliteration_method = "basic",
                                       options = {"anonymize the unknown characters" : 'yes'},
                                      )

LIST_OF_RECIPROCAL_EXAMPLES = (
                ("",        ''      ),
                ("ב",       'ḇ'     ),
                ("בּ",       'b'     ),
                ("וּ",       'W'    ),
                ("בַּ",       "ba"    ),
                ("בֻּ",       "bu"    ),
                # + "HEBREW MARK UPPER DOT" (from SPECIALPOINTS)
                ("בַּׄ",       "ba#HEBREW MARK UPPER DOT#"    ),
                # + "HEBREW MARK LOWER DOT" (from SPECIALPOINTS)
                ("בֻּׅ",       "bu#HEBREW MARK LOWER DOT#"    ),
                ("בֻּֽ",       "bu|"    ),     # + methegh
                ("שׁ",       "š",     ),
                ("שּׁ",       "Š",     ),
                ("שׂ",       "ś",     ),
                ("שּׂ",       "Ś",     ),
                ("ש",       "S",    ),
                ("שּ",       "S+S",  ),
                # + methegh + raphe :
                ("בֻּֽֿ",       "bu|-"    ),
                # + methegh + raphe + TELISHA GEDOLA (05A0) :
                ("בֻּֽֿ֠",       "bu|-<HEBREW ACCENT TELISHA GEDOLA>"    ),
                ("(ב)",       '(ḇ)'     ),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringHBO(unittest.TestCase):
    """
        class TESTSDStringHBO

        We test dchars.languages.hbo.transliterations.basic.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringHBO.test_from_srcstr_2_srcstr()
        """

        for hbo, hbo_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_HBO().init_from_transliteration(hbo_basic)
            self.assertEqual( hbo, str(string) )
            hbo_basic2 = string.get_transliteration()
            self.assertEqual( hbo_basic, hbo_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration1(self):
        """
                TESTSDStringHBO.test_get_transliteration1
        """
        for hbo, hbo_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_HBO(hbo)
            hbo_basic2 = string.get_transliteration()
            self.assertEqual( hbo_basic, hbo_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration2(self):
        """
                TESTSDStringHBO.test_get_transliteration2
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
                                      "text003_Jonah_I.txt")
                         ):

            with open( srcfilename, 'r' ) as src:
                txt = src.readlines()

                for line in txt:
                    string = DSTRING_HBO(line)
                    string.get_transliteration()

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringHBO.test_init_from_transliteration1
        """

        for hbo, hbo_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_HBO().init_from_transliteration(hbo_basic)
            hbo2 = str(string)
            self.assertEqual( hbo, hbo2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration2(self):
        """
                TESTSDStringHBO.test_init_from_transliteration1
        """
        for txt in ( "",
                     "ב",
                     "בּ",
                     "מּמ",
                     "ךכּךככ",
                     "וּוווּ",
                     "נּנ",
                     "ננּ",
                     "ן",
                     "הּה",
                     "פּפף",
                     "ץצּצ",
                     "ש",
                     "שּ",
                     "שׂ",
                     "שּׂ",
                     "לַלִלֹלְלֲ",
                     "כַּֽ",
                     "כַּֿ",
                     "כַּֽֿ",
                     "לַ֕",
                     "לַֽֿ֕",
                     "(ב)",
                     ):

            trans1 = DSTRING_HBO(txt).get_transliteration()
            string = DSTRING_HBO().init_from_transliteration(trans1)
            trans2 = string.get_transliteration()
            self.assertEqual(trans1, trans2)

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration3(self):
        """
                TESTSDStringHBO.test_init_from_transliteration3
        """
        for filename in ( os.path.join("dchars",
                                       "tests",
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

            with open( filename, 'r' ) as src:

                txt = src.read()

                trans1 = DSTRING_HBO(txt).get_transliteration()
                string1 = DSTRING_HBO().init_from_transliteration(trans1)
                trans2 = string1.get_transliteration()
                self.assertEqual(trans1, trans2)
                string2 = DSTRING_HBO().init_from_transliteration(trans2)
                self.assertEqual(string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringHBO.test_unknown_characters
        """

        string = DSTRING_HBO__UNKNOWNCHAR("ðבּð")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"בּ"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_HBO__UNKNOWNCHAR().init_from_transliteration("ðbðbð")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"בּ"+UNKNOWN_CHAR_SYMBOL+ \
                          "בּ"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_HBO__UNKNOWNCHAR().init_from_transliteration("ðbðbð")
        self.assertEqual( string.get_transliteration(),
                          UNKNOWN_CHAR_SYMBOL+"b"+UNKNOWN_CHAR_SYMBOL+ \
                          "b"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_HBO("ðבּð")
        self.assertEqual( str(string), "ðבּð" )

        string = DSTRING_HBO().init_from_transliteration("ðbðbð")
        self.assertEqual( str(string), "ðבּðבּð" )

        string = DSTRING_HBO().init_from_transliteration("ðbðbð")
        self.assertEqual( string.get_transliteration(), "ðbðbð" )

