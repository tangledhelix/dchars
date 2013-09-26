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
    ❏DChars❏ : dchars/languages_name.py
"""

#...............................................................................
# LANGUAGES_NAME : informations about each language. Please use three kinds of keys
#                  for each language : English name, iso639-3 name and original name.
#
#  language's name -> (iso639-3 name,
#                      string type's name,
#                      default transliteration method,
#                      default options)
#
#...............................................................................
BIBLICAL_HEBREW__NAME = "עִבְֿרִיתֿ מִקְרָאִיתֿ"  # defined here to simplify the
                                      # display of <LANGUAGES_NAME>
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

        BIBLICAL_HEBREW__NAME   :       BIBLICAL_HEBREW__NAME,
        "hbo"                   :       BIBLICAL_HEBREW__NAME,
        "Biblical Hebrew"       :       BIBLICAL_HEBREW__NAME,

        "latīna"                :       "latīna",
        "lat"                   :       "latīna",
        "Latin"                 :       "latīna",

        "संस्कृतम्"                 :       "संस्कृतम्",
        "san"                   :       "संस्कृतम्",
        "Sanskrit"              :       "संस्कृतम्",
    }

ISO_639_3_NAME = {
        "བོད་ཡིག"                  : "bod",
        "bod"                   : "bod",
        "Tibetan"               : "bod",

        "Ἑλληνικὴ γλῶττα"       :       "grc",
        "grc"                   :       "grc",
        "Ancient Greek"         :       "grc",

        BIBLICAL_HEBREW__NAME   :       "hbo",
        "hbo"                   :       "hbo",
        "Biblical Hebrew"       :       "hbo",

        "latīna"                :       "lat",
        "lat"                   :       "lat",
        "Latin"                 :       "lat",

        "संस्कृतम्"                 :       "san",
        "san"                   :       "san",
        "Sanskrit"              :       "san",
    }

LANGUAGES_AND_TRANSLITERATIONS = {
                                        "བོད་ཡིག"         : ("ewts",
                                                          "bodsan",
                                                         ),

                                        "latīna"                : ("basic", ),

                                        BIBLICAL_HEBREW__NAME   : ( "basic", ),

                                        "Ἑλληνικὴ γλῶττα"       : ( "basic",
                                                                    "betacode",
                                                                    "gutenberg",
                                                                    "perseus",
                                                                    ),

                                        "संस्कृतम्"                 : ( "iso15919",
                                                                      "itrans",
                                                                    ),
                                 }
