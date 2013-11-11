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
    ❏DChars❏ : dchars/tests/sortingvalue_tests.py
"""

import unittest

from dchars.utilities.sortingvalue import SortingValue

################################################################################
class TESTSortingValue(unittest.TestCase):
    """
        class TESTSortingValue

        We test dchars/sortingvalue.py
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_unit(self):
        """
                TESTSortingValue.test_unit
        """

        #.......................................................................
        unit1 = SortingValue( [1, 2, 3] )
        unit2 = SortingValue( [1, 2, 3] )

        self.assertTrue( unit1 == unit2 )
        self.assertFalse( unit1 < unit2 )
        self.assertFalse( unit1 > unit2 )

        #.......................................................................
        unit1 = SortingValue( [1, 2] )
        unit2 = SortingValue( [1, 2, 3] )

        self.assertFalse( unit1 == unit2 )
        self.assertTrue( unit1 < unit2 )
        self.assertFalse( unit1 > unit2 )

        #.......................................................................
        unit1 = SortingValue( [] )
        unit2 = SortingValue( [1,] )

        self.assertFalse( unit1 == unit2 )
        self.assertTrue( unit1 < unit2 )
        self.assertFalse( unit1 > unit2 )

        #.......................................................................
        unit1 = SortingValue( [1, 2, 3] )
        unit2 = SortingValue( [99,] )

        self.assertFalse( unit1 == unit2 )
        self.assertTrue( unit1 < unit2 )
        self.assertFalse( unit1 > unit2 )

        #.......................................................................
        unit1 = SortingValue( [1, 2, 3] )
        unit2 = SortingValue( [99, 100, 101, 102] )

        self.assertFalse( unit1 == unit2 )
        self.assertTrue( unit1 < unit2 )
        self.assertFalse( unit1 > unit2 )


    #///////////////////////////////////////////////////////////////////////////
    def test_main(self):
        """
                TESTSortingValue.test_main
        """

        #.......................................................................
        alphaw1 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )], )
        alphaw2 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )], )

        self.assertTrue( alphaw1 == alphaw2 )
        self.assertFalse( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

        #.......................................................................
        alphaw1 = list( [SortingValue( [1,] ),
                         SortingValue( [1, 2, 3] )], )
        alphaw2 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )], )

        self.assertFalse( alphaw1 == alphaw2 )
        self.assertTrue( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

        #.......................................................................
        alphaw1 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )], )
        alphaw2 = list( [SortingValue( [99,] ),
                         SortingValue( [1, 2, 3] )], )

        self.assertFalse( alphaw1 == alphaw2 )
        self.assertTrue( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

        #.......................................................................
        alphaw1 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )], )
        alphaw2 = list( [SortingValue( [99, 100, 101, 102] ),
                         SortingValue( [1, 2, 3] )], )

        self.assertFalse( alphaw1 == alphaw2 )
        self.assertTrue( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

        #.......................................................................
        alphaw1 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 2] )]),
        alphaw2 = list( [SortingValue( [1, 2, 3] ),
                         SortingValue( [1, 2, 3] )]),

        self.assertFalse( alphaw1 == alphaw2 )
        self.assertTrue( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

        #.......................................................................
        alphaw1 = list( [SortingValue( [] ) ])
        alphaw2 = list( [SortingValue( [1,] ),])

        self.assertFalse( alphaw1 == alphaw2 )
        self.assertTrue( alphaw1 < alphaw2 )
        self.assertFalse( alphaw1 > alphaw2 )

