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
    ❏DChars❏ : dchars/languages/bod/transliterations/ewts_create_buffers.py
"""

import pickle
from dchars.dchars import new_dstring
from dchars.languages.bod.transliterations.ewts import EWTS_BUFFER__FROM_TRANS_STR, \
                                                       EWTS_BUFFER__FROM_STR
DSTRING_BOD_buff = new_dstring(language="བོད་ཡིག",
                               transliteration_method='ewts',
                               options = {"expected structure"  : "Tibetan or Sanskrit",
                                          "use the buffers"     : False,
                                          "fill the buffers"    : True},
                              )

with open("buffering_ewts_words") as src:
    for _ewts in src.readlines():
        ewts = _ewts[:-1]
        bod = DSTRING_BOD_buff().init_from_transliteration(ewts)
        DSTRING_BOD_buff( str(bod) )

print(len(EWTS_BUFFER__FROM_STR))
print(len(EWTS_BUFFER__FROM_TRANS_STR))
print(len(pickle.dumps(EWTS_BUFFER__FROM_STR)))
print(len(pickle.dumps(EWTS_BUFFER__FROM_TRANS_STR)))

with open("ewts_buffer_str.data", "wb") as dest:
    dest.write( pickle.dumps(EWTS_BUFFER__FROM_STR) )

with open("ewts_buffer_trans_str.data", "wb") as dest:
    dest.write( pickle.dumps(EWTS_BUFFER__FROM_TRANS_STR) )
