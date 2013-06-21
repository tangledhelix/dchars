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
        ❏DChars❏ make_devversion.py
"""
import os
from datetime import datetime
from dchars.system.numversion import VersionOfTheProgram
from getpass import getpass
import dchars.system.communia
import argparse

VERSION = VersionOfTheProgram().numversion

DATE = datetime.today().strftime("%Y-%m-%d_%Hh%Mm")
DESTFILENAME = "dchars_dev__v{0}__{1}.tar.gz".format( VERSION, DATE )
NAME_OF_THE_PROJECT = dchars.system.communia.OPTIONS["ascii_name_of_the_program"]

#///////////////////////////////////////////////////////////////////////////////
def command(cmd):
    """
        Display and execute the command <cmd>
    """
    print(cmd)
    os.system(cmd)

print("::make_devversion.py::", DESTFILENAME)

DEVVERSIONNAME = "devversion"+VERSION

command( "mkdir ../{0}/".format(DEVVERSIONNAME))
command( "cp -r * ../{0}/".format(DEVVERSIONNAME))
command( 'find ../{1}/ -name "*.gz" -exec rm {0} \\;'.format('{}',
                                                           DEVVERSIONNAME) )
command( 'find ../{1}/ -name "*~" -exec rm {0} \\;'.format('{}',
                                                         DEVVERSIONNAME) )
command( 'find ../{1}/ -name "*.pyc" -exec rm {0} \\;'.format('{}',
                                                            DEVVERSIONNAME) )
command( 'find ../{1}/ -name "*.doctree" -exec rm {0} \\;'.format('{}',
                                                                DEVVERSIONNAME) )

AUTDOC_PATH = "dchars/documentation/Sphinx/autodocumentation_for_modules/"

command( 'find ../{1}/{2} -name "..*" -exec rm {0} \\;'.format('{}',
                                                              DEVVERSIONNAME,
                                                              AUTDOC_PATH) )
command( "tar -czf {0} ../{1}/*".format(DESTFILENAME,
                                        DEVVERSIONNAME) )
command( "rm -rf ../{0}/".format(DEVVERSIONNAME) )

#...............................................................................
DESCRIPTION = "Use this file to create {0}'s developer's version".format(NAME_OF_THE_PROJECT)
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

#...............................................................................
# Upload ?
#...............................................................................
if ARGS.upload:

    from ftplib import FTP
    FTP = FTP("94.23.197.37")
    PASSWORD = getpass("FTP password : ")
    FTP.login(user='ftp', passwd=PASSWORD)
    print("... password ok... uploading...")
    FTP.cwd("/dchars/dev/")
    FTP.storbinary("STOR "+DESTFILENAME, open(DESTFILENAME,"rb"))
