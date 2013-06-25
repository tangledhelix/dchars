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
    ❏DChars❏ : dchars/tests/languages/grc/transliterations/gutenberg_tests.py
"""

import unittest, os.path

from dchars.dchars import new_dstring
from dchars.symbols.symbols import UNKNOWN_CHAR_SYMBOL

DSTRING_GRC = new_dstring(language="Ἑλληνικὴ γλῶττα",
                          transliteration_method = "gutenberg",
                          options = {"anonymize the unknown characters" : False,
                                     "gutenberg:ignore smooth breathing" : True,
                                     "gutenberg:ignore accents" : True,
                                     "gutenberg:ignore iota subscript" : True,
                                     "gutenberg:ignore diaeresis" : True,
                                     "gutenberg:transliteration for upsilon" : "u",
                                    },
                          )

DSTRING_GRC__FULL = new_dstring(language="Ἑλληνικὴ γλῶττα",
                          transliteration_method = "gutenberg",
                          options = {"anonymize the unknown characters" : False,
                                     "gutenberg:ignore smooth breathing" : False,
                                     "gutenberg:ignore accents" : False,
                                     "gutenberg:ignore iota subscript" : False,
                                     "gutenberg:ignore diaeresis" : False,
                                     "gutenberg:transliteration for upsilon" : "u",
                                    },
                          )

DSTRING_GRC__UNKNOWNCHAR = new_dstring(language="Ἑλληνικὴ γλῶττα",
                                       transliteration_method = "gutenberg",
                                       options = {"anonymize the unknown characters" : True,
                                                 },
                                      )

LIST_OF_EXAMPLES = (
    ("", ''),
    ("ῥα", "rha"),

    # examples given by Frank Zago :
    ("Ὁ δὲ Καῖσαρ (Οὐερκιγγετόριγα) εὐθὺς ὲν δεσμοῖς ἔδησε καὶ ἐς τὰ ἐπινίκια μετὰ τοῦτο πέμψας ἀπέκτεινε.",
     "Ho de Kaisar (Ouerkingetoriga) euthus en desmois edêse kai es ta epinikia meta touto pempsas apekteine."),

    ("Ὁ Οὐερκιγγετόριξ... καί τι καὐπὸ τῶν [Γερμανῶν] τῶν τοῖς Ῥωμαῖοις συμμαχούντων ἐσφάλη.",
     "Ho Ouerkingetorix... kai ti kaupo tôn [Germanôn] tôn tois Rhômaiois summachountôn esphalê."),

    ("Ὁ Οὐερκιγγετόριξ... ἐν φιλίᾳ ποτὲ τῷ Καίσαρι ἐγεγόνει.",
     "Ho Ouerkingetorix... en philia pote tô Kaisari egegonei."),

    ("Ἀρόερνοι.--Ἔθνοςμαχιμώτατον τῶν πρὸς τῇ Κελτικῇ Γαλατῶν.",
     "Aroernoi.--Ethnosmachimôtaton tôn pros tê Keltikê Galatôn."),

    ("Οἱ Κελτοἰ... ἀνὰ μέσον Ῥήνου... καὶ τῶν Πυρηναίων ὀρῶν... ἀθρόοι καὶ κατὰ πλῆθος ἐμπίπτοντες, ἀθρόοι κατελύοντο.",
     "Hoi Keltoi... ana meson Rhênou... kai tôn Purênaiôn orôn... athrooi kai kata plêthos empiptontes, athrooi kateluonto."),

    ("Καὶ πύργον τινὰ παραχρῆμα... ἑλόντες, ἔπειτα καὶ τὰ λοιπὰ οὐ χαλεπῶς ἐχειρώσαντο",
     "Kai purgon tina parachrêma... helontes, epeita kai ta loipa ou chalepôs echeirôsanto",)
)

LIST_OF_EXAMPLES__FULL = (
    ("",        ''),

    ("ῥα", "rha"),
    ("œῥα", "œrha"),
    ("(ῥα", "(rha"),
    (")ῥα", ")rha"),


    # from http://www.pgdp.net/wiki/Transliterating_Greek/Marking_Accents 
    ("τῷ Ἰουδαϊσμῷ ἀπὸ μέρους",
     "t^ô| )Iouda\"ism^ô| )ap\o m/erous"),

    # from http://www.pgdp.net/wiki/Transliterating_Greek/Marking_Accents
    ("ὅλων Θεόν, οὐκ αὐτὸν δὲ εἶναι τοῦ κόσμου",
     "h/olôn The/on, )ouk )aut\on d\e )e^inai to^u k/osmou"),
)

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).
################################################################################
class TESTSDStringGRC(unittest.TestCase):
    """
        class TESTSDStringGRC

        We test dchars.languages.grc.transliterations.gutenberg.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration(self):
        """
                TESTSDStringGRC.test_get_transliteration
        """
        for grc, grc_gutenberg in LIST_OF_EXAMPLES:

            string = DSTRING_GRC(grc)
            grc_gutenberg2 = string.get_transliteration()
            self.assertEqual( grc_gutenberg, grc_gutenberg2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration__full(self):
        """
                TESTSDStringGRC.test_get_transliteration__full
        """
        for grc, grc_gutenberg in LIST_OF_EXAMPLES__FULL:

            string = DSTRING_GRC__FULL(grc)
            grc_gutenberg2 = string.get_transliteration()
            self.assertEqual( grc_gutenberg, grc_gutenberg2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_get_transliteration__upsilon(self):
        """
                TESTSDStringGRC.test_get_transliteration__upsilon
        """
        DSTRING_GRC__UPSILON = new_dstring(language="Ἑλληνικὴ γλῶττα",
                          transliteration_method = "gutenberg",
                          options = {"anonymize the unknown characters" : False,
                                     "gutenberg:ignore smooth breathing" : True,
                                     "gutenberg:ignore accents" : True,
                                     "gutenberg:ignore iota subscript" : True,
                                     "gutenberg:ignore diaeresis" : True,
                                     "gutenberg:transliteration for upsilon" : "y",
                                    },
                          )

        string = DSTRING_GRC__UPSILON("πύργον")
        grc_gutenberg2 = string.get_transliteration()
        self.assertEqual( "pyrgon", grc_gutenberg2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_unknown_characters(self):
        """
                TESTSDStringGRC.test_unknown_characters
        """
        string = DSTRING_GRC__FULL("²ἆ²")
        self.assertEqual( str(string), "²ἆ²" )

        string = DSTRING_GRC__UNKNOWNCHAR("²ἆ²")
        self.assertEqual( str(string),
                          UNKNOWN_CHAR_SYMBOL+"ἆ"+UNKNOWN_CHAR_SYMBOL )
