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
    ❏DChars❏ : dchars/tests/triggerlist.py
"""

import unittest

from dchars.utilities.triggerlist import TriggerList

# pylint: disable=R0904
# ("Too many public methods")
# Since this classes are derived from unittest.TestCase we have a lot of
# methods in the following classe(s).

################################################################################
class TESTTriggerList(unittest.TestCase):
    """
        class TESTTriggerList

        We test  dchars.system.triggerlist::TriggerList
    """

    #///////////////////////////////////////////////////////////////////////////
    def test_0(self):
        """
                TESTTriggerList.test_0

                We verify that a TriggerList object has the same behavior as a list.
        """
        triggerlist1 = TriggerList()
        triggerlist2 = list()

        self.assertEqual(triggerlist1, triggerlist2)

    #///////////////////////////////////////////////////////////////////////////
    def test_1(self):
        """
                TESTTriggerList.test_1

                We verify that a TriggerList object has the same behavior as a list.
        """
        triggerlist1 = TriggerList( [1, 3, 2], None )
        triggerlist2 = list( [1, 3, 2] )

        triggerlist1 += [-1,]
        triggerlist2 += [-1,]
        self.assertEqual( triggerlist1, triggerlist2 )

        res1 = triggerlist1.append( 4 )
        res2 = triggerlist2.append( 4 )
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.reverse()
        res2 = triggerlist2.reverse()
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.sort()
        res2 = triggerlist2.sort()
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.extend( [-5,] )
        res2 = triggerlist2.extend( [-5,] )
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.pop()
        res2 = triggerlist2.pop()
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.insert(0, -99)
        res2 = triggerlist2.insert(0, -99)
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.remove(3)
        res2 = triggerlist2.remove(3)
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        res1 = triggerlist1.clear()
        res2 = triggerlist2.clear()
        self.assertEqual( triggerlist1, triggerlist2 )
        self.assertEqual( res1, res2 )

        triggerlist1 += [-1,]
        triggerlist2 += [-1,]
        self.assertEqual( triggerlist1, triggerlist2 )

        triggerlist1[0] = -99
        triggerlist2[0] = -99
        self.assertEqual( triggerlist1, triggerlist2 )

        del(triggerlist1[0])
        del(triggerlist2[0])
        self.assertEqual( triggerlist1, triggerlist2 )

    #///////////////////////////////////////////////////////////////////////////
    def test_2(self):
        """
                TESTTriggerList.test_2

                We verify that a TriggerList object calls the alert function every time
                the object is modified.
        """

        self.counter = 0

        #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        def alert():
            """
                We simply count the number of calls to this function.
            """
            self.counter += 1

        triggerlist = TriggerList( [1, 3, 2], alert )
        triggerlist += [-1,]
        triggerlist.append( 4 )
        triggerlist.reverse()
        triggerlist.sort()
        triggerlist.extend( [-5,] )
        triggerlist.pop()
        triggerlist.insert(0, -99)
        triggerlist.remove(3)
        triggerlist.clear()
        triggerlist += [-1,]
        triggerlist[0] = -99
        del(triggerlist[0])

        self.assertEqual( self.counter, 13 )

