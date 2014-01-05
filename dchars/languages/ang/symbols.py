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
#    (at your option) any anger version.
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
    ❏DChars❏ : dchars/languages/ang/symbols.py
"""
# problem with Pylint :
# pylint: disable=E0611
# many errors like "No name 'extensions' in module 'dchars'"
from dchars.utilities.name2symbols import Name2Symbols

#...............................................................................
# symbols used by Latin
#
# CAVEAT ! If you modify these dictionaries, don't forget to modify the
# corresponding transliteration's dictionaries !
#
#...............................................................................
SYMB_UPPER_CASE = Name2Symbols(
      {
      'a'          : ('A',),
      'æ'          : ('Æ',),
      'b'          : ('B',),
      'c'          : ('C',),
      'd'          : ('D',),
      'e'          : ('E',),
      'f'          : ('F',),
      'g'          : ('G',),
      'h'          : ('H',),
      'i'          : ('I',),
      'j'          : ('J',),
      'k'          : ('K',),
      'l'          : ('L',),
      'm'          : ('M',),
      'n'          : ('N',),
      'o'          : ('O',),
      'p'          : ('P',),
      'q'          : ('Q',),
      'r'          : ('R',),
      's'          : ('S',),
      't'          : ('T',),
      'þ'          : ('Þ',),
      'u'          : ('U',),
      'v'          : ('V',),
      'w'          : ('W',),
      'x'          : ('X',),
      'y'          : ('Y',),
      'z'          : ('Z',),
      })

SYMB_LOWER_CASE = Name2Symbols(
      {
      'a'          : ('a',),
      'æ'          : ('æ',),
      'b'          : ('b',),
      'c'          : ('c',),
      'd'          : ('d',),
      'e'          : ('e',),
      'f'          : ('f',),
      'g'          : ('g',),
      'h'          : ('h',),
      'i'          : ('i',),
      'j'          : ('j',),
      'k'          : ('k',),
      'l'          : ('l',),
      'm'          : ('m',),
      'n'          : ('n',),
      'o'          : ('o',),
      'p'          : ('p',),
      'q'          : ('q',),
      'r'          : ('r',),
      's'          : ('s',),
      't'          : ('t',),
      'þ'          : ('þ',),
      'u'          : ('u',),
      'v'          : ('v',),
      'w'          : ('w',),
      'x'          : ('x',),
      'y'          : ('y',),
      'z'          : ('z',),
      })

SYMB_PUNCTUATION = Name2Symbols(
    {'-'        : ("-", "—"),
     ')'        : (')',),
     '('        : ('(',),
     '['        : ('[',),
     ']'        : (']',),
     '{'        : ('{',),
     '}'        : ('}',),
     '0'        : ('0',),
     '1'        : ('1',),
     '2'        : ('2',),
     '3'        : ('3',),
     '4'        : ('4',),
     '5'        : ('5',),
     '6'        : ('6',),
     '7'        : ('7',),
     '8'        : ('8',),
     '9'        : ('9',),
     ' '        : (' ',),
     '.'        : ('.',),
     ','        : (',',),
     ';'        : (';',),
     '!'        : ('!',),
     '?'        : ('?',),
     '"'        : ('"','‘',"’",),
     "'"        : ("'","᾽"),
     ":"        : (":"),
     '\n'       : ('\n',),
     '\r'       : ('\r',),
     '\t'       : ('\t',),
    })

SYMB_DIACRITICS = Name2Symbols(
    {
     "stress1"    : ( chr(0x300), ),  # à
     "stress2"    : ( chr(0x301), chr(0x030D) ),  # á, a̍
     "makron"     : ( chr(0x304),),  # ā
     "upperdot"   : ( chr(0x307),),  # ċ, ġ
    })
# we define these constants in order to avoir multiple calls to SYMB_DIACRITICS.get_default_symbol :
DEFAULTSYMB__STRESS1 = SYMB_DIACRITICS.get_default_symbol("stress1")
DEFAULTSYMB__STRESS2 = SYMB_DIACRITICS.get_default_symbol("stress2")
DEFAULTSYMB__UPPERDOT = SYMB_DIACRITICS.get_default_symbol("upperdot")

#...............................................................................
# we calculate these tuple which is often used in order to speed up the code :
#...............................................................................
SYMB_DIACRITICS__STRESS1 = SYMB_DIACRITICS["stress1"]
SYMB_DIACRITICS__STRESS2 = SYMB_DIACRITICS["stress2"]
SYMB_DIACRITICS__MAKRON =  SYMB_DIACRITICS["makron"]
SYMB_DIACRITICS__UPPERDOT = SYMB_DIACRITICS["upperdot"]