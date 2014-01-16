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
from dchars.languages.jpn.symbols import DEFAULTSYMB__CHOONPU, \
                                         HIRAGANA_TO_HIRAGANA_DAKUTEN, \
                                         HIRAGANA_TO_HIRAGANA_HANDAKUTEN, \
                                         KATAKANA_TO_KATAKANA_DAKUTEN, \
                                         KATAKANA_TO_KATAKANA_HANDAKUTEN, \
                                         HIRAGANA_TO_KATAKANA
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
      'ん'        : "n[no vowel]",

      'ぁ'      : "[small]a",
      'ぃ'      : "[small]i",
      'ぅ'      : "[small]u",
      'ぇ'      : "[small]e",
      'ぉ'      : "[small]o",
      'ゕ'      : "[small]ka",
      'ゖ'      : "[small]ke",
      'っ'      : "[small]tsu",
      'ゃ'      : "[small]ya",
      'ゅ'      : "[small]yu",
      'ょ'      : "[small]yo",
      'ゎ'      : "[small]wa",
    }

HIRAGANA_DAKUTEN = {
      'が'        : "ga",
      'ぎ'        : 'gi',
      'ぐ'        : 'gu',
      'げ'        : 'ge',
      'ご'        : 'go',
      'ざ'        : 'za',
      'じ'        : 'ji',
      'ず'        : 'zu',
      'ぜ'        : 'ze',
      'ぞ'        : 'zo',
      'だ'        : 'da',
#      'ぢ'        : 'ji',
#      'づ'        : 'zu',
      'で'        : 'de',
      'ど'        : 'do',
      'ば'        : 'ba',
      'び'        : 'bi',
      'ぶ'        : 'bu',
      'べ'        : 'be',
      'ぼ'        : 'bo',
    }

HIRAGANA_HANDAKUTEN = {
      'ぱ'        : "pa",
      'ぴ'        : 'pi',
      'ぷ'        : 'pu',
      'ぺ'        : 'pe',
      'ぽ'        : 'po',
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

      'ァ'      : "[small]A",
      'ィ'      : "[small]I",
      'ゥ'      : "[small]U",
      'ェ'      : "[small]E",
      'ォ'      : "[small]O",
      'ヵ'      : "[small]KA",
      'ヶ'      : "[small]KE",
      'ッ'      : "[small]TSU",
      'ャ'      : "[small]YA",
      'ュ'      : "[small]YU",
      'ョ'      : "[small]YO",
      'ヮ'      : "[small]WA",
    }

KATAKANA_DAKUTEN = {
      'ガ'        : "GA",
      'ギ'        : 'GI',
      'グ'        : 'GU',
      'ゲ'        : 'GE',
      'ゴ'        : 'GO',
      'ザ'        : 'ZA',
      'ジ'        : 'JI',
      'ズ'        : 'ZU',
      'ゼ'        : 'ZE',
      'ゾ'        : 'ZO',
      'ダ'        : 'DA',
#      'ヂ'        : 'JI',
#      'ヅ'        : 'ZU',
      'デ'        : 'DE',
      'ド'        : 'DO',
      'バ'        : 'BA',
      'ビ'        : 'BI',
      'ブ'        : 'BU',
      'ベ'        : 'BE',
      'ボ'        : 'BO',
    }

KATAKANA_HANDAKUTEN = {
      'パ'        : "PA",
      'ピ'        : 'PI',
      'プ'        : 'PU',
      'ペ'        : 'PE',
      'ポ'        : 'PO',
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

COMPOSED_TRANSCRIPTIONS = {
        "ki[small]y"    : "ky",
        "gi[small]y"    : "gy",
        "shi[small]y"   : "sh",
        "ji[small]y"    : "j",
        "chi[small]y"   : "ch",
        "ni[small]y"    : "ny",
        "hi[small]y"    : "hy",
        "hi[small]y"    : "hy",
        "hi[small]y"    : "hy",
        "bi[small]y"    : "by",
        "pi[small]y"    : "py",
        "mi[small]y"    : "my",
        "ri[small]y"    : "ry",

        #"n[no vowel]b"        : "mb",
        #"n[no vowel]m"        : "mm",
        #"n[no vowel]p"        : "mp",

        "n[no vowel]y"        : "n'y",

        "n[no vowel]a"        : "n'a",
        "n[no vowel]ā"        : "n'ā",
        "n[no vowel]e"        : "n'e",
        "n[no vowel]ē"        : "n'ē",
        "n[no vowel]i"        : "n'i",
        "n[no vowel]ī"        : "n'ī",
        "n[no vowel]o"        : "n'o",
        "n[no vowel]ō"        : "n'ō",
        "n[no vowel]u"        : "n'u",
        "n[no vowel]ū"        : "n'ū",

        "aa"                  : "ā",
        "ee"                  : "ē",
        "oo"                  : "ō",
        "ou"                  : "ō",
        "uu"                  : "ū",

        "Aー"                   : "Ā",
        "Eー"                   : "Ē",
        "Iー"                   : "Ī",
        "Oー"                   : "Ō",
        "Uー"                   : "Ū",

        # sokuon : http://en.wikipedia.org/wiki/Sokuon
        "[small]tsuk"         : "kk",
        "[small]tsug"         : "gg",
        "[small]tsus"         : "ss",
        "[small]tsuz"         : "zz",
        "[small]tsut"         : "tt",
        "[small]tsud"         : "dd",
        "[small]tsuh"         : "hh",
        "[small]tsush"        : "shh",
        "[small]tsuch"        : "tch",
        "[small]tsuts"        : "tts",        
    }    

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

        elif dchar.chartype == 'hiragana':

            if dchar.diacritic is None:
                if dchar.smallsize:
                    res.append( "[small]" )

                res.append( HIRAGANA[dchar.base_char] )
            elif dchar.diacritic == 'dakuten':
                res.append( HIRAGANA_DAKUTEN[ HIRAGANA_TO_HIRAGANA_DAKUTEN[ dchar.base_char ] ] )
            elif dchar.diacritic == 'handakuten':
                res.append( HIRAGANA_HANDAKUTEN[ HIRAGANA_TO_HIRAGANA_HANDAKUTEN[ dchar.base_char ]])

        elif dchar.chartype == 'katakana':

            if dchar.diacritic is None:
                res.append( KATAKANA[ HIRAGANA_TO_KATAKANA[dchar.base_char]] )
            elif dchar.diacritic == 'dakuten':
                res.append( KATAKANA_DAKUTEN[ \
                    KATAKANA_TO_KATAKANA_DAKUTEN[ HIRAGANA_TO_KATAKANA[dchar.base_char]]] )
            elif dchar.diacritic == 'handakuten':
                res.append( KATAKANA_DAKUTEN[ \
                    KATAKANA_TO_KATAKANA_HANDAKUTEN[ HIRAGANA_TO_KATAKANA[dchar.base_char]]] )

        elif dchar.chartype == 'choonpu':

            res.append( DEFAULTSYMB__CHOONPU )

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

        ## trans_pneuma = element.group('trans_pneuma')
        ## if trans_pneuma is None:
        ##     dchar.pneuma = None
        ## else:
        ##     dchar.pneuma = DIACRITICS_INVERSED[trans_pneuma]

        ## trans_tonos = element.group('trans_tonos')
        ## if trans_tonos is None:
        ##     dchar.tonos = None
        ## else:
        ##     dchar.tonos = DIACRITICS_INVERSED[trans_tonos]

        ## base_char = element.group('base_char')
        ## if base_char in HIRAGANA_INVERSED:
        ##     dchar.base_char = HIRAGANA_INVERSED[base_char]
        ##     dchar.capital_letter = False
        ##     dchar.punctuation = False

        ## elif base_char in KATAKANA_INVERSED:
        ##     dchar.base_char = KATAKANA_INVERSED[base_char]
        ##     dchar.capital_letter = True
        ##     dchar.punctuation = False

        ## elif base_char in OTHER_SYMBOLS_INVERSED:
        ##     dchar.base_char = OTHER_SYMBOLS_INVERSED[base_char]
        ##     dchar.capital_letter = False
        ##     dchar.punctuation = False

        ## else:
        ##     dchar.base_char = PUNCTUATION_INVERSED[base_char]
        ##     dchar.capital_letter = False
        ##     dchar.punctuation = True

        ## trans_mekos = element.group('trans_mekos')
        ## if trans_mekos is None:
        ##     dchar.mekos = None
        ## else:
        ##     dchar.mekos = DIACRITICS_INVERSED[trans_mekos]

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

    res = "".join( res )

    for before, after in COMPOSED_TRANSCRIPTIONS.items():
        res = res.replace(before, after)

    res = res.replace("n[no vowel]", "n")

    if dstring_object.options["long vowels written with circumflex"] == 'yes':
        res = res.replace("ā", "â")
        res = res.replace("ē", "ê")
        res = res.replace("ō", "ô")
        res = res.replace("ū", "û")

    if dstring_object.options["katakanas written with upper case letters"] == 'no':
        res = res.lower()

    return res
