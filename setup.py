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
        ❏DChars❏ setup.py
"""

from distutils.core import setup

setup(name='DChars',
      version='1.0',
      description="DChars (Detailed Characters) is a Python3 module aiming " + \
                  "to modify easily the diacritics signs of complex unicode " + \
                  "characters and to get their transliteration.",
      author='Xavier Faure(suizokukan)',
      author_email='(suizokukan _A.T_ orange•fr)',
      url='94.23.197.37/dchars/',
      packages=['dchars'],
     )
