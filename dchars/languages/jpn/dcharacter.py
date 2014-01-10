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
    ❏DChars❏ : dchars/languages/jpn/dcharacter.py
"""

# problem with Pylint :
# pylint: disable=E0611
# many errors like "No name 'extensions' in module 'dchars'"
from dchars.errors.errors import DCharsError

from dchars.utilities.sortingvalue import SortingValue
from dchars.dcharacter import DCharacterMotherClass
from dchars.symbols.symbols import UNKNOWN_CHAR_SYMBOL
from dchars.languages.jpn.symbols import SYMB_LOWER_CASE, \
                                         SYMB_UPPER_CASE, \
                                         SYMB_OTHER_SYMBOLS, \
                                         DEFAULTSYMB__HANDIACRITICPSILON, \
                                         DEFAULTSYMB__HANDIACRITICDASU, \
                                         DEFAULTSYMB__DIACRITICOXEIA, \
                                         DEFAULTSYMB__DIACRITICBAREIA, \
                                         DEFAULTSYMB__DIACRITICPERISPOMENE, \
                                         DEFAULTSYMB__MEKOSBRAXU, \
                                         DEFAULTSYMB__MEKOSMAKRON, \
                                         DEFAULTSYMB__HUPOGEGRAMMENE, \
                                         DEFAULTSYMB__DIALYTIKA
import unicodedata
import copy
import itertools

# known transliterations :
import dchars.languages.jpn.transliterations.rhepburm.rhepburm as rhepburm

################################################################################
class DCharacterJPN(DCharacterMotherClass):
    """
        class DCharacterJPN
    """

    # transliteration's functions :
    trans__get_transliteration = {
          "rhepburn" : rhepburntrans.dchar__get_translit_str,
          }

    trans__init_from_transliteration = {
          "rhepburn" : rhepburntrans.dchar__init_from_translit_str,
          }

    #///////////////////////////////////////////////////////////////////////////
    def __eq__(self, aliud):
        """
                DCharacterJPN.__eq__

                aliud   :       DCharacterJPN object
        """

        return (self.unknown_char == aliud.unknown_char) and \
               (self.base_char == aliud.base_char) and \
               (self.punctuation == aliud.punctuation) and \
               (self.chartype == aliud.chartype) and \
               (self.diacritic == aliud.diacritic) and \
               (self.smallsize == aliud.smallsize)

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self,
                 dstring_object,
                 unknown_char = False,
                 base_char = None,
                 chartype = None,
                 punctuation = False,
                 diacritic = None,
                 smallsize = False):
        """
                DCharacterJPN.__init__

                .. code-block:: none

                    unknown_char        : bool
                    base_char           : None or a string
                                            o "あ", "い", ... (one hiragana)
                                            
                                            o "東", "名" (one kanji)
                                            
                                            o "ー" (the chōonpu 長音符 symbol)
                                              cd http://en.wikipedia.org/wiki/Ch%C5%8Donpu

                    chartype            : None or a string
                                            "hiragana" / "katakana" / "kanji" / "other"

                    punctuation         : bool
                    diacritic           : None / "dakuten" / "handakuten"
                    smallsize           : bool
        """
        DCharacterMotherClass.__init__(self,
                                       dstring_object = dstring_object,
                                       unknown_char = unknown_char,
                                       base_char = base_char,
                                       punctuation = punctuation)

        self.dstring_object = dstring_object
        self.chartype = chartype
        self.diacritic = diacritic
        self.smallsize = smallsize

    #///////////////////////////////////////////////////////////////////////////
    def __repr__(self):
        """
                DCharacterJPN.__repr__
        """

        return "unknown_char="+repr(self.unknown_char) + "; " + \
               "base_char="+repr(self.base_char) + "; " + \
               "chartype="+repr(self.chartype) + "; " + \
               "punctuation="+repr(self.punctuation) + "; " + \
               "diacritic="+repr(self.diacritic) + "; " + \
               "smallsize="+repr(self.smallsize)

    #///////////////////////////////////////////////////////////////////////////
    def clearAccentuation(self):
        """
                DCharacterJPN.clearAccentuation
        """
        self.diacritic = None

    #///////////////////////////////////////////////////////////////////////////
    def clone(self):
        """
                DCharacterJPN.clone
        """
        return DCharacterJPN( dstring_object = self.dstring_object,
                              unknown_char = self.unknown_char,
                              base_char = self.base_char,
                              chartype = self.chartype,
                              punctuation = self.punctuation,
                              diacritic = self.diacritic,
                              smallsize = self.smallsize )

    #///////////////////////////////////////////////////////////////////////////
    def get_sourcestr_representation(self):
        """
                DCharacterJPN.get_sourcestr_representation

                RETURN VALUE : a (str) string.
        """

        #.......................................................................
        # unknown char ? Nothing to do :
        #.......................................................................
        if self.unknown_char:
            if self.dstring_object.options["anonymize the unknown characters"] == 'yes':
                return UNKNOWN_CHAR_SYMBOL
            else:
                return self.base_char

        #.......................................................................
        # ok, the function can analyse <self> :
        #.......................................................................

        res = []

        if self.base_char is not None:
            if self.punctuation:
                # punctuation symbol :
                res.append( self.base_char )
            elif self.base_char in SYMB_OTHER_SYMBOLS:
                # other symbol :
                res.append( self.base_char )
            elif not self.capital_letter:
                # lower case :

                base_char = self.base_char
                if base_char =='β' and \
                   not self.capital_letter and \
                   self.chartype == "medium+final":
                    base_char = "ϐ"
                elif base_char =='σ' and \
                     not self.capital_letter and \
                     self.chartype == "final":
                    base_char = "ς"

                res.append( SYMB_LOWER_CASE.get_default_symbol(base_char) )
            else:
                # upper case :
                res.append( SYMB_UPPER_CASE.get_default_symbol(self.base_char) )

        if self.diacritic == 'diakuten':
            res.append( DEFAULTSYMB__DIAKUTEN )
        elif self.diacritic == 'handiakuten':
            res.append( DEFAULTSYMB__HANDIAKUTEN )

        res = "".join(res)

        return res

    #///////////////////////////////////////////////////////////////////////////
    def get_transliteration(self, transliteration_method, options):
        """
                DCharacterJPN.get_transliteration

                method  : string
        """
        return DCharacterJPN.trans__get_transliteration[transliteration_method](
            dstring_object = self.dstring_object,
            dchar = self,
            options = options)

    #///////////////////////////////////////////////////////////////////////////
    def get_usefull_combinations(self):
        """
                DCharacterJPN.get_usefull_combinations

                Yield, one dchar at a time,  all the usefull combinations of characters,
                i.e. only the 'interesting' characters (not punctuation if it's too simple
                by example).

                NB : this function has nothing to do with linguistic or a strict
                     approach of the language. This function allows only to get the
                     most common and/or usefull characters of the writing system.

                NB : function required by the dchars-fe project.
        """

        # base_char : we don't use the list stored in symbols.py
        # since we would lost the character's order.
        base_characters  = ( 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι',
                             'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ',
                             'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
                             'ϝ', 'ϗ', 'ϡ', 'ϛ', 'ϙ', )

        #-----------------------------------------------------------------------
        # (1/2) simple characters
        #-----------------------------------------------------------------------
        for base_char in base_characters:
            for capital_letter in (False, True):
                self.__init__( dstring_object = self.dstring_object,
                               base_char = base_char,
                               chartype = "initial+medium+final",
                               punctuation = False,
                               diacritic = None,
                               smallsize = False )

                yield copy.copy(self)

        #-----------------------------------------------------------------------
        # (2/2) complex characters
        #-----------------------------------------------------------------------
        combinations = (itertools.product(
                                           # base_chars
                                           base_characters,

                                           # chartype
                                           ("initial", "medium", "final",
                                            "initial+medium", "medium+final",
                                            "initial+medium+final"),

                                           # diacritic
                                           ( None, "ὀξεῖα", "βαρεῖα", "περισπωμένη" ),

                                           # smallsize
                                           (False, True),

                                           ))

        for base_char, chartype, \
            diacritic, smallsize, in combinations:

            add_this_dchar = True

            if base_char == 'ρ':
                if chartype != "initial+medium+final" or \
                   diacritic is not None or \
                   smallsize == True or \
                   mekos is not None:

                    add_this_dchar = False

            elif base_char in ('β', 'σ'):
                if diacritic is not None or \
                   smallsize == True or \
                   mekos is not None:

                    add_this_dchar = False

            elif base_char in ('α', 'η', 'ω'):
                if chartype != "initial+medium+final" or \
                   mekos is not None:

                    add_this_dchar = False

            elif base_char in ('ε', 'ο'):
                if chartype != "initial+medium+final" or \
                   smallsize == True or \
                   diacritic == "περισπωμένη" or \
                   smallsize == True or \
                   mekos is not None:

                    add_this_dchar = False

            elif base_char in ('ι', 'υ'):
                if chartype != "initial+medium+final" or \
                   smallsize == True or \
                   mekos is not None:

                    add_this_dchar = False

            else:
                if chartype != "initial+medium+final" or \
                   diacritic is not None or \
                   smallsize == True or \
                   mekos is not None:

                    add_this_dchar = False

            if add_this_dchar:
                self.__init__( dstring_object = self.dstring_object,
                               base_char = base_char,
                               chartype = chartype,
                               punctuation = False,
                               diacritic = diacritic,
                               smallsize = smallsize )

                yield copy.copy(self)

    #///////////////////////////////////////////////////////////////////////////
    def init_from_transliteration(self, src, transliteration_method):
        """
                DCharacterJPN.init_from_transliteration

                src     :       string
                transliteration_method  : string

                Return <self>.
        """
        self.reset()
        return DCharacterJPN.trans__init_from_transliteration[transliteration_method](dchar = self,
                                                                                      src = src)

    #///////////////////////////////////////////////////////////////////////////
    def reset(self):
        """
                DCharacterJPN.reset
        """
        self.unknown_char = True
        self.base_char = None
        self.punctuation = False
        self.chartype = None
        self.diacritic = None
        self.smallsize = False

    #///////////////////////////////////////////////////////////////////////////
    def sortingvalue(self):
        """
                DCharacterJPN.sortingvalue

                Return a SortingValue object

                NB : this function has almost no interest; you must use DStringJPN.sortingvalue()
                     to compare two strings. Use this function if you just want to compare
                     two characters.
        """
        res = SortingValue()

        if self.dstring_object.options["sorting method"] == "default":

            if self.unknown_char:
                # unknown char :
                res.append(1)

                # Some base_char may contain more than one character, like "β2".
                base_char_num = 0
                for index_char, char in enumerate(self.base_char):
                    base_char_num += ord(char) << index_char
                res.append( base_char_num )

                return res

            # known char :
            res.append(0)

            # base_char :
            #
            # Some base_char may contain more than one character, like "β2".
            #
            base_char_num = 0
            for index_char, char in enumerate(self.base_char):
                base_char_num += ord(char) << index_char
            res.append( base_char_num )

            # diacritic :
            if self.diacritic is None:
                res.append(0)
            elif self.diacritic == "ὀξεῖα":
                res.append(1)
            elif self.diacritic == "βαρεῖα":
                res.append(2)
            elif self.diacritic == "περισπωμένη":
                res.append(3)
            else:
                raise DCharsError( context = "DCharacterJPN.sortingvalue",
                                   message = "unknown value for diacritic ="+\
                                             str(self.diacritic) )

            # smallsize :
            if not self.smallsize:
                res.append(0)
            else:
                res.append(1)

        else:
            raise DCharsError( context = "DCharacterJPN.sortingvalue",
                               message = "unknown sorting method ="+\
                                         str(self.dstring_object.options["sorting method"]) )

        return res
