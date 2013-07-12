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
    ❏DChars❏ : dchars/config_ini.py

    function write_config_ini()
"""

import os.path
from dchars.config_ini_data import DATA as CONFIG_INI_DATA

#///////////////////////////////////////////////////////////////////////////////
def write_config_ini():
    """
        write_config_ini function :

        Overwrite the config.ini file with an header and the expected comments.
        The usual way to write a config.ini file would not allow to write the
        header and the comments, so we use a less sophisticated approach.
    """

    with open( os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "config.ini" ),
               "w") as config_file:

        #-----------------------------------------------------------------------
        # header :
        #-----------------------------------------------------------------------
        config_file.write( "#"*80 + "\n" )
        config_file.write( "#" + "\n" )
        config_file.write( "# " + "DChars : default values used by DString* objects" + "\n" )
        config_file.write( "#" + "\n" )
        config_file.write( "# " + "file automatically created by the function" + "\n" )
        config_file.write( "# " + "config_ini.py::write_config_ini()" + "\n" )
        config_file.write( "# " + "\n" )
        config_file.write( "# You can modify this file by changing the values affected to\n" +\
                           "# the options; but if you want to change the name or the\n" + \
                           "# number of the options you have to modify dchars.py and/or\n" + \
                           "# config_ini_data.py and/or config_ini.py." + "\n" )
        config_file.write( "#" + "\n" )
        config_file.write( "#"*80 + "\n" )
        config_file.write( "\n" )

        #-----------------------------------------------------------------------
        # sections, language by language
        #-----------------------------------------------------------------------
        for language_name in CONFIG_INI_DATA:

            config_file.write( "# " + "-"*78 + "\n" )
            config_file.write( "# " + CONFIG_INI_DATA[language_name].header + "\n" )
            config_file.write( "# " + "-"*78 + "\n" )

            config_file.write( "[" + language_name + "]" + "\n" )

            for data in CONFIG_INI_DATA[language_name]:

                if data.subsection != "":
                    config_file.write( "[" + data.subsection + "]" + "\n" )

                _values = ('\"{0}\"'.format(string) for string in data.values)
                config_file.write( "# " + " or ".join(_values) + "\n" )
                config_file.write( data.name + " = " + data.defaultvalue + "\n" )

                config_file.write( "\n" )
