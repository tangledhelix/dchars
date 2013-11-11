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
    ❏DChars❏ : dchars/tests/languages/bod/transliterations/bodsan_tests.py
"""

import unittest

from dchars.dchars import new_dstring

DSTRING_BOD_HIGH = new_dstring(language="བོད་ཡིག",
                               transliteration_method='bodsan',
                               options = {"expected structure" : "always Sanskrit",
                                          "fill the buffers"       : 'no',
                                          "look up in the buffers" : 'no',
                                          "san2bod quality"        : "high",
                                          },
                          )

DSTRING_BOD_NORM = new_dstring(language="བོད་ཡིག",
                               transliteration_method='bodsan',
                               options = {"expected structure" : "always Sanskrit",
                                          "fill the buffers"       : 'no',
                                          "look up in the buffers" : 'no',
                                          "san2bod quality"        : "normal",
                                          },
                          )

DSTRING_BOD_LOW  = new_dstring(language="བོད་ཡིག",
                               transliteration_method='bodsan',
                               options = {"expected structure" : "always Sanskrit",
                                          "fill the buffers"       : 'no',
                                          "look up in the buffers" : 'no',
                                          "san2bod quality"        : "low",
                                          },
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
    def test_san2bod__three_qualities(self):
        """
                TESTSDStringBOD.test_san2bod__three_qualities
        """

        for san, bod_high, bod_norm, bod_low in (

                # visarga :
                # maḥ : maH / ma / ma
                ("मः", "མཿ་", "མ་", "མ་"),

                # the "v" consonant :
                # va : va / ba / ba
                ("व", "ཝ་", "བ་", "བ་"),

                # the ō vowel (as an dependent vowel)
                # mō : mo / mau / mau
                ("मो", "མོ་", "མཽ་", "མཽ་"),

                # the ō vowel (as a independent vowel)
                # ō : o / au / au
                ("ओ", "ཨོ་", "ཨཽ་", "ཨཽ་"),

                # long vowels (as dependent vowels)
                # mū : ū / ū / u
                ("मू", "མཱུ་", "མཱུ་", "མུ་"),

                # long vowels (as independent vowels)
                # ū : ū / ū / u
                ("ऊ", "ཨཱུ་", "ཨཱུ་", "ཨུ་"),

                # retroflex consonants :
                # ṇa : ṇa / ṇa / na
                ("ण", "ཎ་", "ཎ་", "ན་"),

                # aspirated consonants :
                # tha : tha / tha / ta
                ("थ", "ཐ་", "ཐ་", "ཏ་"),

                # geminate consonants :
                # mallika : mallika / mallika / malika
                ("मल्लिक", "མ་ལླི་ཀ་", "མ་ལླི་ཀ་", "མ་ལི་ཀ་"),
                ):

            high = DSTRING_BOD_HIGH().init_from_transliteration(san)
            self.assertEqual( str(high), bod_high )

            norm = DSTRING_BOD_NORM().init_from_transliteration(san)
            self.assertEqual( str(norm), bod_norm )

            low  = DSTRING_BOD_LOW().init_from_transliteration(san)
            self.assertEqual( str(low), bod_low )

    # #///////////////////////////////////////////////////////////////////////////
    # def test_san2bod__normal_quality(self):
    #     """
    #             TESTSDStringBOD.test_san2bod__normal_quality
    #     """

    #     for san, bod_norm in (
    #             # agaruḥ :
    #             ("अगरुः", "ཨ་ག་རུ་"),
    #             # śakuniḥ :
    #             ("शकुनिः", "ཤ་ཀུ་ནི་"),
    #             # kuśaḥ :
    #             ("कुशः", "ཀུ་ཤ་"),
    #             # nakraḥ :
    #             ("नक्र", "ན་ཀྲ་"),
    #             # tindukaḥ :
    #             ("तिन्दुकः", "ཏི་ནྡུ་ཀ་"),
    #             # taraṇiḥ :
    #             ("तरणिः", "ཏ་ར་ཎི་"),
    #             # padma :
    #             ("पद्म", "པ་དྨ་"),
    #             # pāṇini :
    #             ("पाणिनि", "པཱ་ཎི་ནི་"),
    #             # magadha :
    #             ("मगध", "མ་ག་དྷ་"),
    #             # magadhā :
    #             ("मगधा", "མ་ག་དྷཱ་"),
    #             # kalpaḥ :
    #             ("कल्पः", "ཀ་ལྤ་"),
    #             # malayaḥ :
    #             ("मलयः", "མ་ལ་ཡ་"),
    #             # kunda :
    #             ("कुन्द", "ཀུ་ནྡ་"),
    #             # gu ru :
    #             ("गुरु", "གུ་རུ་"),
    #             # ṭīkā :
    #             ("टीका", "ཊཱི་ཀཱ་"),
    #             # mahā :
    #             ("महा", "མ་ཧཱ་"),
    #             # maṇḍala :
    #             ("मण्डल", "མ་ཎྜ་ལ་"),
    #             # samaya :
    #             ("समय", "ས་མ་ཡ་"),
    #             # siddhi :
    #             ("सिद्धि", "སི་དདྷི་"),
    #             ):

    #         norm = DSTRING_BOD_NORM().init_from_transliteration(san)
    #         self.assertEqual( str(norm), bod_norm )

# ²"b+ha ga " : bhaga
# ²"haM" : haṃ
# ²"a ti " : ati
# ²"a nu" : anu
# ²"a b+hi She ka " : abhiṣeka
# 'kadambaḥ' 'ka dam ba'
# 'tilaḥ' 'ti la'
# 'mukundaḥ' '[rnga] mu kun da'
# 'asanaḥ' 'a sa na'
# 'bakulaḥ' 'ba ku la'
# 'kundam' 'kun dam'
# 'padmarāgaḥ' 'pad ma rāga'

# aucun problème si l'on admet que ś -> sh
# 'śulkaḥ' 'sho gam'
# ²"bi sho d+ha na "= viśodhana
# ²"shA kya " : śākya
# ² "shrI" : śrī

# aucun problème si l'on admet que c[=च] -> ts [=ཙ]
# 'cakoraḥ' '[bya]tsa ko ra'
