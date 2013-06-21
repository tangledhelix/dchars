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
    ❏DChars❏ : dchars/tests/languages/bod/transliterations/ewts_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL
from dchars.languages.bod.internalstructure import ListOfInternalStructures

DSTRING_BOD_NOBUFF = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False,
                                     "anonymize the unknown characters" : False,
                                     },
                          )

DSTRING_BOD_NOBUFF_A = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False,
                                     "anonymize the unknown characters" : True,
                                     },
                          )

DSTRING_BOD_S = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Sanskrit",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_T = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_O = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "Tibetan or Sanskrit",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )

DSTRING_BOD_BUFF = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : True},
                          )

DSTRING_BOD_S = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Sanskrit",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_T = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_O = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "Tibetan or Sanskrit",
                                     "fill the buffers"       : False,
                                     "look up in the buffers" : False},
                          )


LIST_OF_RECIPROCAL_EXAMPLES = (
        ("ཀ"    , 'ka'),
        ("ཀྲ"    , 'kra'),
        ("ཀྭ",   'kwa'),
        ("ཀྱ",   'kya'),
        ("རྐ",   'rka'),
        ("ཉ",   'nya'),
        ("རྙ",   'rnya'),
        ("ཀི",   'ki'),
        ("ཀུ",   "ku"),
        ("ཀེ",   "ke"),
        ("ཀོ",  "ko"),
        ('ཨི', "i"),
        ("ཀོང", "kong"),
        ("བསྒྲིབས", "bsgribs"),
        ("མགོན", "mgon"),
        ("ཁམ་", "kham "),
        ("ཁམས", "khams"),
        ("འཇམ", "'jam"),
        ("སྤྲུལ", "sprul"),
        ("བློ", "blo"),
        ("གྲོས", "gros"),
        ("མཐའ་ཡས", "mtha' yas"),
        ("འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་",
         "'jam mgon kong sprul blo gros mtha' yas "),
        ("ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་", "shes bya kun khyab mdzod "),
        ("གདམས་ངག་མཛོད་", "gdams ngag mdzod "),
        ("རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་", "rin chen gter mdzod chen mo "),
        ("རྒྱ་ཆེན་བཀའ་མཛོད་", "rgya chen bka' mdzod "),
        ("ངེས་དོན་སྒྲོན་མེ་", "nges don sgron me "),
        ("དཀྱིལ་འཁོར་", "dkyil 'khor "),
        ("རྒྱུད་", "rgyud "),
        ("རྩ་རྒྱུད་", "rtsa rgyud "),
        ("བཤད་རྒྱུད་", "bshad rgyud "),
        ("ཐེག་པ་དགུ་", "theg pa dgu "),
        ("ཐེག་པ་རིམ་པ་དགུ་", "theg pa rim pa dgu "),
        ("བློ་སྦྱོངས་དོན་བདུན་མ་", "blo sbyongs don bdun ma "),
        ("རྙིང་མ་བཀའ་མ་", "rnying ma bka' ma "),
        ("གཏེར་མ་", "gter ma "),
        ("བྲག", "brag"),
        ("བརག", "b.rag"),
        ("གྱང", "gyang"),
        ("གཡང", "g.yang"),
        ("ཏཱ་ལའི་བླ་མ", "tA la'i bla ma"),
        ("ཏཱ་ར་ནཱ་ཐ", "tA ra nA tha"),
        ("བའི", "ba'i"),
        ("པའོ", "pa'o"),
        ("མཚོའི", "mtsho'i"),
        ("མཇ", "mja"),
        ("རྐ", "rka"),
        ("འོད", "'od"),
        ("ཡིད", "yid"),
        ("གཡུག", "g.yug"),
        ("ཁྱིའུ", "khyi'u"),
        ("བམའི", "bma'i"),
        ("བམའ", "bma'"),
        ("མའི" ,"ma'i" ),
        ("དབྱངས", "dbyangs"),
        ("པའོ" , "pa'o" ),
        ("ཨའ", "a'"),
        ("གྱག", "gyag"),
        ("གྱཀ", "gyaka"),
        ("གཡག", "g.yag"),
        ("མང", "mang"),
        ("བརྒྱུད", "brgyud"),
        ("བཀའ་བརྒྱུད་སྔགས་མཛོད་", "bka' brgyud sngags mdzod "),
        ("ཨ་ཁུ", "a khu"),
        ("ཨུག་པ", "ug pa"),
        ("རྡོེ", "rdo+e"),
        ("བྲེུ", "bru+e"),
        ("རྟ", "rta"),
        ("གྷ", "g+ha"),
        ("དྷ", "d+ha"),
        ("བྷ", "b+ha"),
        ("ཛྷ", "dz+ha"),
        ("ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ", "Ta Tha Da D+ha Na Sha"),
        ("ༀ", "oM"),
        ("ཡོཾ", "yoM"),
        ("ཀྵ", "k+Sha"),
        ("ཕ༹", "fa"),
        ("བ༹", "va"),
        ("ཨ", "a"),
        ("ཨཿ", "aH"),
        ("མཱཿ", "mAH"),
        ("གཏིཿ", "gtiH"),
        ("ཀ྄", "k?"),
        ("སཾ", "saM"),
        ("སྃ", "sa~M"),
        ("སྂ", "sa~M`"),
        ("བྷྲཾ", "b+h+raM"),
        ("གྷཾ", "g+haM"),
        ("དྷི", "d+hi"),
        ("བྷོ", "b+ho"),
        ("དྷའི", "d+ha'i"),
        ("ཚ", "tsha"),
        ("ལོ་བུ་རེ་བ་མི་ཚོ་དུ་རི་ཇོ་བོ་དེ་སུ་འོ་", "lo bu re ba mi tsho du ri jo bo de su 'o "),
        ("གྱ་གྱང་རྒྱང་བརྒྱང་བརྒྱངས་", "gya gyang rgyang brgyang brgyangs "),
        ("ངུ་མགུ་ངུབ་རྔུབ་བརྔུབ་བརྔུབས་", "ngu mgu ngub rngub brngub brngubs "),
        ("རྟ།་ནོར།་ལུག་གསུམ།་", "rta/ nor/ lug gsum/ "),
        ("རི་མགོ་ན་ཉལ་ན་དཀའ།་", "ri mgo na nyal na dka'/ "),
        ("གཅིག་", "gcig "),
        ("གཡུ་གཡོ་གཡུལ་གཡང་གཡེང་གཡག་གཡའ་གཡུང་གཡེལད",
         "g.yu g.yo g.yul g.yang g.yeng g.yag g.ya' g.yung g.yeld"),
        ("ངའི་སྐྱེས་ལོ༡༩༦༥རེད།", "nga'i skyes lo1965red/"),
        ("ངའི་སྐྱེས་ལོ ༡༩༦༥ རེད།", "nga'i skyes lo_1965_red/"),
        ("སྤྱི་ལོ་༢༠༠༠ཟླ་༡༡ཚེས་༡༩ལ།", "spyi lo 2000zla 11tshes 19la/"),
        ("སྤྱི་ལོ ༢༠༠༠ ཟླ་ ༡༡ ཚེས་ ༡༩ ལ།", "spyi lo_2000_zla _11_tshes _19_la/"),
        ("ཁི",   "khi"),
        ("ཁིའུ",  "khi'u"),
        ("ཁིའུའི", "khi'u'i"),
        ("ཁིའུའིས","khi'u'is"),
        ("ཁིའུའམ","khi'u'am"),
        ("ཁིའུའང","khi'u'ang"),
        ("ཁིའུའིའོ", "khi'u'i'o"),
        ("ལབཿ", "labH"),
        ("ནམཿ", "namH"),
        ("ཡོགཿ", "yogH"),
        ("མགབཿ", "mgabH"),
        ("ཧོམཿ", "homH"),
        ("སྦུདཿ", "sbudH"),
        ("བེདཿ", "bedH"),
        ("ཀོགསཿ", "kogsH"),
        ("རྡོེཿ", "rdo+eH"),
        ("རྡོེཾ", "rdo+eM"),
        ("སེངྷ", "seng+ha"),
        ("སིངྷ", "sing+ha"),
        ("ཀརྨ་པ་", "karma pa "),
        ("སཏྟྭ", "sat+t+wa"),
        ("ཡོགཿཏནདྲ", "yogHtandra"),
        ("བ༹ནདྱ", "vand+ya"),
        ("དྷརྨཿ", "d+harmaH"),
        )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringBOD(unittest.TestCase):
    """
        class TESTSDStringBOD
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration(self):
        """
                TESTSDStringBOD.test_get_transliteration
        """

        for bod, bod_ewts in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_BOD_NOBUFF(bod)
            bod_ewts2 = string.get_transliteration()
            self.assertEqual( bod_ewts, bod_ewts2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_str(self):
        """
                TESTSDStringBOD.test_init_from_str
        """

        for data_bod in LIST_OF_RECIPROCAL_EXAMPLES:

            bod = data_bod[0]
            #ewts = data_bod[1]

            string = DSTRING_BOD_NOBUFF(bod)
            self.assertEqual( str(string), bod )

            string = DSTRING_BOD_BUFF(bod)
            self.assertEqual( str(string), bod )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration(self):
        """
                TESTSDStringBOD.test_init_from_transliteration
        """

        for bod, bod_ewts in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_BOD_NOBUFF().init_from_transliteration(bod_ewts)
            bod2 = str(string)
            self.assertEqual( bod, bod2 )

            string = DSTRING_BOD_BUFF().init_from_transliteration(bod_ewts)
            bod2 = str(string)
            self.assertEqual( bod, bod2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringBOD.test_from_srcstr_2_srcstr()
        """

        for bod, bod_ewts in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_BOD_NOBUFF().init_from_transliteration(bod_ewts)
            self.assertEqual( bod, str(string) )
            bod_ewts2 = string.get_transliteration()
            self.assertEqual( bod_ewts, bod_ewts2 )

            string = DSTRING_BOD_BUFF().init_from_transliteration(bod_ewts)
            self.assertEqual( bod, str(string) )
            bod_ewts2 = string.get_transliteration()
            self.assertEqual( bod_ewts, bod_ewts2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringBOD.test_unknown_characters
        """

        #.......................................................................
        string = DSTRING_BOD_NOBUFF("²རྙ²")
        self.assertEqual( str(string),
                          "²རྙ²" )

        #.......................................................................
        string = DSTRING_BOD_NOBUFF_A("²རྙ²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL )


        string = DSTRING_BOD_BUFF("²རྙ²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL )

        #.......................................................................
        string = DSTRING_BOD_NOBUFF().init_from_transliteration("²rnya²rnya²")
        self.assertEqual( str(string),
                          "²རྙ²རྙ²" )

        #.......................................................................
        string = DSTRING_BOD_NOBUFF_A().init_from_transliteration("²rnya²rnya²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL )


        string = DSTRING_BOD_BUFF().init_from_transliteration("²rnya²rnya²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL+"རྙ"+UNKNOWN_CHAR_SYMBOL )

    #///////////////////////////////////////////////////////////////////////////
    def test_intstruct(self):
        """
                TESTSDStringBOD.test_intstruct
        """

        #.......................................................................
        # - 1 -
        # (empty dstring)
        #.......................................................................
        bod, ewts_bod  = "", ""
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 0 )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 2 -
        # ཨི (i)
        #.......................................................................
        bod, ewts_bod  = "ཨི", "i"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "A",
                                                                 vowel1 = "I" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 3 -
        # ཀ྄ (k?)
        #.......................................................................
        bod, ewts_bod  = "ཀ྄", "k?"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant ="K",
                                                                 halanta = True,
                                                                 vowel1 = None ))

        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 4 -
        # ཀ (ka)
        #.......................................................................
        bod, ewts_bod  = "ཀ", "ka"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant ="K",
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 5 -
        # ་མ ( ma)
        #.......................................................................
        bod, ewts_bod  = "་མ", " ma"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "བསྒྲིབས", "bsgribs"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཐེག་", "theg "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁི", "khi"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "KH",
                                                                 vowel1 = "I" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 9 -
        # ཁིའུ (khi'u)
        #.......................................................................
        bod, ewts_bod  = "ཁིའུ", "khi'u"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁིའུའི", "khi'u'i"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁིའུའིས", "khi'u'is"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁིའུའམ", "khi'u'am"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁིའུའང", "khi'u'ang"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཁིའུའིའོ", "khi'u'i'o"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཀ་བསྒྲིབས", "ka bsgribs"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ཏཱ་ལའི་བླ་མ", "tA la'i bla ma"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "གྱང", "gyang"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "གཡང", "g.yang"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "གཡུག", "g.yug"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "བམའི", "bma'i"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "རྡོེ", "rdo+e"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "བྲེུ", "bru+e"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "རྟ", "rta"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "གྷ", "g+ha"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "GH",
                                                                 vowel1 = "A",
                                                                ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 25 -
        # བྷ (b+ha)
        #.......................................................................
        bod, ewts_bod  = "བྷ", "b+ha"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "BH",
                                                                 vowel1 = "A",
                                                                ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 26 -
        # ཛྷ (dz+ha)
        #.......................................................................
        bod, ewts_bod  = "ཛྷ", "dz+ha"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "DZH",
                                                                 vowel1 = "A",
                                                                ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 27 -
        # བྷྲཾ (b+h+raM)
        #.......................................................................
        bod, ewts_bod  = "བྷྲཾ", "b+h+raM"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "དྷའི", "d+ha'i"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)DH" \
                              "(vowel1)A" \
                              "(postsuffix 'i)" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 29 -
        # ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ (Ta Tha Da D+ha Na Sha)
        #.......................................................................
        bod, ewts_bod  = "ཊ་ཋ་ཌ་ཌྷ་ཎ་ཥ", "Ta Tha Da D+ha Na Sha"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "ༀ", "oM"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(punct/other symbol)SYLLABLE OM")
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 31 -
        # ཡོཾ (yoM)
        #.......................................................................
        bod, ewts_bod  = "ཡོཾ", "yoM"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)Y" \
                              "(vowel1)O" \
                              "(anusvara/candrabindu)SIGN RJES SU NGA RO" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 32 -
        # ཀྵ (k+Sha)
        #.......................................................................
        bod, ewts_bod  = "ཀྵ", "k+Sha"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)KSS" \
                              "(vowel1)A" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 33 -
        # འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་ ('jam mgon kong sprul blo gros mtha' yas )
        #.......................................................................
        (bod, ewts_bod) = "འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་", \
                          "'jam mgon kong sprul blo gros mtha' yas "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་", "shes bya kun khyab mdzod "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        # གདམས་ངག་མཛོད་ (gdams ngag mdzod )
        #.......................................................................
        bod, ewts_bod  = "གདམས་ངག་མཛོད་", "gdams ngag mdzod "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་", "rin chen gter mdzod chen mo "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "རྒྱ་ཆེན་བཀའ་མཛོད་", "rgya chen bka' mdzod "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "ངེས་དོན་སྒྲོན་མེ་", "nges don sgron me "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "དཀྱིལ་འཁོར་", "dkyil 'khor "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
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
        bod, ewts_bod  = "པའོ", "pa'o"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)P(vowel1)A(postsuffix 'o)" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 41 -
        # མཚོའི (mtsho'i)
        #.......................................................................
        bod, ewts_bod  = "མཚོའི", "mtsho'i"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                          "(prefix)M(consonant)TSH(vowel1)O(postsuffix 'i)" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 42 -
        # མཇ (mja)
        #.......................................................................
        bod, ewts_bod  = "མཇ", "mja"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                          "(prefix)M(consonant)J(vowel1)A" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 43 -
        # ཀྲ (kra)
        #.......................................................................
        bod, ewts_bod  = "ཀྲ", "kra"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)K(subfix)['R'](vowel1)A" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 44 -
        # འོད ('od)
        #.......................................................................
        bod, ewts_bod  = "འོད", "'od"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
        self.assertEqual( str(dstring.istructs),
                              "(consonant)-(vowel1)O(suffix1)D" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 45 -
        # ཡིད (yid)
        #.......................................................................
        bod, ewts_bod  = "ཡིད", "yid"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)
        self.assertEqual( str(dstring.istructs),
                          "(consonant)Y(vowel1)I(suffix1)D" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 46 -
        # ²ཨི² (²i²)
        #.......................................................................
        bod, ewts_bod  = "²ཨི²", "²" + "i" + "²"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 3 )

        self.assertTrue( dstring.istructs[0].check_default_value(unknown_character = True,
                                                                 punctuation_or_other_symbol ="²"))
        self.assertTrue( dstring.istructs[1].check_default_value(consonant = "A",
                                                                 vowel1 = "I" ))
        self.assertTrue( dstring.istructs[2].check_default_value(unknown_character = True,
                                                                 punctuation_or_other_symbol ="²"))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 47 -
        # ཀོཿ (koH)
        #.......................................................................
        bod, ewts_bod  = "ཀོཿ", "koH"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )

        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "K",
                                                                 vowel1 = "O",
                                                                 rnam_bcad = True ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 48 -
        # མང (mang)
        #.......................................................................
        bod, ewts_bod  = "མང", "mang"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )

        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "M",
                                                                 vowel1 = "A",
                                                                 suffix1 = "NG" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 49 -
        # སྤྱི་ལོ ༢༠༠༠ ཟླ་ ༡༡ ཚེས་ ༡༩ ལ། (spyi lo_2000_zla _11_tshes _19_la/)
        #.......................................................................
        bod, ewts_bod  = "སྤྱི་ལོ ༢༠༠༠ ཟླ་ ༡༡ ཚེས་ ༡༩ ལ།", "spyi lo_2000_zla _11_tshes _19_la/"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "སྐྱོལ", "skyol"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "སྲ", "sra"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "S",
                                                                 subfix = ['R',],
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 52 -
        # རླ (rla)
        #.......................................................................
        bod, ewts_bod  = "རླ", "rla"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "R",
                                                                 subfix = ['L',],
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 53 -
        # རྭ (rwa)
        #.......................................................................
        bod, ewts_bod  = "རྭ", "rwa"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "R",
                                                                 subfix = ['W',],
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 54 -
        # ལྭ (lwa)
        #.......................................................................
        bod, ewts_bod  = "ལྭ", "lwa"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "L",
                                                                 subfix = ['W',],
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 54 -
        # སྭ (swa)
        #.......................................................................
        bod, ewts_bod  = "སྭ", "swa"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( len(dstring.istructs), 1 )
        self.assertTrue( dstring.istructs[0].check_default_value(consonant = "S",
                                                                 subfix = ['W',],
                                                                 vowel1 = "A" ))
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 55 -
        # སྐྱོར (skyor)
        #.......................................................................
        bod, ewts_bod = "སྐྱོར", "skyor"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        bod, ewts_bod  = "རྐ", "rka"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(superfix)R(consonant)K(vowel1)A" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 57 -
        # སྟོང (stong)
        #.......................................................................
        bod, ewts_bod  = "སྟོང", "stong"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(superfix)S(consonant)T(vowel1)O(suffix1)NG" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 58 -
        # ཀའ (ka')
        #.......................................................................
        bod, ewts_bod  = "ཀའ", "ka'"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)K(vowel1)A(suffix1)-" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 59 -
        # ཀྰ (k+'a)
        #.......................................................................
        bod, ewts_bod  = "ཀྰ", "k+'a"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(consonant)K(subfix)['-'](vowel1)A" )
        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 60 -
        # µབསµµགྲིབསµ (µbasµµgribsµ)
        #.......................................................................
        bod, ewts_bod  = "µབསµµགྲིབསµ", "µbasµµgribsµ"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

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
        # µ (µ)
        #.......................................................................
        bod, ewts_bod  = "µ", "µ"
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(unknown character)(punct/other symbol)µ" )

        self.assertEqual( bod, str(dstring) )

        #.......................................................................
        # - 62 -
        # ་བརྔུབས་ ( brngubs )
        #.......................................................................
        bod, ewts_bod  = "་བརྔུབས་" , " brngubs "
        dstring = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts_bod)

        self.assertEqual( str(dstring.istructs),
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG; " + \
                              "(prefix)B(superfix)R(consonant)" + \
                              "NG(vowel1)U(suffix1)B(suffix2)S; " + \
                              "(punct/other symbol)MARK INTERSYLLABIC TSHEG" )

        self.assertEqual( bod, str(dstring) )

    #///////////////////////////////////////////////////////////////////////////
    def test_ewts_words(self):
        """
                TESTSDStringBOD.test_ewts_words

                for every word in ewts_words : EWTS -> (istruct) -> EWTS
        """
        with open( os.path.join("dchars",
                                "tests",
                                "languages",
                                "bod",
                                "transliterations",
                                "ewts_words") , 'r' ) as src:

            for word in src.readlines():

                ewts = word[:-1]

                string = DSTRING_BOD_NOBUFF().init_from_transliteration(ewts)
                ewts2 = string.get_transliteration()
                self.assertEqual( ewts, ewts2 )

                string = DSTRING_BOD_BUFF().init_from_transliteration(ewts)
                ewts2 = string.get_transliteration()
                self.assertEqual( ewts, ewts2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_pickle(self):
        """
                TESTSDStringBOD.test_pickle
        """

        for data in LIST_OF_RECIPROCAL_EXAMPLES:

            bod = data[0]
            # bod_ewts = data[1]

            string1 = DSTRING_BOD_NOBUFF(bod)
            istructs1 = string1.istructs

            # in order to compare two "pickled" istructs, we have to neutralize
            # some data :
            for istruct in istructs1:
                istruct.indexes = None
                istruct.real_indexes = None
                istruct.bad_internalstruct = False
                istruct.dstring_object = None

            pickle_strings = istructs1.pickle_repr()
            istructs2 = ListOfInternalStructures(
                anonymize_the_unknown_chars=True).init_from_pickle_repr(
                    src = pickle_strings,
                    dstring_object = string1 )

            self.assertTrue( istructs1.is_identical_to(istructs2) )

    # #///////////////////////////////////////////////////////////////////////////
    # def test_different_structures(self):
    #     """
    #             TESTSDStringBOD.test_different_structures
    #     """

    #     #.......................................................................
    #     for bod, t_ewts, t_istructs, o_ewts, o_istructs, s_ewts, s_istructs in (
    #             ("མ",           "ma", "(consonant)M(vowel1)A",
    #                             "ma", "(consonant)M(vowel1)A",
    #                             "ma", "(consonant)M(vowel1)A",),

    #             ("ཏཱ",           "tA", "(consonant)T(vowel1)AA",
    #                             "tA", "(consonant)T(vowel1)AA",
    #                             "tA", "(consonant)T(vowel1)AA",),

    #             ("བསྒྲད",         "bsgrad", "(prefix)B(superfix)S(consonant)G" + \
    #                                       "(subfix)['R'](vowel1)A(suffix1)D",
    #                             "bsgrad", "(prefix)B(superfix)S(consonant)G" + \
    #                                       "(subfix)['R'](vowel1)A(suffix1)D",
    #                             "bsgrada", "(consonant)B(vowel1)A; " + \
    #                                        "(consonant)S(subfix)['G', 'R'](vowel1)A; " + \
    #                                        "(consonant)D(vowel1)A",),

    #             ("པནཌི",          "panDi", "(consonant)P(vowel1)A(suffix1)N; " + \
    #                                      "(consonant)DD(vowel1)I",
    #                             "panaDi","(consonant)P(vowel1)A; (consonant)N(vowel1)A; " + \
    #                                      "(consonant)DD(vowel1)I",
    #                             "panaDi","(consonant)P(vowel1)A; (consonant)N(vowel1)A; " + \
    #                                      "(consonant)DD(vowel1)I",),

    #             ("ཁསཾ",          "khaMs", "(consonant)KH(vowel1)A" + \
    #                                      "(suffix1)S(anusvara/candrabindu)SIGN RJES SU NGA RO",
    #                             "khaMs", "(consonant)KH(vowel1)A" + \
    #                                      "(suffix1)S(anusvara/candrabindu)SIGN RJES SU NGA RO",
    #                             "khasaM", "(consonant)KH(vowel1)A; " + \
    #                                       "(consonant)S(vowel1)A " + \
    #                                       "(anusvara/candrabindu)SIGN RJES SU NGA RO",),

    #             ("སརྦ་མངྒལཾ" ,      "sarba mang+gaMl", "(consonant)S(vowel1)A; " + \
    #                                                "(superfix)R(consonant)B(vowel1)A; " + \
    #                                                "(punct/other symbol)" + \
    #                                                "MARK INTERSYLLABIC TSHEG; " + \
    #                                                "(consonant)M(vowel1)A; " + \
    #                                                "(consonant)NG(subfix)['G'](vowel1)A" + \
    #                                                "(suffix1)" + \
    #                                                "L(anusvara/candrabindu)SIGN RJES SU NGA RO",
    #                             "sarba mang+gaMl", "(consonant)S(vowel1)A; " + \
    #                                                "(superfix)R(consonant)B(vowel1)A; " + \
    #                                                "(punct/other symbol) " + \
    #                                                "MARK INTERSYLLABIC TSHEG; " + \
    #                                                "(consonant)M(vowel1)A; " + \
    #                                                "(consonant)NG(subfix)['G'](vowel1)A" + \
    #                                                "(suffix1)L" + \
    #                                                "(anusvara/candrabindu)SIGN RJES SU NGA RO",
    #                             "sarba mang+galaM", "(consonant)S(vowel1)A; " + \
    #                                                "(consonant)R(subfix)['B'](vowel1)A; " + \
    #                                                "(punct/other symbol) " + \
    #                                                "MARK INTERSYLLABIC TSHEG; " + \
    #                                                "(consonant)M(vowel1)A; " + \
    #                                                "(consonant)NG(subfix)['G'](vowel1)A; " + \
    #                                                "(consonant)L(vowel1)A" + \
    #                                                "(anusvara/candrabindu)SIGN RJES SU NGA RO",),
    #             ):

    #         string_t = DSTRING_BOD_T(bod)
    #         string_o = DSTRING_BOD_O(bod)
    #         string_s = DSTRING_BOD_S(bod)

    #         self.assertEqual( string_t.get_transliteration(), t_ewts )
    #         self.assertEqual( str(string_t.istructs), t_istructs )

    #         self.assertEqual( string_o.get_transliteration(), o_ewts )
    #         self.assertEqual( str(string_o.istructs), o_istructs )

    #         self.assertEqual( string_s.get_transliteration(), s_ewts )
    #         self.assertEqual( str(string_s.istructs), s_istructs )

    #     #.......................................................................
    #     for ewts, t_ewts, t_istructs, o_ewts, o_istructs, s_ewts, s_istructs in (
    #             ("ma",           "ma", "(consonant)M(vowel1)A",
    #                             "ma", "(consonant)M(vowel1)A",
    #                             "ma", "(consonant)M(vowel1)A",),

    #             ("tA",          "tA", "(consonant)T(vowel1)AA",
    #                             "tA", "(consonant)T(vowel1)AA",
    #                             "tA", "(consonant)T(vowel1)AA",),

    #             ("bsgrad",      "bsgrad", "(prefix)B(superfix)S(consonant)G" + \
    #                             "(subfix)['R'](vowel1)A(suffix1)D",
    #                             "bsgrad", "(prefix)B(superfix)S(consonant)G" + \
    #                             "(subfix)['R'](vowel1)A(suffix1)D",
    #                             "b?sgrada", "(consonant)B; (consonant)S" +\
    #                             "(subfix)['G', 'R'](vowel1)A(suffix1)D",),

    #             ("panDi",       "panDi", "(consonant)P(vowel1)A(suffix1)N; (consonant)DD(vowel1)I",
    #                             "panaDi","(consonant)P(vowel1)A(suffix1)N; (consonant)DD(vowel1)I",
    #                             "panaDi","(consonant)P(vowel1)A(suffix1)N; (consonant)DD(vowel1)I",
    #                             ),
    #             ):

    #         string_t = DSTRING_BOD_T().init_from_transliteration(ewts)
    #         string_o = DSTRING_BOD_O().init_from_transliteration(ewts)
    #         string_s = DSTRING_BOD_S().init_from_transliteration(ewts)

    #         self.assertEqual( string_t.get_transliteration(), t_ewts )
    #         self.assertEqual( str(string_t.istructs), t_istructs )

    #         self.assertEqual( string_o.get_transliteration(), o_ewts )
    #         self.assertEqual( str(string_o.istructs), o_istructs )

    #         self.assertEqual( string_s.get_transliteration(), s_ewts )
    #         self.assertEqual( str(string_s.istructs), s_istructs )

