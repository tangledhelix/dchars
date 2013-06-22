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
    ❏DChars❏ : dchars/languages/san/symbols.py
"""

# problem with Pylint :
# pylint: disable=E0611
# many errors like "No name 'extensions' in module 'dchars'"
from dchars.utilities.name2symbols import Name2Symbols

#...............................................................................
# symbols used by Sanskrit.
#
# CAVEAT ! If you modify these dictionaries, don't forget to modify thei
# corresponding transliteration's dictionaries !
#
#...............................................................................
SYMB_CONSONANTS = Name2Symbols(
    {   'DEVANAGARI LETTER KA'            : (chr(0x0915),),
        'DEVANAGARI LETTER KHA'           : (chr(0x0916),),
        'DEVANAGARI LETTER GA'            : (chr(0x0917),),
        'DEVANAGARI LETTER GHA'           : (chr(0x0918),),
        'DEVANAGARI LETTER NGA'           : (chr(0x0919),),
        'DEVANAGARI LETTER CA'            : (chr(0x091A),),
        'DEVANAGARI LETTER CHA'           : (chr(0x091B),),
        'DEVANAGARI LETTER JA'            : (chr(0x091C),),
        'DEVANAGARI LETTER JHA'           : (chr(0x091D),),
        'DEVANAGARI LETTER NYA'           : (chr(0x091E),),
        'DEVANAGARI LETTER TTA'           : (chr(0x091F),),
        'DEVANAGARI LETTER TTHA'          : (chr(0x0920),),
        'DEVANAGARI LETTER DDA'           : (chr(0x0921),),
        'DEVANAGARI LETTER DDHA'          : (chr(0x0922),),
        'DEVANAGARI LETTER NNA'           : (chr(0x0923),),
        'DEVANAGARI LETTER TA'            : (chr(0x0924),),
        'DEVANAGARI LETTER THA'           : (chr(0x0925),),
        'DEVANAGARI LETTER DA'            : (chr(0x0926),),
        'DEVANAGARI LETTER DHA'           : (chr(0x0927),),
        'DEVANAGARI LETTER NA'            : (chr(0x0928),),
        # 0x0929 ('DEVANAGARI LETTER NNNA') is defined below as a character with nukta.
        'DEVANAGARI LETTER PA'            : (chr(0x092A),),
        'DEVANAGARI LETTER PHA'           : (chr(0x092B),),
        'DEVANAGARI LETTER BA'            : (chr(0x092C),),
        'DEVANAGARI LETTER BHA'           : (chr(0x092D),),
        'DEVANAGARI LETTER MA'            : (chr(0x092E),),
        'DEVANAGARI LETTER YA'            : (chr(0x092F),),
        'DEVANAGARI LETTER RA'            : (chr(0x0930),),
        # 0x0931 ('DEVANAGARI LETTER RRA') is defined below as a character with nukta.
        'DEVANAGARI LETTER LA'            : (chr(0x0932),),
        'DEVANAGARI LETTER LLA'           : (chr(0x0933),),
        # 0x0934 ('DEVANAGARI LETTER LLLA') is defined below as a character with nukta.
        'DEVANAGARI LETTER VA'            : (chr(0x0935),),
        'DEVANAGARI LETTER SHA'           : (chr(0x0936),),
        'DEVANAGARI LETTER SSA'           : (chr(0x0937),),
        'DEVANAGARI LETTER SA'            : (chr(0x0938),),
        'DEVANAGARI LETTER HA'            : (chr(0x0939),),

        # pseudo-consonant :
        'DEVANAGARI SIGN VISARGA'         : (chr(0x0903),),
    })

# Caveat : SYMB_DEPENDENT_VOWELS and SYMB_INDEPENDENT_VOWELS must have the same keys.
SYMB_INDEPENDENT_VOWELS = Name2Symbols(
    { 'SHORT A'                         : (chr(0x0904),),
      'A'                               : (chr(0x0905),),
      'AA'                              : (chr(0x0906),),
      'I'                               : (chr(0x0907),),
      'II'                              : (chr(0x0908),),
      'U'                               : (chr(0x0909),),
      'UU'                              : (chr(0x090A),),
      'VOCALIC R'                       : (chr(0x090B),),
      'VOCALIC RR'                      : (chr(0x0960),),
      'VOCALIC L'                       : (chr(0x090C),),
      'VOCALIC LL'                      : (chr(0x0961),),
      'SHORT E'                         : (chr(0x090E),),
      'E'                               : (chr(0x090F),),
      'SHORT O'                         : (chr(0x0912),),
      'O'                               : (chr(0x0913),),
      'AI'                              : (chr(0x0910),),
      'AU'                              : (chr(0x0914),),
    })

# Caveat : SYMB_DEPENDENT_VOWELS and SYMB_INDEPENDENT_VOWELS must have the same keys.
FAKE_A__SYMBOL = "FAKE_A"       # CAVEAT : can't be set to an empty string !
SYMB_DEPENDENT_VOWELS = Name2Symbols(
    {
      # we need to define 'A' as a dependent vowel even if no symbol exists in
      # devanagari. Such a string will be deleted by DCharacterSAN.get_sourcestr_representation()
      'A'                               : (FAKE_A__SYMBOL,),

      # normal letters :
      'AA'                              : (chr(0x093E),),
      'I'                               : (chr(0x093F),),
      'II'                              : (chr(0x0940),),
      'U'                               : (chr(0x0941),),
      'UU'                              : (chr(0x0942),),
      'VOCALIC R'                       : (chr(0x0943),),
      'VOCALIC RR'                      : (chr(0x0944),),
      'CANDRA E'                        : (chr(0x0945),),
      'SHORT E'                         : (chr(0x0946),),
      'E'                               : (chr(0x0947),),
      'AI'                              : (chr(0x0948),),
      'CANDRA O'                        : (chr(0x0949),),
      'SHORT O'                         : (chr(0x094A),),
      'O'                               : (chr(0x094B),),
      'AU'                              : (chr(0x094C),),
      'VOCALIC L'                       : (chr(0x0962),),
      'VOCALIC LL'                      : (chr(0x0963),),
    })

SYMB_OTHER_SYMBOLS = Name2Symbols(
    {
      'DEVANAGARI OM'                           : (chr(0x0950),),

      'DEVANAGARI DIGIT ZERO'                   : (chr(0x0966),),
      'DEVANAGARI DIGIT ONE'                    : (chr(0x0967),),
      'DEVANAGARI DIGIT TWO'                    : (chr(0x0968),),
      'DEVANAGARI DIGIT THREE'                  : (chr(0x0969),),
      'DEVANAGARI DIGIT FOUR'                   : (chr(0x096A),),
      'DEVANAGARI DIGIT FIVE'                   : (chr(0x096B),),
      'DEVANAGARI DIGIT SIX'                    : (chr(0x096C),),
      'DEVANAGARI DIGIT SEVEN'                  : (chr(0x096D),),
      'DEVANAGARI DIGIT HEIGHT'                 : (chr(0x096E),),
      'DEVANAGARI DIGIT NINE'                   : (chr(0x096F),),

      '0'                                       : ( "0", ),
      '1'                                       : ( "1", ),
      '2'                                       : ( "2", ),
      '3'                                       : ( "3", ),
      '4'                                       : ( "4", ),
      '5'                                       : ( "5", ),
      '6'                                       : ( "6", ),
      '7'                                       : ( "7", ),
      '8'                                       : ( "8", ),
      '9'                                       : ( "9", ),
    })

SYMB_PUNCTUATION = Name2Symbols(
    { 'DEVANAGARI DANDA'                        : (chr(0x0964),),
      'DEVANAGARI DOUBLE DANDA'                 : (chr(0x0965), chr(0x007C)),
      'DEVANAGARI ABBREVIATION SIGN'            : (chr(0x0970),),
      'DEVANAGARI SIGN HIGH SPACING DOT'        : (chr(0x0971),),
      'DEVANAGARI SIGN AVAGRAHA'                : (chr(0x093D),),
      ' '                                       : (" ",),
      '.'                                       : (".",),
      '\n'                                      : ('\n',),
      '\r'                                      : ('\r',),
      '\t'                                      : ('\t',),
      '('                                       : ( "(", ),
      ')'                                       : ( ")", ),
      '-'                                       : ( "-", ),
      '`'                                       : ( "`", ),
      "'"                                       : ( "'",),
      "?"                                       : ( "?",),
      "!"                                       : ( "!",),
    })

SYMB_DIACRITICS = Name2Symbols(
    { 'DEVANAGARI SIGN INVERTED CANDRABINDU'    : (chr(0x0900),),
      'DEVANAGARI SIGN CANDRABINDU'             : (chr(0x0901),),
      'DEVANAGARI SIGN ANUSVARA'                : (chr(0x0902),),
      'DEVANAGARI SIGN NUKTA'                   : (chr(0x093C),),
      'DEVANAGARI STRESS SIGN UDATTA'           : (chr(0x0951),),
      'DEVANAGARI STRESS SIGN ANUDATTA'         : (chr(0x0952),),
      'DEVANAGARI GRAVE ACCENT'                 : (chr(0x0953),chr(0x0300)),
      'DEVANAGARI ACUTE ACCENT'                 : (chr(0x0954),chr(0x0301)),
      'DEVANAGARI SIGN VIRAMA'                  : (chr(0x094D),),
    })
# we define these constants in order to avoir multiple calls to SYMB_DIACRITICS.get_default_symbol :
DEFAULTSYMB__VIRAMA = SYMB_DIACRITICS.get_default_symbol("DEVANAGARI SIGN VIRAMA")
DEFAULTSYMB__ANUDATTA = SYMB_DIACRITICS.get_default_symbol("DEVANAGARI STRESS SIGN ANUDATTA")
DEFAULTSYMB__NUKTA = SYMB_DIACRITICS.get_default_symbol("DEVANAGARI SIGN NUKTA")

#...............................................................................
# we calculate these tuples which are often used in order to speed up the code :
#...............................................................................
SYMB_DIACRITICS__ACCENTS = (
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI STRESS SIGN UDATTA'),
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI ACUTE ACCENT'),
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI GRAVE ACCENT'),
                            )

SYMB_DIACRITICS__NUKTA = (
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN NUKTA'),
                         )

SYMB_DIACRITICS__ANUSVARA_CANDRABINDU = (
                SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN ANUSVARA'),
                SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN CANDRABINDU'),
                SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN INVERTED CANDRABINDU'),
                              )

SYMB_DIACRITICS__VIRAMA = (
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN VIRAMA'),
                          )

SYMB_DIACRITICS__ANUSVARA = (
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI SIGN ANUSVARA'),
                          )

SYMB_DIACRITICS__ANUDATTA = (
                            SYMB_DIACRITICS.get_default_symbol('DEVANAGARI STRESS SIGN ANUDATTA'),
                          )








