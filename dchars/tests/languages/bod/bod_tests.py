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
    ❏DChars❏ : dchars/tests/languages/bod/bod_tests.py
"""

import unittest
import os
from dchars.languages.bod.dstring import DStringBOD
from dchars.errors.errors import DCharsError
from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
from dchars.languages.bod.dcharacter import DCharacterBOD

# we need to specify the transliteration method since the sorting value
# of the dstrings are linked to the choosed method.
DSTRING_BOD = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "Tibetan or Sanskrit",
                                     "look up in the buffers" : False,
                                     "sorting method" : "basic",
                                     "anonymize the unknown characters" : False},)

DSTRING_BOD_BUFF = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "Tibetan or Sanskrit",
                                     "look up in the buffers" : True,
                                     "sorting method" : "basic",
                                     "anonymize the unknown characters" : False},)


DSTRING_BOD__UNKNOWNCHAR = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                           options = {"expected structure" : "Tibetan or Sanskrit",
                                     "look up in the buffers" : False,
                                     "sorting method" : "basic",
                                     "anonymize the unknown characters" : True},)

LIST_OF_EXAMPLES = (
    "ཀ", # 'ka'
    "ཀྲ", # 'kra'
    "ཀྭ", # 'kwa'
    "ཀྱ", # 'kya'
    "ཉ", # 'nya'
    "རྙ", # 'rnya'
    "ཀི", # 'ki'
    "ཀུ", # "ku"
    "ཀེ", # "ke"
    "ཀོ", # "ko"
    'ཨི', # "i"
    "ཀོང", # "kong"
    "བསྒྲིབས", #"bsgribs"
    "མགོན", #"mgon"
    "ཁམ་", #"kham "
    "ཁམས", #"khams"
    "འཇམ", #"'jam"
    "སྤྲུལ", #"sprul"
    "བློ", #"blo"
    "གྲོས", #"gros"
    "མཐའ་ཡས", #"mtha' yas"
    #"'jam mgon kong sprul blo gros mtha' yas "
    "འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་",
    "ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་", #"shes bya kun khyab mdzod "
    "གདམས་ངག་མཛོད་", #"gdams ngag mdzod "
    "རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་", #"rin chen gter mdzod chen mo "
    "རྒྱ་ཆེན་བཀའ་མཛོད་", #"rgya chen bka' mdzod "
    "ངེས་དོན་སྒྲོན་མེ་", #"nges don sgron me "
    "དཀྱིལ་འཁོར་", #"dkyil 'khor "
    "རྒྱུད་", #"rgyud "
    "རྩ་རྒྱུད་", #"rtsa rgyud "
    "བཤད་རྒྱུད་", #"bshad rgyud "
    "ཐེག་པ་དགུ་", #"theg pa dgu "
    "ཐེག་པ་རིམ་པ་དགུ་", #"theg pa rim pa dgu "
    "བློ་སྦྱོངས་དོན་བདུན་མ་", #"blo sbyongs don bdun ma "
    "རྙིང་མ་བཀའ་མ་", #"rnying ma bka' ma "
    "གཏེར་མ་", #"gter ma "
    "བྲག", #"brag"
    "བརག", #"b.rag"
    "གྱང", #"gyang"
    "གཡང", #"g.yang"
    "ཏཱ་ལའི་བླ་མ", #"tA la'i bla ma"
    "ཏཱ་ར་ནཱ་ཐ", #"tA ra nA tha"
    "བའི", #"ba'i"
    "པའོ", #"pa'o"
    "མཚོའི", #"mtsho'i"
    "མཇ", #"mja"
    "རྐ", #"rka"
    "འོད", #"'od"
    "ཡིད", #"yid"
    "གཡུག", #"g.yug"
    "ཁྱིའུ", #"khyi'u"
    "བམའི", #"bma'i"
    "བམའ", #"bma'"
    "མའི" , #"ma'i"
    "དབྱངས", #"dbyangs"
    "པའོ" , #"pa'o"
    "ཨའ", #"a'"
    "གྱཀ", #"gyaka"
    "གཡག", #"g.yag"
    "མང", #"mang"
    "བརྒྱུད", #"brgyud"
    "བཀའ་བརྒྱུད་སྔགས་མཛོད་", #"bka' brgyud sngags mdzod "
    "ཨ་ཁུ", #"a khu"
    "ཨུག་པ", #"ug pa"
    "རྡོེ", #"rdo+e"
    "བྲེུ", #"bru+e"
    "རྟ", #"rta"
    "གྷ", #"g+ha"
    "དྷ", #"d+ha"
    "བྷ", #"b+ha"
    "ཛྷ", #"dz+ha"
    "ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ", #"Ta Tha Da D+ha Na Sha"
    "ༀ", #"oM"
    "ཡོཾ", # yoM
    "ཀྵ", #"k+Sha"
    "ཕ༹", #"fa"
    "བ༹", #"va"
    "ཨ", #"a"
    "ཨཿ", #"aH"
    "མཱཿ", #"mAH"
    "གཏིཿ",# "gtiH"
    "ཀ྄", #"k?"
    "སཾ", #"saM"
    "སྃ", #"sa~M"
    "སྂ", #"sa~M`"
    "བྷྲཾ", #"b+h+raM"
    "གྷཾ", #"g+haM"
    "དྷི", #"d+hi"
    "བྷོ", #" b+ho
    "དྷའི", # "d+ha'i
    "ལབཿ", # labH
    "ནམཿ", # namH
    "ཡོགཿ", # yogH
    "མགབཿ", # mgabH
    "ཧོམཿ", # homH
    "སྦུདཿ", # sbudH
    "བེདཿ", # bedH
    "ཀོགསཿ", # kogsH
    "རྡོེཿ", # rdo+eH
    "རྡོེཾ", # rdo+eM
    "སེ་ངྷ་", # seng+ha
    "སིངྷ", # sing+ha
    "ཀརྨ་པ་ ", # karma pa
    "སཏྟྭ", # sat+t+wa
    "ཡོགཿཏནདྲ", # yogHtandra
    "ཀཽརབཱཿ", # kaurabAH
    "དྷརྨཿ", # d+harmaH
    "བ༹ནདྱ", # vand+ya
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringBOD(unittest.TestCase):
    """
        class TESTSDStringBOD

        We test  dchars.languages.bod.dchars::DStringBOD
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_emptystring(self):
        """
                TESTSDStringBOD.test_emptystring
        """

        string = DSTRING_BOD("")
        self.assertEqual( len(string), 0 )

        string = DSTRING_BOD_BUFF("")
        self.assertEqual( len(string), 0 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringBOD.test_from_srcstr_2_srcstr
        """

        for txt1 in LIST_OF_EXAMPLES:

            string = DSTRING_BOD(txt1)
            txt2 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

            string = DSTRING_BOD(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )


            string = DSTRING_BOD_BUFF(txt1)
            txt2 = string.get_sourcestr_representation()

            self.assertEqual( txt1, txt2 )

            string = DSTRING_BOD_BUFF(txt2)
            txt1 = string.get_sourcestr_representation()
            self.assertEqual( txt1, txt2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_sourcestr_repr(self):
        """
                TESTSDStringBOD.test_get_sourcestr_repr
        """

        #.......................................................................
        txt1 = "ཁ"
        string1 = DSTRING_BOD(txt1)
        txt2 = string1.get_sourcestr_representation()+"ང"
        string2 = DSTRING_BOD(txt2)
        self.assertNotEqual( string1, string2 )

        txt1 = "ཁ"
        string1 = DSTRING_BOD_BUFF(txt1)
        txt2 = string1.get_sourcestr_representation()+"ང"
        string2 = DSTRING_BOD_BUFF(txt2)
        self.assertNotEqual( string1, string2 )

        #.......................................................................
        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_BOD(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_BOD(txt2)
        self.assertEqual( string1, string2 )

        txt1 = UNKNOWN_CHAR_SYMBOL
        string1 = DSTRING_BOD_BUFF(txt1)
        txt2 = string1.get_sourcestr_representation()
        string2 = DSTRING_BOD_BUFF(txt2)
        self.assertEqual( string1, string2 )

        #.......................................................................
        for txt1 in LIST_OF_EXAMPLES:

            string1 = DSTRING_BOD(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_BOD(txt2)
            self.assertEqual( txt1, txt2 )
            self.assertEqual( string1, string2 )

            string1 = DSTRING_BOD_BUFF(txt1)
            txt2 = string1.get_sourcestr_representation()
            string2 = DSTRING_BOD_BUFF(txt2)
            self.assertEqual( txt1, txt2 )
            self.assertEqual( string1, string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_normalstring(self):
        """
                TESTSDStringBOD.test_normalstring
        """

        #.......................................................................
        string = DSTRING_BOD("µབསགྲིབསµ་")
        self.assertEqual( len(string), 8 )

        for index in range(0, 8):
            if index in (0, 6):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "B" )
        self.assertEqual( string[1].punctuation, False )

        self.assertEqual( string[7].base_char, "MARK INTERSYLLABIC TSHEG" )
        self.assertEqual( string[7].punctuation, True )


        string = DSTRING_BOD_BUFF("µབསགྲིབསµ་")
        self.assertEqual( len(string), 8 )

        for index in range(0, 8):
            if index in (0, 6):
                self.assertEqual( string[index].unknown_char, True )
            else:
                self.assertEqual( string[index].unknown_char, False )

        self.assertEqual( string[1].base_char, "B" )
        self.assertEqual( string[1].punctuation, False )

        self.assertEqual( string[7].base_char, "MARK INTERSYLLABIC TSHEG" )
        self.assertEqual( string[7].punctuation, True )


        #.......................................................................
        string = DSTRING_BOD("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

        string = DSTRING_BOD_BUFF("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )


        string = DSTRING_BOD__UNKNOWNCHAR("*")
        self.assertEqual( len(string), 1 )
        self.assertEqual( string[0].unknown_char, True )

    #///////////////////////////////////////////////////////////////////////////
    def test_equivalent_characters(self):
        """
                TESTSDStringBOD.test_equivalent_characters
        """

        #.......................................................................
        # D+ha
        #.......................................................................
        # [0F4C 0FB7] D+ha
        string1 = DSTRING_BOD("ཌྷ")
        # [004D] D+ha
        string2 = DSTRING_BOD("ཌྷ")
        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( str(string1), str(string2) )

        # [0F4C 0FB7] D+ha
        string1 = DSTRING_BOD_BUFF("ཌྷ")
        # [004D] D+ha
        string2 = DSTRING_BOD_BUFF("ཌྷ")
        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( str(string1), str(string2) )

        #.......................................................................
        # d+ha
        #.......................................................................
        # [0F51 0FB7 0F60 0F72] d+ha'i
        string1 = DSTRING_BOD("དྷའི")
        # [0F52 0F60 0F72] d+ha'i
        string2 = DSTRING_BOD("དྷའི")
        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( str(string1), str(string2) )

        # [0F51 0FB7 0F60 0F72] d+ha'i
        string1 = DSTRING_BOD_BUFF("དྷའི")
        # [0F52 0F60 0F72] d+ha'i
        string2 = DSTRING_BOD_BUFF("དྷའི")
        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( str(string1), str(string2) )

        #.......................................................................
        # oM
        #.......................................................................
        # 0F00
        string1 = DSTRING_BOD("ༀ")
        # 0F68 + 0F7C + 0F7E
        string2 = DSTRING_BOD("ཨོཾ")

        # in order to compare the istructs in the two strings we have to
        # set their respective indexes to the same value;
        #
        # their real_indexes are both equal to [0,]
        #
        string1.istructs[0].indexes = None # they are equal to [0,]
        string2.istructs[0].indexes = None # they are equal to [0, 1, 2]

        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( string1.istructs[0].punctuation_or_other_symbol, 'SYLLABLE OM' )
        self.assertEqual( str(string1), str(string2) )


        # 0F00
        string1 = DSTRING_BOD_BUFF("ༀ")
        # 0F68 + 0F7C + 0F7E
        string2 = DSTRING_BOD_BUFF("ཨོཾ")

        # in order to compare the istructs in the two strings we have to
        # set their respective indexes to the same value;
        #
        string1.istructs[0].indexes = None # they are equal to [0,]
        string2.istructs[0].indexes = None # they are equal to [0, 1, 2]

        self.assertTrue( string1.istructs.is_identical_to(string2.istructs) )
        self.assertEqual( string1.istructs[0].punctuation_or_other_symbol, 'SYLLABLE OM' )
        self.assertEqual( str(string1), str(string2) )

    #///////////////////////////////////////////////////////////////////////////
    def test_problematicstrings(self):
        """
                TESTSDStringBOD.test_problematicstrings
        """

        # ཀ with two anusvara (0F7E)
        with self.assertRaises( DCharsError ):
            DSTRING_BOD("ཀཾཾ")

        with self.assertRaises( DCharsError ):
            DSTRING_BOD_BUFF("ཀཾཾ")

        # ཀ with two signs "candrabindu" signs :
        #    SIGN SNA LDAN(0F83) and SIGN NYI ZLA NAA DA(0F82)
        with self.assertRaises( DCharsError ):
            DSTRING_BOD("ཀྂྃ")

        with self.assertRaises( DCharsError ):
            DSTRING_BOD_BUFF("ཀྂྃ")

    #///////////////////////////////////////////////////////////////////////////
    def test_modifications1(self):
        """
                TESTSDStringBOD.test_modifications1

                We modify DStringBOD objects by various manners.
        """

        #.......................................................................
        # (prefix)
        #.......................................................................
        string = DSTRING_BOD("བཐུ") # bthu

        string.istructs[0].prefix = "G" # ག as a prefix
        self.assertEqual( string[0].base_char, 'G' )
        self.assertEqual( str(string), "གཐུ")

        string[0].base_char = "B" # བ as a prefix
        self.assertEqual( string.istructs[0].prefix, 'B' )
        self.assertEqual( str(string), "བཐུ")

        #.......................................................................
        # (prefix->superfix)
        #.......................................................................
        string = DSTRING_BOD("བགྲིབས") # bgribs

        string[0].base_char = "L" # ལ as a superfix
        self.assertEqual( string.istructs[0].prefix, None )
        self.assertEqual( string.istructs[0].superfix, "L" )
        self.assertEqual( str(string), "ལྒྲིབས")

        #.......................................................................
        # (superfix)
        #.......................................................................
        string = DSTRING_BOD("བསྒྲིབས") # bsgribs
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)S(consonant)G" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )

        string.istructs[0].superfix = "R" # ར as a superfix
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)R(consonant)G" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )

        string[1].base_char = "S" # ས as a superfix
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)S(consonant)G" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )

        #.......................................................................
        # (main consonant)
        #.......................................................................
        string = DSTRING_BOD("བསྒྲིབས") # bsgribs
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)S(consonant)G" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )

        string.istructs[0].consonant = "K" # ཀ as a main consonant
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)S(consonant)K" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )

        string[1].subj_consonants[0] = "G" # ག as a main consonant
        self.assertEqual( str(string.istructs),
                          "(prefix)B(superfix)S(consonant)G" + \
                          "(subfix)['R'](vowel1)I(suffix1)B(suffix2)S" )



        #.......................................................................
        # (main consonant)
        #.......................................................................
        string1 = DSTRING_BOD("ཀཀཀ")
        string1.istructs[1].consonant = "G"
        self.assertEqual( str(string1), chr(0x0F40)+chr(0x0F42)+chr(0x0F40) )

        #.......................................................................
        # (suffix1)
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲིདས") # bsgrids

        string = DSTRING_BOD("བསྒྲིབས")

        string.istructs[0].suffix1 = "D" # ད as a suffix1
        self.assertEqual( str(string), str(string2) )

        string[-2].base_char = "B" # བ as a suffix1
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (suffix2)
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲིབད") # bsgribd

        string = DSTRING_BOD("བསྒྲིབས")

        string.istructs[0].suffix2 = "D" # ད as a suffix2
        self.assertEqual( str(string), str(string2) )

        string[-1].base_char = "S" # ས as a suffix2
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (vowel #1)
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲཱིབས") # bsgrIbs

        string = DSTRING_BOD("བསྒྲིབས")

        string.istructs[0].vowel1 = "II"
        self.assertEqual( str(string), str(string2) )

        string[1].vowel1 = "I"
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (vowel #2)
        #.......................................................................
        string1 = DSTRING_BOD("རྡོེ") # rdo+e
        string2 = DSTRING_BOD("རྡོ") # rdo

        string = DSTRING_BOD("རྡོེ")

        string.istructs[0].vowel2 = None
        self.assertEqual( str(string), str(string2) )

        string[0].vowel2 = "E"
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # ('u suffix)
        #.......................................................................
        string1 = DSTRING_BOD("ཁིའུའིའོ") # khi'u'i'o
        string2 = DSTRING_BOD("ཁིའིའོ") # khi'i'o

        string = DSTRING_BOD("ཁིའུའིའོ")

        string.istructs[0].postsuffix_u = False
        self.assertEqual( str(string), str(string2) )

        string.insert( 1,
                       DCharacterBOD(dstring_object = string,
                                     base_char = "-",
                                     vowel1 = "U") )

        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # ('i suffix)
        #.......................................................................
        string1 = DSTRING_BOD("དྷའི") # d+ha'i
        string2 = DSTRING_BOD("དྷ") # d+ha

        string = DSTRING_BOD("དྷའི")

        string.istructs[0].gramm_postsuffix = None
        self.assertEqual( str(string), str(string2) )

        string.append( DCharacterBOD(dstring_object = string,
                                     base_char = "-",
                                     vowel1 = "I") )
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # ('o suffix)
        #.......................................................................
        string1 = DSTRING_BOD("དྷའིའོ") # d+ha'i'o
        string2 = DSTRING_BOD("དྷའི") # d+ha'i

        string = DSTRING_BOD("དྷའིའོ")

        string.istructs[0].postsuffix_o = False
        self.assertEqual( str(string), str(string2) )

        string.append( DCharacterBOD(dstring_object = string,
                                     base_char = "-",
                                     vowel1 = "O") )
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (anusvara/candrabindu)
        #.......................................................................
        string1 = DSTRING_BOD("སྂ") # sa~M`
        string2 = DSTRING_BOD("ས") # sa

        string = DSTRING_BOD("སྂ")

        string.istructs[0].anusvara_candrabindu = None
        self.assertEqual( str(string), str(string2) )

        string[0].anusvara_candrabindu = "SIGN NYI ZLA NAA DA"
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (rnam bcad)
        #.......................................................................
        string1 = DSTRING_BOD("གཏིཿ") # gtiH
        string2 = DSTRING_BOD("གཏི") # gti

        string = DSTRING_BOD("གཏིཿ")

        string.istructs[0].rnam_bcad = False
        self.assertEqual( str(string), str(string2) )

        string[1].rnam_bcad = True
        self.assertEqual( str(string), str(string1) )

        #.......................................................................
        # (halanta)
        #.......................................................................
        string1 = DSTRING_BOD("ཀ྄") # k?
        string2 = DSTRING_BOD("ཀ") # ka

        string = DSTRING_BOD("ཀ྄")

        string.istructs[0].vowel1 = 'A'
        string.istructs[0].halanta = False
        self.assertEqual( str(string), str(string2) )

        string[0].vowel1 = None
        string[0].halanta = True
        self.assertEqual( str(string), str(string1) )

    #///////////////////////////////////////////////////////////////////////////
    def test_modifications2(self):
        """
                TESTSDStringBOD.test_invalid_modifications_to_istructs

                Invalid modifications to istructs.
        """
        string = DSTRING_BOD("བསྒྲིབས")

        with self.assertRaises(DCharsError):
            string.istructs[0].prefix = "L"

        with self.assertRaises(DCharsError):
            string.istructs[0].consonant = "XA"

        with self.assertRaises(DCharsError):
            string.istructs[0].vowel1 = "Y"

        with self.assertRaises(DCharsError):
            string.istructs[0].vowel2 = "Y"

        with self.assertRaises(DCharsError):
            string.istructs[0].suffix1 = "H"

        with self.assertRaises(DCharsError):
            string.istructs[0].suffix2 = "H"

        with self.assertRaises(DCharsError):
            string.istructs[0].postsuffix_u = None

        with self.assertRaises(DCharsError):
            string.istructs[0].gramm_postsuffix = True

        with self.assertRaises(DCharsError):
            string.istructs[0].postsuffix_o = None

        with self.assertRaises(DCharsError):
            string.istructs[0].halanta = None

        with self.assertRaises(DCharsError):
            string.istructs[0].rnam_bcad = None

        with self.assertRaises(DCharsError):
            string.istructs[0].anusvara_candrabindu = True

    #///////////////////////////////////////////////////////////////////////////
    def test_modifications3(self):
        """
                TESTSDStringBOD.test_modifications3

                string manipulations equivalent to an iterable type.
        """

        #.......................................................................
        # +=
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("་") # TSHEG SYMBOL
        string3 = DSTRING_BOD("གཏིཿ") # gtiH
        string4 = DSTRING_BOD("བསྒྲིབས་གཏིཿ") # bsgribs+TSHEG SYMBOL+gtiH

        string1 += string2
        string1 += string3

        self.assertEqual( string1, string4 )

        #.......................................................................
        # pop()
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲིབ") # bsgrib

        string1.pop()
        self.assertEqual( string1, string2 )

        #.......................................................................
        # del()
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲིབ") # bsgrib

        del(string1[-1])
        self.assertEqual( string1, string2 )

        #.......................................................................
        # slices
        #.......................................................................
        string1 = DSTRING_BOD("བསྒྲིབས") # bsgribs
        string2 = DSTRING_BOD("བསྒྲིབ") # bsgrib

        self.assertEqual( string1[:-1], string2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_intstruct(self):
        """
                TESTSDStringBOD.test_intstruct
        """

        #.......................................................................
        # - 1 -
        # (empty dstring)
        #.......................................................................
        bod  = ""
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 0 )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 2 -
        # ཨི (i)
        #.......................................................................
        bod  = "ཨི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "A",
                                                                     vowel1 = "I" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 3 -
        # ཀ྄ (k?)
        #.......................................................................
        bod  = "ཀ྄"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant ="K",
                                                                     halanta = True,
                                                                     vowel1 = None ))

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 4 -
        # ཀ (ka)
        #.......................................................................
        bod  = "ཀ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant ="K",
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 5 -
        # "་མ" ( ma)
        #.......................................................................
        bod  = "་མ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 2 )

            self.assertTrue( dstring.istructs[0].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))
            self.assertTrue( dstring.istructs[1].check_default_value(consonant = "M",
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 6 -
        # བསྒྲིབས (bsgribs)
        #.......................................................................
        bod  = "བསྒྲིབས"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(
                prefix = "B",
                superfix = "S",
                consonant = "G",
                subfix = ["R", ],
                vowel1 = "I",
                suffix1 = "B",
                suffix2 = "S" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 7 -
        # ཐེག་ (theg + tsheg)
        #.......................................................................
        bod  = "ཐེག་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 2 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "TH",
                                                                 vowel1 = "E",
                                                                 suffix1 = "G" ))

            self.assertTrue( dstring.istructs[1].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 8 -
        # ཁི (khi)
        #.......................................................................
        bod  = "ཁི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "KH",
                                                                     vowel1 = "I" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 9 -
        # ཁིའུ (khi'u)
        #.......................................................................
        bod  = "ཁིའུ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "KH",
                                                                 vowel1 = "I",
                                                                 postsuffix_u = True,
                                                                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 10 -
        # ཁིའུའི (khi'u'i)
        #.......................................................................
        bod  = "ཁིའུའི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "KH",
                                                                 vowel1 = "I",
                                                                 postsuffix_u = True,
                                                                 gramm_postsuffix = "'i",
                                                                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 11 -
        # ཁིའུའིས (khi'u'is)
        #.......................................................................
        bod  = "ཁིའུའིས"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "KH",
                                                                 vowel1 = "I",
                                                                 postsuffix_u = True,
                                                                 gramm_postsuffix = "'is",
                                                                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 12 -
        # ཁིའུའམ (khi'u'am)
        #.......................................................................
        bod  = "ཁིའུའམ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( consonant = "KH",
                                                                  vowel1 = "I",
                                                                  postsuffix_u = True,
                                                                  gramm_postsuffix = "'am",
                                                                 ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 13 -
        # ཁིའུའང (khi'u'ang)
        #.......................................................................
        bod  = "ཁིའུའང"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( consonant = "KH",
                                                                  vowel1 = "I",
                                                                  postsuffix_u = True,
                                                                  gramm_postsuffix = "'ang",
                                                                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 14 -
        # ཁིའུའིའོ (khi'u'i'o) ... a highly hypothetical Tibetan dstring ...
        #.......................................................................
        bod  = "ཁིའུའིའོ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( consonant = "KH",
                                                                  vowel1 = "I",
                                                                  postsuffix_u = True,
                                                                  gramm_postsuffix = "'i",
                                                                  postsuffix_o = True,
                                                                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 15 -
        # ཀ་བསྒྲིབས (ka bsgribs)
        #.......................................................................
        bod  = "ཀ་བསྒྲིབས"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 3 )

            self.assertTrue( dstring.istructs[0].check_default_value(consonant ="K",
                                                                     vowel1 = "A" ))

            self.assertTrue( dstring.istructs[1].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[2].check_default_value(
                prefix = "B",
                superfix = "S",
                consonant = "G",
                subfix = ["R", ],
                vowel1 = "I",
                suffix1 = "B",
                suffix2 = "S" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 16 -
        # ཏཱ་ལའི་བླ་མ (tA la'i bla ma)
        #.......................................................................
        bod  = "ཏཱ་ལའི་བླ་མ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):
            self.assertEqual( len(dstring.istructs), 7 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant ="T",
                                                  vowel1 = "AA" ))

            self.assertTrue( dstring.istructs[1].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[2].check_default_value(consonant = "L",
                                                  vowel1 = "A",
                                                  gramm_postsuffix = "'i" ))

            self.assertTrue( dstring.istructs[3].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[4].check_default_value(consonant = "B",
                                                  vowel1 = "A",
                                                  subfix = ["L",] ))

            self.assertTrue( dstring.istructs[5].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[6].check_default_value(consonant = "M",
                                                                 vowel1 = "A" ))

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 17 -
        # གྱང (gyang)
        #.......................................................................
        bod  = "གྱང"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(
                consonant = "G",
                subfix = ["Y"],
                vowel1 = "A",
                suffix1 = "NG"
                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 18 -
        # གཡང (g.yang)
        #.......................................................................
        bod  = "གཡང"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( prefix = "G",
                                                                      consonant = "Y",
                                                                      vowel1 = "A",
                                                                      suffix1 = "NG"
                                                                      ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 19 -
        # གཡུག (g.yug)
        #.......................................................................
        bod  = "གཡུག"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( prefix = "G",
                                                                      consonant = "Y",
                                                                      vowel1 = "U",
                                                                      suffix1 = "G"
                                                                      ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 20 -
        # བམའི (bma'i)
        #.......................................................................
        bod  = "བམའི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value( prefix = "B",
                                                                      consonant = "M",
                                                                      vowel1 = "A",
                                                                      gramm_postsuffix = "'i",
                                                                      ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 21 -
        # རྡོེ (rdo+e)
        #.......................................................................
        bod  = "རྡོེ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(
                superfix = "R",
                consonant = "D",
                vowel1 = "O",
                vowel2 = "E",
                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 22 -
        # བྲེུ (bru+e)
        #.......................................................................
        bod  = "བྲེུ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(
                consonant = "B",
                subfix = ["R"],
                vowel1 = "U",
                vowel2 = "E",
                ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 23 -
        # རྟ (rta)
        #.......................................................................
        bod  = "རྟ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):
            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(
                superfix = "R",
                consonant = "T",
                vowel1 = "A", ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 24 -
        # གྷ (g+ha)
        #.......................................................................
        bod  = "གྷ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "GH",
                                                                     vowel1 = "A",
                                                                     ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 25 -
        # བྷ (b+ha)
        #.......................................................................
        bod  = "བྷ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "BH",
                                                                     vowel1 = "A",
                                                                     ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 26 -
        # ཛྷ (dz+ha)
        #.......................................................................
        bod  = "ཛྷ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "DZH",
                                                                     vowel1 = "A",
                                                                     ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 27 -
        # བྷྲཾ (b+h+raM)
        #.......................................................................
        bod  = "བྷྲཾ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                          "(consonant)BH" \
                          "(subfix)['R']" \
                          "(vowel1)A" \
                          "(anusvara/candrabindu)SIGN RJES SU NGA RO" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 28 -
        # དྷའི (d+ha'i)
        #.......................................................................
        bod  = "དྷའི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)DH" \
                              "(vowel1)A" \
                              "(postsuffix 'i)" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 29 -
        # ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ (Ta Tha Da D+ha Na Sha)
        #.......................................................................
        bod  = "ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)TT(vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)TTH(vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)DD(vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)DDH(vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)NN(vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)SS(vowel1)A")
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 30 -
        # ༀ (oM)
        #.......................................................................
        bod  = "ༀ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(punct/other symbol)SYLLABLE OM")
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 31 -
        # ཡོཾ (yoM)
        #.......................................................................
        bod  = "ཡོཾ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)Y" \
                              "(vowel1)O" \
                              "(anusvara/candrabindu)SIGN RJES SU NGA RO" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 32 -
        # ཀྵ (k+Sha)
        #.......................................................................
        bod  = "ཀྵ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)KSS" \
                              "(vowel1)A" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 33 -
        # འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་ ('jam mgon kong sprul blo gros mtha' yas )
        #.......................................................................
        bod = "འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(prefix)-(consonant)J(vowel1)A(suffix1)M; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)G(vowel1)O(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)K(vowel1)O(suffix1)NG; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(superfix)S(consonant)P(subfix)['R']" \
                              "(vowel1)U(suffix1)L; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)B(subfix)['L'](vowel1)O; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)G(subfix)['R'](vowel1)O" \
                              "(suffix1)S; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)TH(vowel1)A" \
                              "(suffix1)-; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)Y(vowel1)A(suffix1)S; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 34 -
        # ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་ (shes bya kun khyab mdzod )
        #.......................................................................
        bod  = "ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)SH(vowel1)E(suffix1)S; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)B(subfix)['Y'](vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)K(vowel1)U(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)KH(subfix)['Y'](vowel1)A" \
                              "(suffix1)B; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)DZ(vowel1)" \
                              "O(suffix1)D; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 35 -
        # "གདམས་ངག་མཛོད་ (gdams ngag mdzod )
        #.......................................................................
        bod  = "གདམས་ངག་མཛོད་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(prefix)G(consonant)D(vowel1)A" \
                              "(suffix1)M(suffix2)S; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)NG(vowel1)A(suffix1)G; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)DZ" \
                              "(vowel1)O(suffix1)D; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 36 -
        # རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་ (rin chen gter mdzod chen mo )
        #.......................................................................
        bod  = "རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)R(vowel1)I(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)CH(vowel1)E(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)G(consonant)T(vowel1)E(suffix1)R; "\
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)DZ(vowel1)O(suffix1)D; "\
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)CH(vowel1)E(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)M(vowel1)O; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 37 -
        # རྒྱ་ཆེན་བཀའ་མཛོད་ (rgya chen bka' mdzod )
        #.......................................................................
        bod  = "རྒྱ་ཆེན་བཀའ་མཛོད་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(superfix)R(consonant)G" \
                              "(subfix)['Y'](vowel1)A; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)CH(vowel1)E(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)B(consonant)K(vowel1)A(suffix1)-; "\
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)M(consonant)DZ(vowel1)O(suffix1)D; "\
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 38 -
        # ངེས་དོན་སྒྲོན་མེ་ (nges don sgron me )
        #.......................................................................
        bod  = "ངེས་དོན་སྒྲོན་མེ་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)NG(vowel1)E(suffix1)S; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)D(vowel1)O(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(superfix)S(consonant)G(subfix)['R'](vowel1)O" \
                              "(suffix1)N; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(consonant)M(vowel1)E; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 39 -
        # དཀྱིལ་འཁོར་ (dkyil 'khor )
        #.......................................................................
        bod  = "དཀྱིལ་འཁོར་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(prefix)D(consonant)K(subfix)['Y'](vowel1)I" \
                              "(suffix1)L; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " \
                              "(prefix)-(consonant)KH(vowel1)O" \
                              "(suffix1)R; " \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 40 -
        # པའོ (pa'o)
        #.......................................................................
        bod  = "པའོ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)P(vowel1)A(postsuffix 'o)" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 41 -
        # མཚོའི (mtsho'i)
        #.......................................................................
        bod  = "མཚོའི"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                          "(prefix)M(consonant)TSH(vowel1)O(postsuffix 'i)" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 42 -
        # མཇ (mja)
        #.......................................................................
        bod  = "མཇ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                          "(prefix)M(consonant)J(vowel1)A" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 43 -
        # ཀྲ (kra)
        #.......................................................................
        bod  = "ཀྲ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)K(subfix)['R'](vowel1)A" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 44 -
        # འོད ('od)
        #.......................................................................
        bod  = "འོད"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)-(vowel1)O(suffix1)D" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 45 -
        # ཡིད (yid)
        #.......................................................................
        bod  = "ཡིད"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                          "(consonant)Y(vowel1)I(suffix1)D" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 46 -
        # ²ཨི² (²i²)
        #.......................................................................
        bod  = "²" + "ཨི" + "²"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 3 )

            self.assertTrue( dstring.istructs[0].check_default_value( unknown_character = True,
                                                                      punctuation_or_other_symbol = "²" ))
            self.assertTrue( dstring.istructs[1].check_default_value( consonant = "A",
                                                                      vowel1 = "I" ))
            self.assertTrue( dstring.istructs[2].check_default_value( unknown_character = True,
                                                                      punctuation_or_other_symbol = "²" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 47 -
        # ཀོཿ (koH)
        #.......................................................................
        bod  = "ཀོཿ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )

            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "K",
                                                                     vowel1 = "O",
                                                                     rnam_bcad = True ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 48 -
        # མང (mang)
        #.......................................................................
        bod  = "མང"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )

            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "M",
                                                                     vowel1 = "A",
                                                                     suffix1 = "NG" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 49 -
        # སྤྱི་ལོ ༢༠༠༠ ཟླ་ ༡༡ ཚེས་ ༡༩ ལ། (spyi lo_2000_zla _11_tshes _19_la/)
        #.......................................................................
        bod  = "སྤྱི་ལོ ༢༠༠༠ ཟླ་ ༡༡ ཚེས་ ༡༩ ལ།"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 23 )

            self.assertTrue( dstring.istructs[0].check_default_value(
                superfix = "S",
                consonant = "P",
                vowel1 = "I",
                subfix = ["Y"] ))

            self.assertTrue( dstring.istructs[1].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[2].check_default_value(consonant = "L",
                                                                     vowel1 = "O" ))

            self.assertTrue( dstring.istructs[3].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[4].check_default_value(
                punctuation_or_other_symbol = "DIGIT TWO" ))
            self.assertTrue( dstring.istructs[5].check_default_value(
                punctuation_or_other_symbol = "DIGIT ZERO" ))
            self.assertTrue( dstring.istructs[6].check_default_value(
                punctuation_or_other_symbol = "DIGIT ZERO" ))
            self.assertTrue( dstring.istructs[7].check_default_value(
                punctuation_or_other_symbol = "DIGIT ZERO" ))

            self.assertTrue( dstring.istructs[8].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[9].check_default_value(
                consonant = "Z",
                vowel1 = "A",
                subfix = ["L",] ))

            self.assertTrue( dstring.istructs[10].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[11].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[12].check_default_value(
                punctuation_or_other_symbol = "DIGIT ONE" ))
            self.assertTrue( dstring.istructs[13].check_default_value(
                punctuation_or_other_symbol = "DIGIT ONE" ))

            self.assertTrue( dstring.istructs[14].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[15].check_default_value(consonant = "TSH",
                                                                       vowel1 = "E",
                                                                       suffix1 = "S" ))

            self.assertTrue( dstring.istructs[16].check_default_value(
                punctuation_or_other_symbol = "MARK INTERSYLLABIC TSHEG" ))

            self.assertTrue( dstring.istructs[17].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[18].check_default_value(
                punctuation_or_other_symbol = "DIGIT ONE" ))
            self.assertTrue( dstring.istructs[19].check_default_value(
                punctuation_or_other_symbol = "DIGIT NINE" ))

            self.assertTrue( dstring.istructs[20].check_default_value(
                punctuation_or_other_symbol = " " ))

            self.assertTrue( dstring.istructs[21].check_default_value(consonant = "L",
                                                                       vowel1 = "A" ))

            self.assertTrue( dstring.istructs[22].check_default_value(
                punctuation_or_other_symbol = "MARK SHAD" ))

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 50 -
        # སྐྱོལ (skyol)
        #.......................................................................
        bod  = "སྐྱོལ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(superfix = "S",
                                                                     consonant = "K",
                                                                     subfix=["Y"],
                                                                     vowel1 = "O",
                                                                     suffix1 = "L"))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 51 -
        # སྲ (sra)
        #.......................................................................
        bod  = "སྲ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "S",
                                                                     subfix = ['R',],
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 52 -
        # རླ (rla)
        #.......................................................................
        bod  = "རླ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "R",
                                                                     subfix = ['L',],
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 53 -
        # རྭ (rwa)
        #.......................................................................
        bod  = "རྭ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "R",
                                                                     subfix = ['W',],
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 54 -
        # ལྭ (lwa)
        #.......................................................................
        bod  = "ལྭ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "L",
                                                                     subfix = ['W',],
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 54 -
        # སྭ (swa)
        #.......................................................................
        bod  = "སྭ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(consonant = "S",
                                                                     subfix = ['W',],
                                                                     vowel1 = "A" ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 55 -
        # སྐྱོར (skyor)
        #.......................................................................
        bod = "སྐྱོར"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( len(dstring.istructs), 1 )
            self.assertTrue( dstring.istructs[0].check_default_value(superfix = "S",
                                                                     consonant = "K",
                                                                     subfix = ['Y',],
                                                                     vowel1 = "O",
                                                                     suffix1 = "R",
                                                                     ))
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 56 -
        # རྐ (rka)
        #.......................................................................
        bod  = "རྐ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(superfix)R(consonant)K(vowel1)A" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 57 -
        # སྟོང (stong)
        #.......................................................................
        bod  = "སྟོང"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(superfix)S(consonant)T(vowel1)O(suffix1)NG" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 58 -
        # ཀའ (ka')
        #.......................................................................
        bod  = "ཀའ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)K(vowel1)A(suffix1)-" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 59 -
        # ཀྰ (k+'a)
        #.......................................................................
        bod  = "ཀྰ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(consonant)K(subfix)['-'](vowel1)A" )
            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 60 -
        # "µབསµµགྲིབསµ"
        #.......................................................................
        bod  = "µབསµµགྲིབསµ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(unknown character)(punct/other symbol)µ; " + \
                              "(consonant)B(vowel1)A(suffix1)S; " + \
                              "(unknown character)(punct/other symbol)µ; " + \
                              "(unknown character)(punct/other symbol)µ; " + \
                              "(consonant)G(subfix)['R'](vowel1)I(suffix1)B(suffix2)S; " + \
                              "(unknown character)(punct/other symbol)µ" )

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 61 -
        # "µ"
        #.......................................................................
        bod  = "µ"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(unknown character)(punct/other symbol)µ" )

            self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 62 -
        # ་བརྔུབས་ ( brngubs )
        #.......................................................................
        bod  = "་བརྔུབས་"
        for dstring in (DSTRING_BOD(bod), DSTRING_BOD_BUFF(bod)):

            self.assertEqual( str(dstring.istructs),
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " + \
                              "(prefix)B(superfix)R(consonant)NG(vowel1)U(suffix1)B(suffix2)S; " + \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )

            self.assertEqual( bod, str(dstring) )

    #///////////////////////////////////////////////////////////////////////////
    def test_basic_sortingvalue1(self):
        """
                TESTSDStringBOD.test_basic_sortingvalue1
        """

        #.......................................................................
        dstring1 = DSTRING_BOD("ཀ")     # ka

        self.assertTrue( dstring1 == dstring1 )
        self.assertFalse( dstring1 < dstring1 )
        self.assertTrue( dstring1 <= dstring1 )
        self.assertFalse( dstring1 > dstring1 )
        self.assertTrue( dstring1 >= dstring1 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཀ")     # ka
        dstring2 = DSTRING_BOD("ག")     # ga

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཀ")     # ka
        dstring2 = DSTRING_BOD("ཀྲ")     # kra

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཀ་སྐྱོར་")  # ka skyor
        dstring2 = DSTRING_BOD("ཀ་ཁ་")  # ka kha

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཀ་སྐྱོར་")  # ka skyor
        dstring2 = DSTRING_BOD("ཀ་ཁ་")  # ka kha

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཏ")  # ta
        dstring2 = DSTRING_BOD("ཐ")  # tha

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ཐ")  # tha
        dstring2 = DSTRING_BOD("ཊ")  # Ta

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("ད")  # da
        dstring2 = DSTRING_BOD("དྷ")  # dha

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

        #.......................................................................
        dstring1 = DSTRING_BOD("དྷ")  # dha
        dstring2 = DSTRING_BOD("ཌ")  # Da

        self.assertFalse( dstring1 == dstring2 )
        self.assertTrue( dstring1 < dstring2 )
        self.assertTrue( dstring1 <= dstring2 )
        self.assertFalse( dstring1 > dstring2 )
        self.assertFalse( dstring1 >= dstring2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_basic_sortingvalue2(self):
        """
                TESTSDStringBOD.test_basic_sortingvalue2
        """

        filename__words_sorted = os.path.join("dchars",
                                              "tests",
                                              "languages",
                                              "bod",
                                              "words.sorted")
        filename__words_shuffled = os.path.join("dchars",
                                                "tests",
                                                "languages",
                                                "bod",
                                                "words.shuffled")

        with open( filename__words_sorted, 'r' ) as file__words_sorted, \
             open( filename__words_shuffled, 'r' ) as file__words_shuffled:

            words_sorted = []
            for words in file__words_sorted.readlines():
                words_sorted.append( DSTRING_BOD(words.strip()) )

            words_shuffled = []
            for words in file__words_shuffled.readlines():
                words_shuffled.append( DSTRING_BOD(words.strip()) )
            words_shuffled = sorted(words_shuffled, key=DStringBOD.sortingvalue)

            self.assertEqual( words_sorted, words_shuffled )



            words_sorted = []
            for words in file__words_sorted.readlines():
                words_sorted.append( DSTRING_BOD_BUFF(words.strip()) )

            words_shuffled = []
            for words in file__words_shuffled.readlines():
                words_shuffled.append( DSTRING_BOD_BUFF(words.strip()) )
            words_shuffled = sorted(words_shuffled, key=DStringBOD.sortingvalue)

            self.assertEqual( words_sorted, words_shuffled )

