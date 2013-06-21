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
        ❏DChars❏ create_documentation.py

        This script builds the Sphinx documentation in several languages.
"""

import os
import argparse
from getpass import getpass
from datetime import datetime

from dchars.system import numversion as numversion
import dchars.system.communia
from projects_files import get_paths_and_modules__user, get_all_filenames

NAME_OF_THE_PROJECT = dchars.system.communia.OPTIONS["ascii_name_of_the_program"]

VERSION = numversion.VersionOfTheProgram().numversion

with open( os.path.join("dchars",
                        "documentation",
                        "Sphinx",
                        "RSTconf_template.txt"), 'rt') as RSTconf__template__file:
    TEMPLATE__CONF = RSTconf__template__file.read()

with open( os.path.join("dchars",
                        "documentation",
                        "Sphinx",
                        "RST_template.txt"), 'rt') as RST__template__file:
    TEMPLATE__RST = RST__template__file.read()

#///////////////////////////////////////////////////////////////////////////////
def command(strcmd):
    """
        Command (system) call : print and execute the command <strcmd>.
    """
    print(">>> "+strcmd)
    return os.system(strcmd)

#///////////////////////////////////////////////////////////////////////////////
def send_documentation_targzfile():
    """
        fonction send_documentation_targzfile()
    """
    print("_"*30, "send_documentation_targzfile")

    date = datetime.today().strftime("%Y-%m-%d_%Hh%Mm")
    destfilename = "dchars_doc__v{0}__{1}.tar.gz".format( VERSION, date )

    command( "tar -czf {0} doc/".format(destfilename) )

    from ftplib import FTP
    ftp = FTP("94.23.197.37")
    password = getpass("FTP password : ")
    ftp.login(user='ftp', passwd=password)
    print("... password ok... uploading...")
    ftp.cwd("/dchars/")
    ftp.storbinary("STOR "+destfilename, open(destfilename,"rb"))

#///////////////////////////////////////////////////////////////////////////////
def create_the_rst_sourcefiles(dest, modules):
    """
        fonction used by create_the_rst_files()

        * dest          : (str) path
        * modules       : (dict) module["module1"] = [ "file1.py", "file2.py", ... ]
    """
    # We create the source_code.rst file :
    source_code_rst_namefile = os.path.join( ".", dest, "source_code.rst" )
    with open( source_code_rst_namefile, "w" ) as source_code_rst_file:

        source_code_rst_file.write( "=================\n" )
        source_code_rst_file.write( "SOURCE_CODE_TITLE\n" )
        source_code_rst_file.write( "=================\n" )
        source_code_rst_file.write( "\n" )

        # we sort <modules> :
        keys = list(modules.keys())
        keys.sort()

        sorted_modules = []
        for key in keys:
            sorted_modules.append( (key, modules[key] ) )
            sorted_modules[-1][1].sort()     # we sort  modules[key]

        for _path, modules in sorted_modules:
            # _path : "directory.subdirectory"
            # modules : ["file1.py", "file2.py"]

            if _path == "":
                path = "(root directory)"
            else:
                path = _path

            if len(modules)>0:

                source_code_rst_file.write( "-"*80+"\n" )
                source_code_rst_file.write( "{0}\n".format(path) )
                source_code_rst_file.write( "-"*80+"\n" )

                source_code_rst_file.write( "\n" )
                source_code_rst_file.write( ".. toctree::\n" )
                source_code_rst_file.write( "   :maxdepth: 2\n" )
                source_code_rst_file.write( "\n" )

                for module in modules:
                    # module : "myfile.py"

                    # "./dest/dir1.dir2.something.rst" :
                    rst_filename__os = os.path.join( dest, path + "." + module[:-3]+".rst" )

                    # "dir1.dir2.something" :
                    rst_filename__sphinx = path+"."+module[:-3]

                    # "directory1/subdirectory" :
                    path_os = os.path.join( *path.split(".") )

                    with open( rst_filename__os, "w" ) as rst_file:
                        rst_file.write( TEMPLATE__RST.format(rst_filename__sphinx,
                                                             "../../../../"+path_os+"/"+module)
                            )

                        source_code_rst_file.write( "   {0}.{1}\n".format(path, module[:-3]) )

            source_code_rst_file.write( "\n" )

    print(".rst files created for the following modules : "+str(sorted_modules))

#///////////////////////////////////////////////////////////////////////////////
def create_index_file():
    """
        Create the index.rst file in dchars/documentation/Sphinx/RSTsourcefiles/
    """
    print("_"*30, "create_index_file", USERVERSION_FILENAME)

    template = """.. |br| raw:: html

   <br />

===========
INDEX_TITLE
===========

.. image:: images/english_flag_100x50.png
   :alt: English flag
   :width: 50px
   :target: ../../doc/en/index.html

.. image:: images/french_flag_100x50.png
   :alt: French flag
   :width: 50px
   :target: ../../doc/fr/index.html

$INDEX_INTRODUCTION$

----

Download last version :

`► {0} <{1}>`_

If interested, take a look at the developper's directory (`► dev <../../dev/>`_) or at the overall UML diagram (`► UML <{2}>`_).

----

.. toctree::
   :maxdepth: 2

   howto_install
   howto_use
   development
   supported_languages

----

.. toctree::
   :maxdepth: 1

   license
   source_code

    """

    with open("dchars/documentation/Sphinx/RSTsourcefiles/index.rst","w") as dest:

        userversion_full_name = os.path.join( "../../doc/userversion/",
                                              USERVERSION_FILENAME )

        dest.write( template.format(USERVERSION_FILENAME,
                                    userversion_full_name,
                                    UMLIMAGE_FILENAME) )

#///////////////////////////////////////////////////////////////////////////////
def make_user_version():
    """
        Create the user .tar.gz file in doc/

        Return the name of the file.
    """
    print("_"*30, "make_user_version")

    destfilename = "dchars_v{0}.tar.gz".format( VERSION )

    # (1) we create the temp_userversion/ directory :
    if os.path.exists("temp_userversion/"):
        command( "rm -rf temp_userversion/" )

    command( "mkdir temp_userversion/" )

    # (2) we copy the files in temp_userversion/ :
    for filename in get_all_filenames(only_py_files = False, only_user_version = True):
        command( "cp --parents {0} temp_userversion/".format(filename) )

    # (3) we delete some files in temp_userversion/ :
    command( 'find {1} -name "*.gz" -exec rm {0} \\;'.format('{}',
                                                             "temp_userversion/") )

    command( 'find {1} -name "*~" -exec rm {0} \\;'.format('{}',
                                                             "temp_userversion/") )

    command( 'find {1} -name "*.pyc" -exec rm {0} \\;'.format('{}',
                                                             "temp_userversion/") )

    command( 'find {1} -name "*.doctree" -exec rm {0} \\;'.format('{}',
                                                             "temp_userversion/") )

    # (4) we create the archive :
    os.chdir("temp_userversion/")
    command( "tar -czf {0} .".format(destfilename) )
    command( "mv {0} ..".format(destfilename) )

    # (5) we move the file to doc/userversion :
    os.chdir("..")
    command( "mkdir doc/userversion/" )
    command( "mv {0} doc/userversion/".format(destfilename))

    # (6) we erase the  temp_userversion/ directory :
    command( "rm -rf temp_userversion/" )


    return destfilename

#///////////////////////////////////////////////////////////////////////////////
def create_uml_image():
    """
        function create_uml_image

        Create an UML image of all classes.

        Return the name of the file.
    """
    print("_"*30, "create_uml_image")
    command("pyreverse2 --ignore tests --project=dchars -A --output=dot dchars/")
    command("dot -Tbmp classes_dchars.dot -o doc/classes_dchars.bmp")
    command("convert doc/classes_dchars.bmp doc/classes_dchars.png")
    command("rm doc/classes_dchars.bmp")
    command("rm classes_dchars.dot")
    command("rm packages_dchars.dot")

    return "../classes_dchars.png"

################################################################################
################################ STARTING POINT ################################
################################################################################
LANGUAGES = ('fr', 'en')
#
# (1) WARM-UP
# (1.1) command line's options
# (1.2) does the path to the builded html documentation exists ?
# (1.3) we clean the final directory
#
# (2) .rst files and others files
# (2.1) we create the user version
# (2.2) we create an UML image of all classes
# (2.3) we create a .rst file for each .py files
# (2.4) we create the file 'index.rst"
#
# (3) main loop, for each language
# (4) we send the documentation to the server

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (1) WARM-UP
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (1.1) command line's options
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
DESCRIPTION = "Use this file to create {0}'s documentation".format(NAME_OF_THE_PROJECT)
EPILOG = "{0}'s author : Suizokukan (suizokukan _A.T_ orange DOT fr)".format(NAME_OF_THE_PROJECT)
PARSER = argparse.ArgumentParser(description=DESCRIPTION,
                                 epilog=EPILOG,
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                 )

PARSER.add_argument('--upload',
                    action="store_true",
                    help="upload the documentation",
                    default = False)

ARGS = PARSER.parse_args()

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (1.2) does the path to the builded html documentation exists ?
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
if not os.path.exists("doc"):
    command("mkdir doc")

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (1.3) we clean the final directory
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
command("rm -rf doc/*")

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (2) .rst files and others files
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (2.1) we create the user version
USERVERSION_FILENAME = make_user_version()
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (2.2) we create an UML image of all classes
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
UMLIMAGE_FILENAME = create_uml_image()

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (2.3) we create a .rst file for each .py files
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
command("rm -rf dchars/documentation/Sphinx/autodocumentation_for_modules/*")
create_the_rst_sourcefiles( dest = "./dchars/documentation/Sphinx/autodocumentation_for_modules/",
                            modules = get_paths_and_modules__user(only_py_files=True) )

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (2.4) we create the file 'index.rst"
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
create_index_file()

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (3) main loop, for each language
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
for lang_name in LANGUAGES:

    print("////////////////////////////")
    print("We add a new language : "+lang_name)
    print("////////////////////////////")

    # (0) We prepare the "cauldron" directory (dchars/documentation/Sphinx/cauldron/) :
    command("rm -rf dchars/documentation/Sphinx/cauldron/*")

    path_to_RSTsrcfiles = "dchars/documentation/Sphinx/RSTsourcefiles/*.rst"
    command("cp {0} dchars/documentation/Sphinx/cauldron".format(path_to_RSTsrcfiles))

    command("cp -r dchars/documentation/Sphinx/images dchars/documentation/Sphinx/cauldron/")
    command("cp -r dchars/documentation/Sphinx/_static dchars/documentation/Sphinx/cauldron/")
    command("cp -r dchars/documentation/Sphinx/_templates dchars/documentation/Sphinx/cauldron/")
    path_autodoc = "dchars/documentation/Sphinx/autodocumentation_for_modules/*.rst"
    command("cp {0} dchars/documentation/Sphinx/cauldron/".format(path_autodoc))

    # (1) we touch all .rst file :
	# In order to rebuild ALL the files we have to artificially "update" them :
	# Without this line sphinx-build will not build the files whose
	# translation has been changed.
    command("""find dchars/documentation/Sphinx/cauldron/ -name "*.rst" | xargs -ri touch {}""")

    # (2) .po -> .mo
    command("rm -f dchars/documentation/Sphinx/i18n/{0}/LC_MESSAGES/*".format(lang_name))

    cmd =  'find dchars/documentation/Sphinx/i18n/{0} -maxdepth 1 -name "*.po"'.format(lang_name)
    cmd += " | sed 's/\\.po$//' "
    cmd += " | xargs -ri msgfmt --check --verbose {}.po -o {}.mo"
    command(cmd)

    command("mv dchars/documentation/Sphinx/i18n/{0}/*.mo ".format(lang_name)+ \
            "dchars/documentation/Sphinx/i18n/{0}/LC_MESSAGES/".format(lang_name))

    # and we add the i18n/ directory into the cauldron directory :
    command("cp -rf dchars/documentation/Sphinx/i18n dchars/documentation/Sphinx/cauldron")

    # (3) creation of the conf.py file :
    with open("dchars/documentation/Sphinx/cauldron/conf.py","w") as conf_py:
        conf_py.write(TEMPLATE__CONF.format("{}",
											lang_name,
                                            NAME_OF_THE_PROJECT,
                                            VERSION,
                                            VERSION))

    # (4) sphinx-build : creation of the html output :
    dest_path = os.path.join("doc/", lang_name)
    command("mkdir {0}".format(dest_path))

    sphinx_cmd = "sphinx-build -a -b html "
    cauldron = "dchars/documentation/Sphinx/cauldron"
    command("{0} {1} {2}".format(sphinx_cmd,
                                 cauldron,
                                 dest_path))

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
# (4) we send the documentation to the server
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
if ARGS.upload:
    send_documentation_targzfile()
