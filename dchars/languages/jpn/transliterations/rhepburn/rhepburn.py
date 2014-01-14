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
    ❏DChars❏ : dchars/languages/jpn/transliterations/rhepburn/rhepburn.py
"""

from dchars.utilities.regexstring import regexstring_list
from dchars.utilities.dicttools import invertdict
from dchars.utilities.lstringtools import isort_a_lstrings_bylen_nodup
from dchars.utilities.lstringtools import prepare_list_to_strformat
from dchars.symbols.symbols import UNKNOWN_CHAR_SYMBOL
import re

################################################################################
# List of the available directions for this transliteration method :
#
#  +1 (text->transliteration)
#  -1 (transliteration->text)
#
################################################################################
AVAILABLE_DIRECTIONS = (-1, +1)

################################################################################
# transliteration's equivalences :
################################################################################
TRANS_EQUIVALENCES = ()

################################################################################
# transliteration's symbols :
################################################################################

#
# * CAVEAT ! If you modify these dictionaries, don't forget to modify their
#            corresponding symbols' dictionaries in symbols.py !
#
# * CAVEAT ! No duplicate value allowed in these dictionaries !
#
# HIRAGANA[base_char] = transliterated character
# LOWER_CASE[base_char] = transliterated character
HIRAGANA = {
      'あ'        : "a",
      'い'        : "i",
      'う'        : "u",
      'え'        : "e",
      'お'        : "o",
      'か'        : "ka",
      'き'        : "ki",
      'く'        : "ku",
      'け'        : "ke",
      'こ'        : "ko",
      'さ'        : "sa",
      'し'        : "shi",
      'す'        : "su",
      'せ'        : "se",
      'そ'        : "so",
      'た'        : "ta",
      'ち'        : "chi",
      'つ'        : "tsu",
      'て'        : "te",
      'と'        : "to",
      'な'        : "na",
      'に'        : "ni",
      'ぬ'        : "nu",
      'ね'        : "ne",
      'の'        : "no",
      'は'        : "ha",
      'ひ'        : "hi",
      'ふ'        : "hu",
      'へ'        : "he",
      'ほ'        : "ho",
      'ま'        : "ma",
      'み'        : "mi",
      'む'        : "mu",
      'め'        : "me",
      'も'        : "mo",
      'や'        : "ya",
      'ゆ'        : "yu",
      'よ'        : "yo",
      'ら'        : "ra",
      'り'        : "ri",
      'る'        : "ru",
      'れ'        : "re",
      'ろ'        : "ro",
      'わ'        : "wa",
      'ゐ'        : "wi",
      'ゑ'        : "we",
      'を'        : "wo",
      'ん'        : "n",
    }

KATAKANA = {
      'ア'        : "A",
      'イ'        : "I",
      'ウ'        : "U",
      'エ'        : "E",
      'オ'        : "O",
      'カ'        : "KA",
      'キ'        : "KI",
      'ク'        : "KU",
      'ケ'        : "KE",
      'コ'        : "KO",
      'サ'        : "SA",
      'シ'        : "SHI",
      'ス'        : "SU",
      'セ'        : "SE",
      'ソ'        : "SO",
      'タ'        : "TA",
      'チ'        : "CHI",
      'ツ'        : "TSU",
      'テ'        : "TE",
      'ト'        : "TO",
      'ナ'        : "NA",
      'ニ'        : "NI",
      'ヌ'        : "NU",
      'ネ'        : "NE",
      'ノ'        : "NO",
      'ハ'        : "HA",
      'ヒ'        : "HI",
      'フ'        : "HU",
      'ヘ'        : "HE",
      'ホ'        : "HO",
      'マ'        : "MA",
      'ミ'        : "MI",
      'ム'        : "MU",
      'メ'        : "ME",
      'モ'        : "MO",
      'ヤ'        : "YA",
      'ユ'        : "YU",
      'ヨ'        : "YO",
      'ラ'        : "RA",
      'リ'        : "RI",
      'ル'        : "RU",
      'レ'        : "RE",
      'ロ'        : "RO",
      'ワ'        : "WA",
      'ヰ'        : "WI",
      'ヱ'        : "WE",
      'ヲ'        : "WO",
      'ン'        : "N",
    }

# OTHER_SYMBOLS[base_char] = transliterated character
OTHER_SYMBOLS = {
               '0'       : '0',
               '1'       : '1',
               '2'       : '2',
               '3'       : '3',
               '4'       : '4',
               '5'       : '5',
               '6'       : '6',
               '7'       : '7',
               '8'       : '8',
               '9'       : '9',
         }

# PUNCTUATION[base_char] = transliterated character
PUNCTUATION = {'-'       : '-',
               ')'       : ')',
               '('       : '(',
               '['       : '[',
               ']'       : ']',
               '{'       : '{',
               '}'       : '}',
               ' '       : ' ',
               '.'       : '.',
               ','       : ',',
               ';'       : '?',
               '!'       : '!',
               '·'       : ';',
               '"'       : '"',
               "'"       : "'",
               "—"       : "_",
               ":"       : ":",
               '\n'      : '\n',
               '\r'      : '\r',
               '\t'      : '\t',
               "‘"       : '<2018>',
               "’"       : '<2019>',
               "᾽"       : '<1FBD>',
              }

HIRAGANA_INVERSED = invertdict(HIRAGANA, accept_duplicated_values=True)
KATAKANA_INVERSED = invertdict(KATAKANA)
OTHER_SYMBOLS_INVERSED = invertdict(OTHER_SYMBOLS)
PUNCTUATION_INVERSED = invertdict(PUNCTUATION)

################################################################################
# transliteration's patterns :
# PATTERN  is used to cut one complex characters into its elements.
# PATTERN2 is used to cut several complex characters into a list of complex characters.
################################################################################

# in order to build the pattern strings for the regexes we have to SORT the
# result : (|a|b|t|th) won't find 'th' in "theatre" but (th|a|b|t) will.
# We delete the possible duplicates in the resulting string.

LETTERS = isort_a_lstrings_bylen_nodup(
                regexstring_list(tuple(HIRAGANA_INVERSED.keys())) + \
                regexstring_list(tuple(KATAKANA_INVERSED.keys())) + \
                regexstring_list(tuple(OTHER_SYMBOLS_INVERSED.keys())) + \
                regexstring_list(tuple(PUNCTUATION_INVERSED.keys())) )

PATTERN_TXT = "(?P<base_char>({0}))".format("|".join(prepare_list_to_strformat(LETTERS)),)

# we inverse the effect of prepare_list_to_strformat()
PATTERN_TXT = PATTERN_TXT.replace('{{', '{')
PATTERN_TXT = PATTERN_TXT.replace('}}', '}')
PATTERN = re.compile(PATTERN_TXT)

PATTERN_TXT2 = "({0})".format("|".join(prepare_list_to_strformat(LETTERS)),)

# we inverse the effect of prepare_list_to_strformat()
PATTERN_TXT2 = PATTERN_TXT2.replace('{{', '{')
PATTERN_TXT2 = PATTERN_TXT2.replace('}}', '}')

PATTERN2 = re.compile(PATTERN_TXT2)

#///////////////////////////////////////////////////////////////////////////////
def dchar__get_translit_str(dstring_object, dchar):
    """
        function dchar__get_translit_str()

        dchar : DCharacterJPN object

        Return a transliterared string corresponding to <char>.
    """
    res = []

    if dchar.unknown_char:
        if dstring_object.options["anonymize the unknown characters"] == 'yes':
            return UNKNOWN_CHAR_SYMBOL
        else:
            return dchar.base_char

    if dchar.base_char is not None:

        if dchar.punctuation:
            res.append( PUNCTUATION[dchar.base_char] )

        elif dchar.base_char in OTHER_SYMBOLS:
            res.append( OTHER_SYMBOLS[dchar.base_char] )

        else:
            if dchar.chartype == 'hiragana':
                res.append( HIRAGANA[dchar.base_char] )
            elif dchar.chartype == 'katakana':
                res.append( KATAKANA[dchar.base_char] )

    return "".join( res )

#///////////////////////////////////////////////////////////////////////////////
def dchar__init_from_translit_str(dchar, src):
    """
        function init_from_transliteration()

        dchar   :       DCharacterJPN object
        src     :       string

        Initialize and return <dchar>.

    """
    element = re.match(PATTERN, src)

    if element is None:
        dchar.unknown_char = True
        dchar.base_char = dchar.base_char

    else:
        dchar.unknown_char = False

        trans_pneuma = element.group('trans_pneuma')
        if trans_pneuma is None:
            dchar.pneuma = None
        else:
            dchar.pneuma = DIACRITICS_INVERSED[trans_pneuma]

        trans_tonos = element.group('trans_tonos')
        if trans_tonos is None:
            dchar.tonos = None
        else:
            dchar.tonos = DIACRITICS_INVERSED[trans_tonos]

        base_char = element.group('base_char')
        if base_char in HIRAGANA_INVERSED:
            dchar.base_char = HIRAGANA_INVERSED[base_char]
            dchar.capital_letter = False
            dchar.punctuation = False

        elif base_char in KATAKANA_INVERSED:
            dchar.base_char = KATAKANA_INVERSED[base_char]
            dchar.capital_letter = True
            dchar.punctuation = False

        elif base_char in OTHER_SYMBOLS_INVERSED:
            dchar.base_char = OTHER_SYMBOLS_INVERSED[base_char]
            dchar.capital_letter = False
            dchar.punctuation = False

        else:
            dchar.base_char = PUNCTUATION_INVERSED[base_char]
            dchar.capital_letter = False
            dchar.punctuation = True

        dchar.hypogegrammene = element.group('trans_hypogegrammene') is not None

        dchar.dialutika = element.group('trans_dialutika') is not None

        trans_mekos = element.group('trans_mekos')
        if trans_mekos is None:
            dchar.mekos = None
        else:
            dchar.mekos = DIACRITICS_INVERSED[trans_mekos]

    return dchar

#///////////////////////////////////////////////////////////////////////////////
def dstring__init_from_translit_str(dstring, dcharactertype, src):
    """
        function dstring__init_from_translit_str()

        dstring         :       DString object
        dcharactertype  :       type of DCharacterJPN
        src             :       string

        Initialize <dstring>.
    """
    _src = src[:]
    for start, dest in TRANS_EQUIVALENCES:
        _src = _src.replace( start, dest )


    last_real_index = -1
    for element in re.finditer(PATTERN2, _src):

        real_indexes = range(element.start(), element.end())

        # we add the unknown chars placed BEFORE OR WITHIN the recognized characters :
        # pylint: disable=W0612
        # Unused variable 'i'
        for i in range( last_real_index+1, min(real_indexes) ):
            new_dcharacter = dcharactertype(dstring_object=dstring)
            new_dcharacter.unknown_char = True
            new_dcharacter.base_char = src[i]
            dstring.append( new_dcharacter )

        # we add the character read by the regex :
        string = element.string[element.start():element.end()]
        new_character = dcharactertype(dstring_object=dstring).init_from_transliteration(string,
                                                                   "rhepburn")
        dstring.append(new_character)

        last_real_index = max(real_indexes)

    # we add the unknown chars placed AFTER the recognized characters :
    # pylint: disable=W0612
    # Unused variable 'i'
    for i in range( last_real_index+1, len(_src) ):
        new_dcharacter = dcharactertype(dstring_object=dstring)
        new_dcharacter.unknown_char = True
        new_dcharacter.base_char = src[i]
        dstring.append( new_dcharacter )

#///////////////////////////////////////////////////////////////////////////////
def dstring__trans__get_trans(dstring_object):
    """
        function dstring__trans__get_trans

        Return a (unicode) string corresponding to the <dstring_object>.
    """

    res = []

    for dchar in dstring_object:
        res.append( dchar__get_translit_str(dstring_object = dstring_object,
                                            dchar = dchar))

    return "".join( res )
