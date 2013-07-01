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
        ❏DChars❏ pylint_tests.py
"""

import os
import re
from projects_files import get_all_filenames
from console import CONSOLE

CONSOLE.use_the_color("cyan")
CONSOLE.writeln("="*80)
CONSOLE.writeln("TEST : pylint_test.py")
CONSOLE.writeln("="*80)
CONSOLE.use_the_default_color()

COMMANDSTRING = "pylint --rcfile=pylint.rc {0} > z"

NBR_FILES = 0
WORST_MARK = 10

with open("pylint.ouput","w") as dest:

    for filename in get_all_filenames(only_py_files=True):

        if not os.path.exists(filename):
            raise Exception("Unknown file : "+str(filename))

        dest.write("="*80 + "\n")
        dest.write(filename + "\n")
        dest.write("="*80 + "\n")

        os.system(COMMANDSTRING.format(filename))

        try:
            with open("z","r") as src:
                pylintdata = src.read()
        except:
            CONSOLE.use_the_color("red")
            print("   >>> Problem by reading ", filename)
            CONSOLE.use_the_default_color()

        os.system("rm z")

        e = re.search("rated at\\s(?P<evaluation>[-|\\d|.]+)/10",  pylintdata)

        if e is None:
            CONSOLE.use_the_color("red")
            CONSOLE.writeln("problem with : ", filename)
            CONSOLE.use_the_default_color()
            evalution = 0
        else:
            evaluation = float(e.group('evaluation'))

        NBR_FILES += 1
        if evaluation < WORST_MARK:
            WORST_MARK = evaluation

        if evaluation == 10:
            CONSOLE.use_the_color("cyan")
            CONSOLE.writeln(filename, " : ", evaluation)
            CONSOLE.use_the_default_color()
        elif 9.5 <= evaluation < 10:
            CONSOLE.use_the_color("green")
            CONSOLE.writeln(filename, " : ", evaluation)
            CONSOLE.use_the_default_color()
        else:
            CONSOLE.use_the_color("red")
            CONSOLE.writeln(filename, " : ", evaluation)
            CONSOLE.use_the_default_color()

        # we add to the dest file the errors :
        # we read <pylintdata> until the line 'Report'.
        dest.write("\n")
        for line in pylintdata.split("\n"):

            if line == 'Report':
                break

            elif line.strip() != '':
                dest.write(line+"\n")
        dest.write("\n")

CONSOLE.use_the_color("cyan")
CONSOLE.writeln("-"*10)
CONSOLE.writeln("number of files analyzed : ", NBR_FILES)
CONSOLE.writeln("worst mark : ", WORST_MARK)
CONSOLE.writeln("-"*10)
CONSOLE.use_the_default_color()

CONSOLE.use_the_default_color()
