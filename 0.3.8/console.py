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
        ❏DChars❏ console.py

        * class Console and its unique instance, <CONSOLE>
"""

from sys import stdout

#-------------------------------------------------------------------------------
def console_write(*msg):
    """
        function console_write

        write <*msg> to stdout
    """
    string = ""
    for element in msg:
        string += str(element)

    stdout.write(string)

################################################################################
class Console(object):
    """
        class Console, for Unix-like terminals
    """

    #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    def use_the_color(self, name_of_the_color):
        """
                Console.use_the_color
        """
        colors_and_code = {
                            "red"           : chr(0x1B)+"[0;31;1m",
                            "green"         : chr(0x1B)+"[0;32;1m",
                            "yellow"        : chr(0x1B)+"[0;33;1m",
                            "blue"          : chr(0x1B)+"[0;34;1m",
                            "magenta"       : chr(0x1B)+"[0;35;1m",
                            "cyan"          : chr(0x1B)+"[0;36;1m",
                            "white"         : chr(0x1B)+"[0;37;1m",
                          }

        self.write( colors_and_code[name_of_the_color] )

    #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    def use_the_default_color(self):
        """
                Console.use_the_default_color
        """
        self.write( chr(0x1B)+"[0m" )

    #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    def writeln(self, *msg):
        """
                Console.writeln
        """
        self.write( *msg )
        self.write( '\n' )

    #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    def write(self, *msg):
        """
                Console.write
        """
        console_write(*msg)

CONSOLE = Console()
