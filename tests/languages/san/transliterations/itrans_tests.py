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
    ❏DChars❏ : dchars/tests/languages/san/transliterations/itrans_tests.py
"""

import unittest, os.path, re

from dchars.dchars import new_dstring
from dchars.languages.bod.dcharacter import UNKNOWN_CHAR_SYMBOL

DSTRING_SAN = new_dstring(language='संस्कृतम्',
                          transliteration_method = "itrans",
                          options = {"anonymize the unknown characters" : 'no'},
                          )

DSTRING_SAN__UNKNOWNCHAR = new_dstring(language='संस्कृतम्',
                          transliteration_method = "itrans",
                          options = {"anonymize the unknown characters" : 'yes'},
                          )


LIST_OF_RECIPROCAL_EXAMPLES = (
                            ("",                ''              ),
                            # क(0x0915)
                            ("क",               'ka'            ),
                            # क(0x0915) + virama(0x094D)
                            ("क्",               'k'             ),
                            # क(0x0915) + virama(0x094D) + anusvara (0902)
                            ("क्ं",               'kM'            ),
                            # क(0x0915) + anudatta(0x0952)
                            ("क॒",       'ka\\_'         ),
                            # क(0x0915) + anusvara(0x0902)
                            ("कं",       'kaM'        ),
                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902)
                            ("कं॒",       'ka\\_M'         ),
                            # क(0x0915) + nukta(0x093C) + udatta(0x0951) + anudatta(0x0952)
                            ("क़॒॑",       "qa\\_\\'"         ), # q + 0x00E1(a+acute) + 0x0331
                            # क(0x0915) + nukta(0x093C) + virama(0x094D)
                            ("क़",               'qa'            ),
                            # क(0x0915) + nukta(0x093C) + virama(0x094D)
                            ("क़्",               'q'             ),

                            # क(0x0915) + 0x093E
                            ("का",               'kA'         ),
                            # # क(0x0915) + 0x093F
                            ("कि",               'ki'         ),
                            # क(0x0915) + 0x0940
                            ("की",               'kI'         ),
                            # (independent) vowels
                            ("अइउऋऌएओ",         'a+i+uR^iL^i/e+o'   ),
                            # special vowels : SHORT E and SHORT O
                            ("ऎऒ",               '-e/+o'),
                            # (independent) long vowels
                            ("ॠ", "R^I"), # r̥̄ = r + 0325 + 0304 (not 0304 + 0325)
                            ("आईऊॠॡऐऔ",         'A+I/UR^IL^I+ai+au'   ),
                            # # (some consonants)
                            ('कखगघह',           'kakhagaghaha'),
                            ('चछजझ',            'chaChajajha'),
                            ('टठडढ',            'TaThaDaDha'),
                            ('तथदधलस',          'tathadadhalasa'),
                            ('पफबभ'             ,'paphababha'),

                            # visarga(0x0903)
                            ("ः",       'H'        ), # ḥ = 0x1E25 not 0x0068 + 0x0323

                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + visarga(0x0903)
                            ("कं॒ः",      'ka\\_MH'        ),

                            ('मैं', 'maiM'),

                            # १(0x0967) + anudatta(0x0952) + udatta(0x0951)
                            ("१॒॑",       "1\\_\\'"         ), # 1 + 0x0331 + 0x0301

                            # an impossible form for Sanskrit, interesting for the tests :
                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + virama(0x094D)
                            ("कं्॒",       'k\\_M'         ), # ḵ = 1E35 not k + 0331

                            # hiatus :
                            ('यइ', 'ya+i'),
                            ('रआ', "ra/A"),

                            # chandrabindu :
                            ('हूँ', 'hU.N'),
                            ('माँ', 'mA.N'),

                            # k + ā + udatta(0x0951)
                            ("का॑",       "kA\\'"),
                            # p + ā + udatta(0x0951)
                            ("पा॑",       "pA\\'"),
                            # p + ī + udatta(0x0951)
                            ("पी॑",       "pI\\'"),

                            # verses from Ṛgveda-Saṁhitā :
                            # 1.001.01a :
                            ('अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।',
                             "a\\_gnimI\\'Le pu\\_rohi\\'taM ya\\_j~nasya\\' " \
                             "de\\_vamR^i\\_tvija\\'m ."),
                            # 1.001.01c :
                            ('होता॑रं रत्न॒धात॑मम् ॥', "hotA\\'raM ratna\\_dhAta\\'mam .."),
                            # 2.001.01a :
                            ("त्वम॑ग्ने॒ " \
                             "द्युभि॒स्त्वमा॑शुशु॒क्षणि॒स्त्वम॒द्भ्यस्त्वमश्म॑न॒स्परि॑ ।",
                             "tvama\\'gne\\_ dyubhi\\_stvamA\\'shushu\\_k" + \
                             "ShaNi\\_stvama\\_dbhyastvamashma\\'na\\_spari\\' ."),
    )

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringSAN(unittest.TestCase):
    """
        class TESTSDStringSAN

        We test dchars.languages.san.transliterations.default.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_from_srcstr_2_srcstr(self):
        """
                TESTSDStringSAN.test_from_srcstr_2_srcstr()
        """

        for san, san_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_SAN().init_from_transliteration(san_basic)
            self.assertEqual( san, str(string) )
            san_basic2 = string.get_transliteration()
            self.assertEqual( san_basic, san_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration1(self):
        """
                TESTSDStringSAN.test_get_transliteration1
        """
        for san, san_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_SAN(san)
            san_basic2 = string.get_transliteration()
            self.assertEqual( san_basic, san_basic2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration2(self):
        """
                TESTSDStringSAN.test_get_transliteration2

                This function uses non-reciprocal characters.
        """

        for txt, trans in ( ("",                ''           ),
                            # क(0x0915)
                            ("क",               'ka'         ),
                            # क(0x0915) + virama(0x094D)
                            ("क्",               'k'         ),
                            # क(0x0915) + 0x093E
                            ("का",               'kA'         ),
                            # # क(0x0915) + 0x093F
                            ("कि",               'ki'         ),
                            # क(0x0915) + 0x0940
                            ("की",               'kI'         ),
                            # (independent) vowels
                            ("अइउऋऌएओ",         'a+i+uR^iL^i/e+o'   ),
                            # (independent) long vowels
                            ("आईऊॠॡऐऔ",         'A+I/UR^IL^I+ai+au'   ),
                            # (some consonants)
                            ('कखगघह',           'kakhagaghaha'),
                            ('चछजझ',            'chaChajajha'),
                            ('टठडढ',            'TaThaDaDha'),
                            ('तथदधलस',          'tathadadhalasa'),
                            ('पफबभ'             ,'paphababha'),
                            # क(0x0915) + anudatta(0x0952)
                            ("क॒",               'ka\\_'         ),
                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902)
                            ("कं॒",               'ka\\_M'         ),

                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + visarga(0x0903)
                            ("कं॒ः",               'ka\\_MH'         ),

                            # १(0x0967) + anudatta(0x0952) + udatta=svarita(0x0951)
                            ("१॒॑",               "1\\_\\'"         ),

                            # an impossible form for Sanskrit, interesting for the tests :
                            # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + virama(0x094D)
                            ("कं्॒",               'k\\_M'         ),

                            # hiatus :
                            ('यइ', 'ya+i'),
                            ('रआ', "ra/A"),

                            # verses from Ṛgveda-Saṁhitā :
                            # 1.001.01a :
                            ('अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।',
                             "a\\_gnimI\\'Le pu\\_rohi\\'taM ya\\_j~nasya\\' " \
                             "de\\_vamR^i\\_tvija\\'m ."),
                            # 1.001.01c :
                            ('होता॑रं रत्न॒धात॑मम् ॥', "hotA\\'raM ratna\\_dhAta\\'mam .."),
                            # 2.001.01a :
                            ("त्वम॑ग्ने॒ " \
                             "द्युभि॒स्त्वमा॑शुशु॒क्षणि॒स्त्वम॒द्भ्यस्त्वमश्म॑न॒स्परि॑ ।",
                             "tvama\\'gne\\_ dyubhi\\_stvamA\\'shushu\\_k" + \
                             "ShaNi\\_stvama\\_dbhyastvamashma\\'na\\_spari\\' ."),
                          ):

            string = DSTRING_SAN(txt)
            self.assertEqual( string.get_transliteration(), trans )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration3(self):
        """
                TESTSDStringSAN.test_get_transliteration3
        """
        sourceprefix = re.compile("[\\d|\\w|\\.]+\\s+")
        transprefix = re.compile("##[\\d|\\w|\\.\\s]+##\\s+")

        sourcefile = os.path.join( "tests",
                                   "languages",
                                   "san",
                                   "text003_rigveda_samhita__1_10.txt" )
        transfile  = os.path.join( "tests",
                                   "languages",
                                   "san",
                                   "text003_rigveda_samhita__1_10.itrans.txt" )

        with open(sourcefile, "r") as srcfile, \
             open(transfile,  "r") as transfile:

            # pylint: disable=E1103
            # (Instance of 'str' has no 'readlines' member (but some types could not be inferred))
            # readlines is a method of the file objects srcfile, transfile :
            srcdata = srcfile.readlines()
            transdata = transfile.readlines()

            for index, _srcline in enumerate(srcdata):

                if _srcline.strip() != "":
                    srcline = _srcline[re.search(sourceprefix, _srcline).end():]
                    srcline = srcline.strip()

                    _transline = transdata[index]
                    transline = _transline[re.search(transprefix, _transline).end():]
                    transline = transline.strip()

                    string = DSTRING_SAN(srcline)
                    trans = string.get_transliteration()
                    self.assertEqual( trans, transline )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration1(self):
        """
                TESTSDStringSAN.test_init_from_transliteration1
        """

        for san, san_basic in LIST_OF_RECIPROCAL_EXAMPLES:

            string = DSTRING_SAN().init_from_transliteration(san_basic)
            san2 = str(string)
            self.assertEqual( san, san2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration2(self):
        """
                TESTSDStringSAN.test_init_from_transliteration2

                This function uses non-reciprocal characters.
        """

        for txt in ( "",
                    # क(0x0915)
                    "क",
                    # क(0x0915) + space + danda(0x0964)
                    "क ।",
                    # क(0x0915) + virama(0x094D)
                    "क्",
                    # क(0x0915) + 0x093E
                    "का"
                    # क(0x0915) + 0x093E
                    "का",
                    # क(0x0915) + 0x093F
                    "कि",
                    # क(0x0915) + 0x0940
                    "की",

                    # vowels' combinations :
                    "अइउ",
                    "अइउ",
                    "उअइ",

                    # (independent) vowels
                    "अइउऋऌएओ",
                    # (independent) long vowels
                    "आईऊॠॡऐऔ",
                    # (some consonants)
                    'कखगघह',
                    'चछजझ',
                    'टठडढ',
                    'तथदधलस',
                    'पफबभ',

                    # क(0x0915) + anudatta(0x0952)
                    "क॒",
                    # क(0x0915) + anudatta(0x0952) + anusvara(0x0902)
                    "कं॒",

                    # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + visarga(0x0903)
                    "कं॒ः",

                    # १(0x0967) + anudatta(0x0952) + udatta=svarita(0x0951)
                    "१॒॑",

                    # an impossible form for Sanskrit, interesting for the tests :
                    # क(0x0915) + anudatta(0x0952) + anusvara(0x0902) + virama(0x094D)
                    "कं्॒",

                    # # hiatus :
                    'यइ',
                    'रआ',

                    # verses from Ṛgveda-Saṁhitā :
                    # 1.001.01a :
                    'अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।',
                    # 1.001.01c :
                    'होता॑रं रत्न॒धात॑मम् ॥',
                    # 2.001.01a :
                    "त्वम॑ग्ने॒ द्युभि॒स्त्वमा॑शुशु॒क्षणि॒स्त्वम॒द्भ्यस्त्वमश्म॑न॒स्परि॑ ।",
                   ):

            trans1 = DSTRING_SAN(txt).get_transliteration()
            string1 = DSTRING_SAN().init_from_transliteration(trans1)
            trans2 = string1.get_transliteration()
            self.assertEqual(trans1, trans2)
            string2 = DSTRING_SAN().init_from_transliteration(trans2)
            self.assertEqual(string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration3(self):
        """
                TESTSDStringSAN.test_init_from_transliteration3
        """
        sourcefile = os.path.join( "tests",
                                   "languages",
                                   "san",
                                   "text003_rigveda_samhita__1_10.txt" )

        with open(sourcefile, "r") as srcfile:

            sourceprefix = re.compile("[\\d|\\w|\\.]+\\s+")
            sourcedata = srcfile.readlines()

            for _srcline in sourcedata:

                if _srcline.strip() != "":
                    srcline = _srcline[re.search(sourceprefix, _srcline).end():]
                    srcline = srcline.strip()

                    trans1 = DSTRING_SAN(srcline).get_transliteration()
                    string = DSTRING_SAN().init_from_transliteration(trans1)
                    trans2 = string.get_transliteration()
                    self.assertEqual(trans1, trans2)

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration4(self):
        """
                TESTSDStringSAN.test_init_from_transliteration4

                (equivalences)
        """
        for trans1, trans2 in ( ("", ""),
                                ("ka", "ka"),
                                ("RRI", "R^I"),
                                ("LLi", "L^i"),
                              ):

            string1 = DSTRING_SAN().init_from_transliteration(trans1)
            string2 = DSTRING_SAN().init_from_transliteration(trans2)

            self.assertEqual(string1, string2)

    #///////////////////////////////////////////////////////////////////////////
    def test_init_from_transliteration5(self):
        """
                TESTSDStringSAN.test_init_from_transliteration5

                (nukta dot)
        """
        for txt in ( "",
                    # क(0x0915) + nukta(0x093C)
                    "क़",
                    # ढ(0x0922) + nukta(0x093C)
                    "ढ़",

                   ):

            trans1 = DSTRING_SAN(txt).get_transliteration()
            string1 = DSTRING_SAN().init_from_transliteration(trans1)
            trans2 = string1.get_transliteration()
            self.assertEqual(trans1, trans2)
            string2 = DSTRING_SAN().init_from_transliteration(trans2)
            self.assertEqual(string1, string2)

        for txt, trans in ( ("",                ''      ),
                            # क(0x0915) + nukta(0x093C)
                            ("क़",                'qa'    ),
                            # ढ(0x0922) + nukta(0x093C)
                            ("ढ़",                '.Dha'   ),
                          ):

            string = DSTRING_SAN(txt)
            self.assertEqual( string.get_transliteration(), trans )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringSAN.test_unknown_characters
        """
        string = DSTRING_SAN("ðकं॒ःð")
        self.assertEqual( str(string), "ðकं॒ःð" )

        string = DSTRING_SAN().init_from_transliteration("ðka\\_MHðka\\_MHð")
        self.assertEqual( str(string), "ðकं॒ःðकं॒ःð" )

        string = DSTRING_SAN().init_from_transliteration("ðka\\_MHðka\\_MHð")
        self.assertEqual( string.get_transliteration(), "ðka\\_MHðka\\_MHð" )


        string = DSTRING_SAN__UNKNOWNCHAR("ðकं॒ःð")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"कं॒ः"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_SAN__UNKNOWNCHAR().init_from_transliteration("ðka\\_MHðka\\_MHð")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"कं॒ः"+UNKNOWN_CHAR_SYMBOL+ \
                          "कं॒ः"+UNKNOWN_CHAR_SYMBOL )

        string = DSTRING_SAN__UNKNOWNCHAR().init_from_transliteration("ðka\\_MHðka\\_MHð")
        self.assertEqual( string.get_transliteration(),
                          UNKNOWN_CHAR_SYMBOL+"ka\\_MH"+UNKNOWN_CHAR_SYMBOL+ \
                          "ka\\_MH"+UNKNOWN_CHAR_SYMBOL )

