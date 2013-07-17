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
    ❏DChars❏ : dchars/languages/grc/transliterations/ucombinations.py
"""
from dchars.dchars import new_dstring
from dchars.languages.grc.dcharacter import DCharacterGRC
from dchars.languages.grc.transliterations.basic import dchar__get_translit_str

#///////////////////////////////////////////////////////////////////////////
def get_usefull_combinations():
    """
            get_usefull_combinations()

            Return a (str)string with all the usefull combinations of characters,
            i.e. only the 'interesting' characters (not punctuation if it's too simple
            by example).
            
            NB : this function has nothing to do with linguistic or a strict
                 approach of the language. This function allows only to get the
                 most common and/or usefull characters of the writing system.

            NB : function required by the dchars-fe project.
    """
    res = []

    GRC = new_dstring( 'grc' )

    dstring = GRC()

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
            dchar = DCharacterGRC( dstring_object = dstring,
                                   base_char = base_char,
                                   contextual_form = "initial+medium+final",
                                   punctuation = False,
                                   capital_letter = capital_letter,
                                   tonos = None,
                                   pneuma = None,
                                   hypogegrammene = False,
                                   dialutika = False,
                                   mekos = None )

            txt = dchar__get_translit_str(dstring_object = dstring,
                                          dchar = dchar)

            res.append(txt)

    return "".join(res)
