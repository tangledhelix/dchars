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
        ❏DChars❏ projects_files.py
"""

import os

# MODULES[directory.subdirectory] = ( (name, only_for_dev_version), )
MODULES = {

          # CAVEAT : must be ".", not "" :
          "."                   : ( ("console.py", True),
                                    ("bod__create_buffers.py", True),
                                    ("create_documentation.py", True),
                                    ("header_please_test.py", True),
                                    ("header_template.txt", True),
                                    ("projects_files.py", True),
                                    ("pylint.rc", True),
                                    ("pylint_tests.py", True),
                                    ("setup.py", False),
                                    ("sort.py", False),
                                  ),

         "dchars"              : ( ("__init__.py", False),
                                   ("config.ini", False),
                                   ("dcharacter.py", False),
                                   ("dchars.py", False),
                                   ("dstring.py", False),
                                   ("languages_name.py", False),
                                   ("successivetransformations.py", False),
                                  ),

         "dchars.errors"        : ( ("__init__.py", False),
                                    ("errors.py", False),
                                  ),

         "dchars.languages"     : ( ("__init__.py", False),
                                  ),

         "dchars.languages.bod" : ( ("__init__.py", False),
                                    ("buffer.py", False),
                                    ("buffer_str.data", False),
                                    ("dcharacter.py", False),
                                    ("dstring.py", False),
                                    ("internalstructure.py", False),
                                    ("sorting_methods_tables.py", False),
                                    ("syllabic_structure.py", False),
                                    ("symbols.py", False),
                                  ),

         "dchars.languages.bod.transliterations" : ( ("__init__.py", False),

                                                     ("bodsan.py", False),
                                                     ("bodsan_symbols.py", False),
                                                     ("ewts_buffer.py", False),

                                                     ("ewts.py", False),
                                                     ("ewts_buffer_trans_str.data", False),
                                                     ("ewts_symbols.py", False),
                                                     ("ewts_words.txt", False),
                                  ),

         "dchars.languages.grc" : ( ("__init__.py", False),
                                    ("dcharacter.py", False),
                                    ("dstring.py", False),
                                    ("symbols.py", False),
                                  ),

         "dchars.languages.grc.transliterations" : ( ("__init__.py", False),
                                                     ("betacode.py", False),
                                                     ("gutenberg.py", False),
                                                     ("basic.py", False),
                                                     ("perseus.py", False),
                                  ),

         "dchars.languages.hbo" : ( ("__init__.py", False),
                                    ("dcharacter.py", False),
                                    ("dstring.py", False),
                                    ("symbols.py", False),
                                  ),

         "dchars.languages.hbo.transliterations" : ( ("__init__.py", False),
                                                     ("basic.py", False),
                                  ),

         "dchars.languages.lat" : ( ("__init__.py", False),
                                    ("dcharacter.py", False),
                                    ("dstring.py", False),
                                    ("symbols.py", False),
                                  ),

         "dchars.languages.lat.transliterations" : ( ("__init__.py", False),
                                                     ("basic.py", False),
                                  ),

         "dchars.languages.san" : ( ("__init__.py", False),
                                    ("dcharacter.py", False),
                                    ("dstring.py", False),
                                    ("symbols.py", False),
                                  ),

         "dchars.languages.san.transliterations" : ( ("__init__.py", False),
                                                     ("iso15919.py", False),
                                                     ("itrans.py", False),
                                  ),

         "dchars.symbols" : ( ("__init__.py", False),
                              ("symbols.py", False),
                                  ),

         "dchars.tests"          : ( ("__init__.py", False),
                                     ("alphabetical_weight_tests.py", False),
                                     ("dicttools_tests.py", False),
                                     ("orderedset_tests.py", False),
                                     ("sortingvalue_tests.py", False),
                                  ),

         "dchars.tests.languages": ( ("__init__.py", False),
                                  ),

         "dchars.tests.languages.bod": ( ("__init__.py", False),
                                         ("bod_tests.py", False),
                                         ("words.shuffled", False),
                                         ("words.sorted", False),
                                       ),

         "dchars.tests.languages.bod.transliterations": ( ("__init__.py", False),
                                                          ("bodsan_tests.py", False),
                                                          ("ewts_tests.py", False),
                                                          ("ewts_words", False),
                                                        ),

         "dchars.tests.languages.grc": ( ("__init__.py", False),
                                         ("grc_tests.py", False),
                                         ("text001_Lucian_Dialogues_of_the_Gods.txt", False),
                                         ("text002_Iliad_I_v1_205.txt", False),
                                         ("text003_Euripides_Bacchae_1_104.txt", False),
                                       ),

         "dchars.tests.languages.grc.transliterations": ( ("__init__.py", False),
                                                          ("betacode_tests.py", False),
                                                          ("basic_tests.py", False),
                                                          ("gutenberg_tests.py", False),
                                                          ("perseus_tests.py", False),
                                                        ),

         "dchars.tests.languages.hbo": ( ("__init__.py", False),
                                         ("hbo_tests.py", False),
                                         ("text001_Genesis_I.txt", False),
                                         ("text002_Psalms_18.txt", False),
                                         ("text003_Jonah_I.txt", False),
                                       ),

         "dchars.tests.languages.hbo.transliterations": ( ("__init__.py", False),
                                                          ("basic_tests.py", False),
                                                        ),

         "dchars.tests.languages.lat": ( ("__init__.py", False),
                                         ("lat_tests.py", False),
                                         ("text001_Cicero_In_Pisonem.txt", False),
                                         ("text002_Virgil_Aeneid_I.txt", False),
                                         ("text003_Cicero_In_Catilinam_I.txt", False),
                                       ),

         "dchars.tests.languages.lat.transliterations": ( ("__init__.py", False),
                                                          ("basic_tests.py", False),
                                                        ),

         "dchars.tests.languages.san": ( ("__init__.py", False),
                                         ("san_tests.py", False),
                                         ("text001_Rigveda_1.txt", False),
                                         ("text002_Mahabharata_I_1.txt", False),
                                         ("text003_rigveda_samhita__1_10.txt", False),
                                         ("text003_rigveda_samhita__1_10.itrans.txt", False),
                                       ),

         "dchars.tests.languages.san.transliterations": ( ("__init__.py", False),
                                                          ("iso15919_tests.py", False),
                                                          ("itrans_tests.py", False),
                                                        ),



         "dchars.system"       : ( ("__init__.py", False),
                                   ("communia.py", False),
                                   ("numversion", False),
                                   ("numversion.py", False),
                                  ),

         "dchars.utilities"    : ( ("__init__.py", False),
                                   ("dicttools.py", False),
                                   ("lstringtools.py", False),
                                   ("name2symbols.py", False),
                                   ("orderedset.py", False),
                                   ("regexstring.py", False),
                                   ("sortingvalue.py", False),
                                 )
}

#///////////////////////////////////////////////////////////////////////////////
def get_all_filenames(only_py_files = False, only_user_version = False):
    """
        Yield all filenames.

        Produce strings like "directory/subdirectory/filename" on a Linux-based
        system.
    """

    for module in MODULES:
        for element in MODULES[module]:

            fname = element[0]
            only_for_devversion = element[1]

            path = module.split(".")
            path.append(fname)
            finalpath = os.path.join(*path)

            if not os.path.exists(finalpath):
                raise Exception("Unknown file : '"+str(finalpath)+"'")

            ok_for_this_file = True
            if only_py_files and not fname[-3:] == '.py':
                ok_for_this_file = False

            if only_user_version:
                ok_for_this_file = ok_for_this_file and not only_for_devversion

            if ok_for_this_file:
                yield os.path.join(finalpath)

#///////////////////////////////////////////////////////////////////////////////
def get_paths_and_modules__user(only_py_files=False):
    """
        Return a dictionary like { "directory.subdirectory" : [ 'file1.py', ] }

        Does not take in account the files markes as "only for the dev version"
    """

    resdict = dict()

    for module in MODULES:

        resdict[module] = []
        for element in MODULES[module]:

            fname = element[0]
            only_for_devversion = element[1]

            if not only_for_devversion:

                if only_py_files:
                    if fname[-3:] == '.py':
                        resdict[module].append( fname )
                else:
                    resdict[module].append( fname )

    return resdict

################################################################################
################################################################################
if __name__ == "__main__":

    from console import CONSOLE

    CONSOLE.use_the_color("cyan")
    CONSOLE.writeln("="*80)
    CONSOLE.writeln("TEST : projects_files.py")

    #...........................................................................
    # existing files not in MODULES dictionary
    #...........................................................................
    CONSOLE.writeln("="*80)
    CONSOLE.writeln("TEST : existing files not in MODULES dictionary :")
    CONSOLE.use_the_default_color()

    for res in os.walk("."):

        dirpath = res[0]
        #dirnames
        filenames = res[2]

        for filename in filenames:
            if filename[-1] != "~" and filename[-4:] != ".pyc" and filename[-4:] != ".rst":

                dirname = dirpath[:]
                dirname = dirname.replace("./", "")
                dirname = dirname.replace("/", ".")

                if dirname not in MODULES:
                    CONSOLE.use_the_color("red")
                    CONSOLE.writeln("missing directory : ", dirname)
                    CONSOLE.use_the_default_color()
                else:
                    files = [filename for filename, only_for_dev_version in MODULES[dirname]]

                    if filename not in files:
                        CONSOLE.use_the_color("white")
                        CONSOLE.writeln("missing file : ", os.path.join(dirpath, filename))
                        CONSOLE.use_the_default_color()

    #...........................................................................
    # files in MODULES dictionary that doesn't exist :
    #...........................................................................

    CONSOLE.use_the_color("cyan")
    CONSOLE.writeln("files in MODULES dictionary that doesn't exist :")
    CONSOLE.use_the_color("cyan")

    for dirpath in MODULES:
        for filename, only_for_dev_version in MODULES[dirpath]:

            if dirpath[0] == '.':
                dirname = dirpath[1:].replace(".","/")
            else:
                dirname = dirpath.replace(".","/")

            fullname = os.path.join(dirname, filename)
            if not os.path.exists( fullname ):
                CONSOLE.use_the_color("white")
                CONSOLE.writeln("this file doesn't exist: ", fullname)
                CONSOLE.use_the_default_color()

    CONSOLE.use_the_default_color()
