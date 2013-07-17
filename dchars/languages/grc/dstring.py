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
    ❏DChars❏ : dchars/languages/grc/dstring.py
"""

# problem with Pylint :
# pylint: disable=E0611
# many errors like "No name 'extensions' in module 'dchars'"

from dchars.errors.errors import DCharsError
from dchars.utilities.lstringtools import isort_a_lstrings_bylen_nodup
from dchars.dstring import DStringMotherClass
from dchars.languages.grc.dcharacter import DCharacterGRC
from dchars.languages.grc.symbols import SYMB_PUNCTUATION, \
                                         SYMB_UPPER_CASE, \
                                         SYMB_LOWER_CASE, \
                                         SYMB_OTHER_SYMBOLS, \
                                         SYMB_DIACRITICS
from dchars.languages.grc.symbols import SYMB_DIACRITICS__TONOS, \
                                         SYMB_DIACRITICS__MEKOS, \
                                         SYMB_DIACRITICS__PNEUMA

import re
import unicodedata
from dchars.utilities.lstringtools import number_of_occurences

# known transliterations :
import dchars.languages.grc.transliterations.basic.basic as basictrans
import dchars.languages.grc.transliterations.betacode.betacode as betacodetrans
import dchars.languages.grc.transliterations.perseus.perseus as perseustrans
import dchars.languages.grc.transliterations.gutenberg.gutenberg as gutenbergtrans

################################################################################
class DStringGRC(DStringMotherClass):
    """
        class DStringGRC

        DO NOT CREATE A DStringGRC object directly but use instead the
        dchars.py::new_dstring function.
    """

    # regex pattern used to slice a source string :
    #
    # NB : we use the default_symbols__pattern() function, NOT the normal
    #      default_symbols() function since some characters have to be
    #      treated apart to work with a regex.
    pattern_letters = "|".join( isort_a_lstrings_bylen_nodup(
                                SYMB_LOWER_CASE.default_symbols__pattern() + \
                                SYMB_UPPER_CASE.default_symbols__pattern() + \
                                SYMB_OTHER_SYMBOLS.default_symbols__pattern() + \
                                SYMB_PUNCTUATION.default_symbols__pattern() ))
    pattern_diacritics = "|".join( isort_a_lstrings_bylen_nodup(
                                   SYMB_DIACRITICS.default_symbols__pattern() ))
    pattern = re.compile("((?P<letter>{0})(?P<diacritics>({1})+)?)".format( pattern_letters,
                                                                            pattern_diacritics ))

    # transliteration's functions :
    trans__init_from_transliteration = {
          "basic" : basictrans.dstring__init_from_translit_str,
          "betacode": betacodetrans.dstring__init_from_translit_str,
          "perseus" : perseustrans.dstring__init_from_translit_str,
          "gutenberg" : None,
          }

    trans__get_transliteration = {
          "basic"       : basictrans.dstring__trans__get_trans,
          "betacode"    : betacodetrans.dstring__trans__get_trans,
          "perseus"     : perseustrans.dstring__trans__get_trans,
          "gutenberg"   : gutenbergtrans.dstring__trans__get_trans,
          }

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, str_src = None):
        """
                DStringGRC.__init__
        """
        DStringMotherClass.__init__(self)

        if str_src is not None:
            self.init_from_str(str_src)

    #///////////////////////////////////////////////////////////////////////////
    def get_usefull_combinations(self):
        """
                DStringGRC.get_usefull_combinations

                Return a DString with all the usefull combinations of characters,
                i.e. only the 'interesting' characters (not punctuation if it's too simple
                by example). The DChars stored in the dstring will be unique, id est, two
                dchars will not have the same appearence (__str__())

                NB : this function has nothing to do with linguistic or a strict
                     approach of the language. This function allows only to get the
                     most common and/or usefull characters of the writing system.

                NB : function required by the dchars-fe project.
        """
        self.clear()

        dchar = DCharacterGRC(self)
        for dchar in dchar.get_usefull_combinations():

            already_present = False
            for dchar2 in self:
                if str(dchar) == str(dchar2):
                    already_present = True
                
            if not already_present:
                self.append( dchar )
        
        return self

    #///////////////////////////////////////////////////////////////////////////
    def get_transliteration(self):
        """
                DStringGRC.get_transliteration
        """

        # Pylint can't know that <self> has a 'trans__get_transliteration_method' member
        # created when <self> has been initialized by new_dstring() :
        # pylint: disable=E1101
        # -> "Instance of 'DStringBOD' has no 'trans__get_transliteration_method' member"
        res = DStringGRC.trans__get_transliteration[self.transliteration_method](self)
        return res

    #///////////////////////////////////////////////////////////////////////////
    def init_from_str(self, str_src):
        """
                DStringGRC.init_from_str

                Function called by __init__(), initialize <self> and return
                <indexes_of_unrecognized_chars>.

                str_src : str

                HOW IT WORKS :
                * (1) str_src -> (decomposition) unicodedata.normalize('NFD',) = normalized_src
                * (2) = normalized_src -> (default symbols required) :
                *     replace_by_the_default_symbols() -> normalized_src
                * (3) initialisation from the recognized characters.
                *     re.finditer(DStringGRC.pattern) give the symbols{letter+diacritics}
                *     (3.1) base_char
                *     (3.2) contextual_form
                *     (3.3) tonos (τόνος)
                *     (3.4) mekos (μῆκος)
                *     (3.5) pneuma (πνεῦμα)
                *     (3.6) hypogegrammene (ὑπογεγραμμένη)
                *     (3.7) dialutika (διαλυτικά)
                *     (3.8) we add the new character
        """

        #.......................................................................
        # (1) str_src -> (decomposition) unicodedata.normalize('NFD',) = normalized_src
        #.......................................................................
        normalized_src = unicodedata.normalize('NFD', str_src)

        #.......................................................................
        # (2) = normalized_src -> (default symbols required) :
        #     replace_by_the_default_symbols() -> normalized_src
        #.......................................................................
        normalized_src = SYMB_PUNCTUATION.replace_by_the_default_symbols(normalized_src)
        normalized_src = SYMB_LOWER_CASE.replace_by_the_default_symbols(normalized_src)
        normalized_src = SYMB_UPPER_CASE.replace_by_the_default_symbols(normalized_src)
        normalized_src = SYMB_OTHER_SYMBOLS.replace_by_the_default_symbols(normalized_src)
        normalized_src = SYMB_DIACRITICS.replace_by_the_default_symbols(normalized_src)

        #.......................................................................
        # (3) initialisation from the recognized characters.
        #     re.finditer(DStringGRC.pattern) give the symbols{letter+diacritics}
        #.......................................................................
        indexes = []    # indexes of the substring well analyzed : ( start, end )
        for element in re.finditer(DStringGRC.pattern,
                                   normalized_src):

            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            # we add the unknown characters at the beginning and in the middle
            # of the string (see at the end of this function)
            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            if indexes:
                # <indexes> isn't empty :
                # ... we add the unknown character(s) between the last character and
                # the current one :

                for index in range( max(indexes[-1])+1, element.start() ):
                    new_character = DCharacterGRC(dstring_object = self,
                                                  unknown_char = True,
                                                  base_char = normalized_src[index])

                    self.append( new_character )

            else:
                # <indexes> is empty :
                # ... we add the unknown character(s) before the first index in <indexes> :
                for index in range( 0, element.start() ):
                    new_character = DCharacterGRC(dstring_object = self,
                                                  unknown_char = True,
                                                  base_char = normalized_src[index])

                    self.append( new_character )

            indexes.append( (element.start(), element.end()-1 ) )

            data = element.groupdict()
            letter     = data['letter']
            diacritics = data['diacritics']

            punctuation = letter in SYMB_PUNCTUATION.symbol2name
            capital_letter = letter in SYMB_UPPER_CASE.symbol2name

            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            # (3.1) base_char
            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            if punctuation:
                # punctuation symbol :
                base_char = SYMB_PUNCTUATION.get_the_name_for_this_symbol(letter)
            elif letter in SYMB_LOWER_CASE.symbol2name:
                # lower case :
                base_char = SYMB_LOWER_CASE.get_the_name_for_this_symbol(letter)
            elif letter in SYMB_UPPER_CASE.symbol2name:
                # upper case :
                base_char = SYMB_UPPER_CASE.get_the_name_for_this_symbol(letter)
            else:
                # other symbols :
                base_char = SYMB_OTHER_SYMBOLS.get_the_name_for_this_symbol(letter)

            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            # (3.2) contextual_form
            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            if base_char == 'β' and not capital_letter:
                contextual_form = "initial"
            elif base_char == 'ϐ' and not capital_letter:
                base_char = 'β'
                contextual_form = "medium+final"
            elif base_char == 'σ' and not capital_letter:
                contextual_form = "initial+medium"
            elif base_char == 'ς' and not capital_letter:
                base_char = 'σ'
                contextual_form = "final"
            else:
                contextual_form = "initial+medium+final"

            tonos = None
            mekos = None
            pneuma = None
            hypogegrammene = False
            dialutika = False
            if diacritics is not None:

                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                # (3.3) tonos (τόνος)
                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                tonos_nbr = number_of_occurences( source_string = diacritics,
                                                  symbols = SYMB_DIACRITICS__TONOS )

                if tonos_nbr > 1:
                    err_msg = "In '{0}' (start={1}, end={2}), τόνος defined several times."
                    raise DCharsError( context = "DStringGRC.init_from_str",
                                       message = err_msg.format(element.string,
                                                                element.start(),
                                                                element.end()))

                if SYMB_DIACRITICS.are_these_symbols_in_a_string('τόνος.βαρεῖα', diacritics):
                    tonos = "βαρεῖα"
                elif SYMB_DIACRITICS.are_these_symbols_in_a_string('τόνος.ὀξεῖα', diacritics):
                    tonos = "ὀξεῖα"
                elif SYMB_DIACRITICS.are_these_symbols_in_a_string('τόνος.περισπωμένη', diacritics):
                    tonos = "περισπωμένη"

                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                # (3.4) mekos (μῆκος)
                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                mekos_nbr = number_of_occurences( source_string = diacritics,
                                                  symbols = SYMB_DIACRITICS__MEKOS)

                if mekos_nbr > 1:
                    err_msg = "In '{0}' (start={1}, end={2}), μῆκος defined several times."
                    raise DCharsError( context = "DStringGRC.init_from_str",
                                       message = err_msg.format(element.string,
                                                                element.start(),
                                                                element.end()))

                if SYMB_DIACRITICS.are_these_symbols_in_a_string('μῆκος.μακρόν', diacritics):
                    mekos = "μακρόν"
                elif SYMB_DIACRITICS.are_these_symbols_in_a_string('μῆκος.βραχύ', diacritics):
                    mekos = "βραχύ"

                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                # (3.5) pneuma (πνεῦμα)
                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                pneuma_nbr = number_of_occurences( source_string = diacritics,
                                                   symbols = SYMB_DIACRITICS__PNEUMA)

                if pneuma_nbr > 1:
                    err_msg = "In '{0}' (start={1}, end={2}), πνεῦμα defined several times."
                    raise DCharsError( context = "DStringGRC.init_from_str",
                                       message = err_msg.format(element.string,
                                                                element.start(),
                                                                element.end()))

                if SYMB_DIACRITICS.are_these_symbols_in_a_string('πνεῦμα.ψιλὸν', diacritics):
                    pneuma = "ψιλὸν"
                elif SYMB_DIACRITICS.are_these_symbols_in_a_string('πνεῦμα.δασὺ', diacritics):
                    pneuma = "δασὺ"

                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                # (3.6) hypogegrammene (ὑπογεγραμμένη)
                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                hypogegrammene_nbr = number_of_occurences(
                    source_string = diacritics,
                    symbols = SYMB_DIACRITICS['ὑπογεγραμμένη'])

                if hypogegrammene_nbr > 1:
                    err_msg = "In '{0}' (start={1}, end={2}), ὑπογεγραμμένη defined several times."
                    raise DCharsError( context = "DStringGRC.init_from_str",
                                       message = err_msg.format(element.string,
                                                                element.start(),
                                                                element.end()))

                hypogegrammene = SYMB_DIACRITICS.are_these_symbols_in_a_string('ὑπογεγραμμένη',
                                                                               diacritics)

                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                # (3.7) dialutika (διαλυτικά)
                #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
                dialutika_nbr = number_of_occurences( source_string = diacritics,
                                                      symbols = SYMB_DIACRITICS['διαλυτικά'])

                if dialutika_nbr > 1:
                    err_msg = "In '{0}' (start={1}, end={2}), διαλυτικά defined several times."
                    raise DCharsError( context = "DStringGRC.init_from_str",
                                       message = err_msg.format(element.string,
                                                                element.start(),
                                                                element.end()))

                dialutika = SYMB_DIACRITICS.are_these_symbols_in_a_string('διαλυτικά', diacritics)

            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            # (3.8) we add the new character
            #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            new_character = DCharacterGRC(dstring_object = self,
                                          unknown_char = False,
                                          base_char = base_char,
                                          contextual_form = contextual_form,
                                          punctuation = punctuation,
                                          capital_letter = capital_letter,
                                          tonos = tonos,
                                          pneuma = pneuma,
                                          hypogegrammene = hypogegrammene,
                                          dialutika = dialutika,
                                          mekos=mekos)

            self.append( new_character )

        #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        # we add the final unknown characters (see at the beginning of this
        # function)
        #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        if indexes:
            # <element> is the last one and <indexes> isn't empty :
            for index in range( max(indexes[-1])+1, len(normalized_src) ):
                new_character = DCharacterGRC(dstring_object = self,
                                              unknown_char = True,
                                              base_char = normalized_src[index])

                self.append( new_character )

        else:
            # <indexes> is empty :
            for index in range( 0, len(normalized_src) ):
                new_character = DCharacterGRC(dstring_object = self,
                                              unknown_char = True,
                                              base_char = normalized_src[index])

                self.append( new_character )

    #///////////////////////////////////////////////////////////////////////////
    def init_from_transliteration(self, src):
        """
                DStringGRC.init_from_transliteration

                src     :       string

                Return <self>
        """

        # Pylint can't know that <self> has a 'transliteration_method' member
        # created when <self> has been initialized by new_dstring() :
        # pylint: disable=E1101
        # -> "Instance of 'DStringGRC' has no 'transliteration_method' member"
        DStringGRC.trans__init_from_transliteration[self.transliteration_method](
                dstring = self,
                dcharactertype = DCharacterGRC,
                src = src)

        return self
