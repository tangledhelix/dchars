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
    ❏DChars❏ : sort.py

    Read a file where words are stored (one word per line) and writes the sorted
    content to stdout.

    E.g. :
    * sort a Latin file :
      sort.py lat sourcefile

    * sort a Tibetan file :
      sort.py bod sourcefile

    * create two lists (see the documentation below) of the syllables stored
      in several sources, like src1, src2, src3, ... E.g : from src1 
      (e.g. a simple list of unicode Tibetan words) and from src2 (e.g. a
      dictionary written using the EWTS transliteration method) :
      sort.py --sorting_method=basic --modifications=tibetan-spellchecker bod src1 src2

"""

import argparse
from dchars.dchars import new_dstring
from datetime import datetime
from dchars.utilities.orderedset import OrderedSet

# sort.py's version is linked to the equivalent DChars' version :
from dchars.system import numversion as numversion
__version__ = numversion.VersionOfTheProgram().numversion
__version__ += "-sort#4"

#-------------------------------------------------------------------------------
def get_arguments():
    """
        Return the arguments of the command line.
    """
    parser = argparse.ArgumentParser(
        description=">>> (part of the DChars project, required by this file) "  + \
                    "Use sort.py to sort a file (one line = one word): " + \
                    "the result is printed to stdout.",
        epilog= "contact : suizokukan at orange.fr",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

    parser.add_argument('--sorting_method',
                    type=str,
                    help="sorting method : see dchars/config.ini for more details",
                    )

    parser.add_argument('--modifications',
                    type=str,
                    choices = ("tibetan-spellchecker",),
                    help="special modifications after the sort : 'tibetan-spellchecker' " + \
                         "will produce TWO lists of SYLLABLES, separated by the line '***' : " + \
                         "a list of 'pure' Tibetan words, then a list of all words. " + \
                         "This option will allow sort.py to read three kinds of files " + \
                         "(one unicode word by line, one ETWS word by line, one ETWS word " + \
                         "separated by ' - ' from the rest of the line as an entry of a " + \
                         "dictionary. See the code for an explanation about suffixes /A, /B... ."
        )

    parser.add_argument('--bod_addewts',
                    type=str,
                    choices = ("yes", "no"),
                    help="Use this option to add the EWTS transliteration of each form written to" + \
                         "stdout.",
                    default = "no",
        )

    parser.add_argument('--header',
                    type=str,
                    choices = ("yes", "no"),
                    default = "yes",
                    help="write or not a header at the beginning of the output",
        )

    parser.add_argument('language',
                    type=str,
                    choices = ('bod', 'bod', 'grc', 'hbo', 'lat'),
                    help="language's name (ISO 639-3)")

    parser.add_argument('source',
                        nargs = '+',
                        type=str,
                        help="filename(s), separated by a space")

    return parser.parse_args()

#-------------------------------------------------------------------------------
def modifications_tibspellchecker( srclist ):
    """
        (tibetan-spellchecker)
        Apply some modifications to the list of DString objects <srclist> : return
        a list of (unicode) strings, not a list of DStrings !
    """
    res = []

    for src in srclist:

        # src + /A if no suffix :
        if src.istructs[0].suffix1 is None and \
           src.istructs[0].suffix2 is None and \
           not src.istructs[0].postsuffix_u and \
           not src.istructs[0].postsuffix_o and \
           src.istructs[0].gramm_postsuffix is None:

            if ARGS.bod_addewts == "yes":
                transl = " # " + src.get_transliteration() + " / " + str(src.istructs)
            else:
                transl = ""
            res.append( str(src) + "/A" + transl )

        # src + /B if suffix1 == "-" :
        elif src.istructs[0].suffix1 == "-" and \
           src.istructs[0].suffix2 is None and \
           not src.istructs[0].postsuffix_u and \
           not src.istructs[0].postsuffix_o and \
           src.istructs[0].gramm_postsuffix is None:

            if ARGS.bod_addewts == "yes":
                transl = " # " + src.get_transliteration() + " / " + str(src.istructs)
            else:
                transl = ""
            res.append( str(src) + "/B" + transl )

        # src + /C if suffix 'u :
        elif src.istructs[0].suffix1 is None and \
           src.istructs[0].suffix2 is None and \
           src.istructs[0].postsuffix_u and \
           src.istructs[0].gramm_postsuffix is None and \
           not src.istructs[0].postsuffix_o:

            if ARGS.bod_addewts == "yes":
                transl = " # " + src.get_transliteration() + " / " + str(src.istructs)
            else:
                transl = ""
            res.append( str(src) + "/C" + transl )

        else:
            src.istructs[0].gramm_postsuffix = None
            src.istructs[0].postsuffix_o = False
            src.istructs[0].postsuffix_u = False

            src.alert__istructs_have_changed()

            if ARGS.bod_addewts == "yes":
                transl = " # " + src.get_transliteration() + " / " + str(src.istructs)
            else:
                transl = ""

            # we add src only if don't create a doublon :
            if str(src)+"/A" not in res and \
               str(src)+"/B" not in res and \
               str(src)+"/C" not in res:
                res.append( str(src) + transl )

    return res

#-------------------------------------------------------------------------------
def print_header(msg = None):
    """
        Print the informations in ARGS.
    """

    print("# File produced by sort.py, a file belonging to the DChars' project.")
    print("# version of sort.py : " + str(__version__) )
    print("# " + str(datetime.now())[:19])   # [:19] since we don't want to write the milliseconds.
    print("# ")
    print("# language = " + "'"+str(ARGS.language)+"'")
    print("# sorting_method = " + "'"+str(ARGS.sorting_method)+"'" )
    print("# input files = " + str(ARGS.source))
    print("# modifications = "+ "'"+str(ARGS.modifications)+"'")
    print("#")
    if msg is not None:
        print("# " + msg)
        print("#")

#*******************************************************************************
#                                    ENTRY POINT
#
# A) arguments of the command line
# B) creation of the DSTRING object
# C) processing
#    C.1) data reading
#    C.2) unicode strings become DString objects
#    C.3) sort
#    C.4) modifications
#    C.5) output
#
#*******************************************************************************

# A) arguments of the command line
ARGS = get_arguments()

# B) creation of the DSTRING object
DSTRING = new_dstring( language = ARGS.language,
                       options = {"look up in the buffers" : True,
                                  "sorting method" : ARGS.sorting_method})

# C) processing
if ARGS.source is not None:

    if ARGS.modifications is None:
        # normal case :

        # C.1) data reading
        DATA = []

        # we read the source file(s) :
        for filename in ARGS.source:

            with open(filename, 'r') as src:
                # raw words :
                DATA.extend(src.read().split())

        # C.2) unicode strings become DString objects

        # raw words -> DString objects
        WORDS = list(map(DSTRING, DATA))

        # C.3) sort
        SORTED_WORDS = sorted(WORDS, key=DSTRING.sortingvalue)

        # no C.4) modifications

        # C.5) output
        if ARGS.header == "yes":
            print_header()

        # for word in SORTED_WORDS:
        #     print(str(word))

    elif ARGS.modifications == "tibetan-spellchecker":

        # special case : "tibetan-spellchecker"

        # C.1) data reading
        # C.2) unicode strings become DString objects
        DATA = []

        # we read the source file(s) :
        for filename in ARGS.source:

            with open(filename, 'r') as src:

                for line in src.readlines():

                    if "a" in line or \
                       "i" in line or \
                       "e" in line or \
                       "o" in line or \
                       "u" in line or \
                       "k" in line or \
                       "h" in line or \
                       "H" in line or \
                       "g" in line or \
                       "n" in line or \
                       "c" in line or \
                       "j" in line or \
                       "y" in line or \
                       "t" in line or \
                       "T" in line or \
                       "d" in line or \
                       "D" in line or \
                       "p" in line or \
                       "b" in line or \
                       "m" in line or \
                       "M" in line or \
                       "s" in line or \
                       "z" in line or \
                       "w" in line or \
                       "'" in line or \
                       "y" in line or \
                       "r" in line or \
                       "l" in line:
                        # we have a line using transliteration :

                        if " - " in line:
                            # special case : we're in a dictionary with
                            # "entry - article"
                            word = line.split(" - ")[0].strip()

                            #print("(a)", "|"+word+"|")

                        else:
                            # normal line :
                            word = line.strip()

                            #print("(b)", "|"+word+"|")

                        # we add the syllables in <word> to DATA:
                        for istruct in DSTRING().init_from_transliteration(word).istructs:
                            if istruct.punctuation_or_other_symbol is None:
                                new_syllable = DSTRING("")
                                new_syllable.istructs.append( istruct )
                                new_syllable.alert__istructs_have_changed()
                                if new_syllable not in DATA:
                                    DATA.append( new_syllable )

                    else:
                        # pure Tibetan string :
                        word = line.strip()
                        #print("(c)", "|"+word+"|")

                        # we add the syllables in <word> to DATA:
                        for istruct in DSTRING(word).istructs:
                            if istruct.punctuation_or_other_symbol is None:
                                new_syllable = DSTRING("")
                                new_syllable.istructs.append( istruct )
                                new_syllable.alert__istructs_have_changed()
                                if new_syllable not in DATA:
                                    DATA.append( new_syllable )

        #for data in DATA:
        #    print(">>1 "+str(data)+"<<"+data.get_transliteration()+"<<")

        # C.3) sort
        BOD_SYLLABLES = []
        ALL_SYLLABLES = []
        for word in DATA:
            if not word.seems_to_be_a_sanskrit_string(strict_answer=True):
                BOD_SYLLABLES.append(word)
                ALL_SYLLABLES.append(word)
            else:
                ALL_SYLLABLES.append(word)

        SORTED_BOD_SYLLABLES = sorted(BOD_SYLLABLES, key=DSTRING.sortingvalue)
        SORTED_ALL_SYLLABLES = sorted(ALL_SYLLABLES, key=DSTRING.sortingvalue)

        #for data in SORTED_BOD_SYLLABLES:
        #    print(">>2 "+str(data)+"<<"+data.get_transliteration()+"<<"+str(data.istructs))
        #for data in SORTED_ALL_SYLLABLES:
        #    print(">>3 "+str(data)+"<<"+data.get_transliteration()+"<<"+str(data.istructs))

        # C.4) modifications
        # we use OrderedSet() in order to delete doublons : 
        # E.g. 'k' will be insert as 'ཀ', so does 'ka' : the two 'ཀ' will be reduced
        # to one 'ཀ'.
        SORTED_BOD_SYLLABLES = OrderedSet(modifications_tibspellchecker(SORTED_BOD_SYLLABLES))
        SORTED_ALL_SYLLABLES = OrderedSet(modifications_tibspellchecker(SORTED_ALL_SYLLABLES))

        #for data in SORTED_BOD_SYLLABLES:
        #    print(">>4 "+str(data)+"<<")
        #for data in SORTED_ALL_SYLLABLES:
        #    print(">>5 "+str(data)+"<<")

        # C.5) output
        if ARGS.header == "yes":
            print_header("-> only 'pure' Tibetan words, " + \
                         "without the words borrowed from Sanskrit or other languages")

        for word in SORTED_BOD_SYLLABLES:
            print(word)

        print("***")

        if ARGS.header == "yes":
            print_header("-> all words : 'pure' Tibetan and the other ones, " + \
                         "borrowed from Sanskrit and other languages")

        for word in SORTED_ALL_SYLLABLES:
            print(word)

