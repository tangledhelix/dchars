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
    ❏DChars❏ : dchars/languages/fro/transliterations/basic/basic.py
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
# LOWER_CASE[base_char] = transliterated character
LOWER_CASE = {
              'a'     : "a",
              'b'     : "b",
              'c'     : "c",
              'ç'     : "ç",
              'd'     : "d",
              'e'     : "e",
              'f'     : "f",
              'g'     : "g",
              'h'     : "h",
              'i'     : "i",
              'j'     : "j",
              'k'     : "k",
              'l'     : "l",
              'm'     : "m",
              'n'     : "n",
              'o'     : "o",
              'p'     : "p",
              'q'     : "q",
              'r'     : "r",
              's'     : "s",
              't'     : "t",
              'u'     : "u",
              'v'     : "v",
              'w'     : "w",
              'x'     : "x",
              'y'     : "y",
              'z'     : "z",
              }

# UPPER_CASE[base_char] = transliterated character
UPPER_CASE = {'a'     : "A",
              'b'     : "B",
              'c'     : "C",
              'ç'     : "Ç",
              'd'     : "D",
              'e'     : "E",
              'f'     : "F",
              'g'     : "G",
              'h'     : "H",
              'i'     : "I",
              'j'     : "J",
              'k'     : "K",
              'l'     : "L",
              'm'     : "M",
              'n'     : "N",
              'o'     : "O",
              'p'     : "P",
              'q'     : "Q",
              'r'     : "R",
              's'     : "S",
              't'     : "T",
              'u'     : "U",
              'v'     : "V",
              'w'     : "W",
              'x'     : "X",
              'y'     : "Y",
              'z'     : 'Z',
             }

# PUNCTUATION[base_char] = transliterated character
PUNCTUATION = { '-'       : '-',
                ')'       : ')',
                '('       : '(',
                '['       : '[',
                ']'       : ']',
                '{'       : '{',
                '}'       : '}',
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
                ' '       : ' ',
                '.'       : '.',
                ','       : ',',
                ';'       : ';',
                '!'       : '!',
                '?'       : '?',
                '"'       : '"',
                "'"       : "'",
                ":"       : ":",
                '\n'      : '\n',
                '\r'      : '\r',
                '\t'      : '\t',
                "‘"       : '<2018>',
                "’"       : '<2019>',
                "᾽"       : '<1FBD>',
              }

LOWER_CASE_INVERSED = invertdict(LOWER_CASE, accept_duplicated_values=True)
UPPER_CASE_INVERSED = invertdict(UPPER_CASE)
PUNCTUATION_INVERSED = invertdict(PUNCTUATION)

DIACRITICS =  {
                "stress1"      : "\\",
                "stress2"      : "/",
                "stress12"     : "/\\",
              }
DIACRITICS_INVERSED = invertdict(DIACRITICS)

################################################################################
# transliteration's patterns :
# PATTERN  is used to cut one complex characters into its elements.
# PATTERN2 is used to cut several complex characters into a list of complex characters.
################################################################################

# in order to build the pattern strings for the regexes we have to SORT the
# result : (|a|b|t|th) won't find 'th' in "theatre" but (th|a|b|t) will.
# We delete the possible duplicates in the resulting string.
STRESS = isort_a_lstrings_bylen_nodup(
                [re.escape(DIACRITICS['stress1']),
                 re.escape(DIACRITICS['stress2']),
                 re.escape(DIACRITICS['stress12']), ])
LETTERS = isort_a_lstrings_bylen_nodup(
                regexstring_list(tuple(LOWER_CASE_INVERSED.keys())) + \
                regexstring_list(tuple(UPPER_CASE_INVERSED.keys())) + \
                regexstring_list(tuple(PUNCTUATION_INVERSED.keys())) )

PATTERN_TXT = "((?P<base_char>({0}))" \
              "(?P<trans_stress>({1}))?" \
              ")".format("|".join(prepare_list_to_strformat(LETTERS)),
                         "|".join(prepare_list_to_strformat(STRESS)),
                         )
# we inverse the effect of prepare_list_to_strformat()
PATTERN_TXT = PATTERN_TXT.replace('{{', '{')
PATTERN_TXT = PATTERN_TXT.replace('}}', '}')
PATTERN = re.compile(PATTERN_TXT)

PATTERN_TXT2 = "(({0})" \
                "({1})?" \
                ")".format("|".join(prepare_list_to_strformat(LETTERS)),
                           "|".join(prepare_list_to_strformat(STRESS)),
                          )
# we inverse the effect of prepare_list_to_strformat()
PATTERN_TXT2 = PATTERN_TXT2.replace('{{', '{')
PATTERN_TXT2 = PATTERN_TXT2.replace('}}', '}')

PATTERN2 = re.compile(PATTERN_TXT2)

#///////////////////////////////////////////////////////////////////////////////
def dchar__get_translit_str(dstring_object, dchar):
    """
        function dchar__get_translit_str()

        dchar : DCharacterFRO object

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
        else:
            if not dchar.capital_letter:
                # lower case :
                res.append( LOWER_CASE[dchar.base_char] )
            else:
                # upper case :
                res.append( UPPER_CASE[dchar.base_char] )

    if dchar.stress == 1 :
        res.append( DIACRITICS["stress1"] )
    elif dchar.stress == 2 :
        res.append( DIACRITICS["stress2"] )
    elif dchar.stress == 3 :
        res.append( DIACRITICS["stress12"] )

    return "".join( res )

#///////////////////////////////////////////////////////////////////////////////
def dchar__init_from_translit_str(dchar, src):
    """
        function init_from_transliteration()

        dchar   :       DCharacterFRO object
        src     :       string

        Initialize and return <dchar>.

    """
    element = re.match(PATTERN, src)

    if element is None:
        dchar.unknown_char = True

    else:
        dchar.unknown_char = False

        trans_stress = element.group('trans_stress')
        if trans_stress is None:
            dchar.stress = 0
        else:
            dchar.stress = {
                                "stress1"  : 1,
                                "stress2"  : 2,
                                "stress12" : 3,
                           }[DIACRITICS_INVERSED[trans_stress]]

        base_char = element.group('base_char')
        if base_char in LOWER_CASE_INVERSED:
            # lower case :
            dchar.base_char = LOWER_CASE_INVERSED[base_char]
            dchar.capital_letter = False
            dchar.punctuation = False

        elif base_char in UPPER_CASE_INVERSED:
            # upper case :
            dchar.base_char = UPPER_CASE_INVERSED[base_char]
            dchar.capital_letter = True
            dchar.punctuation = False

        else:
            # other symbols :
            dchar.base_char = PUNCTUATION_INVERSED[base_char]
            dchar.capital_letter = False
            dchar.punctuation = True

    return dchar

#///////////////////////////////////////////////////////////////////////////////
def dstring__init_from_translit_str(dstring, dcharactertype, src):
    """
        function dstring__init_from_translit_str()

        dstring         :       DString object
        dcharactertype  :       type of DCharacterFRO
        src             :       string

        Initialize <dstring>.
    """
    for start, dest in TRANS_EQUIVALENCES:
        src = src.replace( start, dest )

    last_real_index = -1
    for element in re.finditer(PATTERN2, src):

        real_indexes = range(element.start(), element.end())
        # we add the unknown chars placed BEFORE OR WITHIN the recognized characters :
        # pylint: disable=W0612
        # Unused variable 'i'
        for i in range( last_real_index+1, min(real_indexes) ):
            new_dcharacter = dcharactertype(dstring_object=dstring)
            new_dcharacter.unknown_char = True
            dstring.append( new_dcharacter )

        # we add the character read by the regex :
        string = element.string[element.start():element.end()]
        new_character = dcharactertype(dstring_object=dstring).init_from_transliteration(string,
                                                                                         "basic")
        dstring.append(new_character)

        last_real_index = max(real_indexes)

    # we add the unknown chars placed AFTER the recognized characters :
    # pylint: disable=W0612
    # Unused variable 'i'
    for i in range( last_real_index+1, len(src) ):
        new_dcharacter = dcharactertype(dstring_object=dstring)
        new_dcharacter.unknown_char = True
        new_dcharacter.base_char = src[i]
        new_dcharacter.unknown_char = True
        dstring.append( new_dcharacter )
