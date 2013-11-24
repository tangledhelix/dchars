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
    ❏DChars❏ : dchars/tests/languages/san/san_tests.py
"""

import unittest, os.path

from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_SAN = new_dstring(language='संस्कृतम्',
                          options = {"anonymize the unknown characters" : 'no'},
                          )

DSTRING_SAN__UNKNOWNCHAR = new_dstring(language='संस्कृतम्',
                          options = {"anonymize the unknown characters" : 'yes'},
                          )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringSAN(unittest.TestCase):
    """
        class TESTSDStringSAN

        We test  dchars.languages.san.dchars::DStringSAN
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTSDStringSAN.test_add
        """
        string1 = DSTRING_SAN("क")
        string2 = DSTRING_SAN("ए")
        string3 = string1 + string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_SAN )
        string1[0].base_char = "भ"
        self.assertEqual( DSTRING_SAN("क") + DSTRING_SAN("ए"), string3 )

        string1 = DSTRING_SAN("क")
        string2 = DSTRING_SAN("ए")
        string3 = string1 + string2
        string1 += string2
        self.assertEqual( string1 + string2, string3 )
        self.assertEqual( type(string3), DSTRING_SAN )

    #///////////////////////////////////////////////////////////////////////////
    def test_base_char(self):
        """
                TESTSDStringSAN.test_base_char
        """

        # क and कि have the same base character :
        string = DSTRING_SAN("क")
        self.assertEqual( string[0].base_char, "KA" )

        string = DSTRING_SAN("कि")
        self.assertEqual( string[0].base_char, "KA" )

    #///////////////////////////////////////////////////////////////////////////
    def test_clone(self):
        """
                TESTSDStringSAN.test_clone
        """
        string0 = DSTRING_SAN("क")
        string1 = DSTRING_SAN("क")
        string2 = string1.clone()
        self.assertEqual( string1, string2 )

        string1[0].base_char = "प"
        string1[0].accent = "DEVANAGARI STRESS SIGN UDATTA"
        string1[0].dependentvowel = "II"

        self.assertEqual( string0, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringSAN.test_emptystring
        """

        string = DSTRING_SAN("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringSAN.test_from_srcstr_2_srcstr
        """

        for txt1 in ('पँ', # 092A(pa) + 0901(candrabindu)
                     '',
                     'क',
                     'कऄ',
                     'का',
                     'कि',
                     'अआइईउऊऋॠएऐओऔ',
                     'कखगघह',
                     'चछजझ',
                     'टठडढ',
                     'तथदधलस',
                     'पफबभ',
                     'अअँपँआआँपाँएएँपेंओओंपों',
                     'एऽ',
                     'एः',
                     'क़ख़ग़ज़ड़ढ़फ़', # + nukta
                     # (consonants) simple character1, simple character2, character1+character2
                     'सतस्तबदब्दषयष्यकयक्यफ़तफ़्त',
                     # (the र consonant) simple character1, simple character2, character1+character2
                     'परप्रगरग्रटरट्ररतर्तरचार्चाररर्र',
                     # (vowels) simple character1, simple character2, character1+character2
                     'दवद्वदधद्धशवश्वहमह्महवह्व',
                     # (special cases) simple character1, simple character2, character1+character2
                     'ततत्ततरत्रकतक्तददद्ददयद्यदमद्मकरक्रजञज्ञकषक्ष',
                     # other characters :
                     "।",
                     "॥",
                     "ॐ",
                     "प॑",       # + udatta
                     "प॒",       # + anudatta
                     "॰"
                     " ",
                     "ऩ॥ककाएःक़स़", # NA + nukta; KA + nukta, SA + nukta
                     ):

            string = DSTRING_SAN(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_SAN(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringSAN.test_get_sourcestr_repr
        """
        txt1 = "क"
        string1 = DSTRING_SAN(txt1)
        txt2 = string1.get_sourcestr_representation()+"इ"
        string2 = DSTRING_SAN(txt2)

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_SAN(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_SAN(txt2)
        self.assertEqual( string1, string2 )

        txt1 = "क"
        string1 = DSTRING_SAN__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()+"इ"
        string2 = DSTRING_SAN__UNKNOWNCHAR(txt2)

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_SAN__UNKNOWNCHAR(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_SAN__UNKNOWNCHAR(txt2)
        self.assertEqual( string1, string2 )

        for txt1 in ('पँ', # 092A(pa) + 0901(candrabindu)
                     '',
                     'क',
                     'कऄ',
                     'का',
                     'कि',
                     'अआइईउऊऋॠएऐओऔ',
                     'कखगघह',
                     'चछजझ',
                     'टठडढ',
                     'तथदधलस',
                     'पफबभ',
                     'अअँपँआआँपाँएएँपेंओओंपों',
                     'एऽ',
                     'एः',
                     'क़ख़ग़ज़ड़ढ़फ़', # + nukta
                     # (consonants) simple character1, simple character2, character1+character2
                     'सतस्तबदब्दषयष्यकयक्यफ़तफ़्त',
                     # (the र consonant) simple character1, simple character2, character1+character2
                     'परप्रगरग्रटरट्ररतर्तरचार्चाररर्र',
                     # (vowels) simple character1, simple character2, character1+character2
                     'दवद्वदधद्धशवश्वहमह्महवह्व',
                     # (special cases) simple character1, simple character2, character1+character2
                     'ततत्ततरत्रकतक्तददद्ददयद्यदमद्मकरक्रजञज्ञकषक्ष',
                     # other characters :
                     "।",
                     "॥",
                     "ॐ",
                     "प॑",       # + udatta
                     "प॒",       # + anudatta
                     "॰"
                     " ",
                     "ऩ॥ककाएःक़स़", # NA + nukta; KA + nukta, SA + nukta
                     ):

            string1 = DSTRING_SAN(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_SAN(txt2)
            self.assertEqual( string1, string2 )

            string1 = DSTRING_SAN__UNKNOWNCHAR(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_SAN__UNKNOWNCHAR(txt2)
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr2(self):
        """
                TESTSDStringSAN.test_get_sourcestr_repr2
        """

        for srcfile in ( os.path.join("tests",
                                      "languages",
                                      "san",
                                      "text001_Rigveda_1.txt"),

                         os.path.join("tests",
                                      "languages",
                                      "san",
                                      "text002_Mahabharata_I_1.txt") ):

            with open( srcfile, 'r') as src:

                for _txt1 in src.readlines():

                    txt1 = _txt1

                    # we have to delete a lot of characters having nothing
                    # to do with the devanagari :
                    for char_to_be_deleted in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                               "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                                               "u", "v", "w", "x", "y", "z"
                                               ):
                        txt1 = txt1.replace(char_to_be_deleted, "")

                    string1 = DSTRING_SAN(txt1)
                    txt2 = string1.get_sourcestr_representation()
                    string2 = DSTRING_SAN(txt2)
                    self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringSAN.test_normalstring
        """

        #.......................................................................
        string = DSTRING_SAN("*ॐ॥*ककाएःक**")
        self.assertEqual( len(string), 11 )

        for index in range(0, 11):
            if index in (0, 3, 9, 10):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "DEVANAGARI OM" )
        self.assertEqual( string[1].punctuation, False )

        self.assertEqual( string[2].base_char, "DEVANAGARI DOUBLE DANDA" )
        self.assertEqual( string[2].punctuation, True )

        self.assertEqual( str(string), "*ॐ॥*ककाएःक**")

        #.......................................................................
        string = DSTRING_SAN__UNKNOWNCHAR("*ॐ॥*ककाएःक**")
        self.assertEqual( len(string), 11 )

        for index in range(0, 11):
            if index in (0, 3, 9, 10):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "DEVANAGARI OM" )
        self.assertEqual( string[1].punctuation, False )

        self.assertEqual( string[2].base_char, "DEVANAGARI DOUBLE DANDA" )
        self.assertEqual( string[2].punctuation, True )

        self.assertEqual( str(string), "{0}ॐ॥{0}ककाएःक{0}{0}".format( UNKNOWN_CHAR_SYMBOL) )

        #.......................................................................
        string = DSTRING_SAN("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_SAN__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring2(self):
        """
                TESTSDStringSAN.test_normalstring2

                (with nukta)
        """
        string = DSTRING_SAN("*ऩ॥*ककाएःक़स़**")
        self.assertEqual( len(string), 12 )

        for index in range(0, 12):
            if index in (0, 3, 10, 11):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        # string[1] = NA + nukta
        self.assertEqual( string[1].base_char, "NA" )
        self.assertEqual( string[1].nukta, True )
        self.assertEqual( string[1].punctuation, False )

        # string[8] = KA + nukta
        self.assertEqual( string[8].base_char, "KA" )
        self.assertEqual( string[8].nukta, True )
        self.assertEqual( string[8].punctuation, False )

        # string[9] = SA + nukta
        self.assertEqual( string[9].base_char, "SA" )
        self.assertEqual( string[9].nukta, True )
        self.assertEqual( string[9].punctuation, False )

        self.assertEqual( str(string), "*ऩ॥*ककाएःक़स़**")


        string = DSTRING_SAN__UNKNOWNCHAR("*ऩ॥*ककाएःक़स़**")
        self.assertEqual( len(string), 12 )

        for index in range(0, 12):
            if index in (0, 3, 10, 11):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        # string[1] = NA + nukta
        self.assertEqual( string[1].base_char, "NA" )
        self.assertEqual( string[1].nukta, True )
        self.assertEqual( string[1].punctuation, False )

        # string[8] = KA + nukta
        self.assertEqual( string[8].base_char, "KA" )
        self.assertEqual( string[8].nukta, True )
        self.assertEqual( string[8].punctuation, False )

        # string[9] = SA + nukta
        self.assertEqual( string[9].base_char, "SA" )
        self.assertEqual( string[9].nukta, True )
        self.assertEqual( string[9].punctuation, False )

        self.assertEqual( str(string), "{0}ऩ॥{0}ककाएःक़स़{0}{0}".format( UNKNOWN_CHAR_SYMBOL) )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstring(self):
        """
                TESTSDStringSAN.test_problematicstring
        """

        # क with two udatta :
        with self.assertRaises( DCharsError ):
            DSTRING_SAN("क॑॑")

        # क with two virama :
        with self.assertRaises( DCharsError ):
            DSTRING_SAN("क््")

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue(self):
        """
                TESTSDStringSAN.test_sortingvalue
        """

        #.......................................................................
        # comparisons between two characters :
        #.......................................................................
        str1 = "क"
        str2 = "क"
        self.assertTrue( DSTRING_SAN(str1)[0] == DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] != DSTRING_SAN(str2)[0] )

        str1 = "क"
        str2 = "ग"
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        str1 = "क"
        str2 = "क़"      # = क + nukta
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        str1 = "हू"
        str2 = "हूँ"      # = हू + candrabindu
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        str1 = "क"
        str2 = "कि"
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        str1 = "अ"
        str2 = "क"
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        str1 = "अ"
        str2 = "आ"
        self.assertTrue( DSTRING_SAN(str1)[0] < DSTRING_SAN(str2)[0] )
        self.assertFalse( DSTRING_SAN(str1)[0] > DSTRING_SAN(str2)[0] )

        #.......................................................................
        # comparisons between two strings :
        #.......................................................................
        str1 = "क"
        str2 = "क"
        self.assertTrue( DSTRING_SAN(str1) == DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) != DSTRING_SAN(str2) )

        str1 = "क"
        str2 = "कक"
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        str1 = "कक"
        str2 = "कं"
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        str1 = "क"
        str2 = "कि"
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertTrue( DSTRING_SAN(str1) <= DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) >= DSTRING_SAN(str2) )

        str1 = "कं"      # क + anusvara
        str2 = "कः"     # क + visarga
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        str1 = "क"      # क
        str2 = "कः"     # क + visarga
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        str1 = "क"     # क
        str2 = "कं"      # क + anusvara
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        str1 = "हू"
        str2 = "हूँ"      # = हू + candrabindu
        self.assertTrue( DSTRING_SAN(str1) < DSTRING_SAN(str2) )
        self.assertFalse( DSTRING_SAN(str1) > DSTRING_SAN(str2) )

        # with unknown characters :
        self.assertTrue( DSTRING_SAN("ककाएःक़स़") < DSTRING_SAN("ककाएः²स़") )
        self.assertFalse( DSTRING_SAN("ककाएःक़स़") > DSTRING_SAN("ककाएः²स़") )

    #///////////////////////////////////////////////////////////////////////////
    def test_sortingvalue2(self):
        """
                TESTSDStringSAN.test_sortingvalue2

                We try to compute the "sorting value" of many words.
        """
        for srcfilename in (
                        os.path.join("tests",
                                     "languages",
                                     "san",
                                     "text001_Rigveda_1.txt"),

                        os.path.join("tests",
                                     "languages",
                                     "san",
                                     "text002_Mahabharata_I_1.txt") ):

            with open( srcfilename, 'r') as src:

                for line in src.readlines():
                    for word in line.split():
                        DSTRING_SAN(word).sortingvalue()

