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
    ❏DChars❏ : bod__create_buffers.py

    This file create the buffers used by the "bod" (Tibetan) part of DChars.

    ############################################################################
    created buffers  :

    (a) dchars/languages/bod/buffer_str.data

    ############################################################################
    summary :

    (1.1) reading a list of EWTS/unicode words
    (1.2) reading the file ewts_words.txt

    (2) informations about the buffers

    (3) we write the buffers

    ############################################################################
"""

import pickle
import os.path
from dchars.dchars import new_dstring
import dchars.languages.bod.buffer as buffer
import dchars.languages.bod.transliterations.ewts.ewts_buffer as ewts_buffer
DSTRING_BOD_BUFF = new_dstring(language="བོད་ཡིག",
                               transliteration_method='ewts',
                               options = {"expected structure"          : "Tibetan or Sanskrit",
                                          "look up in the buffers"      : 'no',
                                          "fill the buffers"            : 'yes'},
                              )

#...............................................................................
# (1.1) reading a list of EWTS/unicode words
# We use a list of EWTS/unicode words in order to read ewts and unicode strings:
#...............................................................................
for bod, ewts in (
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
        ("དྷརྨཿ", "d+harmaH")
        ):
    DSTRING_BOD_BUFF().init_from_transliteration(ewts)
    DSTRING_BOD_BUFF( bod )

#...............................................................................
# (1.2) reading the file ewts_words.txt
#
# From the file dchars/languages/bod/transliterations/ewts_words.txt we
# extract a bunch of EWTS words; we read them and then we read their
# unicode equivalent.
#...............................................................................
with open( os.path.join("dchars",
                        "languages",
                        "bod",
                        "transliterations",
                        "ewts_words.txt"),
                        'r' )as src:

    for _ewts in src.readlines():
        ewts = _ewts[:-1]
        bod = DSTRING_BOD_BUFF().init_from_transliteration(ewts)
        DSTRING_BOD_BUFF( str(bod) )

#...............................................................................
# (2) informations about the buffers
#...............................................................................
print("len(BUFFER__FROM_STR) =" ,
      len(buffer.BUFFER__FROM_STR))
print("len(pickle.dumps(BUFFER__FROM_STR)) =",
      len(pickle.dumps(buffer.BUFFER__FROM_STR)))
print("len(EWTS_BUFFER__FROM_TRANS_STR) =",
      len(ewts_buffer.EWTS_BUFFER__FROM_TRANS_STR))
print("len(pickle.dumps(EWTS_BUFFER__FROM_TRANS_STR)) =",
      len(pickle.dumps(ewts_buffer.EWTS_BUFFER__FROM_TRANS_STR)))

#...............................................................................
# (3) we write the buffers
#...............................................................................
with open( buffer.BUFFER__FROM_STR__FNAME, "wb" ) as dest:
    dest.write( pickle.dumps(buffer.BUFFER__FROM_STR) )

with open( ewts_buffer.EWTS_BUFFER__FROM_TRANS_STR__FNAME, "wb" ) as dest:
    dest.write( pickle.dumps(ewts_buffer.EWTS_BUFFER__FROM_TRANS_STR) )
