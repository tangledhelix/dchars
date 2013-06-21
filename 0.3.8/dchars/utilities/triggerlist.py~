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
        ❏DChars❏ : system/triggerlist.py

        list with an alert if something is modified.

        This class is a wrapper around a list. When the list is modified, a
        function is called. The function is called when the list is created.

        * classe TriggerList
"""

################################################################################
class TriggerList(list):
    """
        class TriggerList : list with a trigger function.
    """

    #///////////////////////////////////////////////////////////////////////////
    def __add__(self, value):
        """
                TriggerList.__add__
        """
        res = list.__add__(self, value)
        self.call_the_alert_function()
        return res

    #///////////////////////////////////////////////////////////////////////////
    def __delitem__(self, i):
        """
                TriggerList.__delitem__
        """
        list.__delitem__(self, i)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def __eq__(self, aliud):
        """
                TriggerList.__eq__
        """
        return list.__eq__(self, aliud)

    #///////////////////////////////////////////////////////////////////////////
    def __iadd__(self, value):
        """
                TriggerList.__iadd__
        """
        list.__iadd__(self, value)
        self.call_the_alert_function()
        return self

    #///////////////////////////////////////////////////////////////////////////
    def __init__(self,
                 iterable=None,
                 alert_function=None):
        """
                TriggerList.__init__
        """
        # use self.alert_off/_on() to modify this attribute :
        self.ignore_alert = False

        self.alert_function = alert_function

        if iterable is not None:
            list.__init__(self, iterable)

        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def __setitem__(self, i, value):
        """
                TriggerList.__setitem__
        """
        list.__setitem__(self, i, value)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def alert_off(self):
        """
                TriggerList.alert_off
        """
        self.ignore_alert = True

    #///////////////////////////////////////////////////////////////////////////
    def alert_on(self):
        """
                TriggerList.alert_on
        """
        self.ignore_alert = False

    #///////////////////////////////////////////////////////////////////////////
    def append(self, value):
        """
                TriggerList.append
        """
        list.append(self, value)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def call_the_alert_function(self):
        """
                TriggerList.alert

                This function calls the alert function; its lenghty named was
                choosed so that derived class from TriggerList will not be
                choose such the same name for their alert function.
        """
        if self.alert_function is not None and not self.ignore_alert:
            self.alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def clear(self):
        """
                TriggerList.clear
        """

        # Something weird with Pylint : class 'list' DO have a "clear" member...
        # pylint: disable=E1101
        # -> "class 'list has no 'clear' member"
        list.clear(self)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def extend(self, iterable):
        """
                TriggerList.extend
        """
        list.extend(self, iterable)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def insert(self, index, value):
        """
                TriggerList.insert
        """
        list.insert(self, index, value)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def pop(self, i=-1):
        """
                TriggerList.pop
        """
        res = list.pop(self, i)
        self.call_the_alert_function()
        return res

    #///////////////////////////////////////////////////////////////////////////
    def remove(self, value):
        """
                TriggerList.remove
        """
        list.remove(self, value)
        self.call_the_alert_function()
        return None

    #///////////////////////////////////////////////////////////////////////////
    def reverse(self):
        """
                TriggerList.reverse
        """
        list.reverse(self)
        self.call_the_alert_function()

    #///////////////////////////////////////////////////////////////////////////
    def sort(self, argkey=None, argreverse=False):
        """
                TriggerList.sort
        """
        list.sort(self, key=argkey, reverse=argreverse)
        self.call_the_alert_function()
