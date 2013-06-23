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
    ❏DChars❏ : dchars/dchars.py
"""

# problem with Pylint :
# pylint: disable=E0611
# "No name 'errors' in module 'dchars.errors'"
from dchars.errors.errors import DCharsError
import os.path

#...............................................................................
# CONFIG_INI : options read in the configuration file.
#...............................................................................

# problem with Pylint :
# pylint: disable=F0401
# "Unable to import 'configparser'"
import configparser
CONFIG_INI = configparser.ConfigParser()
CONFIG_INI.read( os.path.join("dchars", "config.ini") )

#...............................................................................
# LANGUAGES : informations about each language. Please use three kinds of keys
#             for each language : English name, iso639-3 name and original name.
#
#  language's name -> (iso639-3 name,
#                      string type's name,
#                      default transliteration method,
#                      default options)
#
#...............................................................................
BIBLICAL_HEBREW = "עִבְֿרִיתֿ מִקְרָאִיתֿ"  # defined here to simplify the
                                # output of the following dictionary
                                # on editors unable to display right-to-left
                                # writing systems.

# names accepted by calling new_dstring() :
LANGUAGES_NAME = {
        "བོད་ཡིག"                  : "བོད་ཡིག",
        "bod"                   : "བོད་ཡིག",
        "Tibetan"               : "བོད་ཡིག",

        "Ἑλληνικὴ γλῶττα"       :       "Ἑλληνικὴ γλῶττα",
        "grc"                   :       "Ἑλληνικὴ γλῶττα",
        "Ancient Greek"         :       "Ἑλληνικὴ γλῶττα",

        BIBLICAL_HEBREW         :       BIBLICAL_HEBREW,
        "hbo"                   :       BIBLICAL_HEBREW,
        "Biblical Hebrew"       :       BIBLICAL_HEBREW,

        "latīna"                :       "latīna",
        "lat"                   :       "latīna",
        "Latin"                 :       "latīna",

        "संस्कृतम्"                 :       "संस्कृतम्",
        "san"                   :       "संस्कृतम्",
        "Sanskrit"              :       "संस्कृतम्",
    }

LANGUAGES = {
                "བོད་ཡིག"         :
                        ("bod",
                         "DStringBOD" ,
                         CONFIG_INI["bod"]["transliteration method"],
                            {"sorting method"         : CONFIG_INI["bod"]["sorting method"],
                             "expected structure"     : CONFIG_INI["bod"]["expected structure"],
                             "look up in the buffers" : CONFIG_INI["bod"]["look up in the buffers"] == "yes",
                             "fill the buffers"       : CONFIG_INI["bod"]["fill the buffers"] == "yes",
                             "anonymize the unknown characters" : \
                                CONFIG_INI["bod"]["anonymize the unknown characters"] == "yes",
                             },
                        ),

                "Ἑλληνικὴ γλῶττα":      ("grc",
                                         "DStringGRC",
                                         CONFIG_INI["grc"]["transliteration method"],
                                         {"sorting method": \
                                          CONFIG_INI["grc"]["sorting method"],
                                          "anonymize the unknown characters" : \
                                          CONFIG_INI["grc"]["anonymize the unknown characters"] == "yes",
                                          "gutenberg:ignore accents" : \
                                          CONFIG_INI["grc.gutenberg"]["ignore accents"] == "yes",
                                          "gutenberg:ignore smooth breathing" : \
                                          CONFIG_INI["grc.gutenberg"]["ignore smooth breathing"] == "yes",
                                          "gutenberg:ignore diaeresis" : \
                                          CONFIG_INI["grc.gutenberg"]["ignore diaeresis"] == "yes",
                                          "gutenberg:ignore iota subscript" : \
                                          CONFIG_INI["grc.gutenberg"]["ignore iota subscript"] == "yes",}),

                BIBLICAL_HEBREW :       ("hbo",
                                         "DStringHBO",
                                         CONFIG_INI["hbo"]["transliteration method"],
                                         {"sorting method": \
                                          CONFIG_INI["hbo"]["sorting method"],
                                          "anonymize the unknown characters" : \
                                          CONFIG_INI["hbo"]["anonymize the unknown characters"] == "yes",}),

                "latīna"        :       ("lat",
                                         "DStringLAT",
                                         CONFIG_INI["lat"]["transliteration method"],
                                         {"sorting method": \
                                          CONFIG_INI["lat"]["sorting method"],
                                          "anonymize the unknown characters" : \
                                          CONFIG_INI["lat"]["anonymize the unknown characters"] == "yes",}),

                "संस्कृतम्"         :       ("san",
                                         "DStringSAN",
                                         CONFIG_INI["san"]["transliteration method"],
                                         {"sorting method": \
                                          CONFIG_INI["san"]["sorting method"],
                                          "anonymize the unknown characters" : \
                                          CONFIG_INI["san"]["anonymize the unknown characters"] == "yes",}),
            }

# dict : key(language's name, iso639-3) : corresponding dstring type
# E.g.   LOADED_LANGUAGES["bod"] = dchars.languages.bod.dstring.DStringBOD
LOADED_LANGUAGES = {}

#///////////////////////////////////////////////////////////////////////////////
def new_dstring(language, transliteration_method=None, options=None):
    """
        Return a DString* type, e.g. DStringBOD for Tibetan.

        _language               : str
        transliteration_method  : str / None to use defaulttransliteration
        options                 : dict of strings
    """

    #...........................................................................
    # error : unknown language's name.
    #...........................................................................
    if not language in LANGUAGES_NAME:

        msg = "unknown language : '{0}'; known languages={1}".format(
            language,
            list(LANGUAGES.keys() ))

        raise DCharsError( context = "dchars/dchars.py",
                           message = msg,
                         )

    #...........................................................................
    # original language's name :
    #...........................................................................
    _language = LANGUAGES_NAME[language]

    #...........................................................................
    # we get the informations from LANGUAGES :
    #...........................................................................
    (language_iso639_3_name,
     dstring_name,
     default_trans_method,
     default_options) = LANGUAGES[_language]

    #...........................................................................
    # we import the module linked to dstring_name :
    #...........................................................................
    if language_iso639_3_name not in LOADED_LANGUAGES:

        # the following lines are equivalent, e.g. to :
        #    from dchars.languages.lat.dstring import DStringLAT
        #
        # (see http://docs.python.org/3.3/library/functions.html?highlight=__import__#__import__)
        module_name = "dchars.languages.{0}.dstring".format(language_iso639_3_name)
        module = __import__( module_name, globals(), locals(), [dstring_name,], 0)
        dstring_type = getattr( module, dstring_name )
        LOADED_LANGUAGES[language_iso639_3_name] = dstring_type
    else:
        dstring_type = LOADED_LANGUAGES[language_iso639_3_name]

    #...........................................................................
    # if no transliteration method specified as argument, we get the default method :
    #...........................................................................
    _transliteration_method = transliteration_method
    if _transliteration_method is None:
        _transliteration_method = default_trans_method

    #...........................................................................
    # _options is either equal to <options> either equal to the default options :
    #...........................................................................
    if options is None:
        _options = default_options.copy()
    else:
        _options = default_options.copy()
        # we add the options given in the arguments :
        for option in options:
            _options[option] = options[option]

    #...........................................................................
    # return value :
    #...........................................................................
    dstring = type( 'DString',
                    (dstring_type,),
                    {'iso639_3_name' : language_iso639_3_name,
                     'transliteration_method' : _transliteration_method,
                     'options' : _options} )

    return dstring

