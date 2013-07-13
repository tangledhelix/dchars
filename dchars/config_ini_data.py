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
    def __init__( self, subsection, values, name, defaultvalue ):
        """
                ConfigValue.__init__

                subsection      :       (str) can be empty
                values          :       (tuple of str)
                name            :       (str)
                defaultvalue    :       (str)
        """
        self.subsection = subsection
        self.values = values
        self.name = name
        self.defaultvalue = defaultvalue

    #///////////////////////////////////////////////////////////////////////////
    def __repr__( self ):
        """
                ConfigValue.__repr__
        """
        return "subsection={0}; values={1}; name={2}; defaultvalue={3}".format( self.subsection,
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
                              defaultvalue = 'ewts' ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("always Tibetan",
                                        "Tibetan or Sanskrit",
                                        "always Sanskrit"),
                              name = 'expected structure',
                              defaultvalue = 'Tibetan or Sanskrit' ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'look up in the buffers',
                              defaultvalue = 'yes' ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'fill the buffers',
                              defaultvalue = 'no' ))

BOD_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'sorting method',
                              defaultvalue = 'basic' ))

BOD_DATA.append( ConfigValue( subsection = 'bod.bodsan',
                              values = ("high", "normal", "low"),
                              name = 'san2bod quality',
                              defaultvalue = 'high' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ἑλληνικὴ γλῶττα (Ancient Greek)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GRC_DATA = ConfigValuesForOneLanguage(header = "Ἑλληνικὴ γλῶττα (Ancient Greek)")
GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("basic", "betacode", "perseus", "gutenberg"),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

GRC_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore smooth breathing',
                              defaultvalue = 'yes' ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore accents',
                              defaultvalue = 'yes' ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore iota subscript',
                              defaultvalue = 'yes' ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore diaeresis',
                              defaultvalue = 'yes' ))

GRC_DATA.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("u", "y", "u or y"),
                              name = 'transliteration for upsilon',
                              defaultvalue = 'u or y' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  "עִבְֿרִיתֿ מִקְרָאִיתֿ"  (Biblical Hebrew)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HBO_DATA = ConfigValuesForOneLanguage(header = '"עִבְֿרִיתֿ מִקְרָאִיתֿ" (Biblical Hebrew)')
HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

HBO_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# latīna (Latin)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LAT_DATA = ConfigValuesForOneLanguage(header = 'latīna (Latin)')
LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

LAT_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# संस्कृतम् (Sanskrit)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SAN_DATA = ConfigValuesForOneLanguage(header = 'संस्कृतम् (Sanskrit)')
SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("iso15919", "itrans"),
                              name = 'transliteration method',
                              defaultvalue = 'iso15919' ))

SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

SAN_DATA.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))


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
