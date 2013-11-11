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
    ❏DChars❏ : dchars/tests/orderedset_tests.py
"""

import unittest

from dchars.utilities.orderedset import OrderedSet

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).

################################################################################
class TESTOrderedSet(unittest.TestCase):
    """
        class TESTOrderedSet

        We test  dchars.orderedset::OrderedSet
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_len(self):
        """
                TESTOrderedSet.test_len
        """
        ordered_s = OrderedSet()
        self.assertEqual( len(ordered_s), 0 )

        ordered_s = OrderedSet( [1, 2,] )
        self.assertEqual( len(ordered_s), 2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_add(self):
        """
                TESTOrderedSet.test_add
        """
        ordered_s = OrderedSet( [4, 5, 6] )
        ordered_s.add( 9 )
        self.assertEqual( list(ordered_s), [4, 5, 6, 9] )
        ordered_s.add( 9 )
        self.assertEqual( list(ordered_s), [4, 5, 6, 9] )

    #///////////////////////////////////////////////////////////////////////////
    def test_discard(self):
        """
                TESTOrderedSet.test_discard
        """
        ordered_s = OrderedSet( [4, 5, 6] )
        ordered_s.discard( 5 )
        self.assertEqual( list(ordered_s), [4, 6] )

    #///////////////////////////////////////////////////////////////////////////
    def test_pop(self):
        """
                TESTOrderedSet.test_pop
        """
        ordered_s = OrderedSet( [4, 5, 6] )
        ordered_s.pop()
        self.assertEqual( list(ordered_s), [4, 5] )

        ordered_s = OrderedSet( [4, 5, 6] )
        ordered_s.pop(0)
        self.assertEqual( list(ordered_s), [5, 6] )

    #///////////////////////////////////////////////////////////////////////////
    def test_union(self):
        """
                TESTOrderedSet.test_union
        """
        ordered_s = OrderedSet( [4, 5, 6] )
        ordered_s.update( [6, 7, 8, 9, 10, 11] )
        self.assertEqual( list(ordered_s), [4, 5, 6, 7, 8, 9, 10, 11] )


