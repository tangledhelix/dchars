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
    ❏DChars❏ : dchars/config_ini_data.py

    Data related to the config.ini file, especially the dict <DATA>.
"""

################################################################################
class ConfigValue(object):
    """
        class ConfigValue : define the equivalent to the following lines in
        a config.ini file :

            [bod.bodsan]                -> subsection (can be empty if no subsection)
            
            # "high", "normal", "low"   -> list of values
            san2bod quality : high      -> name : defaultvalue
    """

    #///////////////////////////////////////////////////////////////////////////
    def __init__( self, subsection, values, name, defaultvalue, optionname ):
        """
                ConfigValue.__init__

                subsection      :       (str) can be empty
                values          :       (tuple of str)
                name            :       (str)
                defaultvalue    :       (str)
                optionname      :       (str)
        """
        self.subsection = subsection
        self.values = values
        self.name = name
        self.defaultvalue = defaultvalue
        self.optionname = optionname

    #///////////////////////////////////////////////////////////////////////////
    def __repr__( self ):
        """
                ConfigValue.__repr__
        """
        txt = "subsection={0}; values={1}; name={2}; defaultvalue={3}; optionname={4};"
        return txt.format( self.subsection,
                           self.values,
                           self.name,
                           self.defaultvalue )

################################################################################        
class ConfigValuesForOneLanguage(list):
    """
        class ConfigValuesForOneLanguage

        A list of <ConfigValue> objects, with a header specific to the language.
    """

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self, header):
        """
                ConfigValuesForOneLanguage.__init__

                header  :       (str)
        """
        list.__init__(self)
        self.header = header

    #///////////////////////////////////////////////////////////////////////////
    def known_name(self, name):
        """
                ConfigValuesForOneLanguage.known_name

                name    :       (str)

                Return either True if <name> exists in self, either False
        """
        res = False

        for configvalue in self:
            if configvalue.name == name:
                res = True
                break

        return res

    #///////////////////////////////////////////////////////////////////////////
    def name_have_a_known_value(self, name, value):
        """
                ConfigValuesForOneLanguage.name_have_a_known_value

                name    :       (str)
                value   :       (str)

                Return either True if <value> is a correct value for <name>, either False
        """
        res = False

        for configvalue in self:
            if configvalue.name == name and value in configvalue.values:
                res = True
                break

        return res

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# བོད་ཡིག (Tibetan)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BOD_DATA = ConfigValuesForOneLanguage(header = "བོད་ཡིག (Tibetan)")
BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("ewts", "bodsan"),
                              name = 'transliteration method',
                              defaultvalue = 'ewts',
                              optioname = "transliteration method" ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no',
                              optioname = "anonymize the unknown characters" ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("always Tibetan",
                                        "Tibetan or Sanskrit",
                                        "always Sanskrit"),
                              name = 'expected structure',
                              defaultvalue = 'Tibetan or Sanskrit',
                              optioname = "expected structure" ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'look up in the buffers',
                              defaultvalue = 'yes',
                              optioname = "look up in the buffers" ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'fill the buffers',
                              defaultvalue = 'no',
                              optioname = "fill the buffers" ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'sorting method',
                              defaultvalue = 'basic',
                              optioname = "sorting method" ))

BOD_DATA.append( ConfigValue( subsection = 'bod.bodsan',
                              values = ("high", "normal", "low"),
                              name = 'san2bod quality',
                              defaultvalue = 'high',
                              optioname = "bodsan.san2bod quality" ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ἑλληνικὴ γλῶττα (Ancient Greek)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GRC_DATA = ConfigValuesForOneLanguage(header = "Ἑλληνικὴ γλῶττα (Ancient Greek)")
GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("basic", "betacode", "perseus", "gutenberg"),
                              name = 'transliteration method',
                              defaultvalue = 'basic',
                              optioname = "transliteration method" ))

GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no',
                              optioname = "anonymize the unknown characters" ))

GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default',
                              optioname = "sorting method" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore smooth breathing',
                              defaultvalue = 'yes',
                              optioname = "gutenberg:ignore smooth breathing" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore accents',
                              defaultvalue = 'yes',
                              optioname = "gutenberg:ignore accents" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore iota subscript',
                              defaultvalue = 'yes',
                              optioname = "gutenberg:ignore iota subscript" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore diaeresis',
                              defaultvalue = 'yes',
                              optioname = "gutenberg:ignore diaeresis" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'hh becomes h',
                              defaultvalue = 'yes',
                              optioname = "gutenberg:hh becomes h" ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("u", "y", "u or y"),
                              name = 'transliteration for upsilon',
                              defaultvalue = 'u or y',
                              optioname = "gutenberg:transliteration for upsilon" ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  "עִבְֿרִיתֿ מִקְרָאִיתֿ"  (Biblical Hebrew)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HBO_DATA = ConfigValuesForOneLanguage(header = '"עִבְֿרִיתֿ מִקְרָאִיתֿ" (Biblical Hebrew)')
HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic',
                              optioname = "transliteration method" ))

HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no',
                              optioname = "anonymize the unknown characters" ))

HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default',
                              optioname = "sorting method" ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# latīna (Latin)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LAT_DATA = ConfigValuesForOneLanguage(header = 'latīna (Latin)')
LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic',
                              optioname = "transliteration method" ))

LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no',
                              optioname = "anonymize the unknown characters" ))

LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default',
                              optioname = "sorting method" ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# संस्कृतम् (Sanskrit)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SAN_DATA = ConfigValuesForOneLanguage(header = 'संस्कृतम् (Sanskrit)')
SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("iso15919", "itrans"),
                              name = 'transliteration method',
                              defaultvalue = 'iso15919',
                              optioname = "transliteration method" ))

SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no',
                              optioname = "anonymize the unknown characters" ))

SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default',
                              optioname = "sorting method" ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DATA : a dict of language name (ISO 639-3) : <ConfigValuesForOneLanguage> object
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DATA = {
        "bod"   : BOD_DATA,
        "grc"   : GRC_DATA,
        "hbo"   : HBO_DATA,
        "lat"   : LAT_DATA,
        "san"   : SAN_DATA,
       }
