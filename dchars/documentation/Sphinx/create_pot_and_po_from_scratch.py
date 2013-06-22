#!/usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
#    create_pot_and_po_from_scratch Copyright (C) 2012 Suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of create_pot_and_po_from_scratch.
#    create_pot_and_po_from_scratch is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    create_pot_and_po_from_scratch is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with create_pot_and_po_from_scratch.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
        **************************************************
        * create_pot_and_po_from_scratch * version 0.0.1 *
        **************************************************

        Use this file in a directories' structure like :

                ./create_pot_and_po_from_scratch.py
                ./RSTsourcefiles/conf.py, file1.rst, file2.rst, ...
                ./i18n/fr/
                ./i18n/en/

        This file creates .pot files from .rst, then creates .po files from .pot files :
        .rst -> .pot -> en/po, fr/po, ...

        CAVEAT : THIS FILE WORKS ONLY ON LINUX-LIKE SYSTEM !
"""
import os

#///////////////////////////////////////////////////////////////////////////////
def system(order):
    """
        function system : print order and execute it.
    """
    print(">>>", order)
    os.system(order)

#...............................................................................
# (0) do the RSTsourcefiles/conf.py file exist ?
# (1) sphinx-build -b gettext RSTsourcefiles/ RSTsourcefiles/
# (2) msginit --no-translator --locale=fr_FR -i RSTsourcefiles/file.pot -o i18n/fr/file.po
#...............................................................................

#...............................................................................
# (0) do the RSTsourcefiles/conf.py file exist ?
#...............................................................................
if not os.path.exists( os.path.join(".", "RSTsourcefiles", "conf.py" )):
    print("Missing file : ", os.path.join(".", "RSTsourcefiles", "conf.py" ) )

else:

    #...........................................................................
    # (1) sphinx-build -b gettext RSTsourcefiles/ RSTsourcefiles/
    #...........................................................................
    system("rm -f RSTsourcefiles/*.pot")
    system("sphinx-build -b gettext RSTsourcefiles/ RSTsourcefiles/")

    #...........................................................................
    # (2) msginit --no-translator --locale=fr_FR -i RSTsourcefiles/file.pot -o i18n/fr/file.po
    #...........................................................................
    # LANGUAGES[directory's name] : locale's name
    LANGUAGES = {'fr' : 'fr_FR',
                 'en' : 'en_GB'}

    for data in os.walk( os.path.join(".", "RSTsourcefiles/" ) ):

        currentdir = data[0]
        filenames = data[2]

        if currentdir == "./RSTsourcefiles/":

            for filename in filenames:

                if filename[-4:] == '.rst':

                    # 'file.rst' -> 'file'
                    filename_without_extension = filename[:-4]
                    filename_pot = filename_without_extension + ".pot"

                    for language in LANGUAGES:

                        locale = LANGUAGES[language]
                        order = "msginit --no-translator " \
                                "--locale={0} " \
                                "-i RSTsourcefiles/{1} -o i18n/{2}/{3}.po".format(locale,
                                                                                  filename_pot,
                                                                                  language,
                                                                                  filename_without_extension)
                        system(order)

