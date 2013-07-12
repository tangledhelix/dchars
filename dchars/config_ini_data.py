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

    Data related to the config.ini file
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# བོད་ཡིག (Tibetan)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bod_data = ConfigValuesForOneLanguage(header = "བོད་ཡིག (Tibetan)")
bod_data.append( ConfigValue( subsection = '',
                              values = ("ewts", "bodsan"),
                              name = 'transliteration method',
                              defaultvalue = 'ewts' ))

bod_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

bod_data.append( ConfigValue( subsection = '',
                              values = ("always Tibetan", "Tibetan or Sanskrit", "always Sanskrit"),
                              name = 'expected structure',
                              defaultvalue = 'Tibetan or Sanskrit' ))

bod_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'look up in the buffers',
                              defaultvalue = 'yes' ))

bod_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'fill the buffers',
                              defaultvalue = 'no' ))

bod_data.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'sorting method',
                              defaultvalue = 'basic' ))

bod_data.append( ConfigValue( subsection = 'bod.bodsan',
                              values = ("high", "normal", "low"),
                              name = 'san2bod quality',
                              defaultvalue = 'high' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ἑλληνικὴ γλῶττα (Ancient Greek)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

grc_data = ConfigValuesForOneLanguage(header = "Ἑλληνικὴ γλῶττα (Ancient Greek)")
grc_data.append( ConfigValue( subsection = '',
                              values = ("basic", "betacode", "perseus", "gutenberg"),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

grc_data.append( ConfigValue( subsection = 'grc.gutenberg',
                              values = ("yes", "no"),
                              name = 'ignore smooth breathing',
                              defaultvalue = 'yes' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'ignore accents',
                              defaultvalue = 'yes' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'ignore iota subscript',
                              defaultvalue = 'yes' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'ignore diaeresis',
                              defaultvalue = 'yes' ))

grc_data.append( ConfigValue( subsection = '',
                              values = ("u", "y", "u or y"),
                              name = 'transliteration for upsilon',
                              defaultvalue = 'u or y' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  "עִבְֿרִיתֿ מִקְרָאִיתֿ"  (Biblical Hebrew)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hbo_data = ConfigValuesForOneLanguage(header = '"עִבְֿרִיתֿ מִקְרָאִיתֿ" (Biblical Hebrew)')
hbo_data.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

hbo_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

hbo_data.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# latīna (Latin)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lat_data = ConfigValuesForOneLanguage(header = 'latīna (Latin)')
lat_data.append( ConfigValue( subsection = '',
                              values = ("basic",),
                              name = 'transliteration method',
                              defaultvalue = 'basic' ))

lat_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

lat_data.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# संस्कृतम् (Sanskrit)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

san_data = ConfigValuesForOneLanguage(header = 'संस्कृतम् (Sanskrit)')
san_data.append( ConfigValue( subsection = '',
                              values = ("iso15919", "itrans"),
                              name = 'transliteration method',
                              defaultvalue = 'iso15919' ))

san_data.append( ConfigValue( subsection = '',
                              values = ("yes", "no"),
                              name = 'anonymize the unknown characters',
                              defaultvalue = 'no' ))

san_data.append( ConfigValue( subsection = '',
                              values = ("default",),
                              name = 'sorting method',
                              defaultvalue = 'default' ))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DATA : a dict of language name (ISO 639-3) : <ConfigValuesForOneLanguage> object
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DATA = {
        "bod"   : bod_data,
        "grc"   : grc_data,
        "hbo"   : hbo_data,
        "lat"   : lat_data,
        "san"   : san_data,
       }
