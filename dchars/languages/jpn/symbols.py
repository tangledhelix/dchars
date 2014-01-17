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
    ❏DChars❏ : dchars/languages/jpn/symbols.py
"""

# problem with Pylint :
# pylint: disable=E0611
# many errors like "No name 'extensions' in module 'dchars'"
from dchars.utilities.name2symbols import Name2Symbols
from dchars.utilities.dicttools import invertdict

#...............................................................................
# symbols used by Japanese :
#
# CAVEAT ! If you modify these dictionaries, don't forget to modify their
# corresponding transliteration's dictionaries !
#
#...............................................................................

# "ー" (the chōonpu 長音符 symbol)
# confer http://en.wikipedia.org/wiki/Ch%C5%8Donpu
SYMB_CHOONPU = Name2Symbols(
    {
      'ー'      : ('ー',),
    })

SYMB_HIRAGANA = Name2Symbols(
    {
      'あ'        : ('あ',),
      'い'        : ('い',),
      'う'        : ('う',),
      'え'        : ('え',),
      'お'        : ('お',),
      'か'        : ('か',),
      'き'        : ('き',),
      'く'        : ('く',),
      'け'        : ('け',),
      'こ'        : ('こ',),
      'さ'        : ('さ',),
      'し'        : ('し',),
      'す'        : ('す',),
      'せ'        : ('せ',),
      'そ'        : ('そ',),
      'た'        : ('た',),
      'ち'        : ('ち',),
      'つ'        : ('つ',),
      'て'        : ('て',),
      'と'        : ('と',),
      'な'        : ('な',),
      'に'        : ('に',),
      'ぬ'        : ('ぬ',),
      'ね'        : ('ね',),
      'の'        : ('の',),
      'は'        : ('は',),
      'ひ'        : ('ひ',),
      'ふ'        : ('ふ',),
      'へ'        : ('へ',),
      'ほ'        : ('ほ',),
      'ま'        : ('ま',),
      'み'        : ('み',),
      'む'        : ('む',),
      'め'        : ('め',),
      'も'        : ('も',),
      'や'        : ('や',),
      'ゆ'        : ('ゆ',),
      'よ'        : ('よ',),
      'ら'        : ('ら',),
      'り'        : ('り',),
      'る'        : ('る',),
      'れ'        : ('れ',),
      'ろ'        : ('ろ',),
      'わ'        : ('わ',),
      'ゐ'        : ('ゐ',),
      'ゑ'        : ('ゑ',),
      'を'        : ('を',),
      'ん'        : ('ん',),
    })

SYMB_SMALL_HIRAGANA = Name2Symbols(
    {
      'ぁ'        : ('ぁ',),
      'ぃ'        : ('ぃ',),
      'ぅ'        : ('ぅ',),
      'ぇ'        : ('ぇ',),
      'ぉ'        : ('ぉ',),

      # small ka :
      'ゕ'        : ('ゕ',),
      # small ke :
      'ゖ'        : ('ゖ',),

      'っ'        : ('っ',),

      'ゃ'        : ('ゃ',),
      'ゅ'        : ('ゅ',),
      'ょ'        : ('ょ',),

      'ゎ'        : ('ゎ',),
    })

HIRAGANA_TO_SMALL_HIRAGANA = {
      'あ'      : 'ぁ',
      'い'      : 'ぃ',
      'う'      : 'ぅ',
      'え'      : 'ぇ',
      'お'      : 'ぉ',
      'か'      : 'ゕ',
      'け'      : 'ゖ',
      'つ'      : 'っ',
      'や'      : 'ゃ',
      'ゆ'      : 'ゅ',
      'よ'      : 'ょ',
      'わ'      : 'ゎ',
    }
SMALL_HIRAGANA_TO_HIRAGANA = invertdict( HIRAGANA_TO_SMALL_HIRAGANA )

HIRAGANA_DAKUTEN_TO_HIRAGANA = {
      'が'        : "か",
      'ぎ'        : 'き',
      'ぐ'        : 'く',
      'げ'        : 'け',
      'ご'        : 'こ',
      'ざ'        : 'さ',
      'じ'        : 'し',
      'ず'        : 'す',
      'ぜ'        : 'せ',
      'ぞ'        : 'そ',
      'だ'        : 'た',
      'ぢ'        : 'ち',
      'づ'        : 'つ',
      'で'        : 'て',
      'ど'        : 'と',
      'ば'        : 'は',
      'び'        : 'ひ',
      'ぶ'        : 'ふ',
      'べ'        : 'へ',
      'ぼ'        : 'ほ',
    }
HIRAGANA_TO_HIRAGANA_DAKUTEN = invertdict( HIRAGANA_DAKUTEN_TO_HIRAGANA )

HIRAGANA_HANDAKUTEN_TO_HIRAGANA = {
      'ぱ'        : "は",
      'ぴ'        : 'ひ',
      'ぷ'        : 'ふ',
      'ぺ'        : 'へ',
      'ぽ'        : 'ほ',
    }
HIRAGANA_TO_HIRAGANA_HANDAKUTEN = invertdict( HIRAGANA_HANDAKUTEN_TO_HIRAGANA )

HIRAGANA_ORDER = {
      'あ'        : 1,
      'い'        : 2,
      'う'        : 3,
      'え'        : 4,
      'お'        : 5,
      'か'        : 6,
      'き'        : 7,
      'く'        : 8,
      'け'        : 9,
      'こ'        : 10,
      'さ'        : 11,
      'し'        : 12,
      'す'        : 13,
      'せ'        : 14,
      'そ'        : 15,
      'た'        : 16,
      'ち'        : 17,
      'つ'        : 18,
      'て'        : 19,
      'と'        : 20,
      'な'        : 21,
      'に'        : 22,
      'ぬ'        : 23,
      'ね'        : 24,
      'の'        : 25,
      'は'        : 26,
      'ひ'        : 27,
      'ふ'        : 28,
      'へ'        : 29,
      'ほ'        : 30,
      'ま'        : 31,
      'み'        : 32,
      'む'        : 33,
      'も'        : 34,
      'や'        : 35,
      'ゆ'        : 36,
      'よ'        : 37,
      'ら'        : 38,
      'り'        : 39,
      'る'        : 40,
      'れ'        : 41,
      'ろ'        : 42,
      'わ'        : 43,
      'ゐ'        : 44,
      'ゑ'        : 45,
      'を'        : 46,
      'ん'        : 47,
    }

SYMB_KATAKANA = Name2Symbols(
    {
      'ア'        : ('ア',),
      'イ'        : ('イ',),
      'ウ'        : ('ウ',),
      'エ'        : ('エ',),
      'オ'        : ('オ',),
      'カ'        : ('カ',),
      'キ'        : ('キ',),
      'ク'        : ('ク',),
      'ケ'        : ('ケ',),
      'コ'        : ('コ',),
      'サ'        : ('サ',),
      'シ'        : ('シ',),
      'ス'        : ('ス',),
      'セ'        : ('セ',),
      'ソ'        : ('ソ',),
      'タ'        : ('タ',),
      'チ'        : ('チ',),
      'ツ'        : ('ツ',),
      'テ'        : ('テ',),
      'ト'        : ('ト',),
      'ナ'        : ('ナ',),
      'ニ'        : ('ニ',),
      'ヌ'        : ('ヌ',),
      'ネ'        : ('ネ',),
      'ノ'        : ('ノ',),
      'ハ'        : ('ハ',),
      'ヒ'        : ('ヒ',),
      'フ'        : ('フ',),
      'ヘ'        : ('ヘ',),
      'ホ'        : ('ホ',),
      'マ'        : ('マ',),
      'ミ'        : ('ミ',),
      'ム'        : ('ム',),
      'メ'        : ('メ',),
      'モ'        : ('モ',),
      'ヤ'        : ('ヤ',),
      'ユ'        : ('ユ',),
      'ヨ'        : ('ヨ',),
      'ラ'        : ('ラ',),
      'リ'        : ('リ',),
      'ル'        : ('ル',),
      'レ'        : ('レ',),
      'ロ'        : ('ロ',),
      'ワ'        : ('ワ',),
      'ヰ'        : ('ヰ',),
      'ヱ'        : ('ヱ',),
      'ヲ'        : ('ヲ',),
      'ン'        : ('ン',),
    })

SYMB_SMALL_KATAKANA = Name2Symbols(
    {
      'ァ'        : ('ァ',),
      'ィ'        : ('ィ',),
      'ゥ'        : ('ゥ',),
      'ェ'        : ('ェ',),
      'ォ'        : ('ォ',),

      # small ka :
      'ヵ'        : ('ヵ',),
      # small ke :
      'ヶ'        : ('ヶ',),

      'ッ'        : ('ッ',),

      'ャ'        : ('ャ',),
      'ュ'        : ('ュ',),
      'ョ'        : ('ョ',),

      'ヮ'        : ('ヮ',),
    })

KATAKANA_TO_SMALL_KATAKANA = {
      'ア'      : 'ァ',
      'イ'      : 'ィ',
      'ウ'      : 'ゥ',
      'エ'      : 'ェ',
      'オ'      : 'ォ',
      'カ'      : 'ヵ',
      'ケ'      : 'ヶ',
      'ツ'      : 'ッ',
      'ヤ'      : 'ャ',
      'ユ'      : 'ュ',
      'ヨ'      : 'ョ',
      'ワ'      : 'ヮ',
    }
SMALL_KATAKANA_TO_KATAKANA = invertdict( KATAKANA_TO_SMALL_KATAKANA )

KATAKANA_DAKUTEN_TO_KATAKANA = {
      'ガ'        : "カ",
      'ギ'        : 'キ',
      'グ'        : 'ク',
      'ゲ'        : 'ケ',
      'ゴ'        : 'コ',
      'ザ'        : 'サ',
      'ジ'        : 'シ',
      'ズ'        : 'ス',
      'ゼ'        : 'セ',
      'ゾ'        : 'ソ',
      'ダ'        : 'タ',
      'ヂ'        : 'チ',
      'ヅ'        : 'ツ',
      'デ'        : 'テ',
      'ド'        : 'ト',
      'バ'        : 'ハ',
      'ビ'        : 'ヒ',
      'ブ'        : 'フ',
      'ベ'        : 'ヘ',
      'ボ'        : 'ホ',
    }
KATAKANA_TO_KATAKANA_DAKUTEN = invertdict( KATAKANA_DAKUTEN_TO_KATAKANA )

KATAKANA_HANDAKUTEN_TO_KATAKANA = {
      'パ'        : "ハ",
      'ピ'        : 'ヒ',
      'プ'        : 'フ',
      'ペ'        : 'ヘ',
      'ポ'        : 'ホ',
    }
KATAKANA_TO_KATAKANA_HANDAKUTEN = invertdict( KATAKANA_HANDAKUTEN_TO_KATAKANA )

HIRAGANA_TO_KATAKANA = {
      'あ'        : 'ア',
      'い'        : 'イ',
      'う'        : 'ウ',
      'え'        : 'エ',
      'お'        : 'オ',
      'か'        : 'カ',
      'き'        : 'キ',
      'く'        : 'ク',
      'け'        : 'ケ', 
      'こ'        : 'コ',
      'さ'        : 'サ',
      'し'        : 'シ',
      'す'        : 'ス',
      'せ'        : 'セ',
      'そ'        : 'ソ',
      'た'        : 'タ',
      'ち'        : 'チ',
      'つ'        : 'ツ',
      'て'        : 'テ',
      'と'        : 'ト',
      'な'        : 'ナ',
      'に'        : 'ニ',
      'ぬ'        : 'ヌ',
      'ね'        : 'ネ',
      'の'        : 'ノ',
      'は'        : 'ハ',
      'ひ'        : 'ヒ',
      'ふ'        : 'フ',
      'へ'        : 'ヘ',
      'ほ'        : 'ホ',
      'ま'        : 'マ',
      'み'        : 'ミ',
      'む'        : 'ム',
      'め'        : 'メ',
      'も'        : 'モ',
      'や'        : 'ヤ',
      'ゆ'        : 'ユ',
      'よ'        : 'ヨ',
      'ら'        : 'ラ',
      'り'        : 'リ',
      'る'        : 'ル',
      'れ'        : 'レ',
      'ろ'        : 'ロ',
      'わ'        : 'ワ',
      'ゐ'        : 'ヰ',
      'ゑ'        : 'ヱ',
      'を'        : 'ヲ',
      'ん'        : 'ン',
    }
KATAKANA_TO_HIRAGANA = invertdict( HIRAGANA_TO_KATAKANA )

#
# 常用漢字 (jōyō kanji)
# o http://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji
# o https://github.com/suizokukan/getjoyo
#
# 人名用漢字 (jinmeiyō kanji) :
# o http://en.wikipedia.org/wiki/Jinmeiy%C5%8D_kanji
# o https://github.com/suizokukan/getpurejinmeiyo
#
# 表外字 (hyōgaiji) :
# o http://ja.wiktionary.org/wiki/Wiktionary:%E8%A1%A8%E5%A4%96%E6%BC%A2%E5%AD%97%E5%AD%97%E4%BD%93%E8%A1%A8%E3%81%AE%E6%BC%A2%E5%AD%97%E4%B8%80%E8%A6%A7
# o https://github.com/suizokukan/gethyogaiji
#  
SYMB_KANJI = Name2Symbols(
    {
      # jōyō kanji #1
      '亜'        : ('亜', '亞'),
      # jōyō kanji #2
      '哀'        : ('哀',),
      # jōyō kanji #3
      '挨'        : ('挨',),
      # jōyō kanji #4
      '愛'        : ('愛',),
      # jōyō kanji #5
      '曖'        : ('曖',),
      # jōyō kanji #6
      '悪'        : ('悪', '惡'),
      # jōyō kanji #7
      '握'        : ('握',),
      # jōyō kanji #8
      '圧'        : ('圧', '壓'),
      # jōyō kanji #9
      '扱'        : ('扱',),
      # jōyō kanji #10
      '宛'        : ('宛',),
      # jōyō kanji #11
      '嵐'        : ('嵐',),
      # jōyō kanji #12
      '安'        : ('安',),
      # jōyō kanji #13
      '案'        : ('案',),
      # jōyō kanji #14
      '暗'        : ('暗',),
      # jōyō kanji #15
      '以'        : ('以',),
      # jōyō kanji #16
      '衣'        : ('衣',),
      # jōyō kanji #17
      '位'        : ('位',),
      # jōyō kanji #18
      '囲'        : ('囲', '圍'),
      # jōyō kanji #19
      '医'        : ('医', '醫'),
      # jōyō kanji #20
      '依'        : ('依',),
      # jōyō kanji #21
      '委'        : ('委',),
      # jōyō kanji #22
      '威'        : ('威',),
      # jōyō kanji #23
      '為'        : ('為', '爲'),
      # jōyō kanji #24
      '畏'        : ('畏',),
      # jōyō kanji #25
      '胃'        : ('胃',),
      # jōyō kanji #26
      '尉'        : ('尉',),
      # jōyō kanji #27
      '異'        : ('異',),
      # jōyō kanji #28
      '移'        : ('移',),
      # jōyō kanji #29
      '萎'        : ('萎',),
      # jōyō kanji #30
      '偉'        : ('偉',),
      # jōyō kanji #31
      '椅'        : ('椅',),
      # jōyō kanji #32
      '彙'        : ('彙',),
      # jōyō kanji #33
      '意'        : ('意',),
      # jōyō kanji #34
      '違'        : ('違',),
      # jōyō kanji #35
      '維'        : ('維',),
      # jōyō kanji #36
      '慰'        : ('慰',),
      # jōyō kanji #37
      '遺'        : ('遺',),
      # jōyō kanji #38
      '緯'        : ('緯',),
      # jōyō kanji #39
      '域'        : ('域',),
      # jōyō kanji #40
      '育'        : ('育',),
      # jōyō kanji #41
      '一'        : ('一',),
      # jōyō kanji #42
      '壱'        : ('壱', '壹'),
      # jōyō kanji #43
      '逸'        : ('逸', '逸'),
      # jōyō kanji #44
      '茨'        : ('茨',),
      # jōyō kanji #45
      '芋'        : ('芋',),
      # jōyō kanji #46
      '引'        : ('引',),
      # jōyō kanji #47
      '印'        : ('印',),
      # jōyō kanji #48
      '因'        : ('因',),
      # jōyō kanji #49
      '咽'        : ('咽',),
      # jōyō kanji #50
      '姻'        : ('姻',),
      # jōyō kanji #51
      '員'        : ('員',),
      # jōyō kanji #52
      '院'        : ('院',),
      # jōyō kanji #53
      '淫'        : ('淫',),
      # jōyō kanji #54
      '陰'        : ('陰',),
      # jōyō kanji #55
      '飲'        : ('飲',),
      # jōyō kanji #56
      '隠'        : ('隠', '隱'),
      # jōyō kanji #57
      '韻'        : ('韻',),
      # jōyō kanji #58
      '右'        : ('右',),
      # jōyō kanji #59
      '宇'        : ('宇',),
      # jōyō kanji #60
      '羽'        : ('羽',),
      # jōyō kanji #61
      '雨'        : ('雨',),
      # jōyō kanji #62
      '唄'        : ('唄',),
      # jōyō kanji #63
      '鬱'        : ('鬱',),
      # jōyō kanji #64
      '畝'        : ('畝',),
      # jōyō kanji #65
      '浦'        : ('浦',),
      # jōyō kanji #66
      '運'        : ('運',),
      # jōyō kanji #67
      '雲'        : ('雲',),
      # jōyō kanji #68
      '永'        : ('永',),
      # jōyō kanji #69
      '泳'        : ('泳',),
      # jōyō kanji #70
      '英'        : ('英',),
      # jōyō kanji #71
      '映'        : ('映',),
      # jōyō kanji #72
      '栄'        : ('栄', '榮'),
      # jōyō kanji #73
      '営'        : ('営', '營'),
      # jōyō kanji #74
      '詠'        : ('詠',),
      # jōyō kanji #75
      '影'        : ('影',),
      # jōyō kanji #76
      '鋭'        : ('鋭',),
      # jōyō kanji #77
      '衛'        : ('衛', '衞'),
      # jōyō kanji #78
      '易'        : ('易',),
      # jōyō kanji #79
      '疫'        : ('疫',),
      # jōyō kanji #80
      '益'        : ('益',),
      # jōyō kanji #81
      '液'        : ('液',),
      # jōyō kanji #82
      '駅'        : ('駅', '驛'),
      # jōyō kanji #83
      '悦'        : ('悦',),
      # jōyō kanji #84
      '越'        : ('越',),
      # jōyō kanji #85
      '謁'        : ('謁', '謁'),
      # jōyō kanji #86
      '閲'        : ('閲',),
      # jōyō kanji #87
      '円'        : ('円', '圓'),
      # jōyō kanji #88
      '延'        : ('延',),
      # jōyō kanji #89
      '沿'        : ('沿',),
      # jōyō kanji #90
      '炎'        : ('炎',),
      # jōyō kanji #91
      '怨'        : ('怨',),
      # jōyō kanji #92
      '宴'        : ('宴',),
      # jōyō kanji #93
      '媛'        : ('媛',),
      # jōyō kanji #94
      '援'        : ('援',),
      # jōyō kanji #95
      '園'        : ('園',),
      # jōyō kanji #96
      '煙'        : ('煙',),
      # jōyō kanji #97
      '猿'        : ('猿',),
      # jōyō kanji #98
      '遠'        : ('遠',),
      # jōyō kanji #99
      '鉛'        : ('鉛',),
      # jōyō kanji #100
      '塩'        : ('塩', '鹽'),
      # jōyō kanji #101
      '演'        : ('演',),
      # jōyō kanji #102
      '縁'        : ('縁', '緣'),
      # jōyō kanji #103
      '艶'        : ('艶', '艷'),
      # jōyō kanji #104
      '汚'        : ('汚',),
      # jōyō kanji #105
      '王'        : ('王',),
      # jōyō kanji #106
      '凹'        : ('凹',),
      # jōyō kanji #107
      '央'        : ('央',),
      # jōyō kanji #108
      '応'        : ('応', '應'),
      # jōyō kanji #109
      '往'        : ('往',),
      # jōyō kanji #110
      '押'        : ('押',),
      # jōyō kanji #111
      '旺'        : ('旺',),
      # jōyō kanji #112
      '欧'        : ('欧', '歐'),
      # jōyō kanji #113
      '殴'        : ('殴', '毆'),
      # jōyō kanji #114
      '桜'        : ('桜', '櫻'),
      # jōyō kanji #115
      '翁'        : ('翁',),
      # jōyō kanji #116
      '奥'        : ('奥', '奧'),
      # jōyō kanji #117
      '横'        : ('横', '橫'),
      # jōyō kanji #118
      '岡'        : ('岡',),
      # jōyō kanji #119
      '屋'        : ('屋',),
      # jōyō kanji #120
      '億'        : ('億',),
      # jōyō kanji #121
      '憶'        : ('憶',),
      # jōyō kanji #122
      '臆'        : ('臆',),
      # jōyō kanji #123
      '虞'        : ('虞',),
      # jōyō kanji #124
      '乙'        : ('乙',),
      # jōyō kanji #125
      '俺'        : ('俺',),
      # jōyō kanji #126
      '卸'        : ('卸',),
      # jōyō kanji #127
      '音'        : ('音',),
      # jōyō kanji #128
      '恩'        : ('恩',),
      # jōyō kanji #129
      '温'        : ('温', '溫'),
      # jōyō kanji #130
      '穏'        : ('穏', '穩'),
      # jōyō kanji #131
      '下'        : ('下',),
      # jōyō kanji #132
      '化'        : ('化',),
      # jōyō kanji #133
      '火'        : ('火',),
      # jōyō kanji #134
      '加'        : ('加',),
      # jōyō kanji #135
      '可'        : ('可',),
      # jōyō kanji #136
      '仮'        : ('仮', '假'),
      # jōyō kanji #137
      '何'        : ('何',),
      # jōyō kanji #138
      '花'        : ('花',),
      # jōyō kanji #139
      '佳'        : ('佳',),
      # jōyō kanji #140
      '価'        : ('価', '價'),
      # jōyō kanji #141
      '果'        : ('果',),
      # jōyō kanji #142
      '河'        : ('河',),
      # jōyō kanji #143
      '苛'        : ('苛',),
      # jōyō kanji #144
      '科'        : ('科',),
      # jōyō kanji #145
      '架'        : ('架',),
      # jōyō kanji #146
      '夏'        : ('夏',),
      # jōyō kanji #147
      '家'        : ('家',),
      # jōyō kanji #148
      '荷'        : ('荷',),
      # jōyō kanji #149
      '華'        : ('華',),
      # jōyō kanji #150
      '菓'        : ('菓',),
      # jōyō kanji #151
      '貨'        : ('貨',),
      # jōyō kanji #152
      '渦'        : ('渦',),
      # jōyō kanji #153
      '過'        : ('過',),
      # jōyō kanji #154
      '嫁'        : ('嫁',),
      # jōyō kanji #155
      '暇'        : ('暇',),
      # jōyō kanji #156
      '禍'        : ('禍', '禍'),
      # jōyō kanji #157
      '靴'        : ('靴',),
      # jōyō kanji #158
      '寡'        : ('寡',),
      # jōyō kanji #159
      '歌'        : ('歌',),
      # jōyō kanji #160
      '箇'        : ('箇',),
      # jōyō kanji #161
      '稼'        : ('稼',),
      # jōyō kanji #162
      '課'        : ('課',),
      # jōyō kanji #163
      '蚊'        : ('蚊',),
      # jōyō kanji #164
      '牙'        : ('牙',),
      # jōyō kanji #165
      '瓦'        : ('瓦',),
      # jōyō kanji #166
      '我'        : ('我',),
      # jōyō kanji #167
      '画'        : ('画', '畫'),
      # jōyō kanji #168
      '芽'        : ('芽',),
      # jōyō kanji #169
      '賀'        : ('賀',),
      # jōyō kanji #170
      '雅'        : ('雅',),
      # jōyō kanji #171
      '餓'        : ('餓',),
      # jōyō kanji #172
      '介'        : ('介',),
      # jōyō kanji #173
      '回'        : ('回',),
      # jōyō kanji #174
      '灰'        : ('灰',),
      # jōyō kanji #175
      '会'        : ('会', '會'),
      # jōyō kanji #176
      '快'        : ('快',),
      # jōyō kanji #177
      '戒'        : ('戒',),
      # jōyō kanji #178
      '改'        : ('改',),
      # jōyō kanji #179
      '怪'        : ('怪',),
      # jōyō kanji #180
      '拐'        : ('拐',),
      # jōyō kanji #181
      '悔'        : ('悔', '悔'),
      # jōyō kanji #182
      '海'        : ('海', '海'),
      # jōyō kanji #183
      '界'        : ('界',),
      # jōyō kanji #184
      '皆'        : ('皆',),
      # jōyō kanji #185
      '械'        : ('械',),
      # jōyō kanji #186
      '絵'        : ('絵', '繪'),
      # jōyō kanji #187
      '開'        : ('開',),
      # jōyō kanji #188
      '階'        : ('階',),
      # jōyō kanji #189
      '塊'        : ('塊',),
      # jōyō kanji #190
      '楷'        : ('楷',),
      # jōyō kanji #191
      '解'        : ('解',),
      # jōyō kanji #192
      '潰'        : ('潰',),
      # jōyō kanji #193
      '壊'        : ('壊', '壞'),
      # jōyō kanji #194
      '懐'        : ('懐', '懷'),
      # jōyō kanji #195
      '諧'        : ('諧',),
      # jōyō kanji #196
      '貝'        : ('貝',),
      # jōyō kanji #197
      '外'        : ('外',),
      # jōyō kanji #198
      '劾'        : ('劾',),
      # jōyō kanji #199
      '害'        : ('害',),
      # jōyō kanji #200
      '崖'        : ('崖',),
      # jōyō kanji #201
      '涯'        : ('涯',),
      # jōyō kanji #202
      '街'        : ('街',),
      # jōyō kanji #203
      '慨'        : ('慨', '慨'),
      # jōyō kanji #204
      '蓋'        : ('蓋',),
      # jōyō kanji #205
      '該'        : ('該',),
      # jōyō kanji #206
      '概'        : ('概', '槪'),
      # jōyō kanji #207
      '骸'        : ('骸',),
      # jōyō kanji #208
      '垣'        : ('垣',),
      # jōyō kanji #209
      '柿'        : ('柿',),
      # jōyō kanji #210
      '各'        : ('各',),
      # jōyō kanji #211
      '角'        : ('角',),
      # jōyō kanji #212
      '拡'        : ('拡', '擴'),
      # jōyō kanji #213
      '革'        : ('革',),
      # jōyō kanji #214
      '格'        : ('格',),
      # jōyō kanji #215
      '核'        : ('核',),
      # jōyō kanji #216
      '殻'        : ('殻', '殼'),
      # jōyō kanji #217
      '郭'        : ('郭',),
      # jōyō kanji #218
      '覚'        : ('覚', '覺'),
      # jōyō kanji #219
      '較'        : ('較',),
      # jōyō kanji #220
      '隔'        : ('隔',),
      # jōyō kanji #221
      '閣'        : ('閣',),
      # jōyō kanji #222
      '確'        : ('確',),
      # jōyō kanji #223
      '獲'        : ('獲',),
      # jōyō kanji #224
      '嚇'        : ('嚇',),
      # jōyō kanji #225
      '穫'        : ('穫',),
      # jōyō kanji #226
      '学'        : ('学', '學'),
      # jōyō kanji #227
      '岳'        : ('岳', '嶽'),
      # jōyō kanji #228
      '楽'        : ('楽', '樂'),
      # jōyō kanji #229
      '額'        : ('額',),
      # jōyō kanji #230
      '顎'        : ('顎',),
      # jōyō kanji #231
      '掛'        : ('掛',),
      # jōyō kanji #232
      '潟'        : ('潟',),
      # jōyō kanji #233
      '括'        : ('括',),
      # jōyō kanji #234
      '活'        : ('活',),
      # jōyō kanji #235
      '喝'        : ('喝', '喝'),
      # jōyō kanji #236
      '渇'        : ('渇', '渴'),
      # jōyō kanji #237
      '割'        : ('割',),
      # jōyō kanji #238
      '葛'        : ('葛',),
      # jōyō kanji #239
      '滑'        : ('滑',),
      # jōyō kanji #240
      '褐'        : ('褐', '褐'),
      # jōyō kanji #241
      '轄'        : ('轄',),
      # jōyō kanji #242
      '且'        : ('且',),
      # jōyō kanji #243
      '株'        : ('株',),
      # jōyō kanji #244
      '釜'        : ('釜',),
      # jōyō kanji #245
      '鎌'        : ('鎌',),
      # jōyō kanji #246
      '刈'        : ('刈',),
      # jōyō kanji #247
      '干'        : ('干',),
      # jōyō kanji #248
      '刊'        : ('刊',),
      # jōyō kanji #249
      '甘'        : ('甘',),
      # jōyō kanji #250
      '汗'        : ('汗',),
      # jōyō kanji #251
      '缶'        : ('缶', '罐'),
      # jōyō kanji #252
      '完'        : ('完',),
      # jōyō kanji #253
      '肝'        : ('肝',),
      # jōyō kanji #254
      '官'        : ('官',),
      # jōyō kanji #255
      '冠'        : ('冠',),
      # jōyō kanji #256
      '巻'        : ('巻', '卷'),
      # jōyō kanji #257
      '看'        : ('看',),
      # jōyō kanji #258
      '陥'        : ('陥', '陷'),
      # jōyō kanji #259
      '乾'        : ('乾',),
      # jōyō kanji #260
      '勘'        : ('勘',),
      # jōyō kanji #261
      '患'        : ('患',),
      # jōyō kanji #262
      '貫'        : ('貫',),
      # jōyō kanji #263
      '寒'        : ('寒',),
      # jōyō kanji #264
      '喚'        : ('喚',),
      # jōyō kanji #265
      '堪'        : ('堪',),
      # jōyō kanji #266
      '換'        : ('換',),
      # jōyō kanji #267
      '敢'        : ('敢',),
      # jōyō kanji #268
      '棺'        : ('棺',),
      # jōyō kanji #269
      '款'        : ('款',),
      # jōyō kanji #270
      '間'        : ('間',),
      # jōyō kanji #271
      '閑'        : ('閑',),
      # jōyō kanji #272
      '勧'        : ('勧', '勸'),
      # jōyō kanji #273
      '寛'        : ('寛', '寬'),
      # jōyō kanji #274
      '幹'        : ('幹',),
      # jōyō kanji #275
      '感'        : ('感',),
      # jōyō kanji #276
      '漢'        : ('漢', '漢'),
      # jōyō kanji #277
      '慣'        : ('慣',),
      # jōyō kanji #278
      '管'        : ('管',),
      # jōyō kanji #279
      '関'        : ('関', '關'),
      # jōyō kanji #280
      '歓'        : ('歓', '歡'),
      # jōyō kanji #281
      '監'        : ('監',),
      # jōyō kanji #282
      '緩'        : ('緩',),
      # jōyō kanji #283
      '憾'        : ('憾',),
      # jōyō kanji #284
      '還'        : ('還',),
      # jōyō kanji #285
      '館'        : ('館',),
      # jōyō kanji #286
      '環'        : ('環',),
      # jōyō kanji #287
      '簡'        : ('簡',),
      # jōyō kanji #288
      '観'        : ('観', '觀'),
      # jōyō kanji #289
      '韓'        : ('韓',),
      # jōyō kanji #290
      '艦'        : ('艦',),
      # jōyō kanji #291
      '鑑'        : ('鑑',),
      # jōyō kanji #292
      '丸'        : ('丸',),
      # jōyō kanji #293
      '含'        : ('含',),
      # jōyō kanji #294
      '岸'        : ('岸',),
      # jōyō kanji #295
      '岩'        : ('岩',),
      # jōyō kanji #296
      '玩'        : ('玩',),
      # jōyō kanji #297
      '眼'        : ('眼',),
      # jōyō kanji #298
      '頑'        : ('頑',),
      # jōyō kanji #299
      '顔'        : ('顔',),
      # jōyō kanji #300
      '願'        : ('願',),
      # jōyō kanji #301
      '企'        : ('企',),
      # jōyō kanji #302
      '伎'        : ('伎',),
      # jōyō kanji #303
      '危'        : ('危',),
      # jōyō kanji #304
      '机'        : ('机',),
      # jōyō kanji #305
      '気'        : ('気', '氣'),
      # jōyō kanji #306
      '岐'        : ('岐',),
      # jōyō kanji #307
      '希'        : ('希',),
      # jōyō kanji #308
      '忌'        : ('忌',),
      # jōyō kanji #309
      '汽'        : ('汽',),
      # jōyō kanji #310
      '奇'        : ('奇',),
      # jōyō kanji #311
      '祈'        : ('祈', '祈'),
      # jōyō kanji #312
      '季'        : ('季',),
      # jōyō kanji #313
      '紀'        : ('紀',),
      # jōyō kanji #314
      '軌'        : ('軌',),
      # jōyō kanji #315
      '既'        : ('既', '既'),
      # jōyō kanji #316
      '記'        : ('記',),
      # jōyō kanji #317
      '起'        : ('起',),
      # jōyō kanji #318
      '飢'        : ('飢',),
      # jōyō kanji #319
      '鬼'        : ('鬼',),
      # jōyō kanji #320
      '帰'        : ('帰', '歸'),
      # jōyō kanji #321
      '基'        : ('基',),
      # jōyō kanji #322
      '寄'        : ('寄',),
      # jōyō kanji #323
      '規'        : ('規',),
      # jōyō kanji #324
      '亀'        : ('亀', '龜'),
      # jōyō kanji #325
      '喜'        : ('喜',),
      # jōyō kanji #326
      '幾'        : ('幾',),
      # jōyō kanji #327
      '揮'        : ('揮',),
      # jōyō kanji #328
      '期'        : ('期',),
      # jōyō kanji #329
      '棋'        : ('棋',),
      # jōyō kanji #330
      '貴'        : ('貴',),
      # jōyō kanji #331
      '棄'        : ('棄',),
      # jōyō kanji #332
      '毀'        : ('毀',),
      # jōyō kanji #333
      '旗'        : ('旗',),
      # jōyō kanji #334
      '器'        : ('器', '器'),
      # jōyō kanji #335
      '畿'        : ('畿',),
      # jōyō kanji #336
      '輝'        : ('輝',),
      # jōyō kanji #337
      '機'        : ('機',),
      # jōyō kanji #338
      '騎'        : ('騎',),
      # jōyō kanji #339
      '技'        : ('技',),
      # jōyō kanji #340
      '宜'        : ('宜',),
      # jōyō kanji #341
      '偽'        : ('偽', '僞'),
      # jōyō kanji #342
      '欺'        : ('欺',),
      # jōyō kanji #343
      '義'        : ('義',),
      # jōyō kanji #344
      '疑'        : ('疑',),
      # jōyō kanji #345
      '儀'        : ('儀',),
      # jōyō kanji #346
      '戯'        : ('戯', '戲'),
      # jōyō kanji #347
      '擬'        : ('擬',),
      # jōyō kanji #348
      '犠'        : ('犠', '犧'),
      # jōyō kanji #349
      '議'        : ('議',),
      # jōyō kanji #350
      '菊'        : ('菊',),
      # jōyō kanji #351
      '吉'        : ('吉',),
      # jōyō kanji #352
      '喫'        : ('喫',),
      # jōyō kanji #353
      '詰'        : ('詰',),
      # jōyō kanji #354
      '却'        : ('却',),
      # jōyō kanji #355
      '客'        : ('客',),
      # jōyō kanji #356
      '脚'        : ('脚',),
      # jōyō kanji #357
      '逆'        : ('逆',),
      # jōyō kanji #358
      '虐'        : ('虐',),
      # jōyō kanji #359
      '九'        : ('九',),
      # jōyō kanji #360
      '久'        : ('久',),
      # jōyō kanji #361
      '及'        : ('及',),
      # jōyō kanji #362
      '弓'        : ('弓',),
      # jōyō kanji #363
      '丘'        : ('丘',),
      # jōyō kanji #364
      '旧'        : ('旧', '舊'),
      # jōyō kanji #365
      '休'        : ('休',),
      # jōyō kanji #366
      '吸'        : ('吸',),
      # jōyō kanji #367
      '朽'        : ('朽',),
      # jōyō kanji #368
      '臼'        : ('臼',),
      # jōyō kanji #369
      '求'        : ('求',),
      # jōyō kanji #370
      '究'        : ('究',),
      # jōyō kanji #371
      '泣'        : ('泣',),
      # jōyō kanji #372
      '急'        : ('急',),
      # jōyō kanji #373
      '級'        : ('級',),
      # jōyō kanji #374
      '糾'        : ('糾',),
      # jōyō kanji #375
      '宮'        : ('宮',),
      # jōyō kanji #376
      '救'        : ('救',),
      # jōyō kanji #377
      '球'        : ('球',),
      # jōyō kanji #378
      '給'        : ('給',),
      # jōyō kanji #379
      '嗅'        : ('嗅',),
      # jōyō kanji #380
      '窮'        : ('窮',),
      # jōyō kanji #381
      '牛'        : ('牛',),
      # jōyō kanji #382
      '去'        : ('去',),
      # jōyō kanji #383
      '巨'        : ('巨',),
      # jōyō kanji #384
      '居'        : ('居',),
      # jōyō kanji #385
      '拒'        : ('拒',),
      # jōyō kanji #386
      '拠'        : ('拠', '據'),
      # jōyō kanji #387
      '挙'        : ('挙', '擧'),
      # jōyō kanji #388
      '虚'        : ('虚', '虛'),
      # jōyō kanji #389
      '許'        : ('許',),
      # jōyō kanji #390
      '距'        : ('距',),
      # jōyō kanji #391
      '魚'        : ('魚',),
      # jōyō kanji #392
      '御'        : ('御',),
      # jōyō kanji #393
      '漁'        : ('漁',),
      # jōyō kanji #394
      '凶'        : ('凶',),
      # jōyō kanji #395
      '共'        : ('共',),
      # jōyō kanji #396
      '叫'        : ('叫',),
      # jōyō kanji #397
      '狂'        : ('狂',),
      # jōyō kanji #398
      '京'        : ('京',),
      # jōyō kanji #399
      '享'        : ('享',),
      # jōyō kanji #400
      '供'        : ('供',),
      # jōyō kanji #401
      '協'        : ('協',),
      # jōyō kanji #402
      '況'        : ('況',),
      # jōyō kanji #403
      '峡'        : ('峡', '峽'),
      # jōyō kanji #404
      '挟'        : ('挟', '挾'),
      # jōyō kanji #405
      '狭'        : ('狭', '狹'),
      # jōyō kanji #406
      '恐'        : ('恐',),
      # jōyō kanji #407
      '恭'        : ('恭',),
      # jōyō kanji #408
      '胸'        : ('胸',),
      # jōyō kanji #409
      '脅'        : ('脅',),
      # jōyō kanji #410
      '強'        : ('強',),
      # jōyō kanji #411
      '教'        : ('教',),
      # jōyō kanji #412
      '郷'        : ('郷', '鄕'),
      # jōyō kanji #413
      '境'        : ('境',),
      # jōyō kanji #414
      '橋'        : ('橋',),
      # jōyō kanji #415
      '矯'        : ('矯',),
      # jōyō kanji #416
      '鏡'        : ('鏡',),
      # jōyō kanji #417
      '競'        : ('競',),
      # jōyō kanji #418
      '響'        : ('響', '響'),
      # jōyō kanji #419
      '驚'        : ('驚',),
      # jōyō kanji #420
      '仰'        : ('仰',),
      # jōyō kanji #421
      '暁'        : ('暁', '曉'),
      # jōyō kanji #422
      '業'        : ('業',),
      # jōyō kanji #423
      '凝'        : ('凝',),
      # jōyō kanji #424
      '曲'        : ('曲',),
      # jōyō kanji #425
      '局'        : ('局',),
      # jōyō kanji #426
      '極'        : ('極',),
      # jōyō kanji #427
      '玉'        : ('玉',),
      # jōyō kanji #428
      '巾'        : ('巾',),
      # jōyō kanji #429
      '斤'        : ('斤',),
      # jōyō kanji #430
      '均'        : ('均',),
      # jōyō kanji #431
      '近'        : ('近',),
      # jōyō kanji #432
      '金'        : ('金',),
      # jōyō kanji #433
      '菌'        : ('菌',),
      # jōyō kanji #434
      '勤'        : ('勤', '勤'),
      # jōyō kanji #435
      '琴'        : ('琴',),
      # jōyō kanji #436
      '筋'        : ('筋',),
      # jōyō kanji #437
      '僅'        : ('僅',),
      # jōyō kanji #438
      '禁'        : ('禁',),
      # jōyō kanji #439
      '緊'        : ('緊',),
      # jōyō kanji #440
      '錦'        : ('錦',),
      # jōyō kanji #441
      '謹'        : ('謹', '謹'),
      # jōyō kanji #442
      '襟'        : ('襟',),
      # jōyō kanji #443
      '吟'        : ('吟',),
      # jōyō kanji #444
      '銀'        : ('銀',),
      # jōyō kanji #445
      '区'        : ('区', '區'),
      # jōyō kanji #446
      '句'        : ('句',),
      # jōyō kanji #447
      '苦'        : ('苦',),
      # jōyō kanji #448
      '駆'        : ('駆', '驅'),
      # jōyō kanji #449
      '具'        : ('具',),
      # jōyō kanji #450
      '惧'        : ('惧',),
      # jōyō kanji #451
      '愚'        : ('愚',),
      # jōyō kanji #452
      '空'        : ('空',),
      # jōyō kanji #453
      '偶'        : ('偶',),
      # jōyō kanji #454
      '遇'        : ('遇',),
      # jōyō kanji #455
      '隅'        : ('隅',),
      # jōyō kanji #456
      '串'        : ('串',),
      # jōyō kanji #457
      '屈'        : ('屈',),
      # jōyō kanji #458
      '掘'        : ('掘',),
      # jōyō kanji #459
      '窟'        : ('窟',),
      # jōyō kanji #460
      '熊'        : ('熊',),
      # jōyō kanji #461
      '繰'        : ('繰',),
      # jōyō kanji #462
      '君'        : ('君',),
      # jōyō kanji #463
      '訓'        : ('訓',),
      # jōyō kanji #464
      '勲'        : ('勲', '勳'),
      # jōyō kanji #465
      '薫'        : ('薫', '薰'),
      # jōyō kanji #466
      '軍'        : ('軍',),
      # jōyō kanji #467
      '郡'        : ('郡',),
      # jōyō kanji #468
      '群'        : ('群',),
      # jōyō kanji #469
      '兄'        : ('兄',),
      # jōyō kanji #470
      '刑'        : ('刑',),
      # jōyō kanji #471
      '形'        : ('形',),
      # jōyō kanji #472
      '系'        : ('系',),
      # jōyō kanji #473
      '径'        : ('径', '徑'),
      # jōyō kanji #474
      '茎'        : ('茎', '莖'),
      # jōyō kanji #475
      '係'        : ('係',),
      # jōyō kanji #476
      '型'        : ('型',),
      # jōyō kanji #477
      '契'        : ('契',),
      # jōyō kanji #478
      '計'        : ('計',),
      # jōyō kanji #479
      '恵'        : ('恵', '惠'),
      # jōyō kanji #480
      '啓'        : ('啓',),
      # jōyō kanji #481
      '掲'        : ('掲', '揭'),
      # jōyō kanji #482
      '渓'        : ('渓', '溪'),
      # jōyō kanji #483
      '経'        : ('経', '經'),
      # jōyō kanji #484
      '蛍'        : ('蛍', '螢'),
      # jōyō kanji #485
      '敬'        : ('敬',),
      # jōyō kanji #486
      '景'        : ('景',),
      # jōyō kanji #487
      '軽'        : ('軽', '輕'),
      # jōyō kanji #488
      '傾'        : ('傾',),
      # jōyō kanji #489
      '携'        : ('携',),
      # jōyō kanji #490
      '継'        : ('継', '繼'),
      # jōyō kanji #491
      '詣'        : ('詣',),
      # jōyō kanji #492
      '慶'        : ('慶',),
      # jōyō kanji #493
      '憬'        : ('憬',),
      # jōyō kanji #494
      '稽'        : ('稽',),
      # jōyō kanji #495
      '憩'        : ('憩',),
      # jōyō kanji #496
      '警'        : ('警',),
      # jōyō kanji #497
      '鶏'        : ('鶏', '鷄'),
      # jōyō kanji #498
      '芸'        : ('芸', '藝'),
      # jōyō kanji #499
      '迎'        : ('迎',),
      # jōyō kanji #500
      '鯨'        : ('鯨',),
      # jōyō kanji #501
      '隙'        : ('隙',),
      # jōyō kanji #502
      '劇'        : ('劇',),
      # jōyō kanji #503
      '撃'        : ('撃', '擊'),
      # jōyō kanji #504
      '激'        : ('激',),
      # jōyō kanji #505
      '桁'        : ('桁',),
      # jōyō kanji #506
      '欠'        : ('欠', '缺'),
      # jōyō kanji #507
      '穴'        : ('穴',),
      # jōyō kanji #508
      '血'        : ('血',),
      # jōyō kanji #509
      '決'        : ('決',),
      # jōyō kanji #510
      '結'        : ('結',),
      # jōyō kanji #511
      '傑'        : ('傑',),
      # jōyō kanji #512
      '潔'        : ('潔',),
      # jōyō kanji #513
      '月'        : ('月',),
      # jōyō kanji #514
      '犬'        : ('犬',),
      # jōyō kanji #515
      '件'        : ('件',),
      # jōyō kanji #516
      '見'        : ('見',),
      # jōyō kanji #517
      '券'        : ('券',),
      # jōyō kanji #518
      '肩'        : ('肩',),
      # jōyō kanji #519
      '建'        : ('建',),
      # jōyō kanji #520
      '研'        : ('研', '硏'),
      # jōyō kanji #521
      '県'        : ('県', '縣'),
      # jōyō kanji #522
      '倹'        : ('倹', '儉'),
      # jōyō kanji #523
      '兼'        : ('兼',),
      # jōyō kanji #524
      '剣'        : ('剣', '劍'),
      # jōyō kanji #525
      '拳'        : ('拳',),
      # jōyō kanji #526
      '軒'        : ('軒',),
      # jōyō kanji #527
      '健'        : ('健',),
      # jōyō kanji #528
      '険'        : ('険', '險'),
      # jōyō kanji #529
      '圏'        : ('圏', '圈'),
      # jōyō kanji #530
      '堅'        : ('堅',),
      # jōyō kanji #531
      '検'        : ('検', '檢'),
      # jōyō kanji #532
      '嫌'        : ('嫌',),
      # jōyō kanji #533
      '献'        : ('献', '獻'),
      # jōyō kanji #534
      '絹'        : ('絹',),
      # jōyō kanji #535
      '遣'        : ('遣',),
      # jōyō kanji #536
      '権'        : ('権', '權'),
      # jōyō kanji #537
      '憲'        : ('憲',),
      # jōyō kanji #538
      '賢'        : ('賢',),
      # jōyō kanji #539
      '謙'        : ('謙',),
      # jōyō kanji #540
      '鍵'        : ('鍵',),
      # jōyō kanji #541
      '繭'        : ('繭',),
      # jōyō kanji #542
      '顕'        : ('顕', '顯'),
      # jōyō kanji #543
      '験'        : ('験', '驗'),
      # jōyō kanji #544
      '懸'        : ('懸',),
      # jōyō kanji #545
      '元'        : ('元',),
      # jōyō kanji #546
      '幻'        : ('幻',),
      # jōyō kanji #547
      '玄'        : ('玄',),
      # jōyō kanji #548
      '言'        : ('言',),
      # jōyō kanji #549
      '弦'        : ('弦',),
      # jōyō kanji #550
      '限'        : ('限',),
      # jōyō kanji #551
      '原'        : ('原',),
      # jōyō kanji #552
      '現'        : ('現',),
      # jōyō kanji #553
      '舷'        : ('舷',),
      # jōyō kanji #554
      '減'        : ('減',),
      # jōyō kanji #555
      '源'        : ('源',),
      # jōyō kanji #556
      '厳'        : ('厳', '嚴'),
      # jōyō kanji #557
      '己'        : ('己',),
      # jōyō kanji #558
      '戸'        : ('戸',),
      # jōyō kanji #559
      '古'        : ('古',),
      # jōyō kanji #560
      '呼'        : ('呼',),
      # jōyō kanji #561
      '固'        : ('固',),
      # jōyō kanji #562
      '股'        : ('股',),
      # jōyō kanji #563
      '虎'        : ('虎',),
      # jōyō kanji #564
      '孤'        : ('孤',),
      # jōyō kanji #565
      '弧'        : ('弧',),
      # jōyō kanji #566
      '故'        : ('故',),
      # jōyō kanji #567
      '枯'        : ('枯',),
      # jōyō kanji #568
      '個'        : ('個',),
      # jōyō kanji #569
      '庫'        : ('庫',),
      # jōyō kanji #570
      '湖'        : ('湖',),
      # jōyō kanji #571
      '雇'        : ('雇',),
      # jōyō kanji #572
      '誇'        : ('誇',),
      # jōyō kanji #573
      '鼓'        : ('鼓',),
      # jōyō kanji #574
      '錮'        : ('錮',),
      # jōyō kanji #575
      '顧'        : ('顧',),
      # jōyō kanji #576
      '五'        : ('五',),
      # jōyō kanji #577
      '互'        : ('互',),
      # jōyō kanji #578
      '午'        : ('午',),
      # jōyō kanji #579
      '呉'        : ('呉',),
      # jōyō kanji #580
      '後'        : ('後',),
      # jōyō kanji #581
      '娯'        : ('娯',),
      # jōyō kanji #582
      '悟'        : ('悟',),
      # jōyō kanji #583
      '碁'        : ('碁',),
      # jōyō kanji #584
      '語'        : ('語',),
      # jōyō kanji #585
      '誤'        : ('誤',),
      # jōyō kanji #586
      '護'        : ('護',),
      # jōyō kanji #587
      '口'        : ('口',),
      # jōyō kanji #588
      '工'        : ('工',),
      # jōyō kanji #589
      '公'        : ('公',),
      # jōyō kanji #590
      '勾'        : ('勾',),
      # jōyō kanji #591
      '孔'        : ('孔',),
      # jōyō kanji #592
      '功'        : ('功',),
      # jōyō kanji #593
      '巧'        : ('巧',),
      # jōyō kanji #594
      '広'        : ('広', '廣'),
      # jōyō kanji #595
      '甲'        : ('甲',),
      # jōyō kanji #596
      '交'        : ('交',),
      # jōyō kanji #597
      '光'        : ('光',),
      # jōyō kanji #598
      '向'        : ('向',),
      # jōyō kanji #599
      '后'        : ('后',),
      # jōyō kanji #600
      '好'        : ('好',),
      # jōyō kanji #601
      '江'        : ('江',),
      # jōyō kanji #602
      '考'        : ('考',),
      # jōyō kanji #603
      '行'        : ('行',),
      # jōyō kanji #604
      '坑'        : ('坑',),
      # jōyō kanji #605
      '孝'        : ('孝',),
      # jōyō kanji #606
      '抗'        : ('抗',),
      # jōyō kanji #607
      '攻'        : ('攻',),
      # jōyō kanji #608
      '更'        : ('更',),
      # jōyō kanji #609
      '効'        : ('効', '效'),
      # jōyō kanji #610
      '幸'        : ('幸',),
      # jōyō kanji #611
      '拘'        : ('拘',),
      # jōyō kanji #612
      '肯'        : ('肯',),
      # jōyō kanji #613
      '侯'        : ('侯',),
      # jōyō kanji #614
      '厚'        : ('厚',),
      # jōyō kanji #615
      '恒'        : ('恒', '恆'),
      # jōyō kanji #616
      '洪'        : ('洪',),
      # jōyō kanji #617
      '皇'        : ('皇',),
      # jōyō kanji #618
      '紅'        : ('紅',),
      # jōyō kanji #619
      '荒'        : ('荒',),
      # jōyō kanji #620
      '郊'        : ('郊',),
      # jōyō kanji #621
      '香'        : ('香',),
      # jōyō kanji #622
      '候'        : ('候',),
      # jōyō kanji #623
      '校'        : ('校',),
      # jōyō kanji #624
      '耕'        : ('耕',),
      # jōyō kanji #625
      '航'        : ('航',),
      # jōyō kanji #626
      '貢'        : ('貢',),
      # jōyō kanji #627
      '降'        : ('降',),
      # jōyō kanji #628
      '高'        : ('高',),
      # jōyō kanji #629
      '康'        : ('康',),
      # jōyō kanji #630
      '控'        : ('控',),
      # jōyō kanji #631
      '梗'        : ('梗',),
      # jōyō kanji #632
      '黄'        : ('黄', '黃'),
      # jōyō kanji #633
      '喉'        : ('喉',),
      # jōyō kanji #634
      '慌'        : ('慌',),
      # jōyō kanji #635
      '港'        : ('港',),
      # jōyō kanji #636
      '硬'        : ('硬',),
      # jōyō kanji #637
      '絞'        : ('絞',),
      # jōyō kanji #638
      '項'        : ('項',),
      # jōyō kanji #639
      '溝'        : ('溝',),
      # jōyō kanji #640
      '鉱'        : ('鉱', '鑛'),
      # jōyō kanji #641
      '構'        : ('構',),
      # jōyō kanji #642
      '綱'        : ('綱',),
      # jōyō kanji #643
      '酵'        : ('酵',),
      # jōyō kanji #644
      '稿'        : ('稿',),
      # jōyō kanji #645
      '興'        : ('興',),
      # jōyō kanji #646
      '衡'        : ('衡',),
      # jōyō kanji #647
      '鋼'        : ('鋼',),
      # jōyō kanji #648
      '講'        : ('講',),
      # jōyō kanji #649
      '購'        : ('購',),
      # jōyō kanji #650
      '乞'        : ('乞',),
      # jōyō kanji #651
      '号'        : ('号', '號'),
      # jōyō kanji #652
      '合'        : ('合',),
      # jōyō kanji #653
      '拷'        : ('拷',),
      # jōyō kanji #654
      '剛'        : ('剛',),
      # jōyō kanji #655
      '傲'        : ('傲',),
      # jōyō kanji #656
      '豪'        : ('豪',),
      # jōyō kanji #657
      '克'        : ('克',),
      # jōyō kanji #658
      '告'        : ('告',),
      # jōyō kanji #659
      '谷'        : ('谷',),
      # jōyō kanji #660
      '刻'        : ('刻',),
      # jōyō kanji #661
      '国'        : ('国', '國'),
      # jōyō kanji #662
      '黒'        : ('黒', '黑'),
      # jōyō kanji #663
      '穀'        : ('穀', '穀'),
      # jōyō kanji #664
      '酷'        : ('酷',),
      # jōyō kanji #665
      '獄'        : ('獄',),
      # jōyō kanji #666
      '骨'        : ('骨',),
      # jōyō kanji #667
      '駒'        : ('駒',),
      # jōyō kanji #668
      '込'        : ('込',),
      # jōyō kanji #669
      '頃'        : ('頃',),
      # jōyō kanji #670
      '今'        : ('今',),
      # jōyō kanji #671
      '困'        : ('困',),
      # jōyō kanji #672
      '昆'        : ('昆',),
      # jōyō kanji #673
      '恨'        : ('恨',),
      # jōyō kanji #674
      '根'        : ('根',),
      # jōyō kanji #675
      '婚'        : ('婚',),
      # jōyō kanji #676
      '混'        : ('混',),
      # jōyō kanji #677
      '痕'        : ('痕',),
      # jōyō kanji #678
      '紺'        : ('紺',),
      # jōyō kanji #679
      '魂'        : ('魂',),
      # jōyō kanji #680
      '墾'        : ('墾',),
      # jōyō kanji #681
      '懇'        : ('懇',),
      # jōyō kanji #682
      '左'        : ('左',),
      # jōyō kanji #683
      '佐'        : ('佐',),
      # jōyō kanji #684
      '沙'        : ('沙',),
      # jōyō kanji #685
      '査'        : ('査',),
      # jōyō kanji #686
      '砂'        : ('砂',),
      # jōyō kanji #687
      '唆'        : ('唆',),
      # jōyō kanji #688
      '差'        : ('差',),
      # jōyō kanji #689
      '詐'        : ('詐',),
      # jōyō kanji #690
      '鎖'        : ('鎖',),
      # jōyō kanji #691
      '座'        : ('座',),
      # jōyō kanji #692
      '挫'        : ('挫',),
      # jōyō kanji #693
      '才'        : ('才',),
      # jōyō kanji #694
      '再'        : ('再',),
      # jōyō kanji #695
      '災'        : ('災',),
      # jōyō kanji #696
      '妻'        : ('妻',),
      # jōyō kanji #697
      '采'        : ('采',),
      # jōyō kanji #698
      '砕'        : ('砕', '碎'),
      # jōyō kanji #699
      '宰'        : ('宰',),
      # jōyō kanji #700
      '栽'        : ('栽',),
      # jōyō kanji #701
      '彩'        : ('彩',),
      # jōyō kanji #702
      '採'        : ('採',),
      # jōyō kanji #703
      '済'        : ('済', '濟'),
      # jōyō kanji #704
      '祭'        : ('祭',),
      # jōyō kanji #705
      '斎'        : ('斎', '齋'),
      # jōyō kanji #706
      '細'        : ('細',),
      # jōyō kanji #707
      '菜'        : ('菜',),
      # jōyō kanji #708
      '最'        : ('最',),
      # jōyō kanji #709
      '裁'        : ('裁',),
      # jōyō kanji #710
      '債'        : ('債',),
      # jōyō kanji #711
      '催'        : ('催',),
      # jōyō kanji #712
      '塞'        : ('塞',),
      # jōyō kanji #713
      '歳'        : ('歳',),
      # jōyō kanji #714
      '載'        : ('載',),
      # jōyō kanji #715
      '際'        : ('際',),
      # jōyō kanji #716
      '埼'        : ('埼',),
      # jōyō kanji #717
      '在'        : ('在',),
      # jōyō kanji #718
      '材'        : ('材',),
      # jōyō kanji #719
      '剤'        : ('剤', '劑'),
      # jōyō kanji #720
      '財'        : ('財',),
      # jōyō kanji #721
      '罪'        : ('罪',),
      # jōyō kanji #722
      '崎'        : ('崎',),
      # jōyō kanji #723
      '作'        : ('作',),
      # jōyō kanji #724
      '削'        : ('削',),
      # jōyō kanji #725
      '昨'        : ('昨',),
      # jōyō kanji #726
      '柵'        : ('柵',),
      # jōyō kanji #727
      '索'        : ('索',),
      # jōyō kanji #728
      '策'        : ('策',),
      # jōyō kanji #729
      '酢'        : ('酢',),
      # jōyō kanji #730
      '搾'        : ('搾',),
      # jōyō kanji #731
      '錯'        : ('錯',),
      # jōyō kanji #732
      '咲'        : ('咲',),
      # jōyō kanji #733
      '冊'        : ('冊',),
      # jōyō kanji #734
      '札'        : ('札',),
      # jōyō kanji #735
      '刷'        : ('刷',),
      # jōyō kanji #736
      '刹'        : ('刹',),
      # jōyō kanji #737
      '拶'        : ('拶',),
      # jōyō kanji #738
      '殺'        : ('殺', '殺'),
      # jōyō kanji #739
      '察'        : ('察',),
      # jōyō kanji #740
      '撮'        : ('撮',),
      # jōyō kanji #741
      '擦'        : ('擦',),
      # jōyō kanji #742
      '雑'        : ('雑', '雜'),
      # jōyō kanji #743
      '皿'        : ('皿',),
      # jōyō kanji #744
      '三'        : ('三',),
      # jōyō kanji #745
      '山'        : ('山',),
      # jōyō kanji #746
      '参'        : ('参', '參'),
      # jōyō kanji #747
      '桟'        : ('桟', '棧'),
      # jōyō kanji #748
      '蚕'        : ('蚕', '蠶'),
      # jōyō kanji #749
      '惨'        : ('惨', '慘'),
      # jōyō kanji #750
      '産'        : ('産',),
      # jōyō kanji #751
      '傘'        : ('傘',),
      # jōyō kanji #752
      '散'        : ('散',),
      # jōyō kanji #753
      '算'        : ('算',),
      # jōyō kanji #754
      '酸'        : ('酸',),
      # jōyō kanji #755
      '賛'        : ('賛', '贊'),
      # jōyō kanji #756
      '残'        : ('残', '殘'),
      # jōyō kanji #757
      '斬'        : ('斬',),
      # jōyō kanji #758
      '暫'        : ('暫',),
      # jōyō kanji #759
      '士'        : ('士',),
      # jōyō kanji #760
      '子'        : ('子',),
      # jōyō kanji #761
      '支'        : ('支',),
      # jōyō kanji #762
      '止'        : ('止',),
      # jōyō kanji #763
      '氏'        : ('氏',),
      # jōyō kanji #764
      '仕'        : ('仕',),
      # jōyō kanji #765
      '史'        : ('史',),
      # jōyō kanji #766
      '司'        : ('司',),
      # jōyō kanji #767
      '四'        : ('四',),
      # jōyō kanji #768
      '市'        : ('市',),
      # jōyō kanji #769
      '矢'        : ('矢',),
      # jōyō kanji #770
      '旨'        : ('旨',),
      # jōyō kanji #771
      '死'        : ('死',),
      # jōyō kanji #772
      '糸'        : ('糸', '絲'),
      # jōyō kanji #773
      '至'        : ('至',),
      # jōyō kanji #774
      '伺'        : ('伺',),
      # jōyō kanji #775
      '志'        : ('志',),
      # jōyō kanji #776
      '私'        : ('私',),
      # jōyō kanji #777
      '使'        : ('使',),
      # jōyō kanji #778
      '刺'        : ('刺',),
      # jōyō kanji #779
      '始'        : ('始',),
      # jōyō kanji #780
      '姉'        : ('姉',),
      # jōyō kanji #781
      '枝'        : ('枝',),
      # jōyō kanji #782
      '祉'        : ('祉', '祉'),
      # jōyō kanji #783
      '肢'        : ('肢',),
      # jōyō kanji #784
      '姿'        : ('姿',),
      # jōyō kanji #785
      '思'        : ('思',),
      # jōyō kanji #786
      '指'        : ('指',),
      # jōyō kanji #787
      '施'        : ('施',),
      # jōyō kanji #788
      '師'        : ('師',),
      # jōyō kanji #789
      '恣'        : ('恣',),
      # jōyō kanji #790
      '紙'        : ('紙',),
      # jōyō kanji #791
      '脂'        : ('脂',),
      # jōyō kanji #792
      '視'        : ('視', '視'),
      # jōyō kanji #793
      '紫'        : ('紫',),
      # jōyō kanji #794
      '詞'        : ('詞',),
      # jōyō kanji #795
      '歯'        : ('歯', '齒'),
      # jōyō kanji #796
      '嗣'        : ('嗣',),
      # jōyō kanji #797
      '試'        : ('試',),
      # jōyō kanji #798
      '詩'        : ('詩',),
      # jōyō kanji #799
      '資'        : ('資',),
      # jōyō kanji #800
      '飼'        : ('飼',),
      # jōyō kanji #801
      '誌'        : ('誌',),
      # jōyō kanji #802
      '雌'        : ('雌',),
      # jōyō kanji #803
      '摯'        : ('摯',),
      # jōyō kanji #804
      '賜'        : ('賜',),
      # jōyō kanji #805
      '諮'        : ('諮',),
      # jōyō kanji #806
      '示'        : ('示',),
      # jōyō kanji #807
      '字'        : ('字',),
      # jōyō kanji #808
      '寺'        : ('寺',),
      # jōyō kanji #809
      '次'        : ('次',),
      # jōyō kanji #810
      '耳'        : ('耳',),
      # jōyō kanji #811
      '自'        : ('自',),
      # jōyō kanji #812
      '似'        : ('似',),
      # jōyō kanji #813
      '児'        : ('児', '兒'),
      # jōyō kanji #814
      '事'        : ('事',),
      # jōyō kanji #815
      '侍'        : ('侍',),
      # jōyō kanji #816
      '治'        : ('治',),
      # jōyō kanji #817
      '持'        : ('持',),
      # jōyō kanji #818
      '時'        : ('時',),
      # jōyō kanji #819
      '滋'        : ('滋',),
      # jōyō kanji #820
      '慈'        : ('慈',),
      # jōyō kanji #821
      '辞'        : ('辞', '辭'),
      # jōyō kanji #822
      '磁'        : ('磁',),
      # jōyō kanji #823
      '餌'        : ('餌',),
      # jōyō kanji #824
      '璽'        : ('璽',),
      # jōyō kanji #825
      '鹿'        : ('鹿',),
      # jōyō kanji #826
      '式'        : ('式',),
      # jōyō kanji #827
      '識'        : ('識',),
      # jōyō kanji #828
      '軸'        : ('軸',),
      # jōyō kanji #829
      '七'        : ('七',),
      # jōyō kanji #830
      '𠮟'        : ('𠮟',),
      # jōyō kanji #831
      '失'        : ('失',),
      # jōyō kanji #832
      '室'        : ('室',),
      # jōyō kanji #833
      '疾'        : ('疾',),
      # jōyō kanji #834
      '執'        : ('執',),
      # jōyō kanji #835
      '湿'        : ('湿', '濕'),
      # jōyō kanji #836
      '嫉'        : ('嫉',),
      # jōyō kanji #837
      '漆'        : ('漆',),
      # jōyō kanji #838
      '質'        : ('質',),
      # jōyō kanji #839
      '実'        : ('実', '實'),
      # jōyō kanji #840
      '芝'        : ('芝',),
      # jōyō kanji #841
      '写'        : ('写', '寫'),
      # jōyō kanji #842
      '社'        : ('社', '社'),
      # jōyō kanji #843
      '車'        : ('車',),
      # jōyō kanji #844
      '舎'        : ('舎',),
      # jōyō kanji #845
      '者'        : ('者', '者'),
      # jōyō kanji #846
      '射'        : ('射',),
      # jōyō kanji #847
      '捨'        : ('捨',),
      # jōyō kanji #848
      '赦'        : ('赦',),
      # jōyō kanji #849
      '斜'        : ('斜',),
      # jōyō kanji #850
      '煮'        : ('煮', '煮'),
      # jōyō kanji #851
      '遮'        : ('遮',),
      # jōyō kanji #852
      '謝'        : ('謝',),
      # jōyō kanji #853
      '邪'        : ('邪',),
      # jōyō kanji #854
      '蛇'        : ('蛇',),
      # jōyō kanji #855
      '尺'        : ('尺',),
      # jōyō kanji #856
      '借'        : ('借',),
      # jōyō kanji #857
      '酌'        : ('酌',),
      # jōyō kanji #858
      '釈'        : ('釈', '釋'),
      # jōyō kanji #859
      '爵'        : ('爵',),
      # jōyō kanji #860
      '若'        : ('若',),
      # jōyō kanji #861
      '弱'        : ('弱',),
      # jōyō kanji #862
      '寂'        : ('寂',),
      # jōyō kanji #863
      '手'        : ('手',),
      # jōyō kanji #864
      '主'        : ('主',),
      # jōyō kanji #865
      '守'        : ('守',),
      # jōyō kanji #866
      '朱'        : ('朱',),
      # jōyō kanji #867
      '取'        : ('取',),
      # jōyō kanji #868
      '狩'        : ('狩',),
      # jōyō kanji #869
      '首'        : ('首',),
      # jōyō kanji #870
      '殊'        : ('殊',),
      # jōyō kanji #871
      '珠'        : ('珠',),
      # jōyō kanji #872
      '酒'        : ('酒',),
      # jōyō kanji #873
      '腫'        : ('腫',),
      # jōyō kanji #874
      '種'        : ('種',),
      # jōyō kanji #875
      '趣'        : ('趣',),
      # jōyō kanji #876
      '寿'        : ('寿', '壽'),
      # jōyō kanji #877
      '受'        : ('受',),
      # jōyō kanji #878
      '呪'        : ('呪',),
      # jōyō kanji #879
      '授'        : ('授',),
      # jōyō kanji #880
      '需'        : ('需',),
      # jōyō kanji #881
      '儒'        : ('儒',),
      # jōyō kanji #882
      '樹'        : ('樹',),
      # jōyō kanji #883
      '収'        : ('収', '收'),
      # jōyō kanji #884
      '囚'        : ('囚',),
      # jōyō kanji #885
      '州'        : ('州',),
      # jōyō kanji #886
      '舟'        : ('舟',),
      # jōyō kanji #887
      '秀'        : ('秀',),
      # jōyō kanji #888
      '周'        : ('周',),
      # jōyō kanji #889
      '宗'        : ('宗',),
      # jōyō kanji #890
      '拾'        : ('拾',),
      # jōyō kanji #891
      '秋'        : ('秋',),
      # jōyō kanji #892
      '臭'        : ('臭', '臭'),
      # jōyō kanji #893
      '修'        : ('修',),
      # jōyō kanji #894
      '袖'        : ('袖',),
      # jōyō kanji #895
      '終'        : ('終',),
      # jōyō kanji #896
      '羞'        : ('羞',),
      # jōyō kanji #897
      '習'        : ('習',),
      # jōyō kanji #898
      '週'        : ('週',),
      # jōyō kanji #899
      '就'        : ('就',),
      # jōyō kanji #900
      '衆'        : ('衆',),
      # jōyō kanji #901
      '集'        : ('集',),
      # jōyō kanji #902
      '愁'        : ('愁',),
      # jōyō kanji #903
      '酬'        : ('酬',),
      # jōyō kanji #904
      '醜'        : ('醜',),
      # jōyō kanji #905
      '蹴'        : ('蹴',),
      # jōyō kanji #906
      '襲'        : ('襲',),
      # jōyō kanji #907
      '十'        : ('十',),
      # jōyō kanji #908
      '汁'        : ('汁',),
      # jōyō kanji #909
      '充'        : ('充',),
      # jōyō kanji #910
      '住'        : ('住',),
      # jōyō kanji #911
      '柔'        : ('柔',),
      # jōyō kanji #912
      '重'        : ('重',),
      # jōyō kanji #913
      '従'        : ('従', '從'),
      # jōyō kanji #914
      '渋'        : ('渋', '澁'),
      # jōyō kanji #915
      '銃'        : ('銃',),
      # jōyō kanji #916
      '獣'        : ('獣', '獸'),
      # jōyō kanji #917
      '縦'        : ('縦', '縱'),
      # jōyō kanji #918
      '叔'        : ('叔',),
      # jōyō kanji #919
      '祝'        : ('祝', '祝'),
      # jōyō kanji #920
      '宿'        : ('宿',),
      # jōyō kanji #921
      '淑'        : ('淑',),
      # jōyō kanji #922
      '粛'        : ('粛', '肅'),
      # jōyō kanji #923
      '縮'        : ('縮',),
      # jōyō kanji #924
      '塾'        : ('塾',),
      # jōyō kanji #925
      '熟'        : ('熟',),
      # jōyō kanji #926
      '出'        : ('出',),
      # jōyō kanji #927
      '述'        : ('述',),
      # jōyō kanji #928
      '術'        : ('術',),
      # jōyō kanji #929
      '俊'        : ('俊',),
      # jōyō kanji #930
      '春'        : ('春',),
      # jōyō kanji #931
      '瞬'        : ('瞬',),
      # jōyō kanji #932
      '旬'        : ('旬',),
      # jōyō kanji #933
      '巡'        : ('巡',),
      # jōyō kanji #934
      '盾'        : ('盾',),
      # jōyō kanji #935
      '准'        : ('准',),
      # jōyō kanji #936
      '殉'        : ('殉',),
      # jōyō kanji #937
      '純'        : ('純',),
      # jōyō kanji #938
      '循'        : ('循',),
      # jōyō kanji #939
      '順'        : ('順',),
      # jōyō kanji #940
      '準'        : ('準',),
      # jōyō kanji #941
      '潤'        : ('潤',),
      # jōyō kanji #942
      '遵'        : ('遵',),
      # jōyō kanji #943
      '処'        : ('処', '處'),
      # jōyō kanji #944
      '初'        : ('初',),
      # jōyō kanji #945
      '所'        : ('所',),
      # jōyō kanji #946
      '書'        : ('書',),
      # jōyō kanji #947
      '庶'        : ('庶',),
      # jōyō kanji #948
      '暑'        : ('暑', '暑'),
      # jōyō kanji #949
      '署'        : ('署', '署'),
      # jōyō kanji #950
      '緒'        : ('緒', '緖'),
      # jōyō kanji #951
      '諸'        : ('諸', '諸'),
      # jōyō kanji #952
      '女'        : ('女',),
      # jōyō kanji #953
      '如'        : ('如',),
      # jōyō kanji #954
      '助'        : ('助',),
      # jōyō kanji #955
      '序'        : ('序',),
      # jōyō kanji #956
      '叙'        : ('叙', '敍'),
      # jōyō kanji #957
      '徐'        : ('徐',),
      # jōyō kanji #958
      '除'        : ('除',),
      # jōyō kanji #959
      '小'        : ('小',),
      # jōyō kanji #960
      '升'        : ('升',),
      # jōyō kanji #961
      '少'        : ('少',),
      # jōyō kanji #962
      '召'        : ('召',),
      # jōyō kanji #963
      '匠'        : ('匠',),
      # jōyō kanji #964
      '床'        : ('床',),
      # jōyō kanji #965
      '抄'        : ('抄',),
      # jōyō kanji #966
      '肖'        : ('肖',),
      # jōyō kanji #967
      '尚'        : ('尚',),
      # jōyō kanji #968
      '招'        : ('招',),
      # jōyō kanji #969
      '承'        : ('承',),
      # jōyō kanji #970
      '昇'        : ('昇',),
      # jōyō kanji #971
      '松'        : ('松',),
      # jōyō kanji #972
      '沼'        : ('沼',),
      # jōyō kanji #973
      '昭'        : ('昭',),
      # jōyō kanji #974
      '宵'        : ('宵',),
      # jōyō kanji #975
      '将'        : ('将', '將'),
      # jōyō kanji #976
      '消'        : ('消',),
      # jōyō kanji #977
      '症'        : ('症',),
      # jōyō kanji #978
      '祥'        : ('祥', '祥'),
      # jōyō kanji #979
      '称'        : ('称', '稱'),
      # jōyō kanji #980
      '笑'        : ('笑',),
      # jōyō kanji #981
      '唱'        : ('唱',),
      # jōyō kanji #982
      '商'        : ('商',),
      # jōyō kanji #983
      '渉'        : ('渉', '涉'),
      # jōyō kanji #984
      '章'        : ('章',),
      # jōyō kanji #985
      '紹'        : ('紹',),
      # jōyō kanji #986
      '訟'        : ('訟',),
      # jōyō kanji #987
      '勝'        : ('勝',),
      # jōyō kanji #988
      '掌'        : ('掌',),
      # jōyō kanji #989
      '晶'        : ('晶',),
      # jōyō kanji #990
      '焼'        : ('焼', '燒'),
      # jōyō kanji #991
      '焦'        : ('焦',),
      # jōyō kanji #992
      '硝'        : ('硝',),
      # jōyō kanji #993
      '粧'        : ('粧',),
      # jōyō kanji #994
      '詔'        : ('詔',),
      # jōyō kanji #995
      '証'        : ('証', '證'),
      # jōyō kanji #996
      '象'        : ('象',),
      # jōyō kanji #997
      '傷'        : ('傷',),
      # jōyō kanji #998
      '奨'        : ('奨', '奬'),
      # jōyō kanji #999
      '照'        : ('照',),
      # jōyō kanji #1000
      '詳'        : ('詳',),
      # jōyō kanji #1001
      '彰'        : ('彰',),
      # jōyō kanji #1002
      '障'        : ('障',),
      # jōyō kanji #1003
      '憧'        : ('憧',),
      # jōyō kanji #1004
      '衝'        : ('衝',),
      # jōyō kanji #1005
      '賞'        : ('賞',),
      # jōyō kanji #1006
      '償'        : ('償',),
      # jōyō kanji #1007
      '礁'        : ('礁',),
      # jōyō kanji #1008
      '鐘'        : ('鐘',),
      # jōyō kanji #1009
      '上'        : ('上',),
      # jōyō kanji #1010
      '丈'        : ('丈',),
      # jōyō kanji #1011
      '冗'        : ('冗',),
      # jōyō kanji #1012
      '条'        : ('条', '條'),
      # jōyō kanji #1013
      '状'        : ('状', '狀'),
      # jōyō kanji #1014
      '乗'        : ('乗', '乘'),
      # jōyō kanji #1015
      '城'        : ('城',),
      # jōyō kanji #1016
      '浄'        : ('浄', '淨'),
      # jōyō kanji #1017
      '剰'        : ('剰', '剩'),
      # jōyō kanji #1018
      '常'        : ('常',),
      # jōyō kanji #1019
      '情'        : ('情',),
      # jōyō kanji #1020
      '場'        : ('場',),
      # jōyō kanji #1021
      '畳'        : ('畳', '疊'),
      # jōyō kanji #1022
      '蒸'        : ('蒸',),
      # jōyō kanji #1023
      '縄'        : ('縄', '繩'),
      # jōyō kanji #1024
      '壌'        : ('壌', '壤'),
      # jōyō kanji #1025
      '嬢'        : ('嬢', '孃'),
      # jōyō kanji #1026
      '錠'        : ('錠',),
      # jōyō kanji #1027
      '譲'        : ('譲', '讓'),
      # jōyō kanji #1028
      '醸'        : ('醸', '釀'),
      # jōyō kanji #1029
      '色'        : ('色',),
      # jōyō kanji #1030
      '拭'        : ('拭',),
      # jōyō kanji #1031
      '食'        : ('食',),
      # jōyō kanji #1032
      '植'        : ('植',),
      # jōyō kanji #1033
      '殖'        : ('殖',),
      # jōyō kanji #1034
      '飾'        : ('飾',),
      # jōyō kanji #1035
      '触'        : ('触', '觸'),
      # jōyō kanji #1036
      '嘱'        : ('嘱', '囑'),
      # jōyō kanji #1037
      '織'        : ('織',),
      # jōyō kanji #1038
      '職'        : ('職',),
      # jōyō kanji #1039
      '辱'        : ('辱',),
      # jōyō kanji #1040
      '尻'        : ('尻',),
      # jōyō kanji #1041
      '心'        : ('心',),
      # jōyō kanji #1042
      '申'        : ('申',),
      # jōyō kanji #1043
      '伸'        : ('伸',),
      # jōyō kanji #1044
      '臣'        : ('臣',),
      # jōyō kanji #1045
      '芯'        : ('芯',),
      # jōyō kanji #1046
      '身'        : ('身',),
      # jōyō kanji #1047
      '辛'        : ('辛',),
      # jōyō kanji #1048
      '侵'        : ('侵',),
      # jōyō kanji #1049
      '信'        : ('信',),
      # jōyō kanji #1050
      '津'        : ('津',),
      # jōyō kanji #1051
      '神'        : ('神', '神'),
      # jōyō kanji #1052
      '唇'        : ('唇',),
      # jōyō kanji #1053
      '娠'        : ('娠',),
      # jōyō kanji #1054
      '振'        : ('振',),
      # jōyō kanji #1055
      '浸'        : ('浸',),
      # jōyō kanji #1056
      '真'        : ('真', '眞'),
      # jōyō kanji #1057
      '針'        : ('針',),
      # jōyō kanji #1058
      '深'        : ('深',),
      # jōyō kanji #1059
      '紳'        : ('紳',),
      # jōyō kanji #1060
      '進'        : ('進',),
      # jōyō kanji #1061
      '森'        : ('森',),
      # jōyō kanji #1062
      '診'        : ('診',),
      # jōyō kanji #1063
      '寝'        : ('寝', '寢'),
      # jōyō kanji #1064
      '慎'        : ('慎', '愼'),
      # jōyō kanji #1065
      '新'        : ('新',),
      # jōyō kanji #1066
      '審'        : ('審',),
      # jōyō kanji #1067
      '震'        : ('震',),
      # jōyō kanji #1068
      '薪'        : ('薪',),
      # jōyō kanji #1069
      '親'        : ('親',),
      # jōyō kanji #1070
      '人'        : ('人',),
      # jōyō kanji #1071
      '刃'        : ('刃',),
      # jōyō kanji #1072
      '仁'        : ('仁',),
      # jōyō kanji #1073
      '尽'        : ('尽', '盡'),
      # jōyō kanji #1074
      '迅'        : ('迅',),
      # jōyō kanji #1075
      '甚'        : ('甚',),
      # jōyō kanji #1076
      '陣'        : ('陣',),
      # jōyō kanji #1077
      '尋'        : ('尋',),
      # jōyō kanji #1078
      '腎'        : ('腎',),
      # jōyō kanji #1079
      '須'        : ('須',),
      # jōyō kanji #1080
      '図'        : ('図', '圖'),
      # jōyō kanji #1081
      '水'        : ('水',),
      # jōyō kanji #1082
      '吹'        : ('吹',),
      # jōyō kanji #1083
      '垂'        : ('垂',),
      # jōyō kanji #1084
      '炊'        : ('炊',),
      # jōyō kanji #1085
      '帥'        : ('帥',),
      # jōyō kanji #1086
      '粋'        : ('粋', '粹'),
      # jōyō kanji #1087
      '衰'        : ('衰',),
      # jōyō kanji #1088
      '推'        : ('推',),
      # jōyō kanji #1089
      '酔'        : ('酔', '醉'),
      # jōyō kanji #1090
      '遂'        : ('遂',),
      # jōyō kanji #1091
      '睡'        : ('睡',),
      # jōyō kanji #1092
      '穂'        : ('穂', '穗'),
      # jōyō kanji #1093
      '随'        : ('随', '隨'),
      # jōyō kanji #1094
      '髄'        : ('髄', '髓'),
      # jōyō kanji #1095
      '枢'        : ('枢', '樞'),
      # jōyō kanji #1096
      '崇'        : ('崇',),
      # jōyō kanji #1097
      '数'        : ('数', '數'),
      # jōyō kanji #1098
      '据'        : ('据',),
      # jōyō kanji #1099
      '杉'        : ('杉',),
      # jōyō kanji #1100
      '裾'        : ('裾',),
      # jōyō kanji #1101
      '寸'        : ('寸',),
      # jōyō kanji #1102
      '瀬'        : ('瀬', '瀨'),
      # jōyō kanji #1103
      '是'        : ('是',),
      # jōyō kanji #1104
      '井'        : ('井',),
      # jōyō kanji #1105
      '世'        : ('世',),
      # jōyō kanji #1106
      '正'        : ('正',),
      # jōyō kanji #1107
      '生'        : ('生',),
      # jōyō kanji #1108
      '成'        : ('成',),
      # jōyō kanji #1109
      '西'        : ('西',),
      # jōyō kanji #1110
      '声'        : ('声', '聲'),
      # jōyō kanji #1111
      '制'        : ('制',),
      # jōyō kanji #1112
      '姓'        : ('姓',),
      # jōyō kanji #1113
      '征'        : ('征',),
      # jōyō kanji #1114
      '性'        : ('性',),
      # jōyō kanji #1115
      '青'        : ('青',),
      # jōyō kanji #1116
      '斉'        : ('斉', '齊'),
      # jōyō kanji #1117
      '政'        : ('政',),
      # jōyō kanji #1118
      '星'        : ('星',),
      # jōyō kanji #1119
      '牲'        : ('牲',),
      # jōyō kanji #1120
      '省'        : ('省',),
      # jōyō kanji #1121
      '凄'        : ('凄',),
      # jōyō kanji #1122
      '逝'        : ('逝',),
      # jōyō kanji #1123
      '清'        : ('清',),
      # jōyō kanji #1124
      '盛'        : ('盛',),
      # jōyō kanji #1125
      '婿'        : ('婿',),
      # jōyō kanji #1126
      '晴'        : ('晴',),
      # jōyō kanji #1127
      '勢'        : ('勢',),
      # jōyō kanji #1128
      '聖'        : ('聖',),
      # jōyō kanji #1129
      '誠'        : ('誠',),
      # jōyō kanji #1130
      '精'        : ('精',),
      # jōyō kanji #1131
      '製'        : ('製',),
      # jōyō kanji #1132
      '誓'        : ('誓',),
      # jōyō kanji #1133
      '静'        : ('静', '靜'),
      # jōyō kanji #1134
      '請'        : ('請',),
      # jōyō kanji #1135
      '整'        : ('整',),
      # jōyō kanji #1136
      '醒'        : ('醒',),
      # jōyō kanji #1137
      '税'        : ('税',),
      # jōyō kanji #1138
      '夕'        : ('夕',),
      # jōyō kanji #1139
      '斥'        : ('斥',),
      # jōyō kanji #1140
      '石'        : ('石',),
      # jōyō kanji #1141
      '赤'        : ('赤',),
      # jōyō kanji #1142
      '昔'        : ('昔',),
      # jōyō kanji #1143
      '析'        : ('析',),
      # jōyō kanji #1144
      '席'        : ('席',),
      # jōyō kanji #1145
      '脊'        : ('脊',),
      # jōyō kanji #1146
      '隻'        : ('隻',),
      # jōyō kanji #1147
      '惜'        : ('惜',),
      # jōyō kanji #1148
      '戚'        : ('戚',),
      # jōyō kanji #1149
      '責'        : ('責',),
      # jōyō kanji #1150
      '跡'        : ('跡',),
      # jōyō kanji #1151
      '積'        : ('積',),
      # jōyō kanji #1152
      '績'        : ('績',),
      # jōyō kanji #1153
      '籍'        : ('籍',),
      # jōyō kanji #1154
      '切'        : ('切',),
      # jōyō kanji #1155
      '折'        : ('折',),
      # jōyō kanji #1156
      '拙'        : ('拙',),
      # jōyō kanji #1157
      '窃'        : ('窃', '竊'),
      # jōyō kanji #1158
      '接'        : ('接',),
      # jōyō kanji #1159
      '設'        : ('設',),
      # jōyō kanji #1160
      '雪'        : ('雪',),
      # jōyō kanji #1161
      '摂'        : ('摂', '攝'),
      # jōyō kanji #1162
      '節'        : ('節', '節'),
      # jōyō kanji #1163
      '説'        : ('説',),
      # jōyō kanji #1164
      '舌'        : ('舌',),
      # jōyō kanji #1165
      '絶'        : ('絶',),
      # jōyō kanji #1166
      '千'        : ('千',),
      # jōyō kanji #1167
      '川'        : ('川',),
      # jōyō kanji #1168
      '仙'        : ('仙',),
      # jōyō kanji #1169
      '占'        : ('占',),
      # jōyō kanji #1170
      '先'        : ('先',),
      # jōyō kanji #1171
      '宣'        : ('宣',),
      # jōyō kanji #1172
      '専'        : ('専', '專'),
      # jōyō kanji #1173
      '泉'        : ('泉',),
      # jōyō kanji #1174
      '浅'        : ('浅', '淺'),
      # jōyō kanji #1175
      '洗'        : ('洗',),
      # jōyō kanji #1176
      '染'        : ('染',),
      # jōyō kanji #1177
      '扇'        : ('扇',),
      # jōyō kanji #1178
      '栓'        : ('栓',),
      # jōyō kanji #1179
      '旋'        : ('旋',),
      # jōyō kanji #1180
      '船'        : ('船',),
      # jōyō kanji #1181
      '戦'        : ('戦', '戰'),
      # jōyō kanji #1182
      '煎'        : ('煎',),
      # jōyō kanji #1183
      '羨'        : ('羨',),
      # jōyō kanji #1184
      '腺'        : ('腺',),
      # jōyō kanji #1185
      '詮'        : ('詮',),
      # jōyō kanji #1186
      '践'        : ('践', '踐'),
      # jōyō kanji #1187
      '箋'        : ('箋',),
      # jōyō kanji #1188
      '銭'        : ('銭', '錢'),
      # jōyō kanji #1189
      '潜'        : ('潜', '潛'),
      # jōyō kanji #1190
      '線'        : ('線',),
      # jōyō kanji #1191
      '遷'        : ('遷',),
      # jōyō kanji #1192
      '選'        : ('選',),
      # jōyō kanji #1193
      '薦'        : ('薦',),
      # jōyō kanji #1194
      '繊'        : ('繊', '纖'),
      # jōyō kanji #1195
      '鮮'        : ('鮮',),
      # jōyō kanji #1196
      '全'        : ('全',),
      # jōyō kanji #1197
      '前'        : ('前',),
      # jōyō kanji #1198
      '善'        : ('善',),
      # jōyō kanji #1199
      '然'        : ('然',),
      # jōyō kanji #1200
      '禅'        : ('禅', '禪'),
      # jōyō kanji #1201
      '漸'        : ('漸',),
      # jōyō kanji #1202
      '膳'        : ('膳',),
      # jōyō kanji #1203
      '繕'        : ('繕',),
      # jōyō kanji #1204
      '狙'        : ('狙',),
      # jōyō kanji #1205
      '阻'        : ('阻',),
      # jōyō kanji #1206
      '祖'        : ('祖', '祖'),
      # jōyō kanji #1207
      '租'        : ('租',),
      # jōyō kanji #1208
      '素'        : ('素',),
      # jōyō kanji #1209
      '措'        : ('措',),
      # jōyō kanji #1210
      '粗'        : ('粗',),
      # jōyō kanji #1211
      '組'        : ('組',),
      # jōyō kanji #1212
      '疎'        : ('疎',),
      # jōyō kanji #1213
      '訴'        : ('訴',),
      # jōyō kanji #1214
      '塑'        : ('塑',),
      # jōyō kanji #1215
      '遡'        : ('遡',),
      # jōyō kanji #1216
      '礎'        : ('礎',),
      # jōyō kanji #1217
      '双'        : ('双', '雙'),
      # jōyō kanji #1218
      '壮'        : ('壮', '壯'),
      # jōyō kanji #1219
      '早'        : ('早',),
      # jōyō kanji #1220
      '争'        : ('争', '爭'),
      # jōyō kanji #1221
      '走'        : ('走',),
      # jōyō kanji #1222
      '奏'        : ('奏',),
      # jōyō kanji #1223
      '相'        : ('相',),
      # jōyō kanji #1224
      '荘'        : ('荘', '莊'),
      # jōyō kanji #1225
      '草'        : ('草',),
      # jōyō kanji #1226
      '送'        : ('送',),
      # jōyō kanji #1227
      '倉'        : ('倉',),
      # jōyō kanji #1228
      '捜'        : ('捜', '搜'),
      # jōyō kanji #1229
      '挿'        : ('挿', '插'),
      # jōyō kanji #1230
      '桑'        : ('桑',),
      # jōyō kanji #1231
      '巣'        : ('巣', '巢'),
      # jōyō kanji #1232
      '掃'        : ('掃',),
      # jōyō kanji #1233
      '曹'        : ('曹',),
      # jōyō kanji #1234
      '曽'        : ('曽', '曾'),
      # jōyō kanji #1235
      '爽'        : ('爽',),
      # jōyō kanji #1236
      '窓'        : ('窓',),
      # jōyō kanji #1237
      '創'        : ('創',),
      # jōyō kanji #1238
      '喪'        : ('喪',),
      # jōyō kanji #1239
      '痩'        : ('痩', '瘦'),
      # jōyō kanji #1240
      '葬'        : ('葬',),
      # jōyō kanji #1241
      '装'        : ('装', '裝'),
      # jōyō kanji #1242
      '僧'        : ('僧', '僧'),
      # jōyō kanji #1243
      '想'        : ('想',),
      # jōyō kanji #1244
      '層'        : ('層', '層'),
      # jōyō kanji #1245
      '総'        : ('総', '總'),
      # jōyō kanji #1246
      '遭'        : ('遭',),
      # jōyō kanji #1247
      '槽'        : ('槽',),
      # jōyō kanji #1248
      '踪'        : ('踪',),
      # jōyō kanji #1249
      '操'        : ('操',),
      # jōyō kanji #1250
      '燥'        : ('燥',),
      # jōyō kanji #1251
      '霜'        : ('霜',),
      # jōyō kanji #1252
      '騒'        : ('騒', '騷'),
      # jōyō kanji #1253
      '藻'        : ('藻',),
      # jōyō kanji #1254
      '造'        : ('造',),
      # jōyō kanji #1255
      '像'        : ('像',),
      # jōyō kanji #1256
      '増'        : ('増', '增'),
      # jōyō kanji #1257
      '憎'        : ('憎', '憎'),
      # jōyō kanji #1258
      '蔵'        : ('蔵', '藏'),
      # jōyō kanji #1259
      '贈'        : ('贈', '贈'),
      # jōyō kanji #1260
      '臓'        : ('臓', '臟'),
      # jōyō kanji #1261
      '即'        : ('即', '卽'),
      # jōyō kanji #1262
      '束'        : ('束',),
      # jōyō kanji #1263
      '足'        : ('足',),
      # jōyō kanji #1264
      '促'        : ('促',),
      # jōyō kanji #1265
      '則'        : ('則',),
      # jōyō kanji #1266
      '息'        : ('息',),
      # jōyō kanji #1267
      '捉'        : ('捉',),
      # jōyō kanji #1268
      '速'        : ('速',),
      # jōyō kanji #1269
      '側'        : ('側',),
      # jōyō kanji #1270
      '測'        : ('測',),
      # jōyō kanji #1271
      '俗'        : ('俗',),
      # jōyō kanji #1272
      '族'        : ('族',),
      # jōyō kanji #1273
      '属'        : ('属', '屬'),
      # jōyō kanji #1274
      '賊'        : ('賊',),
      # jōyō kanji #1275
      '続'        : ('続', '續'),
      # jōyō kanji #1276
      '卒'        : ('卒',),
      # jōyō kanji #1277
      '率'        : ('率',),
      # jōyō kanji #1278
      '存'        : ('存',),
      # jōyō kanji #1279
      '村'        : ('村',),
      # jōyō kanji #1280
      '孫'        : ('孫',),
      # jōyō kanji #1281
      '尊'        : ('尊',),
      # jōyō kanji #1282
      '損'        : ('損',),
      # jōyō kanji #1283
      '遜'        : ('遜',),
      # jōyō kanji #1284
      '他'        : ('他',),
      # jōyō kanji #1285
      '多'        : ('多',),
      # jōyō kanji #1286
      '汰'        : ('汰',),
      # jōyō kanji #1287
      '打'        : ('打',),
      # jōyō kanji #1288
      '妥'        : ('妥',),
      # jōyō kanji #1289
      '唾'        : ('唾',),
      # jōyō kanji #1290
      '堕'        : ('堕', '墮'),
      # jōyō kanji #1291
      '惰'        : ('惰',),
      # jōyō kanji #1292
      '駄'        : ('駄',),
      # jōyō kanji #1293
      '太'        : ('太',),
      # jōyō kanji #1294
      '対'        : ('対', '對'),
      # jōyō kanji #1295
      '体'        : ('体', '體'),
      # jōyō kanji #1296
      '耐'        : ('耐',),
      # jōyō kanji #1297
      '待'        : ('待',),
      # jōyō kanji #1298
      '怠'        : ('怠',),
      # jōyō kanji #1299
      '胎'        : ('胎',),
      # jōyō kanji #1300
      '退'        : ('退',),
      # jōyō kanji #1301
      '帯'        : ('帯', '帶'),
      # jōyō kanji #1302
      '泰'        : ('泰',),
      # jōyō kanji #1303
      '堆'        : ('堆',),
      # jōyō kanji #1304
      '袋'        : ('袋',),
      # jōyō kanji #1305
      '逮'        : ('逮',),
      # jōyō kanji #1306
      '替'        : ('替',),
      # jōyō kanji #1307
      '貸'        : ('貸',),
      # jōyō kanji #1308
      '隊'        : ('隊',),
      # jōyō kanji #1309
      '滞'        : ('滞', '滯'),
      # jōyō kanji #1310
      '態'        : ('態',),
      # jōyō kanji #1311
      '戴'        : ('戴',),
      # jōyō kanji #1312
      '大'        : ('大',),
      # jōyō kanji #1313
      '代'        : ('代',),
      # jōyō kanji #1314
      '台'        : ('台', '臺'),
      # jōyō kanji #1315
      '第'        : ('第',),
      # jōyō kanji #1316
      '題'        : ('題',),
      # jōyō kanji #1317
      '滝'        : ('滝', '瀧'),
      # jōyō kanji #1318
      '宅'        : ('宅',),
      # jōyō kanji #1319
      '択'        : ('択', '擇'),
      # jōyō kanji #1320
      '沢'        : ('沢', '澤'),
      # jōyō kanji #1321
      '卓'        : ('卓',),
      # jōyō kanji #1322
      '拓'        : ('拓',),
      # jōyō kanji #1323
      '託'        : ('託',),
      # jōyō kanji #1324
      '濯'        : ('濯',),
      # jōyō kanji #1325
      '諾'        : ('諾',),
      # jōyō kanji #1326
      '濁'        : ('濁',),
      # jōyō kanji #1327
      '但'        : ('但',),
      # jōyō kanji #1328
      '達'        : ('達',),
      # jōyō kanji #1329
      '脱'        : ('脱',),
      # jōyō kanji #1330
      '奪'        : ('奪',),
      # jōyō kanji #1331
      '棚'        : ('棚',),
      # jōyō kanji #1332
      '誰'        : ('誰',),
      # jōyō kanji #1333
      '丹'        : ('丹',),
      # jōyō kanji #1334
      '旦'        : ('旦',),
      # jōyō kanji #1335
      '担'        : ('担', '擔'),
      # jōyō kanji #1336
      '単'        : ('単', '單'),
      # jōyō kanji #1337
      '炭'        : ('炭',),
      # jōyō kanji #1338
      '胆'        : ('胆', '膽'),
      # jōyō kanji #1339
      '探'        : ('探',),
      # jōyō kanji #1340
      '淡'        : ('淡',),
      # jōyō kanji #1341
      '短'        : ('短',),
      # jōyō kanji #1342
      '嘆'        : ('嘆', '嘆'),
      # jōyō kanji #1343
      '端'        : ('端',),
      # jōyō kanji #1344
      '綻'        : ('綻',),
      # jōyō kanji #1345
      '誕'        : ('誕',),
      # jōyō kanji #1346
      '鍛'        : ('鍛',),
      # jōyō kanji #1347
      '団'        : ('団', '團'),
      # jōyō kanji #1348
      '男'        : ('男',),
      # jōyō kanji #1349
      '段'        : ('段',),
      # jōyō kanji #1350
      '断'        : ('断', '斷'),
      # jōyō kanji #1351
      '弾'        : ('弾', '彈'),
      # jōyō kanji #1352
      '暖'        : ('暖',),
      # jōyō kanji #1353
      '談'        : ('談',),
      # jōyō kanji #1354
      '壇'        : ('壇',),
      # jōyō kanji #1355
      '地'        : ('地',),
      # jōyō kanji #1356
      '池'        : ('池',),
      # jōyō kanji #1357
      '知'        : ('知',),
      # jōyō kanji #1358
      '値'        : ('値',),
      # jōyō kanji #1359
      '恥'        : ('恥',),
      # jōyō kanji #1360
      '致'        : ('致',),
      # jōyō kanji #1361
      '遅'        : ('遅', '遲'),
      # jōyō kanji #1362
      '痴'        : ('痴', '癡'),
      # jōyō kanji #1363
      '稚'        : ('稚',),
      # jōyō kanji #1364
      '置'        : ('置',),
      # jōyō kanji #1365
      '緻'        : ('緻',),
      # jōyō kanji #1366
      '竹'        : ('竹',),
      # jōyō kanji #1367
      '畜'        : ('畜',),
      # jōyō kanji #1368
      '逐'        : ('逐',),
      # jōyō kanji #1369
      '蓄'        : ('蓄',),
      # jōyō kanji #1370
      '築'        : ('築',),
      # jōyō kanji #1371
      '秩'        : ('秩',),
      # jōyō kanji #1372
      '窒'        : ('窒',),
      # jōyō kanji #1373
      '茶'        : ('茶',),
      # jōyō kanji #1374
      '着'        : ('着',),
      # jōyō kanji #1375
      '嫡'        : ('嫡',),
      # jōyō kanji #1376
      '中'        : ('中',),
      # jōyō kanji #1377
      '仲'        : ('仲',),
      # jōyō kanji #1378
      '虫'        : ('虫', '蟲'),
      # jōyō kanji #1379
      '沖'        : ('沖',),
      # jōyō kanji #1380
      '宙'        : ('宙',),
      # jōyō kanji #1381
      '忠'        : ('忠',),
      # jōyō kanji #1382
      '抽'        : ('抽',),
      # jōyō kanji #1383
      '注'        : ('注',),
      # jōyō kanji #1384
      '昼'        : ('昼', '晝'),
      # jōyō kanji #1385
      '柱'        : ('柱',),
      # jōyō kanji #1386
      '衷'        : ('衷',),
      # jōyō kanji #1387
      '酎'        : ('酎',),
      # jōyō kanji #1388
      '鋳'        : ('鋳', '鑄'),
      # jōyō kanji #1389
      '駐'        : ('駐',),
      # jōyō kanji #1390
      '著'        : ('著', '著'),
      # jōyō kanji #1391
      '貯'        : ('貯',),
      # jōyō kanji #1392
      '丁'        : ('丁',),
      # jōyō kanji #1393
      '弔'        : ('弔',),
      # jōyō kanji #1394
      '庁'        : ('庁', '廳'),
      # jōyō kanji #1395
      '兆'        : ('兆',),
      # jōyō kanji #1396
      '町'        : ('町',),
      # jōyō kanji #1397
      '長'        : ('長',),
      # jōyō kanji #1398
      '挑'        : ('挑',),
      # jōyō kanji #1399
      '帳'        : ('帳',),
      # jōyō kanji #1400
      '張'        : ('張',),
      # jōyō kanji #1401
      '彫'        : ('彫',),
      # jōyō kanji #1402
      '眺'        : ('眺',),
      # jōyō kanji #1403
      '釣'        : ('釣',),
      # jōyō kanji #1404
      '頂'        : ('頂',),
      # jōyō kanji #1405
      '鳥'        : ('鳥',),
      # jōyō kanji #1406
      '朝'        : ('朝',),
      # jōyō kanji #1407
      '貼'        : ('貼',),
      # jōyō kanji #1408
      '超'        : ('超',),
      # jōyō kanji #1409
      '腸'        : ('腸',),
      # jōyō kanji #1410
      '跳'        : ('跳',),
      # jōyō kanji #1411
      '徴'        : ('徴', '徵'),
      # jōyō kanji #1412
      '嘲'        : ('嘲',),
      # jōyō kanji #1413
      '潮'        : ('潮',),
      # jōyō kanji #1414
      '澄'        : ('澄',),
      # jōyō kanji #1415
      '調'        : ('調',),
      # jōyō kanji #1416
      '聴'        : ('聴', '聽'),
      # jōyō kanji #1417
      '懲'        : ('懲', '懲'),
      # jōyō kanji #1418
      '直'        : ('直',),
      # jōyō kanji #1419
      '勅'        : ('勅', '敕'),
      # jōyō kanji #1420
      '捗'        : ('捗',),
      # jōyō kanji #1421
      '沈'        : ('沈',),
      # jōyō kanji #1422
      '珍'        : ('珍',),
      # jōyō kanji #1423
      '朕'        : ('朕',),
      # jōyō kanji #1424
      '陳'        : ('陳',),
      # jōyō kanji #1425
      '賃'        : ('賃',),
      # jōyō kanji #1426
      '鎮'        : ('鎮', '鎭'),
      # jōyō kanji #1427
      '追'        : ('追',),
      # jōyō kanji #1428
      '椎'        : ('椎',),
      # jōyō kanji #1429
      '墜'        : ('墜',),
      # jōyō kanji #1430
      '通'        : ('通',),
      # jōyō kanji #1431
      '痛'        : ('痛',),
      # jōyō kanji #1432
      '塚'        : ('塚', '塚'),
      # jōyō kanji #1433
      '漬'        : ('漬',),
      # jōyō kanji #1434
      '坪'        : ('坪',),
      # jōyō kanji #1435
      '爪'        : ('爪',),
      # jōyō kanji #1436
      '鶴'        : ('鶴',),
      # jōyō kanji #1437
      '低'        : ('低',),
      # jōyō kanji #1438
      '呈'        : ('呈',),
      # jōyō kanji #1439
      '廷'        : ('廷',),
      # jōyō kanji #1440
      '弟'        : ('弟',),
      # jōyō kanji #1441
      '定'        : ('定',),
      # jōyō kanji #1442
      '底'        : ('底',),
      # jōyō kanji #1443
      '抵'        : ('抵',),
      # jōyō kanji #1444
      '邸'        : ('邸',),
      # jōyō kanji #1445
      '亭'        : ('亭',),
      # jōyō kanji #1446
      '貞'        : ('貞',),
      # jōyō kanji #1447
      '帝'        : ('帝',),
      # jōyō kanji #1448
      '訂'        : ('訂',),
      # jōyō kanji #1449
      '庭'        : ('庭',),
      # jōyō kanji #1450
      '逓'        : ('逓', '遞'),
      # jōyō kanji #1451
      '停'        : ('停',),
      # jōyō kanji #1452
      '偵'        : ('偵',),
      # jōyō kanji #1453
      '堤'        : ('堤',),
      # jōyō kanji #1454
      '提'        : ('提',),
      # jōyō kanji #1455
      '程'        : ('程',),
      # jōyō kanji #1456
      '艇'        : ('艇',),
      # jōyō kanji #1457
      '締'        : ('締',),
      # jōyō kanji #1458
      '諦'        : ('諦',),
      # jōyō kanji #1459
      '泥'        : ('泥',),
      # jōyō kanji #1460
      '的'        : ('的',),
      # jōyō kanji #1461
      '笛'        : ('笛',),
      # jōyō kanji #1462
      '摘'        : ('摘',),
      # jōyō kanji #1463
      '滴'        : ('滴',),
      # jōyō kanji #1464
      '適'        : ('適',),
      # jōyō kanji #1465
      '敵'        : ('敵',),
      # jōyō kanji #1466
      '溺'        : ('溺',),
      # jōyō kanji #1467
      '迭'        : ('迭',),
      # jōyō kanji #1468
      '哲'        : ('哲',),
      # jōyō kanji #1469
      '鉄'        : ('鉄', '鐵'),
      # jōyō kanji #1470
      '徹'        : ('徹',),
      # jōyō kanji #1471
      '撤'        : ('撤',),
      # jōyō kanji #1472
      '天'        : ('天',),
      # jōyō kanji #1473
      '典'        : ('典',),
      # jōyō kanji #1474
      '店'        : ('店',),
      # jōyō kanji #1475
      '点'        : ('点', '點'),
      # jōyō kanji #1476
      '展'        : ('展',),
      # jōyō kanji #1477
      '添'        : ('添',),
      # jōyō kanji #1478
      '転'        : ('転', '轉'),
      # jōyō kanji #1479
      '塡'        : ('塡',),
      # jōyō kanji #1480
      '田'        : ('田',),
      # jōyō kanji #1481
      '伝'        : ('伝', '傳'),
      # jōyō kanji #1482
      '殿'        : ('殿',),
      # jōyō kanji #1483
      '電'        : ('電',),
      # jōyō kanji #1484
      '斗'        : ('斗',),
      # jōyō kanji #1485
      '吐'        : ('吐',),
      # jōyō kanji #1486
      '妬'        : ('妬',),
      # jōyō kanji #1487
      '徒'        : ('徒',),
      # jōyō kanji #1488
      '途'        : ('途',),
      # jōyō kanji #1489
      '都'        : ('都', '都'),
      # jōyō kanji #1490
      '渡'        : ('渡',),
      # jōyō kanji #1491
      '塗'        : ('塗',),
      # jōyō kanji #1492
      '賭'        : ('賭',),
      # jōyō kanji #1493
      '土'        : ('土',),
      # jōyō kanji #1494
      '奴'        : ('奴',),
      # jōyō kanji #1495
      '努'        : ('努',),
      # jōyō kanji #1496
      '度'        : ('度',),
      # jōyō kanji #1497
      '怒'        : ('怒',),
      # jōyō kanji #1498
      '刀'        : ('刀',),
      # jōyō kanji #1499
      '冬'        : ('冬',),
      # jōyō kanji #1500
      '灯'        : ('灯', '燈'),
      # jōyō kanji #1501
      '当'        : ('当', '當'),
      # jōyō kanji #1502
      '投'        : ('投',),
      # jōyō kanji #1503
      '豆'        : ('豆',),
      # jōyō kanji #1504
      '東'        : ('東',),
      # jōyō kanji #1505
      '到'        : ('到',),
      # jōyō kanji #1506
      '逃'        : ('逃',),
      # jōyō kanji #1507
      '倒'        : ('倒',),
      # jōyō kanji #1508
      '凍'        : ('凍',),
      # jōyō kanji #1509
      '唐'        : ('唐',),
      # jōyō kanji #1510
      '島'        : ('島',),
      # jōyō kanji #1511
      '桃'        : ('桃',),
      # jōyō kanji #1512
      '討'        : ('討',),
      # jōyō kanji #1513
      '透'        : ('透',),
      # jōyō kanji #1514
      '党'        : ('党', '黨'),
      # jōyō kanji #1515
      '悼'        : ('悼',),
      # jōyō kanji #1516
      '盗'        : ('盗', '盜'),
      # jōyō kanji #1517
      '陶'        : ('陶',),
      # jōyō kanji #1518
      '塔'        : ('塔',),
      # jōyō kanji #1519
      '搭'        : ('搭',),
      # jōyō kanji #1520
      '棟'        : ('棟',),
      # jōyō kanji #1521
      '湯'        : ('湯',),
      # jōyō kanji #1522
      '痘'        : ('痘',),
      # jōyō kanji #1523
      '登'        : ('登',),
      # jōyō kanji #1524
      '答'        : ('答',),
      # jōyō kanji #1525
      '等'        : ('等',),
      # jōyō kanji #1526
      '筒'        : ('筒',),
      # jōyō kanji #1527
      '統'        : ('統',),
      # jōyō kanji #1528
      '稲'        : ('稲', '稻'),
      # jōyō kanji #1529
      '踏'        : ('踏',),
      # jōyō kanji #1530
      '糖'        : ('糖',),
      # jōyō kanji #1531
      '頭'        : ('頭',),
      # jōyō kanji #1532
      '謄'        : ('謄',),
      # jōyō kanji #1533
      '藤'        : ('藤',),
      # jōyō kanji #1534
      '闘'        : ('闘', '鬭'),
      # jōyō kanji #1535
      '騰'        : ('騰',),
      # jōyō kanji #1536
      '同'        : ('同',),
      # jōyō kanji #1537
      '洞'        : ('洞',),
      # jōyō kanji #1538
      '胴'        : ('胴',),
      # jōyō kanji #1539
      '動'        : ('動',),
      # jōyō kanji #1540
      '堂'        : ('堂',),
      # jōyō kanji #1541
      '童'        : ('童',),
      # jōyō kanji #1542
      '道'        : ('道',),
      # jōyō kanji #1543
      '働'        : ('働',),
      # jōyō kanji #1544
      '銅'        : ('銅',),
      # jōyō kanji #1545
      '導'        : ('導',),
      # jōyō kanji #1546
      '瞳'        : ('瞳',),
      # jōyō kanji #1547
      '峠'        : ('峠',),
      # jōyō kanji #1548
      '匿'        : ('匿',),
      # jōyō kanji #1549
      '特'        : ('特',),
      # jōyō kanji #1550
      '得'        : ('得',),
      # jōyō kanji #1551
      '督'        : ('督',),
      # jōyō kanji #1552
      '徳'        : ('徳', '德'),
      # jōyō kanji #1553
      '篤'        : ('篤',),
      # jōyō kanji #1554
      '毒'        : ('毒',),
      # jōyō kanji #1555
      '独'        : ('独', '獨'),
      # jōyō kanji #1556
      '読'        : ('読', '讀'),
      # jōyō kanji #1557
      '栃'        : ('栃',),
      # jōyō kanji #1558
      '凸'        : ('凸',),
      # jōyō kanji #1559
      '突'        : ('突', '突'),
      # jōyō kanji #1560
      '届'        : ('届', '屆'),
      # jōyō kanji #1561
      '屯'        : ('屯',),
      # jōyō kanji #1562
      '豚'        : ('豚',),
      # jōyō kanji #1563
      '頓'        : ('頓',),
      # jōyō kanji #1564
      '貪'        : ('貪',),
      # jōyō kanji #1565
      '鈍'        : ('鈍',),
      # jōyō kanji #1566
      '曇'        : ('曇',),
      # jōyō kanji #1567
      '丼'        : ('丼',),
      # jōyō kanji #1568
      '那'        : ('那',),
      # jōyō kanji #1569
      '奈'        : ('奈',),
      # jōyō kanji #1570
      '内'        : ('内',),
      # jōyō kanji #1571
      '梨'        : ('梨',),
      # jōyō kanji #1572
      '謎'        : ('謎',),
      # jōyō kanji #1573
      '鍋'        : ('鍋',),
      # jōyō kanji #1574
      '南'        : ('南',),
      # jōyō kanji #1575
      '軟'        : ('軟',),
      # jōyō kanji #1576
      '難'        : ('難', '難'),
      # jōyō kanji #1577
      '二'        : ('二',),
      # jōyō kanji #1578
      '尼'        : ('尼',),
      # jōyō kanji #1579
      '弐'        : ('弐', '貳'),
      # jōyō kanji #1580
      '匂'        : ('匂',),
      # jōyō kanji #1581
      '肉'        : ('肉',),
      # jōyō kanji #1582
      '虹'        : ('虹',),
      # jōyō kanji #1583
      '日'        : ('日',),
      # jōyō kanji #1584
      '入'        : ('入',),
      # jōyō kanji #1585
      '乳'        : ('乳',),
      # jōyō kanji #1586
      '尿'        : ('尿',),
      # jōyō kanji #1587
      '任'        : ('任',),
      # jōyō kanji #1588
      '妊'        : ('妊',),
      # jōyō kanji #1589
      '忍'        : ('忍',),
      # jōyō kanji #1590
      '認'        : ('認',),
      # jōyō kanji #1591
      '寧'        : ('寧',),
      # jōyō kanji #1592
      '熱'        : ('熱',),
      # jōyō kanji #1593
      '年'        : ('年',),
      # jōyō kanji #1594
      '念'        : ('念',),
      # jōyō kanji #1595
      '捻'        : ('捻',),
      # jōyō kanji #1596
      '粘'        : ('粘',),
      # jōyō kanji #1597
      '燃'        : ('燃',),
      # jōyō kanji #1598
      '悩'        : ('悩', '惱'),
      # jōyō kanji #1599
      '納'        : ('納',),
      # jōyō kanji #1600
      '能'        : ('能',),
      # jōyō kanji #1601
      '脳'        : ('脳', '腦'),
      # jōyō kanji #1602
      '農'        : ('農',),
      # jōyō kanji #1603
      '濃'        : ('濃',),
      # jōyō kanji #1604
      '把'        : ('把',),
      # jōyō kanji #1605
      '波'        : ('波',),
      # jōyō kanji #1606
      '派'        : ('派',),
      # jōyō kanji #1607
      '破'        : ('破',),
      # jōyō kanji #1608
      '覇'        : ('覇', '霸'),
      # jōyō kanji #1609
      '馬'        : ('馬',),
      # jōyō kanji #1610
      '婆'        : ('婆',),
      # jōyō kanji #1611
      '罵'        : ('罵',),
      # jōyō kanji #1612
      '拝'        : ('拝', '拜'),
      # jōyō kanji #1613
      '杯'        : ('杯',),
      # jōyō kanji #1614
      '背'        : ('背',),
      # jōyō kanji #1615
      '肺'        : ('肺',),
      # jōyō kanji #1616
      '俳'        : ('俳',),
      # jōyō kanji #1617
      '配'        : ('配',),
      # jōyō kanji #1618
      '排'        : ('排',),
      # jōyō kanji #1619
      '敗'        : ('敗',),
      # jōyō kanji #1620
      '廃'        : ('廃', '廢'),
      # jōyō kanji #1621
      '輩'        : ('輩',),
      # jōyō kanji #1622
      '売'        : ('売', '賣'),
      # jōyō kanji #1623
      '倍'        : ('倍',),
      # jōyō kanji #1624
      '梅'        : ('梅', '梅'),
      # jōyō kanji #1625
      '培'        : ('培',),
      # jōyō kanji #1626
      '陪'        : ('陪',),
      # jōyō kanji #1627
      '媒'        : ('媒',),
      # jōyō kanji #1628
      '買'        : ('買',),
      # jōyō kanji #1629
      '賠'        : ('賠',),
      # jōyō kanji #1630
      '白'        : ('白',),
      # jōyō kanji #1631
      '伯'        : ('伯',),
      # jōyō kanji #1632
      '拍'        : ('拍',),
      # jōyō kanji #1633
      '泊'        : ('泊',),
      # jōyō kanji #1634
      '迫'        : ('迫',),
      # jōyō kanji #1635
      '剝'        : ('剝',),
      # jōyō kanji #1636
      '舶'        : ('舶',),
      # jōyō kanji #1637
      '博'        : ('博',),
      # jōyō kanji #1638
      '薄'        : ('薄',),
      # jōyō kanji #1639
      '麦'        : ('麦', '麥'),
      # jōyō kanji #1640
      '漠'        : ('漠',),
      # jōyō kanji #1641
      '縛'        : ('縛',),
      # jōyō kanji #1642
      '爆'        : ('爆',),
      # jōyō kanji #1643
      '箱'        : ('箱',),
      # jōyō kanji #1644
      '箸'        : ('箸',),
      # jōyō kanji #1645
      '畑'        : ('畑',),
      # jōyō kanji #1646
      '肌'        : ('肌',),
      # jōyō kanji #1647
      '八'        : ('八',),
      # jōyō kanji #1648
      '鉢'        : ('鉢',),
      # jōyō kanji #1649
      '発'        : ('発', '發'),
      # jōyō kanji #1650
      '髪'        : ('髪', '髮'),
      # jōyō kanji #1651
      '伐'        : ('伐',),
      # jōyō kanji #1652
      '抜'        : ('抜', '拔'),
      # jōyō kanji #1653
      '罰'        : ('罰',),
      # jōyō kanji #1654
      '閥'        : ('閥',),
      # jōyō kanji #1655
      '反'        : ('反',),
      # jōyō kanji #1656
      '半'        : ('半',),
      # jōyō kanji #1657
      '氾'        : ('氾',),
      # jōyō kanji #1658
      '犯'        : ('犯',),
      # jōyō kanji #1659
      '帆'        : ('帆',),
      # jōyō kanji #1660
      '汎'        : ('汎',),
      # jōyō kanji #1661
      '伴'        : ('伴',),
      # jōyō kanji #1662
      '判'        : ('判',),
      # jōyō kanji #1663
      '坂'        : ('坂',),
      # jōyō kanji #1664
      '阪'        : ('阪',),
      # jōyō kanji #1665
      '板'        : ('板',),
      # jōyō kanji #1666
      '版'        : ('版',),
      # jōyō kanji #1667
      '班'        : ('班',),
      # jōyō kanji #1668
      '畔'        : ('畔',),
      # jōyō kanji #1669
      '般'        : ('般',),
      # jōyō kanji #1670
      '販'        : ('販',),
      # jōyō kanji #1671
      '斑'        : ('斑',),
      # jōyō kanji #1672
      '飯'        : ('飯',),
      # jōyō kanji #1673
      '搬'        : ('搬',),
      # jōyō kanji #1674
      '煩'        : ('煩',),
      # jōyō kanji #1675
      '頒'        : ('頒',),
      # jōyō kanji #1676
      '範'        : ('範',),
      # jōyō kanji #1677
      '繁'        : ('繁', '繁'),
      # jōyō kanji #1678
      '藩'        : ('藩',),
      # jōyō kanji #1679
      '晩'        : ('晩', '晚'),
      # jōyō kanji #1680
      '番'        : ('番',),
      # jōyō kanji #1681
      '蛮'        : ('蛮', '蠻'),
      # jōyō kanji #1682
      '盤'        : ('盤',),
      # jōyō kanji #1683
      '比'        : ('比',),
      # jōyō kanji #1684
      '皮'        : ('皮',),
      # jōyō kanji #1685
      '妃'        : ('妃',),
      # jōyō kanji #1686
      '否'        : ('否',),
      # jōyō kanji #1687
      '批'        : ('批',),
      # jōyō kanji #1688
      '彼'        : ('彼',),
      # jōyō kanji #1689
      '披'        : ('披',),
      # jōyō kanji #1690
      '肥'        : ('肥',),
      # jōyō kanji #1691
      '非'        : ('非',),
      # jōyō kanji #1692
      '卑'        : ('卑', '卑'),
      # jōyō kanji #1693
      '飛'        : ('飛',),
      # jōyō kanji #1694
      '疲'        : ('疲',),
      # jōyō kanji #1695
      '秘'        : ('秘', '祕'),
      # jōyō kanji #1696
      '被'        : ('被',),
      # jōyō kanji #1697
      '悲'        : ('悲',),
      # jōyō kanji #1698
      '扉'        : ('扉',),
      # jōyō kanji #1699
      '費'        : ('費',),
      # jōyō kanji #1700
      '碑'        : ('碑', '碑'),
      # jōyō kanji #1701
      '罷'        : ('罷',),
      # jōyō kanji #1702
      '避'        : ('避',),
      # jōyō kanji #1703
      '尾'        : ('尾',),
      # jōyō kanji #1704
      '眉'        : ('眉',),
      # jōyō kanji #1705
      '美'        : ('美',),
      # jōyō kanji #1706
      '備'        : ('備',),
      # jōyō kanji #1707
      '微'        : ('微',),
      # jōyō kanji #1708
      '鼻'        : ('鼻',),
      # jōyō kanji #1709
      '膝'        : ('膝',),
      # jōyō kanji #1710
      '肘'        : ('肘',),
      # jōyō kanji #1711
      '匹'        : ('匹',),
      # jōyō kanji #1712
      '必'        : ('必',),
      # jōyō kanji #1713
      '泌'        : ('泌',),
      # jōyō kanji #1714
      '筆'        : ('筆',),
      # jōyō kanji #1715
      '姫'        : ('姫',),
      # jōyō kanji #1716
      '百'        : ('百',),
      # jōyō kanji #1717
      '氷'        : ('氷',),
      # jōyō kanji #1718
      '表'        : ('表',),
      # jōyō kanji #1719
      '俵'        : ('俵',),
      # jōyō kanji #1720
      '票'        : ('票',),
      # jōyō kanji #1721
      '評'        : ('評',),
      # jōyō kanji #1722
      '漂'        : ('漂',),
      # jōyō kanji #1723
      '標'        : ('標',),
      # jōyō kanji #1724
      '苗'        : ('苗',),
      # jōyō kanji #1725
      '秒'        : ('秒',),
      # jōyō kanji #1726
      '病'        : ('病',),
      # jōyō kanji #1727
      '描'        : ('描',),
      # jōyō kanji #1728
      '猫'        : ('猫',),
      # jōyō kanji #1729
      '品'        : ('品',),
      # jōyō kanji #1730
      '浜'        : ('浜', '濱'),
      # jōyō kanji #1731
      '貧'        : ('貧',),
      # jōyō kanji #1732
      '賓'        : ('賓', '賓'),
      # jōyō kanji #1733
      '頻'        : ('頻', '頻'),
      # jōyō kanji #1734
      '敏'        : ('敏', '敏'),
      # jōyō kanji #1735
      '瓶'        : ('瓶', '甁'),
      # jōyō kanji #1736
      '不'        : ('不',),
      # jōyō kanji #1737
      '夫'        : ('夫',),
      # jōyō kanji #1738
      '父'        : ('父',),
      # jōyō kanji #1739
      '付'        : ('付',),
      # jōyō kanji #1740
      '布'        : ('布',),
      # jōyō kanji #1741
      '扶'        : ('扶',),
      # jōyō kanji #1742
      '府'        : ('府',),
      # jōyō kanji #1743
      '怖'        : ('怖',),
      # jōyō kanji #1744
      '阜'        : ('阜',),
      # jōyō kanji #1745
      '附'        : ('附',),
      # jōyō kanji #1746
      '訃'        : ('訃',),
      # jōyō kanji #1747
      '負'        : ('負',),
      # jōyō kanji #1748
      '赴'        : ('赴',),
      # jōyō kanji #1749
      '浮'        : ('浮',),
      # jōyō kanji #1750
      '婦'        : ('婦',),
      # jōyō kanji #1751
      '符'        : ('符',),
      # jōyō kanji #1752
      '富'        : ('富',),
      # jōyō kanji #1753
      '普'        : ('普',),
      # jōyō kanji #1754
      '腐'        : ('腐',),
      # jōyō kanji #1755
      '敷'        : ('敷',),
      # jōyō kanji #1756
      '膚'        : ('膚',),
      # jōyō kanji #1757
      '賦'        : ('賦',),
      # jōyō kanji #1758
      '譜'        : ('譜',),
      # jōyō kanji #1759
      '侮'        : ('侮', '侮'),
      # jōyō kanji #1760
      '武'        : ('武',),
      # jōyō kanji #1761
      '部'        : ('部',),
      # jōyō kanji #1762
      '舞'        : ('舞',),
      # jōyō kanji #1763
      '封'        : ('封',),
      # jōyō kanji #1764
      '風'        : ('風',),
      # jōyō kanji #1765
      '伏'        : ('伏',),
      # jōyō kanji #1766
      '服'        : ('服',),
      # jōyō kanji #1767
      '副'        : ('副',),
      # jōyō kanji #1768
      '幅'        : ('幅',),
      # jōyō kanji #1769
      '復'        : ('復',),
      # jōyō kanji #1770
      '福'        : ('福', '福'),
      # jōyō kanji #1771
      '腹'        : ('腹',),
      # jōyō kanji #1772
      '複'        : ('複',),
      # jōyō kanji #1773
      '覆'        : ('覆',),
      # jōyō kanji #1774
      '払'        : ('払', '拂'),
      # jōyō kanji #1775
      '沸'        : ('沸',),
      # jōyō kanji #1776
      '仏'        : ('仏', '佛'),
      # jōyō kanji #1777
      '物'        : ('物',),
      # jōyō kanji #1778
      '粉'        : ('粉',),
      # jōyō kanji #1779
      '紛'        : ('紛',),
      # jōyō kanji #1780
      '雰'        : ('雰',),
      # jōyō kanji #1781
      '噴'        : ('噴',),
      # jōyō kanji #1782
      '墳'        : ('墳',),
      # jōyō kanji #1783
      '憤'        : ('憤',),
      # jōyō kanji #1784
      '奮'        : ('奮',),
      # jōyō kanji #1785
      '分'        : ('分',),
      # jōyō kanji #1786
      '文'        : ('文',),
      # jōyō kanji #1787
      '聞'        : ('聞',),
      # jōyō kanji #1788
      '丙'        : ('丙',),
      # jōyō kanji #1789
      '平'        : ('平',),
      # jōyō kanji #1790
      '兵'        : ('兵',),
      # jōyō kanji #1791
      '併'        : ('併', '倂'),
      # jōyō kanji #1792
      '並'        : ('並', '竝'),
      # jōyō kanji #1793
      '柄'        : ('柄',),
      # jōyō kanji #1794
      '陛'        : ('陛',),
      # jōyō kanji #1795
      '閉'        : ('閉',),
      # jōyō kanji #1796
      '塀'        : ('塀', '塀'),
      # jōyō kanji #1797
      '幣'        : ('幣',),
      # jōyō kanji #1798
      '弊'        : ('弊',),
      # jōyō kanji #1799
      '蔽'        : ('蔽',),
      # jōyō kanji #1800
      '餅'        : ('餅', '餠'),
      # jōyō kanji #1801
      '米'        : ('米',),
      # jōyō kanji #1802
      '壁'        : ('壁',),
      # jōyō kanji #1803
      '璧'        : ('璧',),
      # jōyō kanji #1804
      '癖'        : ('癖',),
      # jōyō kanji #1805
      '別'        : ('別',),
      # jōyō kanji #1806
      '蔑'        : ('蔑',),
      # jōyō kanji #1807
      '片'        : ('片',),
      # jōyō kanji #1808
      '辺'        : ('辺', '邊'),
      # jōyō kanji #1809
      '返'        : ('返',),
      # jōyō kanji #1810
      '変'        : ('変', '變'),
      # jōyō kanji #1811
      '偏'        : ('偏',),
      # jōyō kanji #1812
      '遍'        : ('遍',),
      # jōyō kanji #1813
      '編'        : ('編',),
      # jōyō kanji #1815
      '便'        : ('便',),
      # jōyō kanji #1816
      '勉'        : ('勉', '勉'),
      # jōyō kanji #1817
      '歩'        : ('歩', '步'),
      # jōyō kanji #1818
      '保'        : ('保',),
      # jōyō kanji #1819
      '哺'        : ('哺',),
      # jōyō kanji #1820
      '捕'        : ('捕',),
      # jōyō kanji #1821
      '補'        : ('補',),
      # jōyō kanji #1822
      '舗'        : ('舗',),
      # jōyō kanji #1823
      '母'        : ('母',),
      # jōyō kanji #1824
      '募'        : ('募',),
      # jōyō kanji #1825
      '墓'        : ('墓',),
      # jōyō kanji #1826
      '慕'        : ('慕',),
      # jōyō kanji #1827
      '暮'        : ('暮',),
      # jōyō kanji #1828
      '簿'        : ('簿',),
      # jōyō kanji #1829
      '方'        : ('方',),
      # jōyō kanji #1830
      '包'        : ('包',),
      # jōyō kanji #1831
      '芳'        : ('芳',),
      # jōyō kanji #1832
      '邦'        : ('邦',),
      # jōyō kanji #1833
      '奉'        : ('奉',),
      # jōyō kanji #1834
      '宝'        : ('宝', '寶'),
      # jōyō kanji #1835
      '抱'        : ('抱',),
      # jōyō kanji #1836
      '放'        : ('放',),
      # jōyō kanji #1837
      '法'        : ('法',),
      # jōyō kanji #1838
      '泡'        : ('泡',),
      # jōyō kanji #1839
      '胞'        : ('胞',),
      # jōyō kanji #1840
      '俸'        : ('俸',),
      # jōyō kanji #1841
      '倣'        : ('倣',),
      # jōyō kanji #1842
      '峰'        : ('峰',),
      # jōyō kanji #1843
      '砲'        : ('砲',),
      # jōyō kanji #1844
      '崩'        : ('崩',),
      # jōyō kanji #1845
      '訪'        : ('訪',),
      # jōyō kanji #1846
      '報'        : ('報',),
      # jōyō kanji #1847
      '蜂'        : ('蜂',),
      # jōyō kanji #1848
      '豊'        : ('豊', '豐'),
      # jōyō kanji #1849
      '飽'        : ('飽',),
      # jōyō kanji #1850
      '褒'        : ('褒', '襃'),
      # jōyō kanji #1851
      '縫'        : ('縫',),
      # jōyō kanji #1852
      '亡'        : ('亡',),
      # jōyō kanji #1853
      '乏'        : ('乏',),
      # jōyō kanji #1854
      '忙'        : ('忙',),
      # jōyō kanji #1855
      '坊'        : ('坊',),
      # jōyō kanji #1856
      '妨'        : ('妨',),
      # jōyō kanji #1857
      '忘'        : ('忘',),
      # jōyō kanji #1858
      '防'        : ('防',),
      # jōyō kanji #1859
      '房'        : ('房',),
      # jōyō kanji #1860
      '肪'        : ('肪',),
      # jōyō kanji #1861
      '某'        : ('某',),
      # jōyō kanji #1862
      '冒'        : ('冒',),
      # jōyō kanji #1863
      '剖'        : ('剖',),
      # jōyō kanji #1864
      '紡'        : ('紡',),
      # jōyō kanji #1865
      '望'        : ('望',),
      # jōyō kanji #1866
      '傍'        : ('傍',),
      # jōyō kanji #1867
      '帽'        : ('帽',),
      # jōyō kanji #1868
      '棒'        : ('棒',),
      # jōyō kanji #1869
      '貿'        : ('貿',),
      # jōyō kanji #1870
      '貌'        : ('貌',),
      # jōyō kanji #1871
      '暴'        : ('暴',),
      # jōyō kanji #1872
      '膨'        : ('膨',),
      # jōyō kanji #1873
      '謀'        : ('謀',),
      # jōyō kanji #1874
      '頰'        : ('頰',),
      # jōyō kanji #1875
      '北'        : ('北',),
      # jōyō kanji #1876
      '木'        : ('木',),
      # jōyō kanji #1877
      '朴'        : ('朴',),
      # jōyō kanji #1878
      '牧'        : ('牧',),
      # jōyō kanji #1879
      '睦'        : ('睦',),
      # jōyō kanji #1880
      '僕'        : ('僕',),
      # jōyō kanji #1881
      '墨'        : ('墨', '墨'),
      # jōyō kanji #1882
      '撲'        : ('撲',),
      # jōyō kanji #1883
      '没'        : ('没',),
      # jōyō kanji #1884
      '勃'        : ('勃',),
      # jōyō kanji #1885
      '堀'        : ('堀',),
      # jōyō kanji #1886
      '本'        : ('本',),
      # jōyō kanji #1887
      '奔'        : ('奔',),
      # jōyō kanji #1888
      '翻'        : ('翻', '飜'),
      # jōyō kanji #1889
      '凡'        : ('凡',),
      # jōyō kanji #1890
      '盆'        : ('盆',),
      # jōyō kanji #1891
      '麻'        : ('麻',),
      # jōyō kanji #1892
      '摩'        : ('摩',),
      # jōyō kanji #1893
      '磨'        : ('磨',),
      # jōyō kanji #1894
      '魔'        : ('魔',),
      # jōyō kanji #1895
      '毎'        : ('毎', '每'),
      # jōyō kanji #1896
      '妹'        : ('妹',),
      # jōyō kanji #1897
      '枚'        : ('枚',),
      # jōyō kanji #1898
      '昧'        : ('昧',),
      # jōyō kanji #1899
      '埋'        : ('埋',),
      # jōyō kanji #1900
      '幕'        : ('幕',),
      # jōyō kanji #1901
      '膜'        : ('膜',),
      # jōyō kanji #1902
      '枕'        : ('枕',),
      # jōyō kanji #1903
      '又'        : ('又',),
      # jōyō kanji #1904
      '末'        : ('末',),
      # jōyō kanji #1905
      '抹'        : ('抹',),
      # jōyō kanji #1906
      '万'        : ('万', '萬'),
      # jōyō kanji #1907
      '満'        : ('満', '滿'),
      # jōyō kanji #1908
      '慢'        : ('慢',),
      # jōyō kanji #1909
      '漫'        : ('漫',),
      # jōyō kanji #1910
      '未'        : ('未',),
      # jōyō kanji #1911
      '味'        : ('味',),
      # jōyō kanji #1912
      '魅'        : ('魅',),
      # jōyō kanji #1913
      '岬'        : ('岬',),
      # jōyō kanji #1914
      '密'        : ('密',),
      # jōyō kanji #1915
      '蜜'        : ('蜜',),
      # jōyō kanji #1916
      '脈'        : ('脈',),
      # jōyō kanji #1917
      '妙'        : ('妙',),
      # jōyō kanji #1918
      '民'        : ('民',),
      # jōyō kanji #1919
      '眠'        : ('眠',),
      # jōyō kanji #1920
      '矛'        : ('矛',),
      # jōyō kanji #1921
      '務'        : ('務',),
      # jōyō kanji #1922
      '無'        : ('無',),
      # jōyō kanji #1923
      '夢'        : ('夢',),
      # jōyō kanji #1924
      '霧'        : ('霧',),
      # jōyō kanji #1925
      '娘'        : ('娘',),
      # jōyō kanji #1926
      '名'        : ('名',),
      # jōyō kanji #1927
      '命'        : ('命',),
      # jōyō kanji #1928
      '明'        : ('明',),
      # jōyō kanji #1929
      '迷'        : ('迷',),
      # jōyō kanji #1930
      '冥'        : ('冥',),
      # jōyō kanji #1931
      '盟'        : ('盟',),
      # jōyō kanji #1932
      '銘'        : ('銘',),
      # jōyō kanji #1933
      '鳴'        : ('鳴',),
      # jōyō kanji #1934
      '滅'        : ('滅',),
      # jōyō kanji #1935
      '免'        : ('免', '免'),
      # jōyō kanji #1936
      '面'        : ('面',),
      # jōyō kanji #1937
      '綿'        : ('綿',),
      # jōyō kanji #1938
      '麺'        : ('麺', '麵'),
      # jōyō kanji #1939
      '茂'        : ('茂',),
      # jōyō kanji #1940
      '模'        : ('模',),
      # jōyō kanji #1941
      '毛'        : ('毛',),
      # jōyō kanji #1942
      '妄'        : ('妄',),
      # jōyō kanji #1943
      '盲'        : ('盲',),
      # jōyō kanji #1944
      '耗'        : ('耗',),
      # jōyō kanji #1945
      '猛'        : ('猛',),
      # jōyō kanji #1946
      '網'        : ('網',),
      # jōyō kanji #1947
      '目'        : ('目',),
      # jōyō kanji #1948
      '黙'        : ('黙', '默'),
      # jōyō kanji #1949
      '門'        : ('門',),
      # jōyō kanji #1950
      '紋'        : ('紋',),
      # jōyō kanji #1951
      '問'        : ('問',),
      # jōyō kanji #1952
      '冶'        : ('冶',),
      # jōyō kanji #1953
      '夜'        : ('夜',),
      # jōyō kanji #1954
      '野'        : ('野',),
      # jōyō kanji #1955
      '弥'        : ('弥', '彌'),
      # jōyō kanji #1956
      '厄'        : ('厄',),
      # jōyō kanji #1957
      '役'        : ('役',),
      # jōyō kanji #1958
      '約'        : ('約',),
      # jōyō kanji #1959
      '訳'        : ('訳', '譯'),
      # jōyō kanji #1960
      '薬'        : ('薬', '藥'),
      # jōyō kanji #1961
      '躍'        : ('躍',),
      # jōyō kanji #1962
      '闇'        : ('闇',),
      # jōyō kanji #1963
      '由'        : ('由',),
      # jōyō kanji #1964
      '油'        : ('油',),
      # jōyō kanji #1965
      '喩'        : ('喩',),
      # jōyō kanji #1966
      '愉'        : ('愉',),
      # jōyō kanji #1967
      '諭'        : ('諭',),
      # jōyō kanji #1968
      '輸'        : ('輸',),
      # jōyō kanji #1969
      '癒'        : ('癒',),
      # jōyō kanji #1970
      '唯'        : ('唯',),
      # jōyō kanji #1971
      '友'        : ('友',),
      # jōyō kanji #1972
      '有'        : ('有',),
      # jōyō kanji #1973
      '勇'        : ('勇',),
      # jōyō kanji #1974
      '幽'        : ('幽',),
      # jōyō kanji #1975
      '悠'        : ('悠',),
      # jōyō kanji #1976
      '郵'        : ('郵',),
      # jōyō kanji #1977
      '湧'        : ('湧',),
      # jōyō kanji #1978
      '猶'        : ('猶',),
      # jōyō kanji #1979
      '裕'        : ('裕',),
      # jōyō kanji #1980
      '遊'        : ('遊',),
      # jōyō kanji #1981
      '雄'        : ('雄',),
      # jōyō kanji #1982
      '誘'        : ('誘',),
      # jōyō kanji #1983
      '憂'        : ('憂',),
      # jōyō kanji #1984
      '融'        : ('融',),
      # jōyō kanji #1985
      '優'        : ('優',),
      # jōyō kanji #1986
      '与'        : ('与', '與'),
      # jōyō kanji #1987
      '予'        : ('予', '豫'),
      # jōyō kanji #1988
      '余'        : ('余', '餘'),
      # jōyō kanji #1989
      '誉'        : ('誉', '譽'),
      # jōyō kanji #1990
      '預'        : ('預',),
      # jōyō kanji #1991
      '幼'        : ('幼',),
      # jōyō kanji #1992
      '用'        : ('用',),
      # jōyō kanji #1993
      '羊'        : ('羊',),
      # jōyō kanji #1994
      '妖'        : ('妖',),
      # jōyō kanji #1995
      '洋'        : ('洋',),
      # jōyō kanji #1996
      '要'        : ('要',),
      # jōyō kanji #1997
      '容'        : ('容',),
      # jōyō kanji #1998
      '庸'        : ('庸',),
      # jōyō kanji #1999
      '揚'        : ('揚',),
      # jōyō kanji #2000
      '揺'        : ('揺', '搖'),
      # jōyō kanji #2001
      '葉'        : ('葉',),
      # jōyō kanji #2002
      '陽'        : ('陽',),
      # jōyō kanji #2003
      '溶'        : ('溶',),
      # jōyō kanji #2004
      '腰'        : ('腰',),
      # jōyō kanji #2005
      '様'        : ('様', '樣'),
      # jōyō kanji #2006
      '瘍'        : ('瘍',),
      # jōyō kanji #2007
      '踊'        : ('踊',),
      # jōyō kanji #2008
      '窯'        : ('窯',),
      # jōyō kanji #2009
      '養'        : ('養',),
      # jōyō kanji #2010
      '擁'        : ('擁',),
      # jōyō kanji #2011
      '謡'        : ('謡', '謠'),
      # jōyō kanji #2012
      '曜'        : ('曜',),
      # jōyō kanji #2013
      '抑'        : ('抑',),
      # jōyō kanji #2014
      '沃'        : ('沃',),
      # jōyō kanji #2015
      '浴'        : ('浴',),
      # jōyō kanji #2016
      '欲'        : ('欲',),
      # jōyō kanji #2017
      '翌'        : ('翌',),
      # jōyō kanji #2018
      '翼'        : ('翼',),
      # jōyō kanji #2019
      '拉'        : ('拉',),
      # jōyō kanji #2020
      '裸'        : ('裸',),
      # jōyō kanji #2021
      '羅'        : ('羅',),
      # jōyō kanji #2022
      '来'        : ('来', '來'),
      # jōyō kanji #2023
      '雷'        : ('雷',),
      # jōyō kanji #2024
      '頼'        : ('頼', '賴'),
      # jōyō kanji #2025
      '絡'        : ('絡',),
      # jōyō kanji #2026
      '落'        : ('落',),
      # jōyō kanji #2027
      '酪'        : ('酪',),
      # jōyō kanji #2028
      '辣'        : ('辣',),
      # jōyō kanji #2029
      '乱'        : ('乱', '亂'),
      # jōyō kanji #2030
      '卵'        : ('卵',),
      # jōyō kanji #2031
      '覧'        : ('覧', '覽'),
      # jōyō kanji #2032
      '濫'        : ('濫',),
      # jōyō kanji #2033
      '藍'        : ('藍',),
      # jōyō kanji #2034
      '欄'        : ('欄', '欄'),
      # jōyō kanji #2035
      '吏'        : ('吏',),
      # jōyō kanji #2036
      '利'        : ('利',),
      # jōyō kanji #2037
      '里'        : ('里',),
      # jōyō kanji #2038
      '理'        : ('理',),
      # jōyō kanji #2039
      '痢'        : ('痢',),
      # jōyō kanji #2040
      '裏'        : ('裏',),
      # jōyō kanji #2041
      '履'        : ('履',),
      # jōyō kanji #2042
      '璃'        : ('璃',),
      # jōyō kanji #2043
      '離'        : ('離',),
      # jōyō kanji #2044
      '陸'        : ('陸',),
      # jōyō kanji #2045
      '立'        : ('立',),
      # jōyō kanji #2046
      '律'        : ('律',),
      # jōyō kanji #2047
      '慄'        : ('慄',),
      # jōyō kanji #2048
      '略'        : ('略',),
      # jōyō kanji #2049
      '柳'        : ('柳',),
      # jōyō kanji #2050
      '流'        : ('流',),
      # jōyō kanji #2051
      '留'        : ('留',),
      # jōyō kanji #2052
      '竜'        : ('竜', '龍'),
      # jōyō kanji #2053
      '粒'        : ('粒',),
      # jōyō kanji #2054
      '隆'        : ('隆', '隆'),
      # jōyō kanji #2055
      '硫'        : ('硫',),
      # jōyō kanji #2056
      '侶'        : ('侶',),
      # jōyō kanji #2057
      '旅'        : ('旅',),
      # jōyō kanji #2058
      '虜'        : ('虜', '虜'),
      # jōyō kanji #2059
      '慮'        : ('慮',),
      # jōyō kanji #2060
      '了'        : ('了',),
      # jōyō kanji #2061
      '両'        : ('両', '兩'),
      # jōyō kanji #2062
      '良'        : ('良',),
      # jōyō kanji #2063
      '料'        : ('料',),
      # jōyō kanji #2064
      '涼'        : ('涼',),
      # jōyō kanji #2065
      '猟'        : ('猟', '獵'),
      # jōyō kanji #2066
      '陵'        : ('陵',),
      # jōyō kanji #2067
      '量'        : ('量',),
      # jōyō kanji #2068
      '僚'        : ('僚',),
      # jōyō kanji #2069
      '領'        : ('領',),
      # jōyō kanji #2070
      '寮'        : ('寮',),
      # jōyō kanji #2071
      '療'        : ('療',),
      # jōyō kanji #2072
      '瞭'        : ('瞭',),
      # jōyō kanji #2073
      '糧'        : ('糧',),
      # jōyō kanji #2074
      '力'        : ('力',),
      # jōyō kanji #2075
      '緑'        : ('緑', '綠'),
      # jōyō kanji #2076
      '林'        : ('林',),
      # jōyō kanji #2077
      '厘'        : ('厘',),
      # jōyō kanji #2078
      '倫'        : ('倫',),
      # jōyō kanji #2079
      '輪'        : ('輪',),
      # jōyō kanji #2080
      '隣'        : ('隣',),
      # jōyō kanji #2081
      '臨'        : ('臨',),
      # jōyō kanji #2082
      '瑠'        : ('瑠',),
      # jōyō kanji #2083
      '涙'        : ('涙', '淚'),
      # jōyō kanji #2084
      '累'        : ('累',),
      # jōyō kanji #2085
      '塁'        : ('塁', '壘'),
      # jōyō kanji #2086
      '類'        : ('類', '類'),
      # jōyō kanji #2087
      '令'        : ('令',),
      # jōyō kanji #2088
      '礼'        : ('礼', '禮'),
      # jōyō kanji #2089
      '冷'        : ('冷',),
      # jōyō kanji #2090
      '励'        : ('励', '勵'),
      # jōyō kanji #2091
      '戻'        : ('戻', '戾'),
      # jōyō kanji #2092
      '例'        : ('例',),
      # jōyō kanji #2093
      '鈴'        : ('鈴',),
      # jōyō kanji #2094
      '零'        : ('零',),
      # jōyō kanji #2095
      '霊'        : ('霊', '靈'),
      # jōyō kanji #2096
      '隷'        : ('隷',),
      # jōyō kanji #2097
      '齢'        : ('齢', '齡'),
      # jōyō kanji #2098
      '麗'        : ('麗',),
      # jōyō kanji #2099
      '暦'        : ('暦', '曆'),
      # jōyō kanji #2100
      '歴'        : ('歴', '歷'),
      # jōyō kanji #2101
      '列'        : ('列',),
      # jōyō kanji #2102
      '劣'        : ('劣',),
      # jōyō kanji #2103
      '烈'        : ('烈',),
      # jōyō kanji #2104
      '裂'        : ('裂',),
      # jōyō kanji #2105
      '恋'        : ('恋', '戀'),
      # jōyō kanji #2106
      '連'        : ('連',),
      # jōyō kanji #2107
      '廉'        : ('廉',),
      # jōyō kanji #2108
      '練'        : ('練', '練'),
      # jōyō kanji #2109
      '錬'        : ('錬', '鍊'),
      # jōyō kanji #2110
      '呂'        : ('呂',),
      # jōyō kanji #2111
      '炉'        : ('炉', '爐'),
      # jōyō kanji #2112
      '賂'        : ('賂',),
      # jōyō kanji #2113
      '路'        : ('路',),
      # jōyō kanji #2114
      '露'        : ('露',),
      # jōyō kanji #2115
      '老'        : ('老',),
      # jōyō kanji #2116
      '労'        : ('労', '勞'),
      # jōyō kanji #2117
      '弄'        : ('弄',),
      # jōyō kanji #2118
      '郎'        : ('郎', '郞'),
      # jōyō kanji #2119
      '朗'        : ('朗', '朗'),
      # jōyō kanji #2120
      '浪'        : ('浪',),
      # jōyō kanji #2121
      '廊'        : ('廊', '廊'),
      # jōyō kanji #2122
      '楼'        : ('楼', '樓'),
      # jōyō kanji #2123
      '漏'        : ('漏',),
      # jōyō kanji #2124
      '籠'        : ('籠',),
      # jōyō kanji #2125
      '六'        : ('六',),
      # jōyō kanji #2126
      '録'        : ('録', '錄'),
      # jōyō kanji #2127
      '麓'        : ('麓',),
      # jōyō kanji #2128
      '論'        : ('論',),
      # jōyō kanji #2129
      '和'        : ('和',),
      # jōyō kanji #2130
      '話'        : ('話',),
      # jōyō kanji #2131
      '賄'        : ('賄',),
      # jōyō kanji #2132
      '脇'        : ('脇',),
      # jōyō kanji #2133
      '惑'        : ('惑',),
      # jōyō kanji #2134
      '枠'        : ('枠',),
      # jōyō kanji #2135
      '湾'        : ('湾', '灣'),
      # jōyō kanji #2136
      '腕'        : ('腕',),

      # jinmeiyō kanji #1
      '丑'        : ('丑',),
      # jinmeiyō kanji #2
      '丞'        : ('丞',),
      # jinmeiyō kanji #3
      '乃'        : ('乃',),
      # jinmeiyō kanji #4
      '之'        : ('之',),
      # jinmeiyō kanji #5
      '乎'        : ('乎',),
      # jinmeiyō kanji #6
      '也'        : ('也',),
      # jinmeiyō kanji #7
      '云'        : ('云',),
      # jinmeiyō kanji #8
      '亘'        : ('亘', '亙'),
      # jinmeiyō kanji #9
      '些'        : ('些',),
      # jinmeiyō kanji #10
      '亦'        : ('亦',),
      # jinmeiyō kanji #11
      '亥'        : ('亥',),
      # jinmeiyō kanji #12
      '亨'        : ('亨',),
      # jinmeiyō kanji #13
      '亮'        : ('亮',),
      # jinmeiyō kanji #14
      '仔'        : ('仔',),
      # jinmeiyō kanji #15
      '伊'        : ('伊',),
      # jinmeiyō kanji #16
      '伍'        : ('伍',),
      # jinmeiyō kanji #17
      '伽'        : ('伽',),
      # jinmeiyō kanji #18
      '佃'        : ('佃',),
      # jinmeiyō kanji #19
      '佑'        : ('佑',),
      # jinmeiyō kanji #20
      '伶'        : ('伶',),
      # jinmeiyō kanji #21
      '侃'        : ('侃',),
      # jinmeiyō kanji #22
      '侑'        : ('侑',),
      # jinmeiyō kanji #23
      '俄'        : ('俄',),
      # jinmeiyō kanji #24
      '俠'        : ('俠',),
      # jinmeiyō kanji #25
      '俣'        : ('俣',),
      # jinmeiyō kanji #26
      '俐'        : ('俐',),
      # jinmeiyō kanji #27
      '倭'        : ('倭',),
      # jinmeiyō kanji #28
      '俱'        : ('俱',),
      # jinmeiyō kanji #29
      '倦'        : ('倦',),
      # jinmeiyō kanji #30
      '倖'        : ('倖',),
      # jinmeiyō kanji #31
      '偲'        : ('偲',),
      # jinmeiyō kanji #32
      '傭'        : ('傭',),
      # jinmeiyō kanji #33
      '儲'        : ('儲',),
      # jinmeiyō kanji #34
      '允'        : ('允',),
      # jinmeiyō kanji #35
      '兎'        : ('兎',),
      # jinmeiyō kanji #36
      '兜'        : ('兜',),
      # jinmeiyō kanji #37
      '其'        : ('其',),
      # jinmeiyō kanji #38
      '冴'        : ('冴',),
      # jinmeiyō kanji #39
      '凌'        : ('凌',),
      # jinmeiyō kanji #40
      '凜'        : ('凜', '凛'),
      # jinmeiyō kanji #41
      '凧'        : ('凧',),
      # jinmeiyō kanji #42
      '凪'        : ('凪',),
      # jinmeiyō kanji #43
      '凰'        : ('凰',),
      # jinmeiyō kanji #44
      '凱'        : ('凱',),
      # jinmeiyō kanji #45
      '函'        : ('函',),
      # jinmeiyō kanji #46
      '劉'        : ('劉',),
      # jinmeiyō kanji #47
      '劫'        : ('劫',),
      # jinmeiyō kanji #48
      '勁'        : ('勁',),
      # jinmeiyō kanji #49
      '勺'        : ('勺',),
      # jinmeiyō kanji #50
      '勿'        : ('勿',),
      # jinmeiyō kanji #51
      '匁'        : ('匁',),
      # jinmeiyō kanji #52
      '匡'        : ('匡',),
      # jinmeiyō kanji #53
      '廿'        : ('廿',),
      # jinmeiyō kanji #54
      '卜'        : ('卜',),
      # jinmeiyō kanji #55
      '卯'        : ('卯',),
      # jinmeiyō kanji #56
      '卿'        : ('卿',),
      # jinmeiyō kanji #57
      '厨'        : ('厨',),
      # jinmeiyō kanji #58
      '厩'        : ('厩',),
      # jinmeiyō kanji #59
      '叉'        : ('叉',),
      # jinmeiyō kanji #60
      '叡'        : ('叡',),
      # jinmeiyō kanji #61
      '叢'        : ('叢',),
      # jinmeiyō kanji #62
      '叶'        : ('叶',),
      # jinmeiyō kanji #63
      '只'        : ('只',),
      # jinmeiyō kanji #64
      '吾'        : ('吾',),
      # jinmeiyō kanji #65
      '吞'        : ('吞',),
      # jinmeiyō kanji #66
      '吻'        : ('吻',),
      # jinmeiyō kanji #67
      '哉'        : ('哉',),
      # jinmeiyō kanji #68
      '哨'        : ('哨',),
      # jinmeiyō kanji #69
      '啄'        : ('啄',),
      # jinmeiyō kanji #70
      '哩'        : ('哩',),
      # jinmeiyō kanji #71
      '喬'        : ('喬',),
      # jinmeiyō kanji #72
      '喧'        : ('喧',),
      # jinmeiyō kanji #73
      '喰'        : ('喰',),
      # jinmeiyō kanji #74
      '喋'        : ('喋',),
      # jinmeiyō kanji #75
      '嘩'        : ('嘩',),
      # jinmeiyō kanji #76
      '嘉'        : ('嘉',),
      # jinmeiyō kanji #77
      '嘗'        : ('嘗',),
      # jinmeiyō kanji #78
      '噌'        : ('噌',),
      # jinmeiyō kanji #79
      '噂'        : ('噂',),
      # jinmeiyō kanji #80
      '圃'        : ('圃',),
      # jinmeiyō kanji #81
      '圭'        : ('圭',),
      # jinmeiyō kanji #82
      '坐'        : ('坐',),
      # jinmeiyō kanji #83
      '尭'        : ('尭', '堯'),
      # jinmeiyō kanji #84
      '坦'        : ('坦',),
      # jinmeiyō kanji #85
      '埴'        : ('埴',),
      # jinmeiyō kanji #86
      '堰'        : ('堰',),
      # jinmeiyō kanji #87
      '堺'        : ('堺',),
      # jinmeiyō kanji #88
      '堵'        : ('堵',),
      # jinmeiyō kanji #89
      '塙'        : ('塙',),
      # jinmeiyō kanji #90
      '壕'        : ('壕',),
      # jinmeiyō kanji #91
      '壬'        : ('壬',),
      # jinmeiyō kanji #92
      '夷'        : ('夷',),
      # jinmeiyō kanji #93
      '奄'        : ('奄',),
      # jinmeiyō kanji #94
      '奎'        : ('奎',),
      # jinmeiyō kanji #95
      '套'        : ('套',),
      # jinmeiyō kanji #96
      '娃'        : ('娃',),
      # jinmeiyō kanji #97
      '姪'        : ('姪',),
      # jinmeiyō kanji #98
      '姥'        : ('姥',),
      # jinmeiyō kanji #99
      '娩'        : ('娩',),
      # jinmeiyō kanji #100
      '嬉'        : ('嬉',),
      # jinmeiyō kanji #101
      '孟'        : ('孟',),
      # jinmeiyō kanji #102
      '宏'        : ('宏',),
      # jinmeiyō kanji #103
      '宋'        : ('宋',),
      # jinmeiyō kanji #104
      '宕'        : ('宕',),
      # jinmeiyō kanji #105
      '宥'        : ('宥',),
      # jinmeiyō kanji #106
      '寅'        : ('寅',),
      # jinmeiyō kanji #107
      '寓'        : ('寓',),
      # jinmeiyō kanji #108
      '寵'        : ('寵',),
      # jinmeiyō kanji #109
      '尖'        : ('尖',),
      # jinmeiyō kanji #110
      '尤'        : ('尤',),
      # jinmeiyō kanji #111
      '屑'        : ('屑',),
      # jinmeiyō kanji #112
      '峨'        : ('峨',),
      # jinmeiyō kanji #113
      '峻'        : ('峻',),
      # jinmeiyō kanji #114
      '崚'        : ('崚',),
      # jinmeiyō kanji #115
      '嵯'        : ('嵯',),
      # jinmeiyō kanji #116
      '嵩'        : ('嵩',),
      # jinmeiyō kanji #117
      '嶺'        : ('嶺',),
      # jinmeiyō kanji #118
      '巌'        : ('巌', '巖'),
      # jinmeiyō kanji #119
      '已'        : ('已',),
      # jinmeiyō kanji #120
      '巳'        : ('巳',),
      # jinmeiyō kanji #121
      '巴'        : ('巴',),
      # jinmeiyō kanji #122
      '巷'        : ('巷',),
      # jinmeiyō kanji #123
      '巽'        : ('巽',),
      # jinmeiyō kanji #124
      '帖'        : ('帖',),
      # jinmeiyō kanji #125
      '幌'        : ('幌',),
      # jinmeiyō kanji #126
      '幡'        : ('幡',),
      # jinmeiyō kanji #127
      '庄'        : ('庄',),
      # jinmeiyō kanji #128
      '庇'        : ('庇',),
      # jinmeiyō kanji #129
      '庚'        : ('庚',),
      # jinmeiyō kanji #130
      '庵'        : ('庵',),
      # jinmeiyō kanji #131
      '廟'        : ('廟',),
      # jinmeiyō kanji #132
      '廻'        : ('廻',),
      # jinmeiyō kanji #133
      '弘'        : ('弘',),
      # jinmeiyō kanji #134
      '弛'        : ('弛',),
      # jinmeiyō kanji #135
      '彗'        : ('彗',),
      # jinmeiyō kanji #136
      '彦'        : ('彦',),
      # jinmeiyō kanji #137
      '彪'        : ('彪',),
      # jinmeiyō kanji #138
      '彬'        : ('彬',),
      # jinmeiyō kanji #139
      '徠'        : ('徠',),
      # jinmeiyō kanji #140
      '忽'        : ('忽',),
      # jinmeiyō kanji #141
      '怜'        : ('怜',),
      # jinmeiyō kanji #142
      '恢'        : ('恢',),
      # jinmeiyō kanji #143
      '恰'        : ('恰',),
      # jinmeiyō kanji #144
      '恕'        : ('恕',),
      # jinmeiyō kanji #145
      '悌'        : ('悌',),
      # jinmeiyō kanji #146
      '惟'        : ('惟',),
      # jinmeiyō kanji #147
      '惚'        : ('惚',),
      # jinmeiyō kanji #148
      '悉'        : ('悉',),
      # jinmeiyō kanji #149
      '惇'        : ('惇',),
      # jinmeiyō kanji #150
      '惹'        : ('惹',),
      # jinmeiyō kanji #151
      '惺'        : ('惺',),
      # jinmeiyō kanji #152
      '惣'        : ('惣',),
      # jinmeiyō kanji #153
      '慧'        : ('慧',),
      # jinmeiyō kanji #154
      '憐'        : ('憐',),
      # jinmeiyō kanji #155
      '戊'        : ('戊',),
      # jinmeiyō kanji #156
      '或'        : ('或',),
      # jinmeiyō kanji #157
      '戟'        : ('戟',),
      # jinmeiyō kanji #158
      '托'        : ('托',),
      # jinmeiyō kanji #159
      '按'        : ('按',),
      # jinmeiyō kanji #160
      '挺'        : ('挺',),
      # jinmeiyō kanji #161
      '挽'        : ('挽',),
      # jinmeiyō kanji #162
      '掬'        : ('掬',),
      # jinmeiyō kanji #163
      '捲'        : ('捲',),
      # jinmeiyō kanji #164
      '捷'        : ('捷',),
      # jinmeiyō kanji #165
      '捺'        : ('捺',),
      # jinmeiyō kanji #166
      '捧'        : ('捧',),
      # jinmeiyō kanji #167
      '掠'        : ('掠',),
      # jinmeiyō kanji #168
      '揃'        : ('揃', '摑'),
      # jinmeiyō kanji #169
      '摺'        : ('摺',),
      # jinmeiyō kanji #170
      '撒'        : ('撒',),
      # jinmeiyō kanji #171
      '撰'        : ('撰',),
      # jinmeiyō kanji #172
      '撞'        : ('撞',),
      # jinmeiyō kanji #173
      '播'        : ('播',),
      # jinmeiyō kanji #174
      '撫'        : ('撫',),
      # jinmeiyō kanji #175
      '擢'        : ('擢',),
      # jinmeiyō kanji #176
      '孜'        : ('孜',),
      # jinmeiyō kanji #177
      '敦'        : ('敦',),
      # jinmeiyō kanji #178
      '斐'        : ('斐',),
      # jinmeiyō kanji #179
      '斡'        : ('斡',),
      # jinmeiyō kanji #180
      '斧'        : ('斧',),
      # jinmeiyō kanji #181
      '斯'        : ('斯',),
      # jinmeiyō kanji #182
      '於'        : ('於',),
      # jinmeiyō kanji #183
      '旭'        : ('旭',),
      # jinmeiyō kanji #184
      '昂'        : ('昂',),
      # jinmeiyō kanji #185
      '昊'        : ('昊',),
      # jinmeiyō kanji #186
      '昏'        : ('昏',),
      # jinmeiyō kanji #187
      '昌'        : ('昌',),
      # jinmeiyō kanji #188
      '昴'        : ('昴',),
      # jinmeiyō kanji #189
      '晏'        : ('晏',),
      # jinmeiyō kanji #190
      '晃'        : ('晃', '晄'),
      # jinmeiyō kanji #191
      '晒'        : ('晒',),
      # jinmeiyō kanji #192
      '晋'        : ('晋',),
      # jinmeiyō kanji #193
      '晟'        : ('晟',),
      # jinmeiyō kanji #194
      '晦'        : ('晦',),
      # jinmeiyō kanji #195
      '晨'        : ('晨',),
      # jinmeiyō kanji #196
      '智'        : ('智',),
      # jinmeiyō kanji #197
      '暉'        : ('暉',),
      # jinmeiyō kanji #198
      '暢'        : ('暢',),
      # jinmeiyō kanji #199
      '曙'        : ('曙',),
      # jinmeiyō kanji #200
      '曝'        : ('曝',),
      # jinmeiyō kanji #201
      '曳'        : ('曳',),
      # jinmeiyō kanji #202
      '朋'        : ('朋',),
      # jinmeiyō kanji #203
      '朔'        : ('朔',),
      # jinmeiyō kanji #204
      '杏'        : ('杏',),
      # jinmeiyō kanji #205
      '杖'        : ('杖',),
      # jinmeiyō kanji #206
      '杜'        : ('杜',),
      # jinmeiyō kanji #207
      '李'        : ('李',),
      # jinmeiyō kanji #208
      '杭'        : ('杭',),
      # jinmeiyō kanji #209
      '杵'        : ('杵',),
      # jinmeiyō kanji #210
      '杷'        : ('杷',),
      # jinmeiyō kanji #211
      '枇'        : ('枇',),
      # jinmeiyō kanji #212
      '柑'        : ('柑',),
      # jinmeiyō kanji #213
      '柴'        : ('柴',),
      # jinmeiyō kanji #214
      '柘'        : ('柘',),
      # jinmeiyō kanji #215
      '柊'        : ('柊',),
      # jinmeiyō kanji #216
      '柏'        : ('柏',),
      # jinmeiyō kanji #217
      '柾'        : ('柾',),
      # jinmeiyō kanji #218
      '柚'        : ('柚',),
      # jinmeiyō kanji #219
      '桧'        : ('桧', '檜'),
      # jinmeiyō kanji #220
      '栞'        : ('栞',),
      # jinmeiyō kanji #221
      '桔'        : ('桔',),
      # jinmeiyō kanji #222
      '桂'        : ('桂',),
      # jinmeiyō kanji #223
      '栖'        : ('栖',),
      # jinmeiyō kanji #224
      '桐'        : ('桐',),
      # jinmeiyō kanji #225
      '栗'        : ('栗',),
      # jinmeiyō kanji #226
      '梧'        : ('梧',),
      # jinmeiyō kanji #227
      '梓'        : ('梓',),
      # jinmeiyō kanji #228
      '梢'        : ('梢',),
      # jinmeiyō kanji #229
      '梛'        : ('梛',),
      # jinmeiyō kanji #230
      '梯'        : ('梯',),
      # jinmeiyō kanji #231
      '桶'        : ('桶',),
      # jinmeiyō kanji #232
      '梶'        : ('梶',),
      # jinmeiyō kanji #233
      '椛'        : ('椛',),
      # jinmeiyō kanji #234
      '梁'        : ('梁',),
      # jinmeiyō kanji #235
      '棲'        : ('棲',),
      # jinmeiyō kanji #236
      '椋'        : ('椋',),
      # jinmeiyō kanji #237
      '椀'        : ('椀',),
      # jinmeiyō kanji #238
      '楯'        : ('楯',),
      # jinmeiyō kanji #239
      '楚'        : ('楚',),
      # jinmeiyō kanji #240
      '楕'        : ('楕',),
      # jinmeiyō kanji #241
      '椿'        : ('椿',),
      # jinmeiyō kanji #242
      '楠'        : ('楠',),
      # jinmeiyō kanji #243
      '楓'        : ('楓',),
      # jinmeiyō kanji #244
      '椰'        : ('椰',),
      # jinmeiyō kanji #245
      '楢'        : ('楢',),
      # jinmeiyō kanji #246
      '楊'        : ('楊',),
      # jinmeiyō kanji #247
      '榎'        : ('榎',),
      # jinmeiyō kanji #248
      '樺'        : ('樺',),
      # jinmeiyō kanji #249
      '榊'        : ('榊',),
      # jinmeiyō kanji #250
      '榛'        : ('榛',),
      # jinmeiyō kanji #251
      '槙'        : ('槙', '槇'),
      # jinmeiyō kanji #252
      '槍'        : ('槍',),
      # jinmeiyō kanji #253
      '槌'        : ('槌',),
      # jinmeiyō kanji #254
      '樫'        : ('樫',),
      # jinmeiyō kanji #255
      '槻'        : ('槻',),
      # jinmeiyō kanji #256
      '樟'        : ('樟',),
      # jinmeiyō kanji #257
      '樋'        : ('樋',),
      # jinmeiyō kanji #258
      '橘'        : ('橘',),
      # jinmeiyō kanji #259
      '樽'        : ('樽',),
      # jinmeiyō kanji #260
      '橙'        : ('橙',),
      # jinmeiyō kanji #261
      '檎'        : ('檎',),
      # jinmeiyō kanji #262
      '檀'        : ('檀',),
      # jinmeiyō kanji #263
      '櫂'        : ('櫂',),
      # jinmeiyō kanji #264
      '櫛'        : ('櫛',),
      # jinmeiyō kanji #265
      '櫓'        : ('櫓',),
      # jinmeiyō kanji #266
      '欣'        : ('欣',),
      # jinmeiyō kanji #267
      '欽'        : ('欽',),
      # jinmeiyō kanji #268
      '歎'        : ('歎',),
      # jinmeiyō kanji #269
      '此'        : ('此',),
      # jinmeiyō kanji #270
      '殆'        : ('殆',),
      # jinmeiyō kanji #271
      '毅'        : ('毅',),
      # jinmeiyō kanji #272
      '毘'        : ('毘',),
      # jinmeiyō kanji #273
      '毬'        : ('毬',),
      # jinmeiyō kanji #274
      '汀'        : ('汀',),
      # jinmeiyō kanji #275
      '汝'        : ('汝',),
      # jinmeiyō kanji #276
      '汐'        : ('汐',),
      # jinmeiyō kanji #277
      '汲'        : ('汲',),
      # jinmeiyō kanji #278
      '沌'        : ('沌',),
      # jinmeiyō kanji #279
      '沓'        : ('沓',),
      # jinmeiyō kanji #280
      '沫'        : ('沫',),
      # jinmeiyō kanji #281
      '洸'        : ('洸',),
      # jinmeiyō kanji #282
      '洲'        : ('洲',),
      # jinmeiyō kanji #283
      '洵'        : ('洵',),
      # jinmeiyō kanji #284
      '洛'        : ('洛',),
      # jinmeiyō kanji #285
      '浩'        : ('浩',),
      # jinmeiyō kanji #286
      '浬'        : ('浬',),
      # jinmeiyō kanji #287
      '淵'        : ('淵',),
      # jinmeiyō kanji #288
      '淳'        : ('淳',),
      # jinmeiyō kanji #289
      '渚'        : ('渚', '渚'),
      # jinmeiyō kanji #290
      '淀'        : ('淀',),
      # jinmeiyō kanji #291
      '淋'        : ('淋',),
      # jinmeiyō kanji #292
      '渥'        : ('渥',),
      # jinmeiyō kanji #293
      '湘'        : ('湘',),
      # jinmeiyō kanji #294
      '湊'        : ('湊',),
      # jinmeiyō kanji #295
      '湛'        : ('湛',),
      # jinmeiyō kanji #296
      '溢'        : ('溢',),
      # jinmeiyō kanji #297
      '滉'        : ('滉',),
      # jinmeiyō kanji #298
      '溜'        : ('溜',),
      # jinmeiyō kanji #299
      '漱'        : ('漱',),
      # jinmeiyō kanji #300
      '漕'        : ('漕',),
      # jinmeiyō kanji #301
      '漣'        : ('漣',),
      # jinmeiyō kanji #302
      '澪'        : ('澪',),
      # jinmeiyō kanji #303
      '濡'        : ('濡',),
      # jinmeiyō kanji #304
      '瀕'        : ('瀕',),
      # jinmeiyō kanji #305
      '灘'        : ('灘',),
      # jinmeiyō kanji #306
      '灸'        : ('灸',),
      # jinmeiyō kanji #307
      '灼'        : ('灼',),
      # jinmeiyō kanji #308
      '烏'        : ('烏',),
      # jinmeiyō kanji #309
      '焰'        : ('焰',),
      # jinmeiyō kanji #310
      '焚'        : ('焚',),
      # jinmeiyō kanji #311
      '煌'        : ('煌',),
      # jinmeiyō kanji #312
      '煤'        : ('煤',),
      # jinmeiyō kanji #313
      '煉'        : ('煉',),
      # jinmeiyō kanji #314
      '熙'        : ('熙',),
      # jinmeiyō kanji #315
      '燕'        : ('燕',),
      # jinmeiyō kanji #316
      '燎'        : ('燎',),
      # jinmeiyō kanji #317
      '燦'        : ('燦',),
      # jinmeiyō kanji #318
      '燭'        : ('燭',),
      # jinmeiyō kanji #319
      '燿'        : ('燿',),
      # jinmeiyō kanji #320
      '爾'        : ('爾',),
      # jinmeiyō kanji #321
      '牒'        : ('牒',),
      # jinmeiyō kanji #322
      '牟'        : ('牟',),
      # jinmeiyō kanji #323
      '牡'        : ('牡',),
      # jinmeiyō kanji #324
      '牽'        : ('牽',),
      # jinmeiyō kanji #325
      '犀'        : ('犀',),
      # jinmeiyō kanji #326
      '狼'        : ('狼',),
      # jinmeiyō kanji #327
      '猪'        : ('猪', '猪'),
      # jinmeiyō kanji #328
      '獅'        : ('獅',),
      # jinmeiyō kanji #329
      '玖'        : ('玖',),
      # jinmeiyō kanji #330
      '珂'        : ('珂',),
      # jinmeiyō kanji #331
      '珈'        : ('珈',),
      # jinmeiyō kanji #332
      '珊'        : ('珊',),
      # jinmeiyō kanji #333
      '珀'        : ('珀',),
      # jinmeiyō kanji #334
      '玲'        : ('玲',),
      # jinmeiyō kanji #335
      '琢'        : ('琢', '琢'),
      # jinmeiyō kanji #336
      '琉'        : ('琉',),
      # jinmeiyō kanji #337
      '瑛'        : ('瑛',),
      # jinmeiyō kanji #338
      '琥'        : ('琥',),
      # jinmeiyō kanji #339
      '琶'        : ('琶',),
      # jinmeiyō kanji #340
      '琵'        : ('琵',),
      # jinmeiyō kanji #341
      '琳'        : ('琳',),
      # jinmeiyō kanji #342
      '瑚'        : ('瑚',),
      # jinmeiyō kanji #343
      '瑞'        : ('瑞',),
      # jinmeiyō kanji #344
      '瑶'        : ('瑶',),
      # jinmeiyō kanji #345
      '瑳'        : ('瑳',),
      # jinmeiyō kanji #346
      '瓜'        : ('瓜',),
      # jinmeiyō kanji #347
      '瓢'        : ('瓢',),
      # jinmeiyō kanji #348
      '甥'        : ('甥',),
      # jinmeiyō kanji #349
      '甫'        : ('甫',),
      # jinmeiyō kanji #350
      '畠'        : ('畠',),
      # jinmeiyō kanji #351
      '畢'        : ('畢',),
      # jinmeiyō kanji #352
      '疋'        : ('疋',),
      # jinmeiyō kanji #353
      '疏'        : ('疏',),
      # jinmeiyō kanji #354
      '皐'        : ('皐',),
      # jinmeiyō kanji #355
      '皓'        : ('皓',),
      # jinmeiyō kanji #356
      '眸'        : ('眸',),
      # jinmeiyō kanji #357
      '瞥'        : ('瞥',),
      # jinmeiyō kanji #358
      '矩'        : ('矩',),
      # jinmeiyō kanji #359
      '砦'        : ('砦',),
      # jinmeiyō kanji #360
      '砥'        : ('砥',),
      # jinmeiyō kanji #361
      '砧'        : ('砧',),
      # jinmeiyō kanji #362
      '硯'        : ('硯',),
      # jinmeiyō kanji #363
      '碓'        : ('碓',),
      # jinmeiyō kanji #364
      '碗'        : ('碗',),
      # jinmeiyō kanji #365
      '碩'        : ('碩',),
      # jinmeiyō kanji #366
      '碧'        : ('碧',),
      # jinmeiyō kanji #367
      '磐'        : ('磐',),
      # jinmeiyō kanji #368
      '磯'        : ('磯',),
      # jinmeiyō kanji #369
      '祇'        : ('祇',),
      # jinmeiyō kanji #370
      '祢'        : ('祢', '禰'),
      # jinmeiyō kanji #371
      '祐'        : ('祐', '祐'),
      # jinmeiyō kanji #372
      '祷'        : ('祷', '禱'),
      # jinmeiyō kanji #373
      '禄'        : ('禄', '祿'),
      # jinmeiyō kanji #374
      '禎'        : ('禎', '禎'),
      # jinmeiyō kanji #375
      '禽'        : ('禽',),
      # jinmeiyō kanji #376
      '禾'        : ('禾',),
      # jinmeiyō kanji #377
      '秦'        : ('秦',),
      # jinmeiyō kanji #378
      '秤'        : ('秤',),
      # jinmeiyō kanji #379
      '稀'        : ('稀',),
      # jinmeiyō kanji #380
      '稔'        : ('稔',),
      # jinmeiyō kanji #381
      '稟'        : ('稟',),
      # jinmeiyō kanji #382
      '稜'        : ('稜',),
      # jinmeiyō kanji #383
      '穣'        : ('穣', '穰'),
      # jinmeiyō kanji #384
      '穹'        : ('穹',),
      # jinmeiyō kanji #385
      '穿'        : ('穿',),
      # jinmeiyō kanji #386
      '窄'        : ('窄',),
      # jinmeiyō kanji #387
      '窪'        : ('窪',),
      # jinmeiyō kanji #388
      '窺'        : ('窺',),
      # jinmeiyō kanji #389
      '竣'        : ('竣',),
      # jinmeiyō kanji #390
      '竪'        : ('竪',),
      # jinmeiyō kanji #391
      '竺'        : ('竺',),
      # jinmeiyō kanji #392
      '竿'        : ('竿',),
      # jinmeiyō kanji #393
      '笈'        : ('笈',),
      # jinmeiyō kanji #394
      '笹'        : ('笹',),
      # jinmeiyō kanji #395
      '笙'        : ('笙',),
      # jinmeiyō kanji #396
      '笠'        : ('笠',),
      # jinmeiyō kanji #397
      '筈'        : ('筈',),
      # jinmeiyō kanji #398
      '筑'        : ('筑',),
      # jinmeiyō kanji #399
      '箕'        : ('箕',),
      # jinmeiyō kanji #400
      '箔'        : ('箔',),
      # jinmeiyō kanji #401
      '篇'        : ('篇',),
      # jinmeiyō kanji #402
      '篠'        : ('篠',),
      # jinmeiyō kanji #403
      '簞'        : ('簞',),
      # jinmeiyō kanji #404
      '簾'        : ('簾',),
      # jinmeiyō kanji #405
      '籾'        : ('籾',),
      # jinmeiyō kanji #406
      '粥'        : ('粥',),
      # jinmeiyō kanji #407
      '粟'        : ('粟',),
      # jinmeiyō kanji #408
      '糊'        : ('糊',),
      # jinmeiyō kanji #409
      '紘'        : ('紘',),
      # jinmeiyō kanji #410
      '紗'        : ('紗',),
      # jinmeiyō kanji #411
      '紐'        : ('紐',),
      # jinmeiyō kanji #412
      '絃'        : ('絃',),
      # jinmeiyō kanji #413
      '紬'        : ('紬',),
      # jinmeiyō kanji #414
      '絆'        : ('絆',),
      # jinmeiyō kanji #415
      '絢'        : ('絢',),
      # jinmeiyō kanji #416
      '綺'        : ('綺',),
      # jinmeiyō kanji #417
      '綜'        : ('綜',),
      # jinmeiyō kanji #418
      '綴'        : ('綴',),
      # jinmeiyō kanji #419
      '緋'        : ('緋',),
      # jinmeiyō kanji #420
      '綾'        : ('綾',),
      # jinmeiyō kanji #421
      '綸'        : ('綸',),
      # jinmeiyō kanji #422
      '縞'        : ('縞',),
      # jinmeiyō kanji #423
      '徽'        : ('徽',),
      # jinmeiyō kanji #424
      '繫'        : ('繫',),
      # jinmeiyō kanji #425
      '繡'        : ('繡',),
      # jinmeiyō kanji #426
      '纂'        : ('纂',),
      # jinmeiyō kanji #427
      '纏'        : ('纏',),
      # jinmeiyō kanji #428
      '羚'        : ('羚',),
      # jinmeiyō kanji #429
      '翔'        : ('翔',),
      # jinmeiyō kanji #430
      '翠'        : ('翠',),
      # jinmeiyō kanji #431
      '耀'        : ('耀',),
      # jinmeiyō kanji #432
      '而'        : ('而',),
      # jinmeiyō kanji #433
      '耶'        : ('耶',),
      # jinmeiyō kanji #434
      '耽'        : ('耽',),
      # jinmeiyō kanji #435
      '聡'        : ('聡',),
      # jinmeiyō kanji #436
      '肇'        : ('肇',),
      # jinmeiyō kanji #437
      '肋'        : ('肋',),
      # jinmeiyō kanji #438
      '肴'        : ('肴',),
      # jinmeiyō kanji #439
      '胤'        : ('胤',),
      # jinmeiyō kanji #440
      '胡'        : ('胡',),
      # jinmeiyō kanji #441
      '脩'        : ('脩',),
      # jinmeiyō kanji #442
      '腔'        : ('腔',),
      # jinmeiyō kanji #443
      '脹'        : ('脹',),
      # jinmeiyō kanji #444
      '膏'        : ('膏',),
      # jinmeiyō kanji #445
      '臥'        : ('臥',),
      # jinmeiyō kanji #446
      '舜'        : ('舜',),
      # jinmeiyō kanji #447
      '舵'        : ('舵',),
      # jinmeiyō kanji #448
      '芥'        : ('芥',),
      # jinmeiyō kanji #449
      '芹'        : ('芹',),
      # jinmeiyō kanji #450
      '芭'        : ('芭',),
      # jinmeiyō kanji #451
      '芙'        : ('芙',),
      # jinmeiyō kanji #452
      '芦'        : ('芦',),
      # jinmeiyō kanji #453
      '苑'        : ('苑',),
      # jinmeiyō kanji #454
      '茄'        : ('茄',),
      # jinmeiyō kanji #455
      '苔'        : ('苔',),
      # jinmeiyō kanji #456
      '苺'        : ('苺',),
      # jinmeiyō kanji #457
      '茅'        : ('茅',),
      # jinmeiyō kanji #458
      '茉'        : ('茉',),
      # jinmeiyō kanji #459
      '茸'        : ('茸',),
      # jinmeiyō kanji #460
      '茜'        : ('茜',),
      # jinmeiyō kanji #461
      '莞'        : ('莞',),
      # jinmeiyō kanji #462
      '荻'        : ('荻',),
      # jinmeiyō kanji #463
      '莫'        : ('莫',),
      # jinmeiyō kanji #464
      '莉'        : ('莉',),
      # jinmeiyō kanji #465
      '菅'        : ('菅',),
      # jinmeiyō kanji #466
      '菫'        : ('菫',),
      # jinmeiyō kanji #467
      '菖'        : ('菖',),
      # jinmeiyō kanji #468
      '萄'        : ('萄',),
      # jinmeiyō kanji #469
      '菩'        : ('菩',),
      # jinmeiyō kanji #470
      '萌'        : ('萌', '萠'),
      # jinmeiyō kanji #471
      '萊'        : ('萊',),
      # jinmeiyō kanji #472
      '菱'        : ('菱',),
      # jinmeiyō kanji #473
      '葦'        : ('葦',),
      # jinmeiyō kanji #474
      '葵'        : ('葵',),
      # jinmeiyō kanji #475
      '萱'        : ('萱',),
      # jinmeiyō kanji #476
      '葺'        : ('葺',),
      # jinmeiyō kanji #477
      '萩'        : ('萩',),
      # jinmeiyō kanji #478
      '董'        : ('董',),
      # jinmeiyō kanji #479
      '葡'        : ('葡',),
      # jinmeiyō kanji #480
      '蓑'        : ('蓑',),
      # jinmeiyō kanji #481
      '蒔'        : ('蒔',),
      # jinmeiyō kanji #482
      '蒐'        : ('蒐',),
      # jinmeiyō kanji #483
      '蒼'        : ('蒼',),
      # jinmeiyō kanji #484
      '蒲'        : ('蒲',),
      # jinmeiyō kanji #485
      '蒙'        : ('蒙',),
      # jinmeiyō kanji #486
      '蓉'        : ('蓉',),
      # jinmeiyō kanji #487
      '蓮'        : ('蓮',),
      # jinmeiyō kanji #488
      '蔭'        : ('蔭',),
      # jinmeiyō kanji #489
      '蔣'        : ('蔣',),
      # jinmeiyō kanji #490
      '蔦'        : ('蔦',),
      # jinmeiyō kanji #491
      '蓬'        : ('蓬',),
      # jinmeiyō kanji #492
      '蔓'        : ('蔓',),
      # jinmeiyō kanji #493
      '蕎'        : ('蕎',),
      # jinmeiyō kanji #494
      '蕨'        : ('蕨',),
      # jinmeiyō kanji #495
      '蕉'        : ('蕉',),
      # jinmeiyō kanji #496
      '蕃'        : ('蕃',),
      # jinmeiyō kanji #497
      '蕪'        : ('蕪',),
      # jinmeiyō kanji #498
      '薙'        : ('薙',),
      # jinmeiyō kanji #499
      '蕾'        : ('蕾',),
      # jinmeiyō kanji #500
      '蕗'        : ('蕗',),
      # jinmeiyō kanji #501
      '藁'        : ('藁',),
      # jinmeiyō kanji #502
      '薩'        : ('薩',),
      # jinmeiyō kanji #503
      '蘇'        : ('蘇',),
      # jinmeiyō kanji #504
      '蘭'        : ('蘭',),
      # jinmeiyō kanji #505
      '蝦'        : ('蝦',),
      # jinmeiyō kanji #506
      '蝶'        : ('蝶',),
      # jinmeiyō kanji #507
      '螺'        : ('螺',),
      # jinmeiyō kanji #508
      '蟬'        : ('蟬',),
      # jinmeiyō kanji #509
      '蟹'        : ('蟹',),
      # jinmeiyō kanji #510
      '蠟'        : ('蠟',),
      # jinmeiyō kanji #511
      '衿'        : ('衿',),
      # jinmeiyō kanji #512
      '袈'        : ('袈',),
      # jinmeiyō kanji #513
      '袴'        : ('袴',),
      # jinmeiyō kanji #514
      '裡'        : ('裡',),
      # jinmeiyō kanji #515
      '裟'        : ('裟',),
      # jinmeiyō kanji #516
      '裳'        : ('裳',),
      # jinmeiyō kanji #517
      '襖'        : ('襖',),
      # jinmeiyō kanji #518
      '訊'        : ('訊',),
      # jinmeiyō kanji #519
      '訣'        : ('訣',),
      # jinmeiyō kanji #520
      '註'        : ('註',),
      # jinmeiyō kanji #521
      '詢'        : ('詢',),
      # jinmeiyō kanji #522
      '詫'        : ('詫',),
      # jinmeiyō kanji #523
      '誼'        : ('誼',),
      # jinmeiyō kanji #524
      '諏'        : ('諏',),
      # jinmeiyō kanji #525
      '諄'        : ('諄',),
      # jinmeiyō kanji #526
      '諒'        : ('諒',),
      # jinmeiyō kanji #527
      '謂'        : ('謂',),
      # jinmeiyō kanji #528
      '諺'        : ('諺',),
      # jinmeiyō kanji #529
      '讃'        : ('讃',),
      # jinmeiyō kanji #530
      '豹'        : ('豹',),
      # jinmeiyō kanji #531
      '貰'        : ('貰',),
      # jinmeiyō kanji #532
      '賑'        : ('賑',),
      # jinmeiyō kanji #533
      '赳'        : ('赳',),
      # jinmeiyō kanji #534
      '跨'        : ('跨',),
      # jinmeiyō kanji #535
      '蹄'        : ('蹄',),
      # jinmeiyō kanji #536
      '蹟'        : ('蹟',),
      # jinmeiyō kanji #537
      '輔'        : ('輔',),
      # jinmeiyō kanji #538
      '輯'        : ('輯',),
      # jinmeiyō kanji #539
      '輿'        : ('輿',),
      # jinmeiyō kanji #540
      '轟'        : ('轟',),
      # jinmeiyō kanji #541
      '辰'        : ('辰',),
      # jinmeiyō kanji #542
      '辻'        : ('辻',),
      # jinmeiyō kanji #543
      '迂'        : ('迂',),
      # jinmeiyō kanji #544
      '迄'        : ('迄',),
      # jinmeiyō kanji #545
      '辿'        : ('辿',),
      # jinmeiyō kanji #546
      '迪'        : ('迪',),
      # jinmeiyō kanji #547
      '迦'        : ('迦',),
      # jinmeiyō kanji #548
      '這'        : ('這',),
      # jinmeiyō kanji #549
      '逞'        : ('逞',),
      # jinmeiyō kanji #550
      '逗'        : ('逗',),
      # jinmeiyō kanji #551
      '逢'        : ('逢',),
      # jinmeiyō kanji #552
      '遥'        : ('遥', '遙'),
      # jinmeiyō kanji #553
      '遁'        : ('遁',),
      # jinmeiyō kanji #554
      '遼'        : ('遼',),
      # jinmeiyō kanji #555
      '邑'        : ('邑',),
      # jinmeiyō kanji #556
      '祁'        : ('祁',),
      # jinmeiyō kanji #557
      '郁'        : ('郁',),
      # jinmeiyō kanji #558
      '鄭'        : ('鄭',),
      # jinmeiyō kanji #559
      '酉'        : ('酉',),
      # jinmeiyō kanji #560
      '醇'        : ('醇',),
      # jinmeiyō kanji #561
      '醐'        : ('醐',),
      # jinmeiyō kanji #562
      '醍'        : ('醍',),
      # jinmeiyō kanji #563
      '醬'        : ('醬',),
      # jinmeiyō kanji #564
      '釉'        : ('釉',),
      # jinmeiyō kanji #565
      '釘'        : ('釘',),
      # jinmeiyō kanji #566
      '釧'        : ('釧',),
      # jinmeiyō kanji #567
      '銑'        : ('銑',),
      # jinmeiyō kanji #568
      '鋒'        : ('鋒',),
      # jinmeiyō kanji #569
      '鋸'        : ('鋸',),
      # jinmeiyō kanji #570
      '錘'        : ('錘',),
      # jinmeiyō kanji #571
      '錐'        : ('錐',),
      # jinmeiyō kanji #572
      '錆'        : ('錆',),
      # jinmeiyō kanji #573
      '錫'        : ('錫',),
      # jinmeiyō kanji #574
      '鍬'        : ('鍬',),
      # jinmeiyō kanji #575
      '鎧'        : ('鎧',),
      # jinmeiyō kanji #576
      '閃'        : ('閃',),
      # jinmeiyō kanji #577
      '閏'        : ('閏',),
      # jinmeiyō kanji #578
      '閤'        : ('閤',),
      # jinmeiyō kanji #579
      '阿'        : ('阿',),
      # jinmeiyō kanji #580
      '陀'        : ('陀',),
      # jinmeiyō kanji #581
      '隈'        : ('隈',),
      # jinmeiyō kanji #582
      '隼'        : ('隼',),
      # jinmeiyō kanji #583
      '雀'        : ('雀',),
      # jinmeiyō kanji #584
      '雁'        : ('雁',),
      # jinmeiyō kanji #585
      '雛'        : ('雛',),
      # jinmeiyō kanji #586
      '雫'        : ('雫',),
      # jinmeiyō kanji #587
      '霞'        : ('霞',),
      # jinmeiyō kanji #588
      '靖'        : ('靖',),
      # jinmeiyō kanji #589
      '鞄'        : ('鞄',),
      # jinmeiyō kanji #590
      '鞍'        : ('鞍',),
      # jinmeiyō kanji #591
      '鞘'        : ('鞘',),
      # jinmeiyō kanji #592
      '鞠'        : ('鞠',),
      # jinmeiyō kanji #593
      '鞭'        : ('鞭',),
      # jinmeiyō kanji #594
      '頁'        : ('頁',),
      # jinmeiyō kanji #595
      '頌'        : ('頌',),
      # jinmeiyō kanji #596
      '頗'        : ('頗',),
      # jinmeiyō kanji #597
      '顚'        : ('顚',),
      # jinmeiyō kanji #598
      '颯'        : ('颯',),
      # jinmeiyō kanji #599
      '饗'        : ('饗',),
      # jinmeiyō kanji #600
      '馨'        : ('馨',),
      # jinmeiyō kanji #601
      '馴'        : ('馴',),
      # jinmeiyō kanji #602
      '馳'        : ('馳',),
      # jinmeiyō kanji #603
      '駕'        : ('駕',),
      # jinmeiyō kanji #604
      '駿'        : ('駿',),
      # jinmeiyō kanji #605
      '驍'        : ('驍',),
      # jinmeiyō kanji #606
      '魁'        : ('魁',),
      # jinmeiyō kanji #607
      '魯'        : ('魯',),
      # jinmeiyō kanji #608
      '鮎'        : ('鮎',),
      # jinmeiyō kanji #609
      '鯉'        : ('鯉',),
      # jinmeiyō kanji #610
      '鯛'        : ('鯛',),
      # jinmeiyō kanji #611
      '鰯'        : ('鰯',),
      # jinmeiyō kanji #612
      '鱒'        : ('鱒',),
      # jinmeiyō kanji #613
      '鱗'        : ('鱗',),
      # jinmeiyō kanji #614
      '鳩'        : ('鳩',),
      # jinmeiyō kanji #615
      '鳶'        : ('鳶',),
      # jinmeiyō kanji #616
      '鳳'        : ('鳳',),
      # jinmeiyō kanji #617
      '鴨'        : ('鴨',),
      # jinmeiyō kanji #618
      '鴻'        : ('鴻',),
      # jinmeiyō kanji #619
      '鵜'        : ('鵜',),
      # jinmeiyō kanji #620
      '鵬'        : ('鵬',),
      # jinmeiyō kanji #621
      '鷗'        : ('鷗',),
      # jinmeiyō kanji #622
      '鷲'        : ('鷲',),
      # jinmeiyō kanji #623
      '鷺'        : ('鷺',),
      # jinmeiyō kanji #624
      '鷹'        : ('鷹',),
      # jinmeiyō kanji #625
      '麒'        : ('麒',),
      # jinmeiyō kanji #626
      '麟'        : ('麟',),
      # jinmeiyō kanji #627
      '麿'        : ('麿',),
      # jinmeiyō kanji #628
      '黎'        : ('黎',),
      # jinmeiyō kanji #629
      '黛'        : ('黛',),
      # jinmeiyō kanji #630
      '鼎'        : ('鼎',),

      # hyōgaiji kanji #1
      '啞'        : ('啞', '唖'),
      # hyōgaiji kanji #2
      '蛙'        : ('蛙',),
      # hyōgaiji kanji #3
      '鴉'        : ('鴉',),
      # hyōgaiji kanji #4
      '埃'        : ('埃',),
      # hyōgaiji kanji #5
      '挨'        : ('挨',),
      # hyōgaiji kanji #6
      '曖'        : ('曖',),
      # hyōgaiji kanji #7
      '靄'        : ('靄',),
      # hyōgaiji kanji #8
      '軋'        : ('軋',),
      # hyōgaiji kanji #9
      '斡'        : ('斡',),
      # hyōgaiji kanji #10
      '按'        : ('按',),
      # hyōgaiji kanji #11
      '庵'        : ('庵',),
      # hyōgaiji kanji #12
      '鞍'        : ('鞍',),
      # hyōgaiji kanji #13
      '闇'        : ('闇',),
      # hyōgaiji kanji #14
      '已'        : ('已',),
      # hyōgaiji kanji #15
      '夷'        : ('夷',),
      # hyōgaiji kanji #16
      '畏'        : ('畏',),
      # hyōgaiji kanji #17
      '韋'        : ('韋',),
      # hyōgaiji kanji #18
      '帷'        : ('帷',),
      # hyōgaiji kanji #19
      '萎'        : ('萎',),
      # hyōgaiji kanji #20
      '椅'        : ('椅',),
      # hyōgaiji kanji #21
      '葦'        : ('葦',),
      # hyōgaiji kanji #22
      '彙'        : ('彙',),
      # hyōgaiji kanji #23
      '飴'        : ('飴',),
      # hyōgaiji kanji #24
      '謂'        : ('謂',),
      # hyōgaiji kanji #25
      '閾'        : ('閾',),
      # hyōgaiji kanji #26
      '溢'        : ('溢',),
      # hyōgaiji kanji #27
      '鰯'        : ('鰯',),
      # hyōgaiji kanji #28
      '尹'        : ('尹',),
      # hyōgaiji kanji #29
      '咽'        : ('咽',),
      # hyōgaiji kanji #30
      '殷'        : ('殷',),
      # hyōgaiji kanji #31
      '淫'        : ('淫',),
      # hyōgaiji kanji #32
      '隕'        : ('隕',),
      # hyōgaiji kanji #33
      '蔭'        : ('蔭',),
      # hyōgaiji kanji #34
      '于'        : ('于',),
      # hyōgaiji kanji #35
      '迂'        : ('迂',),
      # hyōgaiji kanji #36
      '盂'        : ('盂',),
      # hyōgaiji kanji #37
      '烏'        : ('烏',),
      # hyōgaiji kanji #38
      '鬱'        : ('鬱',),
      # hyōgaiji kanji #39
      '云'        : ('云',),
      # hyōgaiji kanji #40
      '暈'        : ('暈',),
      # hyōgaiji kanji #41
      '穢'        : ('穢',),
      # hyōgaiji kanji #42
      '曳'        : ('曳',),
      # hyōgaiji kanji #43
      '洩'        : ('洩',),
      # hyōgaiji kanji #44
      '裔'        : ('裔',),
      # hyōgaiji kanji #45
      '穎'        : ('穎', '頴'),
      # hyōgaiji kanji #46
      '嬰'        : ('嬰',),
      # hyōgaiji kanji #47
      '翳'        : ('翳',),
      # hyōgaiji kanji #48
      '腋'        : ('腋',),
      # hyōgaiji kanji #49
      '曰'        : ('曰',),
      # hyōgaiji kanji #50
      '奄'        : ('奄',),
      # hyōgaiji kanji #51
      '宛'        : ('宛',),
      # hyōgaiji kanji #52
      '怨'        : ('怨',),
      # hyōgaiji kanji #53
      '俺'        : ('俺',),
      # hyōgaiji kanji #54
      '冤'        : ('冤',),
      # hyōgaiji kanji #55
      '袁'        : ('袁',),
      # hyōgaiji kanji #56
      '婉'        : ('婉',),
      # hyōgaiji kanji #57
      '焉'        : ('焉',),
      # hyōgaiji kanji #58
      '堰'        : ('堰',),
      # hyōgaiji kanji #59
      '淵'        : ('淵',),
      # hyōgaiji kanji #60
      '焰'        : ('焰',),
      # hyōgaiji kanji #61
      '筵'        : ('筵',),
      # hyōgaiji kanji #62
      '厭'        : ('厭',),
      # hyōgaiji kanji #63
      '鳶'        : ('鳶',),
      # hyōgaiji kanji #64
      '燕'        : ('燕',),
      # hyōgaiji kanji #65
      '閻'        : ('閻',),
      # hyōgaiji kanji #66
      '嚥'        : ('嚥',),
      # hyōgaiji kanji #67
      '嗚'        : ('嗚',),
      # hyōgaiji kanji #68
      '凰'        : ('凰',),
      # hyōgaiji kanji #69
      '嘔'        : ('嘔',),
      # hyōgaiji kanji #70
      '鴨'        : ('鴨',),
      # hyōgaiji kanji #71
      '甕'        : ('甕',),
      # hyōgaiji kanji #72
      '襖'        : ('襖',),
      # hyōgaiji kanji #73
      '謳'        : ('謳',),
      # hyōgaiji kanji #74
      '鶯'        : ('鶯',),
      # hyōgaiji kanji #75
      '鷗'        : ('鷗', '鴎'),
      # hyōgaiji kanji #76
      '鸚'        : ('鸚',),
      # hyōgaiji kanji #77
      '臆'        : ('臆',),
      # hyōgaiji kanji #78
      '俤'        : ('俤',),
      # hyōgaiji kanji #79
      '瓜'        : ('瓜',),
      # hyōgaiji kanji #80
      '呵'        : ('呵',),
      # hyōgaiji kanji #81
      '苛'        : ('苛',),
      # hyōgaiji kanji #82
      '珂'        : ('珂',),
      # hyōgaiji kanji #83
      '迦'        : ('迦',),
      # hyōgaiji kanji #84
      '訛'        : ('訛',),
      # hyōgaiji kanji #85
      '訶'        : ('訶',),
      # hyōgaiji kanji #86
      '跏'        : ('跏',),
      # hyōgaiji kanji #87
      '嘩'        : ('嘩',),
      # hyōgaiji kanji #88
      '瑕'        : ('瑕',),
      # hyōgaiji kanji #89
      '榎'        : ('榎',),
      # hyōgaiji kanji #90
      '窩'        : ('窩',),
      # hyōgaiji kanji #91
      '蝦'        : ('蝦',),
      # hyōgaiji kanji #92
      '蝸'        : ('蝸',),
      # hyōgaiji kanji #93
      '鍋'        : ('鍋',),
      # hyōgaiji kanji #94
      '顆'        : ('顆',),
      # hyōgaiji kanji #95
      '牙'        : ('牙',),
      # hyōgaiji kanji #96
      '瓦'        : ('瓦',),
      # hyōgaiji kanji #97
      '臥'        : ('臥',),
      # hyōgaiji kanji #98
      '俄'        : ('俄',),
      # hyōgaiji kanji #99
      '峨'        : ('峨',),
      # hyōgaiji kanji #100
      '訝'        : ('訝',),
      # hyōgaiji kanji #101
      '蛾'        : ('蛾',),
      # hyōgaiji kanji #102
      '衙'        : ('衙',),
      # hyōgaiji kanji #103
      '駕'        : ('駕',),
      # hyōgaiji kanji #104
      '芥'        : ('芥',),
      # hyōgaiji kanji #105
      '乖'        : ('乖',),
      # hyōgaiji kanji #106
      '廻'        : ('廻',),
      # hyōgaiji kanji #107
      '徊'        : ('徊',),
      # hyōgaiji kanji #108
      '恢'        : ('恢',),
      # hyōgaiji kanji #109
      '晦'        : ('晦',),
      # hyōgaiji kanji #110
      '堺'        : ('堺',),
      # hyōgaiji kanji #111
      '潰'        : ('潰',),
      # hyōgaiji kanji #112
      '鞋'        : ('鞋',),
      # hyōgaiji kanji #113
      '諧'        : ('諧',),
      # hyōgaiji kanji #114
      '檜'        : ('檜',),
      # hyōgaiji kanji #115
      '蟹'        : ('蟹',),
      # hyōgaiji kanji #116
      '咳'        : ('咳',),
      # hyōgaiji kanji #117
      '崖'        : ('崖',),
      # hyōgaiji kanji #118
      '蓋'        : ('蓋',),
      # hyōgaiji kanji #119
      '漑'        : ('漑',),
      # hyōgaiji kanji #120
      '骸'        : ('骸',),
      # hyōgaiji kanji #121
      '鎧'        : ('鎧',),
      # hyōgaiji kanji #122
      '喀'        : ('喀',),
      # hyōgaiji kanji #123
      '廓'        : ('廓',),
      # hyōgaiji kanji #124
      '摑'        : ('摑',),
      # hyōgaiji kanji #125
      '攪'        : ('攪', '撹'),
      # hyōgaiji kanji #126
      '愕'        : ('愕',),
      # hyōgaiji kanji #127
      '萼'        : ('萼',),
      # hyōgaiji kanji #128
      '諤'        : ('諤',),
      # hyōgaiji kanji #129
      '顎'        : ('顎',),
      # hyōgaiji kanji #130
      '鰐'        : ('鰐',),
      # hyōgaiji kanji #131
      '樫'        : ('樫',),
      # hyōgaiji kanji #132
      '絣'        : ('絣',),
      # hyōgaiji kanji #133
      '筈'        : ('筈',),
      # hyōgaiji kanji #134
      '葛'        : ('葛',),
      # hyōgaiji kanji #135
      '闊'        : ('闊',),
      # hyōgaiji kanji #136
      '鰹'        : ('鰹',),
      # hyōgaiji kanji #137
      '萱'        : ('萱',),
      # hyōgaiji kanji #138
      '奸'        : ('奸',),
      # hyōgaiji kanji #139
      '串'        : ('串',),
      # hyōgaiji kanji #140
      '旱'        : ('旱',),
      # hyōgaiji kanji #141
      '函'        : ('函',),
      # hyōgaiji kanji #142
      '咸'        : ('咸',),
      # hyōgaiji kanji #143
      '姦'        : ('姦',),
      # hyōgaiji kanji #144
      '宦'        : ('宦',),
      # hyōgaiji kanji #145
      '柑'        : ('柑',),
      # hyōgaiji kanji #146
      '竿'        : ('竿',),
      # hyōgaiji kanji #147
      '悍'        : ('悍',),
      # hyōgaiji kanji #148
      '桓'        : ('桓',),
      # hyōgaiji kanji #149
      '涵'        : ('涵',),
      # hyōgaiji kanji #150
      '菅'        : ('菅',),
      # hyōgaiji kanji #151
      '嵌'        : ('嵌',),
      # hyōgaiji kanji #152
      '鉗'        : ('鉗',),
      # hyōgaiji kanji #153
      '澗'        : ('澗',),
      # hyōgaiji kanji #154
      '翰'        : ('翰',),
      # hyōgaiji kanji #155
      '諫'        : ('諫',),
      # hyōgaiji kanji #156
      '瞰'        : ('瞰',),
      # hyōgaiji kanji #157
      '韓'        : ('韓',),
      # hyōgaiji kanji #158
      '檻'        : ('檻',),
      # hyōgaiji kanji #159
      '灌'        : ('灌',),
      # hyōgaiji kanji #160
      '玩'        : ('玩',),
      # hyōgaiji kanji #161
      '雁'        : ('雁',),
      # hyōgaiji kanji #162
      '翫'        : ('翫',),
      # hyōgaiji kanji #163
      '頷'        : ('頷',),
      # hyōgaiji kanji #164
      '癌'        : ('癌',),
      # hyōgaiji kanji #165
      '贋'        : ('贋',),
      # hyōgaiji kanji #166
      '几'        : ('几',),
      # hyōgaiji kanji #167
      '卉'        : ('卉',),
      # hyōgaiji kanji #168
      '其'        : ('其',),
      # hyōgaiji kanji #169
      '祁'        : ('祁',),
      # hyōgaiji kanji #170
      '耆'        : ('耆',),
      # hyōgaiji kanji #171
      '埼'        : ('埼',),
      # hyōgaiji kanji #172
      '悸'        : ('悸',),
      # hyōgaiji kanji #173
      '揆'        : ('揆',),
      # hyōgaiji kanji #174
      '毀'        : ('毀',),
      # hyōgaiji kanji #175
      '箕'        : ('箕',),
      # hyōgaiji kanji #176
      '畿'        : ('畿',),
      # hyōgaiji kanji #177
      '窺'        : ('窺',),
      # hyōgaiji kanji #178
      '諱'        : ('諱',),
      # hyōgaiji kanji #179
      '徽'        : ('徽',),
      # hyōgaiji kanji #180
      '櫃'        : ('櫃',),
      # hyōgaiji kanji #181
      '妓'        : ('妓',),
      # hyōgaiji kanji #182
      '祇'        : ('祇',),
      # hyōgaiji kanji #183
      '魏'        : ('魏',),
      # hyōgaiji kanji #184
      '蟻'        : ('蟻',),
      # hyōgaiji kanji #185
      '掬'        : ('掬',),
      # hyōgaiji kanji #186
      '麴'        : ('麴', '麹'),
      # hyōgaiji kanji #187
      '吃'        : ('吃',),
      # hyōgaiji kanji #188
      '屹'        : ('屹',),
      # hyōgaiji kanji #189
      '拮'        : ('拮',),
      # hyōgaiji kanji #190
      '謔'        : ('謔',),
      # hyōgaiji kanji #191
      '仇'        : ('仇',),
      # hyōgaiji kanji #192
      '臼'        : ('臼',),
      # hyōgaiji kanji #193
      '汲'        : ('汲',),
      # hyōgaiji kanji #194
      '灸'        : ('灸',),
      # hyōgaiji kanji #195
      '咎'        : ('咎',),
      # hyōgaiji kanji #196
      '邱'        : ('邱',),
      # hyōgaiji kanji #197
      '柩'        : ('柩',),
      # hyōgaiji kanji #198
      '笈'        : ('笈',),
      # hyōgaiji kanji #199
      '躬'        : ('躬',),
      # hyōgaiji kanji #200
      '厩'        : ('厩',),
      # hyōgaiji kanji #201
      '嗅'        : ('嗅',),
      # hyōgaiji kanji #202
      '舅'        : ('舅',),
      # hyōgaiji kanji #203
      '炬'        : ('炬',),
      # hyōgaiji kanji #204
      '渠'        : ('渠',),
      # hyōgaiji kanji #205
      '裾'        : ('裾',),
      # hyōgaiji kanji #206
      '噓'        : ('噓',),
      # hyōgaiji kanji #207
      '墟'        : ('墟',),
      # hyōgaiji kanji #208
      '鋸'        : ('鋸',),
      # hyōgaiji kanji #209
      '遽'        : ('遽',),
      # hyōgaiji kanji #210
      '欅'        : ('欅',),
      # hyōgaiji kanji #211
      '匈'        : ('匈',),
      # hyōgaiji kanji #212
      '怯'        : ('怯',),
      # hyōgaiji kanji #213
      '俠'        : ('俠',),
      # hyōgaiji kanji #214
      '脇'        : ('脇',),
      # hyōgaiji kanji #215
      '莢'        : ('莢',),
      # hyōgaiji kanji #216
      '竟'        : ('竟',),
      # hyōgaiji kanji #217
      '卿'        : ('卿',),
      # hyōgaiji kanji #218
      '僑'        : ('僑',),
      # hyōgaiji kanji #219
      '嬌'        : ('嬌',),
      # hyōgaiji kanji #220
      '蕎'        : ('蕎',),
      # hyōgaiji kanji #221
      '鋏'        : ('鋏',),
      # hyōgaiji kanji #222
      '頰'        : ('頰',),
      # hyōgaiji kanji #223
      '橿'        : ('橿',),
      # hyōgaiji kanji #224
      '疆'        : ('疆',),
      # hyōgaiji kanji #225
      '饗'        : ('饗',),
      # hyōgaiji kanji #226
      '棘'        : ('棘',),
      # hyōgaiji kanji #227
      '髷'        : ('髷',),
      # hyōgaiji kanji #228
      '巾'        : ('巾',),
      # hyōgaiji kanji #229
      '僅'        : ('僅',),
      # hyōgaiji kanji #230
      '禽'        : ('禽',),
      # hyōgaiji kanji #231
      '饉'        : ('饉',),
      # hyōgaiji kanji #232
      '狗'        : ('狗',),
      # hyōgaiji kanji #233
      '惧'        : ('惧',),
      # hyōgaiji kanji #234
      '軀'        : ('軀',),
      # hyōgaiji kanji #235
      '懼'        : ('懼',),
      # hyōgaiji kanji #236
      '俱'        : ('俱',),
      # hyōgaiji kanji #237
      '喰'        : ('喰',),
      # hyōgaiji kanji #238
      '寓'        : ('寓',),
      # hyōgaiji kanji #239
      '窟'        : ('窟',),
      # hyōgaiji kanji #240
      '粂'        : ('粂',),
      # hyōgaiji kanji #241
      '偈'        : ('偈',),
      # hyōgaiji kanji #242
      '荊'        : ('荊',),
      # hyōgaiji kanji #243
      '珪'        : ('珪',),
      # hyōgaiji kanji #244
      '畦'        : ('畦',),
      # hyōgaiji kanji #245
      '脛'        : ('脛',),
      # hyōgaiji kanji #246
      '頃'        : ('頃',),
      # hyōgaiji kanji #247
      '痙'        : ('痙',),
      # hyōgaiji kanji #248
      '詣'        : ('詣',),
      # hyōgaiji kanji #249
      '禊'        : ('禊',),
      # hyōgaiji kanji #250
      '閨'        : ('閨',),
      # hyōgaiji kanji #251
      '稽'        : ('稽',),
      # hyōgaiji kanji #252
      '頸'        : ('頸',),
      # hyōgaiji kanji #253
      '髻'        : ('髻',),
      # hyōgaiji kanji #254
      '蹊'        : ('蹊',),
      # hyōgaiji kanji #255
      '鮭'        : ('鮭',),
      # hyōgaiji kanji #256
      '繫'        : ('繫',),
      # hyōgaiji kanji #257
      '睨'        : ('睨',),
      # hyōgaiji kanji #258
      '戟'        : ('戟',),
      # hyōgaiji kanji #259
      '隙'        : ('隙',),
      # hyōgaiji kanji #260
      '抉'        : ('抉',),
      # hyōgaiji kanji #261
      '頁'        : ('頁',),
      # hyōgaiji kanji #262
      '訣'        : ('訣',),
      # hyōgaiji kanji #263
      '蕨'        : ('蕨',),
      # hyōgaiji kanji #264
      '姸'        : ('姸',),
      # hyōgaiji kanji #265
      '倦'        : ('倦',),
      # hyōgaiji kanji #266
      '虔'        : ('虔',),
      # hyōgaiji kanji #267
      '捲'        : ('捲',),
      # hyōgaiji kanji #268
      '牽'        : ('牽',),
      # hyōgaiji kanji #269
      '喧'        : ('喧',),
      # hyōgaiji kanji #270
      '硯'        : ('硯',),
      # hyōgaiji kanji #271
      '腱'        : ('腱',),
      # hyōgaiji kanji #272
      '鍵'        : ('鍵',),
      # hyōgaiji kanji #273
      '瞼'        : ('瞼',),
      # hyōgaiji kanji #274
      '鹼'        : ('鹼', '鹸'),
      # hyōgaiji kanji #275
      '呟'        : ('呟',),
      # hyōgaiji kanji #276
      '眩'        : ('眩',),
      # hyōgaiji kanji #277
      '舷'        : ('舷',),
      # hyōgaiji kanji #278
      '諺'        : ('諺',),
      # hyōgaiji kanji #279
      '乎'        : ('乎',),
      # hyōgaiji kanji #280
      '姑'        : ('姑',),
      # hyōgaiji kanji #281
      '狐'        : ('狐',),
      # hyōgaiji kanji #282
      '股'        : ('股',),
      # hyōgaiji kanji #283
      '涸'        : ('涸',),
      # hyōgaiji kanji #284
      '菰'        : ('菰',),
      # hyōgaiji kanji #285
      '袴'        : ('袴',),
      # hyōgaiji kanji #286
      '壺'        : ('壺',),
      # hyōgaiji kanji #287
      '跨'        : ('跨',),
      # hyōgaiji kanji #288
      '糊'        : ('糊',),
      # hyōgaiji kanji #289
      '醐'        : ('醐',),
      # hyōgaiji kanji #290
      '齬'        : ('齬',),
      # hyōgaiji kanji #291
      '亢'        : ('亢',),
      # hyōgaiji kanji #292
      '勾'        : ('勾',),
      # hyōgaiji kanji #293
      '叩'        : ('叩',),
      # hyōgaiji kanji #294
      '尻'        : ('尻',),
      # hyōgaiji kanji #295
      '吼'        : ('吼',),
      # hyōgaiji kanji #296
      '肛'        : ('肛',),
      # hyōgaiji kanji #297
      '岡'        : ('岡',),
      # hyōgaiji kanji #298
      '庚'        : ('庚',),
      # hyōgaiji kanji #299
      '杭'        : ('杭',),
      # hyōgaiji kanji #300
      '肴'        : ('肴',),
      # hyōgaiji kanji #301
      '咬'        : ('咬',),
      # hyōgaiji kanji #302
      '垢'        : ('垢',),
      # hyōgaiji kanji #303
      '巷'        : ('巷',),
      # hyōgaiji kanji #304
      '恍'        : ('恍',),
      # hyōgaiji kanji #305
      '恰'        : ('恰',),
      # hyōgaiji kanji #306
      '狡'        : ('狡',),
      # hyōgaiji kanji #307
      '桁'        : ('桁',),
      # hyōgaiji kanji #308
      '胱'        : ('胱',),
      # hyōgaiji kanji #309
      '崗'        : ('崗',),
      # hyōgaiji kanji #310
      '梗'        : ('梗',),
      # hyōgaiji kanji #311
      '喉'        : ('喉',),
      # hyōgaiji kanji #312
      '腔'        : ('腔',),
      # hyōgaiji kanji #313
      '蛤'        : ('蛤',),
      # hyōgaiji kanji #314
      '幌'        : ('幌',),
      # hyōgaiji kanji #315
      '煌'        : ('煌',),
      # hyōgaiji kanji #316
      '鉤'        : ('鉤',),
      # hyōgaiji kanji #317
      '敲'        : ('敲',),
      # hyōgaiji kanji #318
      '睾'        : ('睾',),
      # hyōgaiji kanji #319
      '膏'        : ('膏',),
      # hyōgaiji kanji #320
      '閤'        : ('閤',),
      # hyōgaiji kanji #321
      '膠'        : ('膠',),
      # hyōgaiji kanji #322
      '篝'        : ('篝',),
      # hyōgaiji kanji #323
      '縞'        : ('縞',),
      # hyōgaiji kanji #324
      '薨'        : ('薨',),
      # hyōgaiji kanji #325
      '糠'        : ('糠',),
      # hyōgaiji kanji #326
      '藁'        : ('藁',),
      # hyōgaiji kanji #327
      '鮫'        : ('鮫',),
      # hyōgaiji kanji #328
      '壙'        : ('壙',),
      # hyōgaiji kanji #329
      '曠'        : ('曠',),
      # hyōgaiji kanji #330
      '劫'        : ('劫',),
      # hyōgaiji kanji #331
      '毫'        : ('毫',),
      # hyōgaiji kanji #332
      '傲'        : ('傲',),
      # hyōgaiji kanji #333
      '壕'        : ('壕',),
      # hyōgaiji kanji #334
      '濠'        : ('濠',),
      # hyōgaiji kanji #335
      '嚙'        : ('嚙', '噛'),
      # hyōgaiji kanji #336
      '轟'        : ('轟',),
      # hyōgaiji kanji #337
      '剋'        : ('剋',),
      # hyōgaiji kanji #338
      '哭'        : ('哭',),
      # hyōgaiji kanji #339
      '鵠'        : ('鵠',),
      # hyōgaiji kanji #340
      '乞'        : ('乞',),
      # hyōgaiji kanji #341
      '忽'        : ('忽',),
      # hyōgaiji kanji #342
      '惚'        : ('惚',),
      # hyōgaiji kanji #343
      '昏'        : ('昏',),
      # hyōgaiji kanji #344
      '痕'        : ('痕',),
      # hyōgaiji kanji #345
      '渾'        : ('渾',),
      # hyōgaiji kanji #346
      '褌'        : ('褌',),
      # hyōgaiji kanji #347
      '叉'        : ('叉',),
      # hyōgaiji kanji #348
      '些'        : ('些',),
      # hyōgaiji kanji #349
      '嗟'        : ('嗟',),
      # hyōgaiji kanji #350
      '蓑'        : ('蓑',),
      # hyōgaiji kanji #351
      '磋'        : ('磋',),
      # hyōgaiji kanji #352
      '坐'        : ('坐',),
      # hyōgaiji kanji #353
      '挫'        : ('挫',),
      # hyōgaiji kanji #354
      '晒'        : ('晒',),
      # hyōgaiji kanji #355
      '柴'        : ('柴',),
      # hyōgaiji kanji #356
      '砦'        : ('砦',),
      # hyōgaiji kanji #357
      '犀'        : ('犀',),
      # hyōgaiji kanji #358
      '賽'        : ('賽',),
      # hyōgaiji kanji #359
      '鰓'        : ('鰓',),
      # hyōgaiji kanji #360
      '榊'        : ('榊',),
      # hyōgaiji kanji #361
      '柵'        : ('柵',),
      # hyōgaiji kanji #362
      '炸'        : ('炸',),
      # hyōgaiji kanji #363
      '窄'        : ('窄',),
      # hyōgaiji kanji #364
      '簀'        : ('簀',),
      # hyōgaiji kanji #365
      '刹'        : ('刹',),
      # hyōgaiji kanji #366
      '拶'        : ('拶',),
      # hyōgaiji kanji #367
      '紮'        : ('紮',),
      # hyōgaiji kanji #368
      '撒'        : ('撒',),
      # hyōgaiji kanji #369
      '薩'        : ('薩',),
      # hyōgaiji kanji #370
      '珊'        : ('珊',),
      # hyōgaiji kanji #371
      '餐'        : ('餐',),
      # hyōgaiji kanji #372
      '纂'        : ('纂',),
      # hyōgaiji kanji #373
      '霰'        : ('霰',),
      # hyōgaiji kanji #374
      '攢'        : ('攢',),
      # hyōgaiji kanji #375
      '讃'        : ('讃',),
      # hyōgaiji kanji #376
      '斬'        : ('斬',),
      # hyōgaiji kanji #377
      '懺'        : ('懺',),
      # hyōgaiji kanji #378
      '仔'        : ('仔',),
      # hyōgaiji kanji #379
      '弛'        : ('弛',),
      # hyōgaiji kanji #380
      '此'        : ('此',),
      # hyōgaiji kanji #381
      '址'        : ('址',),
      # hyōgaiji kanji #382
      '祀'        : ('祀',),
      # hyōgaiji kanji #383
      '屍'        : ('屍',),
      # hyōgaiji kanji #384
      '屎'        : ('屎',),
      # hyōgaiji kanji #385
      '柿'        : ('柿',),
      # hyōgaiji kanji #386
      '茨'        : ('茨',),
      # hyōgaiji kanji #387
      '恣'        : ('恣',),
      # hyōgaiji kanji #388
      '砥'        : ('砥',),
      # hyōgaiji kanji #389
      '祠'        : ('祠',),
      # hyōgaiji kanji #390
      '翅'        : ('翅',),
      # hyōgaiji kanji #391
      '舐'        : ('舐',),
      # hyōgaiji kanji #392
      '疵'        : ('疵',),
      # hyōgaiji kanji #393
      '趾'        : ('趾',),
      # hyōgaiji kanji #394
      '斯'        : ('斯',),
      # hyōgaiji kanji #395
      '覗'        : ('覗',),
      # hyōgaiji kanji #396
      '嗜'        : ('嗜',),
      # hyōgaiji kanji #397
      '滓'        : ('滓',),
      # hyōgaiji kanji #398
      '獅'        : ('獅',),
      # hyōgaiji kanji #399
      '幟'        : ('幟',),
      # hyōgaiji kanji #400
      '摯'        : ('摯',),
      # hyōgaiji kanji #401
      '嘴'        : ('嘴',),
      # hyōgaiji kanji #402
      '熾'        : ('熾',),
      # hyōgaiji kanji #403
      '髭'        : ('髭',),
      # hyōgaiji kanji #404
      '贄'        : ('贄',),
      # hyōgaiji kanji #405
      '而'        : ('而',),
      # hyōgaiji kanji #406
      '峙'        : ('峙',),
      # hyōgaiji kanji #407
      '痔'        : ('痔',),
      # hyōgaiji kanji #408
      '餌'        : ('餌',),
      # hyōgaiji kanji #409
      '竺'        : ('竺',),
      # hyōgaiji kanji #410
      '雫'        : ('雫',),
      # hyōgaiji kanji #411
      '𠮟'        : ('𠮟',),
      # hyōgaiji kanji #412
      '悉'        : ('悉',),
      # hyōgaiji kanji #413
      '蛭'        : ('蛭',),
      # hyōgaiji kanji #414
      '嫉'        : ('嫉',),
      # hyōgaiji kanji #415
      '膝'        : ('膝',),
      # hyōgaiji kanji #416
      '櫛'        : ('櫛',),
      # hyōgaiji kanji #417
      '柘'        : ('柘',),
      # hyōgaiji kanji #418
      '洒'        : ('洒',),
      # hyōgaiji kanji #419
      '娑'        : ('娑',),
      # hyōgaiji kanji #420
      '這'        : ('這',),
      # hyōgaiji kanji #421
      '奢'        : ('奢',),
      # hyōgaiji kanji #422
      '闍'        : ('闍',),
      # hyōgaiji kanji #423
      '杓'        : ('杓',),
      # hyōgaiji kanji #424
      '灼'        : ('灼',),
      # hyōgaiji kanji #425
      '綽'        : ('綽',),
      # hyōgaiji kanji #426
      '錫'        : ('錫',),
      # hyōgaiji kanji #427
      '雀'        : ('雀',),
      # hyōgaiji kanji #428
      '惹'        : ('惹',),
      # hyōgaiji kanji #429
      '娶'        : ('娶',),
      # hyōgaiji kanji #430
      '腫'        : ('腫',),
      # hyōgaiji kanji #431
      '諏'        : ('諏',),
      # hyōgaiji kanji #432
      '鬚'        : ('鬚',),
      # hyōgaiji kanji #433
      '呪'        : ('呪',),
      # hyōgaiji kanji #434
      '竪'        : ('竪',),
      # hyōgaiji kanji #435
      '綬'        : ('綬',),
      # hyōgaiji kanji #436
      '聚'        : ('聚',),
      # hyōgaiji kanji #437
      '濡'        : ('濡',),
      # hyōgaiji kanji #438
      '襦'        : ('襦',),
      # hyōgaiji kanji #439
      '帚'        : ('帚',),
      # hyōgaiji kanji #440
      '酋'        : ('酋',),
      # hyōgaiji kanji #441
      '袖'        : ('袖',),
      # hyōgaiji kanji #442
      '羞'        : ('羞',),
      # hyōgaiji kanji #443
      '葺'        : ('葺',),
      # hyōgaiji kanji #444
      '蒐'        : ('蒐',),
      # hyōgaiji kanji #445
      '箒'        : ('箒',),
      # hyōgaiji kanji #446
      '皺'        : ('皺',),
      # hyōgaiji kanji #447
      '輯'        : ('輯',),
      # hyōgaiji kanji #448
      '鍬'        : ('鍬',),
      # hyōgaiji kanji #449
      '繡'        : ('繡', '繍'),
      # hyōgaiji kanji #450
      '蹴'        : ('蹴',),
      # hyōgaiji kanji #451
      '讐'        : ('讐',),
      # hyōgaiji kanji #452
      '鷲'        : ('鷲',),
      # hyōgaiji kanji #453
      '廿'        : ('廿',),
      # hyōgaiji kanji #454
      '揉'        : ('揉',),
      # hyōgaiji kanji #455
      '絨'        : ('絨',),
      # hyōgaiji kanji #456
      '粥'        : ('粥',),
      # hyōgaiji kanji #457
      '戌'        : ('戌',),
      # hyōgaiji kanji #458
      '閏'        : ('閏',),
      # hyōgaiji kanji #459
      '楯'        : ('楯',),
      # hyōgaiji kanji #460
      '馴'        : ('馴',),
      # hyōgaiji kanji #461
      '杵'        : ('杵',),
      # hyōgaiji kanji #462
      '薯'        : ('薯',),
      # hyōgaiji kanji #463
      '藷'        : ('藷',),
      # hyōgaiji kanji #464
      '汝'        : ('汝',),
      # hyōgaiji kanji #465
      '抒'        : ('抒',),
      # hyōgaiji kanji #466
      '鋤'        : ('鋤',),
      # hyōgaiji kanji #467
      '妾'        : ('妾',),
      # hyōgaiji kanji #468
      '哨'        : ('哨',),
      # hyōgaiji kanji #469
      '秤'        : ('秤',),
      # hyōgaiji kanji #470
      '娼'        : ('娼',),
      # hyōgaiji kanji #471
      '逍'        : ('逍',),
      # hyōgaiji kanji #472
      '廂'        : ('廂',),
      # hyōgaiji kanji #473
      '椒'        : ('椒',),
      # hyōgaiji kanji #474
      '湘'        : ('湘',),
      # hyōgaiji kanji #475
      '竦'        : ('竦',),
      # hyōgaiji kanji #476
      '鈔'        : ('鈔',),
      # hyōgaiji kanji #477
      '睫'        : ('睫',),
      # hyōgaiji kanji #478
      '蛸'        : ('蛸',),
      # hyōgaiji kanji #479
      '鉦'        : ('鉦',),
      # hyōgaiji kanji #480
      '摺'        : ('摺',),
      # hyōgaiji kanji #481
      '蔣'        : ('蔣', '蒋'),
      # hyōgaiji kanji #482
      '裳'        : ('裳',),
      # hyōgaiji kanji #483
      '誦'        : ('誦',),
      # hyōgaiji kanji #484
      '漿'        : ('漿',),
      # hyōgaiji kanji #485
      '蕭'        : ('蕭',),
      # hyōgaiji kanji #486
      '踵'        : ('踵',),
      # hyōgaiji kanji #487
      '鞘'        : ('鞘',),
      # hyōgaiji kanji #488
      '篠'        : ('篠',),
      # hyōgaiji kanji #489
      '聳'        : ('聳',),
      # hyōgaiji kanji #490
      '鍾'        : ('鍾',),
      # hyōgaiji kanji #491
      '醬'        : ('醬', '醤'),
      # hyōgaiji kanji #492
      '囁'        : ('囁',),
      # hyōgaiji kanji #493
      '杖'        : ('杖',),
      # hyōgaiji kanji #494
      '茸'        : ('茸',),
      # hyōgaiji kanji #495
      '嘗'        : ('嘗',),
      # hyōgaiji kanji #496
      '擾'        : ('擾',),
      # hyōgaiji kanji #497
      '攘'        : ('攘',),
      # hyōgaiji kanji #498
      '饒'        : ('饒',),
      # hyōgaiji kanji #499
      '拭'        : ('拭',),
      # hyōgaiji kanji #500
      '埴'        : ('埴',),
      # hyōgaiji kanji #501
      '蜀'        : ('蜀',),
      # hyōgaiji kanji #502
      '蝕'        : ('蝕',),
      # hyōgaiji kanji #503
      '燭'        : ('燭',),
      # hyōgaiji kanji #504
      '褥'        : ('褥',),
      # hyōgaiji kanji #505
      '沁'        : ('沁',),
      # hyōgaiji kanji #506
      '芯'        : ('芯',),
      # hyōgaiji kanji #507
      '呻'        : ('呻',),
      # hyōgaiji kanji #508
      '宸'        : ('宸',),
      # hyōgaiji kanji #509
      '疹'        : ('疹',),
      # hyōgaiji kanji #510
      '蜃'        : ('蜃',),
      # hyōgaiji kanji #511
      '滲'        : ('滲',),
      # hyōgaiji kanji #512
      '賑'        : ('賑',),
      # hyōgaiji kanji #513
      '鍼'        : ('鍼',),
      # hyōgaiji kanji #514
      '壬'        : ('壬',),
      # hyōgaiji kanji #515
      '訊'        : ('訊',),
      # hyōgaiji kanji #516
      '腎'        : ('腎',),
      # hyōgaiji kanji #517
      '靱'        : ('靱',),
      # hyōgaiji kanji #518
      '塵'        : ('塵',),
      # hyōgaiji kanji #519
      '儘'        : ('儘',),
      # hyōgaiji kanji #520
      '笥'        : ('笥',),
      # hyōgaiji kanji #521
      '祟'        : ('祟',),
      # hyōgaiji kanji #522
      '膵'        : ('膵',),
      # hyōgaiji kanji #523
      '誰'        : ('誰',),
      # hyōgaiji kanji #524
      '錐'        : ('錐',),
      # hyōgaiji kanji #525
      '雖'        : ('雖',),
      # hyōgaiji kanji #526
      '隋'        : ('隋',),
      # hyōgaiji kanji #527
      '隧'        : ('隧',),
      # hyōgaiji kanji #528
      '芻'        : ('芻',),
      # hyōgaiji kanji #529
      '趨'        : ('趨',),
      # hyōgaiji kanji #530
      '鮨'        : ('鮨',),
      # hyōgaiji kanji #531
      '丼'        : ('丼',),
      # hyōgaiji kanji #532
      '凄'        : ('凄',),
      # hyōgaiji kanji #533
      '栖'        : ('栖',),
      # hyōgaiji kanji #534
      '棲'        : ('棲',),
      # hyōgaiji kanji #535
      '甥'        : ('甥',),
      # hyōgaiji kanji #536
      '貰'        : ('貰',),
      # hyōgaiji kanji #537
      '蜻'        : ('蜻',),
      # hyōgaiji kanji #538
      '醒'        : ('醒',),
      # hyōgaiji kanji #539
      '錆'        : ('錆',),
      # hyōgaiji kanji #540
      '臍'        : ('臍',),
      # hyōgaiji kanji #541
      '瀞'        : ('瀞',),
      # hyōgaiji kanji #542
      '鯖'        : ('鯖',),
      # hyōgaiji kanji #543
      '脆'        : ('脆',),
      # hyōgaiji kanji #544
      '贅'        : ('贅',),
      # hyōgaiji kanji #545
      '脊'        : ('脊',),
      # hyōgaiji kanji #546
      '戚'        : ('戚',),
      # hyōgaiji kanji #547
      '晰'        : ('晰',),
      # hyōgaiji kanji #548
      '蹟'        : ('蹟',),
      # hyōgaiji kanji #549
      '泄'        : ('泄',),
      # hyōgaiji kanji #550
      '屑'        : ('屑',),
      # hyōgaiji kanji #551
      '浙'        : ('浙',),
      # hyōgaiji kanji #552
      '啜'        : ('啜',),
      # hyōgaiji kanji #553
      '楔'        : ('楔',),
      # hyōgaiji kanji #554
      '截'        : ('截',),
      # hyōgaiji kanji #555
      '尖'        : ('尖',),
      # hyōgaiji kanji #556
      '苫'        : ('苫',),
      # hyōgaiji kanji #557
      '穿'        : ('穿',),
      # hyōgaiji kanji #558
      '閃'        : ('閃',),
      # hyōgaiji kanji #559
      '陝'        : ('陝',),
      # hyōgaiji kanji #560
      '釧'        : ('釧',),
      # hyōgaiji kanji #561
      '揃'        : ('揃',),
      # hyōgaiji kanji #562
      '煎'        : ('煎',),
      # hyōgaiji kanji #563
      '羨'        : ('羨',),
      # hyōgaiji kanji #564
      '腺'        : ('腺',),
      # hyōgaiji kanji #565
      '詮'        : ('詮',),
      # hyōgaiji kanji #566
      '煽'        : ('煽',),
      # hyōgaiji kanji #567
      '箋'        : ('箋',),
      # hyōgaiji kanji #568
      '撰'        : ('撰',),
      # hyōgaiji kanji #569
      '箭'        : ('箭',),
      # hyōgaiji kanji #570
      '賤'        : ('賤',),
      # hyōgaiji kanji #571
      '蟬'        : ('蟬',),
      # hyōgaiji kanji #572
      '癬'        : ('癬',),
      # hyōgaiji kanji #573
      '喘'        : ('喘',),
      # hyōgaiji kanji #574
      '膳'        : ('膳',),
      # hyōgaiji kanji #575
      '狙'        : ('狙',),
      # hyōgaiji kanji #576
      '疽'        : ('疽',),
      # hyōgaiji kanji #577
      '疏'        : ('疏',),
      # hyōgaiji kanji #578
      '甦'        : ('甦',),
      # hyōgaiji kanji #579
      '楚'        : ('楚',),
      # hyōgaiji kanji #580
      '鼠'        : ('鼠',),
      # hyōgaiji kanji #581
      '遡'        : ('遡',),
      # hyōgaiji kanji #582
      '蘇'        : ('蘇',),
      # hyōgaiji kanji #583
      '齟'        : ('齟',),
      # hyōgaiji kanji #584
      '爪'        : ('爪',),
      # hyōgaiji kanji #585
      '宋'        : ('宋',),
      # hyōgaiji kanji #586
      '炒'        : ('炒',),
      # hyōgaiji kanji #587
      '叟'        : ('叟',),
      # hyōgaiji kanji #588
      '蚤'        : ('蚤',),
      # hyōgaiji kanji #589
      '曾'        : ('曾', '曽'),
      # hyōgaiji kanji #590
      '湊'        : ('湊',),
      # hyōgaiji kanji #591
      '葱'        : ('葱',),
      # hyōgaiji kanji #592
      '搔'        : ('搔', '掻'),
      # hyōgaiji kanji #593
      '槍'        : ('槍',),
      # hyōgaiji kanji #594
      '漕'        : ('漕',),
      # hyōgaiji kanji #595
      '箏'        : ('箏',),
      # hyōgaiji kanji #596
      '噌'        : ('噌',),
      # hyōgaiji kanji #597
      '瘡'        : ('瘡',),
      # hyōgaiji kanji #598
      '瘦'        : ('瘦', '痩'),
      # hyōgaiji kanji #599
      '踪'        : ('踪',),
      # hyōgaiji kanji #600
      '艘'        : ('艘',),
      # hyōgaiji kanji #601
      '薔'        : ('薔',),
      # hyōgaiji kanji #602
      '甑'        : ('甑',),
      # hyōgaiji kanji #603
      '叢'        : ('叢',),
      # hyōgaiji kanji #604
      '藪'        : ('藪',),
      # hyōgaiji kanji #605
      '躁'        : ('躁',),
      # hyōgaiji kanji #606
      '囃'        : ('囃',),
      # hyōgaiji kanji #607
      '竈'        : ('竈',),
      # hyōgaiji kanji #608
      '鰺'        : ('鰺',),
      # hyōgaiji kanji #609
      '仄'        : ('仄',),
      # hyōgaiji kanji #610
      '捉'        : ('捉',),
      # hyōgaiji kanji #611
      '塞'        : ('塞',),
      # hyōgaiji kanji #612
      '粟'        : ('粟',),
      # hyōgaiji kanji #613
      '杣'        : ('杣',),
      # hyōgaiji kanji #614
      '遜'        : ('遜',),
      # hyōgaiji kanji #615
      '噂'        : ('噂',),
      # hyōgaiji kanji #616
      '樽'        : ('樽',),
      # hyōgaiji kanji #617
      '鱒'        : ('鱒',),
      # hyōgaiji kanji #618
      '侘'        : ('侘',),
      # hyōgaiji kanji #619
      '咤'        : ('咤',),
      # hyōgaiji kanji #620
      '詫'        : ('詫',),
      # hyōgaiji kanji #621
      '陀'        : ('陀',),
      # hyōgaiji kanji #622
      '拿'        : ('拿',),
      # hyōgaiji kanji #623
      '荼'        : ('荼',),
      # hyōgaiji kanji #624
      '唾'        : ('唾',),
      # hyōgaiji kanji #625
      '舵'        : ('舵',),
      # hyōgaiji kanji #626
      '楕'        : ('楕',),
      # hyōgaiji kanji #627
      '驒'        : ('驒',),
      # hyōgaiji kanji #628
      '苔'        : ('苔',),
      # hyōgaiji kanji #629
      '殆'        : ('殆',),
      # hyōgaiji kanji #630
      '堆'        : ('堆',),
      # hyōgaiji kanji #631
      '碓'        : ('碓',),
      # hyōgaiji kanji #632
      '腿'        : ('腿',),
      # hyōgaiji kanji #633
      '頽'        : ('頽',),
      # hyōgaiji kanji #634
      '戴'        : ('戴',),
      # hyōgaiji kanji #635
      '醍'        : ('醍',),
      # hyōgaiji kanji #636
      '托'        : ('托',),
      # hyōgaiji kanji #637
      '鐸'        : ('鐸',),
      # hyōgaiji kanji #638
      '凧'        : ('凧',),
      # hyōgaiji kanji #639
      '襷'        : ('襷',),
      # hyōgaiji kanji #640
      '燵'        : ('燵',),
      # hyōgaiji kanji #641
      '坦'        : ('坦',),
      # hyōgaiji kanji #642
      '疸'        : ('疸',),
      # hyōgaiji kanji #643
      '耽'        : ('耽',),
      # hyōgaiji kanji #644
      '啖'        : ('啖',),
      # hyōgaiji kanji #645
      '蛋'        : ('蛋',),
      # hyōgaiji kanji #646
      '毯'        : ('毯',),
      # hyōgaiji kanji #647
      '湛'        : ('湛',),
      # hyōgaiji kanji #648
      '痰'        : ('痰',),
      # hyōgaiji kanji #649
      '綻'        : ('綻',),
      # hyōgaiji kanji #650
      '憚'        : ('憚',),
      # hyōgaiji kanji #651
      '歎'        : ('歎',),
      # hyōgaiji kanji #652
      '簞'        : ('簞',),
      # hyōgaiji kanji #653
      '譚'        : ('譚',),
      # hyōgaiji kanji #654
      '灘'        : ('灘',),
      # hyōgaiji kanji #655
      '雉'        : ('雉',),
      # hyōgaiji kanji #656
      '馳'        : ('馳',),
      # hyōgaiji kanji #657
      '蜘'        : ('蜘',),
      # hyōgaiji kanji #658
      '緻'        : ('緻',),
      # hyōgaiji kanji #659
      '筑'        : ('筑',),
      # hyōgaiji kanji #660
      '膣'        : ('膣',),
      # hyōgaiji kanji #661
      '肘'        : ('肘',),
      # hyōgaiji kanji #662
      '冑'        : ('冑',),
      # hyōgaiji kanji #663
      '紐'        : ('紐',),
      # hyōgaiji kanji #664
      '酎'        : ('酎',),
      # hyōgaiji kanji #665
      '厨'        : ('厨',),
      # hyōgaiji kanji #666
      '蛛'        : ('蛛',),
      # hyōgaiji kanji #667
      '註'        : ('註',),
      # hyōgaiji kanji #668
      '誅'        : ('誅',),
      # hyōgaiji kanji #669
      '疇'        : ('疇',),
      # hyōgaiji kanji #670
      '躊'        : ('躊',),
      # hyōgaiji kanji #671
      '佇'        : ('佇',),
      # hyōgaiji kanji #672
      '楮'        : ('楮',),
      # hyōgaiji kanji #673
      '箸'        : ('箸',),
      # hyōgaiji kanji #674
      '儲'        : ('儲',),
      # hyōgaiji kanji #675
      '瀦'        : ('瀦',),
      # hyōgaiji kanji #676
      '躇'        : ('躇',),
      # hyōgaiji kanji #677
      '吊'        : ('吊',),
      # hyōgaiji kanji #678
      '帖'        : ('帖',),
      # hyōgaiji kanji #679
      '喋'        : ('喋',),
      # hyōgaiji kanji #680
      '貼'        : ('貼',),
      # hyōgaiji kanji #681
      '牒'        : ('牒',),
      # hyōgaiji kanji #682
      '趙'        : ('趙',),
      # hyōgaiji kanji #683
      '銚'        : ('銚',),
      # hyōgaiji kanji #684
      '嘲'        : ('嘲',),
      # hyōgaiji kanji #685
      '諜'        : ('諜',),
      # hyōgaiji kanji #686
      '寵'        : ('寵',),
      # hyōgaiji kanji #687
      '捗'        : ('捗',),
      # hyōgaiji kanji #688
      '枕'        : ('枕',),
      # hyōgaiji kanji #689
      '槌'        : ('槌',),
      # hyōgaiji kanji #690
      '鎚'        : ('鎚',),
      # hyōgaiji kanji #691
      '辻'        : ('辻',),
      # hyōgaiji kanji #692
      '剃'        : ('剃',),
      # hyōgaiji kanji #693
      '挺'        : ('挺',),
      # hyōgaiji kanji #694
      '釘'        : ('釘',),
      # hyōgaiji kanji #695
      '掟'        : ('掟',),
      # hyōgaiji kanji #696
      '梯'        : ('梯',),
      # hyōgaiji kanji #697
      '逞'        : ('逞',),
      # hyōgaiji kanji #698
      '啼'        : ('啼',),
      # hyōgaiji kanji #699
      '碇'        : ('碇',),
      # hyōgaiji kanji #700
      '鼎'        : ('鼎',),
      # hyōgaiji kanji #701
      '綴'        : ('綴',),
      # hyōgaiji kanji #702
      '鄭'        : ('鄭',),
      # hyōgaiji kanji #703
      '薙'        : ('薙',),
      # hyōgaiji kanji #704
      '諦'        : ('諦',),
      # hyōgaiji kanji #705
      '蹄'        : ('蹄',),
      # hyōgaiji kanji #706
      '鵜'        : ('鵜',),
      # hyōgaiji kanji #707
      '荻'        : ('荻',),
      # hyōgaiji kanji #708
      '擢'        : ('擢',),
      # hyōgaiji kanji #709
      '溺'        : ('溺',),
      # hyōgaiji kanji #710
      '姪'        : ('姪',),
      # hyōgaiji kanji #711
      '轍'        : ('轍',),
      # hyōgaiji kanji #712
      '辿'        : ('辿',),
      # hyōgaiji kanji #713
      '唸'        : ('唸',),
      # hyōgaiji kanji #714
      '塡'        : ('塡',),
      # hyōgaiji kanji #715
      '篆'        : ('篆',),
      # hyōgaiji kanji #716
      '顚'        : ('顚',),
      # hyōgaiji kanji #717
      '囀'        : ('囀',),
      # hyōgaiji kanji #718
      '纏'        : ('纏',),
      # hyōgaiji kanji #719
      '佃'        : ('佃',),
      # hyōgaiji kanji #720
      '淀'        : ('淀',),
      # hyōgaiji kanji #721
      '澱'        : ('澱',),
      # hyōgaiji kanji #722
      '臀'        : ('臀',),
      # hyōgaiji kanji #723
      '兎'        : ('兎',),
      # hyōgaiji kanji #724
      '妬'        : ('妬',),
      # hyōgaiji kanji #725
      '兜'        : ('兜',),
      # hyōgaiji kanji #726
      '堵'        : ('堵',),
      # hyōgaiji kanji #727
      '屠'        : ('屠',),
      # hyōgaiji kanji #728
      '賭'        : ('賭',),
      # hyōgaiji kanji #729
      '宕'        : ('宕',),
      # hyōgaiji kanji #730
      '沓'        : ('沓',),
      # hyōgaiji kanji #731
      '套'        : ('套',),
      # hyōgaiji kanji #732
      '疼'        : ('疼',),
      # hyōgaiji kanji #733
      '桶'        : ('桶',),
      # hyōgaiji kanji #734
      '淘'        : ('淘',),
      # hyōgaiji kanji #735
      '萄'        : ('萄',),
      # hyōgaiji kanji #736
      '逗'        : ('逗',),
      # hyōgaiji kanji #737
      '棹'        : ('棹',),
      # hyōgaiji kanji #738
      '樋'        : ('樋',),
      # hyōgaiji kanji #739
      '蕩'        : ('蕩',),
      # hyōgaiji kanji #740
      '鄧'        : ('鄧',),
      # hyōgaiji kanji #741
      '橙'        : ('橙',),
      # hyōgaiji kanji #742
      '濤'        : ('濤',),
      # hyōgaiji kanji #743
      '檮'        : ('檮',),
      # hyōgaiji kanji #744
      '櫂'        : ('櫂',),
      # hyōgaiji kanji #745
      '禱'        : ('禱', '祷'),
      # hyōgaiji kanji #746
      '撞'        : ('撞',),
      # hyōgaiji kanji #747
      '禿'        : ('禿',),
      # hyōgaiji kanji #748
      '瀆'        : ('瀆',),
      # hyōgaiji kanji #749
      '栃'        : ('栃',),
      # hyōgaiji kanji #750
      '咄'        : ('咄',),
      # hyōgaiji kanji #751
      '沌'        : ('沌',),
      # hyōgaiji kanji #752
      '遁'        : ('遁',),
      # hyōgaiji kanji #753
      '頓'        : ('頓',),
      # hyōgaiji kanji #754
      '吞'        : ('吞',),
      # hyōgaiji kanji #755
      '貪'        : ('貪',),
      # hyōgaiji kanji #756
      '邇'        : ('邇',),
      # hyōgaiji kanji #757
      '匂'        : ('匂',),
      # hyōgaiji kanji #758
      '韮'        : ('韮',),
      # hyōgaiji kanji #759
      '涅'        : ('涅',),
      # hyōgaiji kanji #760
      '禰'        : ('禰',),
      # hyōgaiji kanji #761
      '捏'        : ('捏',),
      # hyōgaiji kanji #762
      '捻'        : ('捻',),
      # hyōgaiji kanji #763
      '撚'        : ('撚',),
      # hyōgaiji kanji #764
      '膿'        : ('膿',),
      # hyōgaiji kanji #765
      '囊'        : ('囊',),
      # hyōgaiji kanji #766
      '杷'        : ('杷',),
      # hyōgaiji kanji #767
      '爬'        : ('爬',),
      # hyōgaiji kanji #768
      '琶'        : ('琶',),
      # hyōgaiji kanji #769
      '頗'        : ('頗',),
      # hyōgaiji kanji #770
      '播'        : ('播',),
      # hyōgaiji kanji #771
      '芭'        : ('芭',),
      # hyōgaiji kanji #772
      '罵'        : ('罵',),
      # hyōgaiji kanji #773
      '蟇'        : ('蟇',),
      # hyōgaiji kanji #774
      '胚'        : ('胚',),
      # hyōgaiji kanji #775
      '徘'        : ('徘',),
      # hyōgaiji kanji #776
      '牌'        : ('牌',),
      # hyōgaiji kanji #777
      '稗'        : ('稗',),
      # hyōgaiji kanji #778
      '狽'        : ('狽',),
      # hyōgaiji kanji #779
      '煤'        : ('煤',),
      # hyōgaiji kanji #780
      '帛'        : ('帛',),
      # hyōgaiji kanji #781
      '柏'        : ('柏',),
      # hyōgaiji kanji #782
      '剝'        : ('剝',),
      # hyōgaiji kanji #783
      '粕'        : ('粕',),
      # hyōgaiji kanji #784
      '箔'        : ('箔',),
      # hyōgaiji kanji #785
      '莫'        : ('莫',),
      # hyōgaiji kanji #786
      '駁'        : ('駁',),
      # hyōgaiji kanji #787
      '瀑'        : ('瀑',),
      # hyōgaiji kanji #788
      '曝'        : ('曝',),
      # hyōgaiji kanji #789
      '畠'        : ('畠',),
      # hyōgaiji kanji #790
      '捌'        : ('捌',),
      # hyōgaiji kanji #791
      '撥'        : ('撥',),
      # hyōgaiji kanji #792
      '潑'        : ('潑',),
      # hyōgaiji kanji #793
      '醱'        : ('醱',),
      # hyōgaiji kanji #794
      '筏'        : ('筏',),
      # hyōgaiji kanji #795
      '跋'        : ('跋',),
      # hyōgaiji kanji #796
      '噺'        : ('噺',),
      # hyōgaiji kanji #797
      '氾'        : ('氾',),
      # hyōgaiji kanji #798
      '汎'        : ('汎',),
      # hyōgaiji kanji #799
      '阪'        : ('阪',),
      # hyōgaiji kanji #800
      '叛'        : ('叛',),
      # hyōgaiji kanji #801
      '袢'        : ('袢',),
      # hyōgaiji kanji #802
      '絆'        : ('絆',),
      # hyōgaiji kanji #803
      '斑'        : ('斑',),
      # hyōgaiji kanji #804
      '槃'        : ('槃',),
      # hyōgaiji kanji #805
      '幡'        : ('幡',),
      # hyōgaiji kanji #806
      '攀'        : ('攀',),
      # hyōgaiji kanji #807
      '挽'        : ('挽',),
      # hyōgaiji kanji #808
      '磐'        : ('磐',),
      # hyōgaiji kanji #809
      '蕃'        : ('蕃',),
      # hyōgaiji kanji #810
      '屁'        : ('屁',),
      # hyōgaiji kanji #811
      '庇'        : ('庇',),
      # hyōgaiji kanji #812
      '砒'        : ('砒',),
      # hyōgaiji kanji #813
      '脾'        : ('脾',),
      # hyōgaiji kanji #814
      '痺'        : ('痺',),
      # hyōgaiji kanji #815
      '鄙'        : ('鄙',),
      # hyōgaiji kanji #816
      '誹'        : ('誹',),
      # hyōgaiji kanji #817
      '臂'        : ('臂',),
      # hyōgaiji kanji #818
      '枇'        : ('枇',),
      # hyōgaiji kanji #819
      '毘'        : ('毘',),
      # hyōgaiji kanji #820
      '梶'        : ('梶',),
      # hyōgaiji kanji #821
      '媚'        : ('媚',),
      # hyōgaiji kanji #822
      '琵'        : ('琵',),
      # hyōgaiji kanji #823
      '薇'        : ('薇',),
      # hyōgaiji kanji #824
      '靡'        : ('靡',),
      # hyōgaiji kanji #825
      '疋'        : ('疋',),
      # hyōgaiji kanji #826
      '畢'        : ('畢',),
      # hyōgaiji kanji #827
      '逼'        : ('逼',),
      # hyōgaiji kanji #828
      '謬'        : ('謬',),
      # hyōgaiji kanji #829
      '豹'        : ('豹',),
      # hyōgaiji kanji #830
      '憑'        : ('憑',),
      # hyōgaiji kanji #831
      '瓢'        : ('瓢',),
      # hyōgaiji kanji #832
      '屛'        : ('屛', '屏'),
      # hyōgaiji kanji #833
      '廟'        : ('廟',),
      # hyōgaiji kanji #834
      '牝'        : ('牝',),
      # hyōgaiji kanji #835
      '瀕'        : ('瀕',),
      # hyōgaiji kanji #836
      '憫'        : ('憫',),
      # hyōgaiji kanji #837
      '鬢'        : ('鬢',),
      # hyōgaiji kanji #838
      '斧'        : ('斧',),
      # hyōgaiji kanji #839
      '阜'        : ('阜',),
      # hyōgaiji kanji #840
      '訃'        : ('訃',),
      # hyōgaiji kanji #841
      '俯'        : ('俯',),
      # hyōgaiji kanji #842
      '釜'        : ('釜',),
      # hyōgaiji kanji #843
      '腑'        : ('腑',),
      # hyōgaiji kanji #844
      '孵'        : ('孵',),
      # hyōgaiji kanji #845
      '鮒'        : ('鮒',),
      # hyōgaiji kanji #846
      '巫'        : ('巫',),
      # hyōgaiji kanji #847
      '葡'        : ('葡',),
      # hyōgaiji kanji #848
      '撫'        : ('撫',),
      # hyōgaiji kanji #849
      '蕪'        : ('蕪',),
      # hyōgaiji kanji #850
      '諷'        : ('諷',),
      # hyōgaiji kanji #851
      '祓'        : ('祓',),
      # hyōgaiji kanji #852
      '吻'        : ('吻',),
      # hyōgaiji kanji #853
      '扮'        : ('扮',),
      # hyōgaiji kanji #854
      '焚'        : ('焚',),
      # hyōgaiji kanji #855
      '糞'        : ('糞',),
      # hyōgaiji kanji #856
      '幷'        : ('幷', '并'),
      # hyōgaiji kanji #857
      '聘'        : ('聘',),
      # hyōgaiji kanji #858
      '蔽'        : ('蔽',),
      # hyōgaiji kanji #859
      '餅'        : ('餅',),
      # hyōgaiji kanji #860
      '斃'        : ('斃',),
      # hyōgaiji kanji #861
      '袂'        : ('袂',),
      # hyōgaiji kanji #862
      '僻'        : ('僻',),
      # hyōgaiji kanji #863
      '璧'        : ('璧',),
      # hyōgaiji kanji #864
      '襞'        : ('襞',),
      # hyōgaiji kanji #865
      '蔑'        : ('蔑',),
      # hyōgaiji kanji #866
      '瞥'        : ('瞥',),
      # hyōgaiji kanji #867
      '扁'        : ('扁',),
      # hyōgaiji kanji #868
      '篇'        : ('篇',),
      # hyōgaiji kanji #869
      '騙'        : ('騙',),
      # hyōgaiji kanji #870
      '娩'        : ('娩',),
      # hyōgaiji kanji #871
      '鞭'        : ('鞭',),
      # hyōgaiji kanji #872
      '哺'        : ('哺',),
      # hyōgaiji kanji #873
      '圃'        : ('圃',),
      # hyōgaiji kanji #874
      '蒲'        : ('蒲',),
      # hyōgaiji kanji #875
      '戊'        : ('戊',),
      # hyōgaiji kanji #876
      '牡'        : ('牡',),
      # hyōgaiji kanji #877
      '姥'        : ('姥',),
      # hyōgaiji kanji #878
      '菩'        : ('菩',),
      # hyōgaiji kanji #879
      '呆'        : ('呆',),
      # hyōgaiji kanji #880
      '彷'        : ('彷',),
      # hyōgaiji kanji #881
      '庖'        : ('庖',),
      # hyōgaiji kanji #882
      '苞'        : ('苞',),
      # hyōgaiji kanji #883
      '疱'        : ('疱',),
      # hyōgaiji kanji #884
      '捧'        : ('捧',),
      # hyōgaiji kanji #885
      '逢'        : ('逢',),
      # hyōgaiji kanji #886
      '蜂'        : ('蜂',),
      # hyōgaiji kanji #887
      '蓬'        : ('蓬',),
      # hyōgaiji kanji #888
      '鞄'        : ('鞄',),
      # hyōgaiji kanji #889
      '鋒'        : ('鋒',),
      # hyōgaiji kanji #890
      '牟'        : ('牟',),
      # hyōgaiji kanji #891
      '芒'        : ('芒',),
      # hyōgaiji kanji #892
      '茫'        : ('茫',),
      # hyōgaiji kanji #893
      '虻'        : ('虻',),
      # hyōgaiji kanji #894
      '榜'        : ('榜',),
      # hyōgaiji kanji #895
      '膀'        : ('膀',),
      # hyōgaiji kanji #896
      '貌'        : ('貌',),
      # hyōgaiji kanji #897
      '鉾'        : ('鉾',),
      # hyōgaiji kanji #898
      '謗'        : ('謗',),
      # hyōgaiji kanji #899
      '吠'        : ('吠',),
      # hyōgaiji kanji #900
      '卜'        : ('卜',),
      # hyōgaiji kanji #901
      '勃'        : ('勃',),
      # hyōgaiji kanji #902
      '梵'        : ('梵',),
      # hyōgaiji kanji #903
      '昧'        : ('昧',),
      # hyōgaiji kanji #904
      '邁'        : ('邁',),
      # hyōgaiji kanji #905
      '枡'        : ('枡', '桝'),
      # hyōgaiji kanji #906
      '俣'        : ('俣',),
      # hyōgaiji kanji #907
      '沫'        : ('沫',),
      # hyōgaiji kanji #908
      '迄'        : ('迄',),
      # hyōgaiji kanji #909
      '曼'        : ('曼',),
      # hyōgaiji kanji #910
      '蔓'        : ('蔓',),
      # hyōgaiji kanji #911
      '瞞'        : ('瞞',),
      # hyōgaiji kanji #912
      '饅'        : ('饅',),
      # hyōgaiji kanji #913
      '鬘'        : ('鬘',),
      # hyōgaiji kanji #914
      '鰻'        : ('鰻',),
      # hyōgaiji kanji #915
      '蜜'        : ('蜜',),
      # hyōgaiji kanji #916
      '鵡'        : ('鵡',),
      # hyōgaiji kanji #917
      '冥'        : ('冥',),
      # hyōgaiji kanji #918
      '瞑'        : ('瞑',),
      # hyōgaiji kanji #919
      '謎'        : ('謎',),
      # hyōgaiji kanji #920
      '麵'        : ('麵', '麺'),
      # hyōgaiji kanji #921
      '蒙'        : ('蒙',),
      # hyōgaiji kanji #922
      '朦'        : ('朦',),
      # hyōgaiji kanji #923
      '勿'        : ('勿',),
      # hyōgaiji kanji #924
      '籾'        : ('籾',),
      # hyōgaiji kanji #925
      '悶'        : ('悶',),
      # hyōgaiji kanji #926
      '揶'        : ('揶',),
      # hyōgaiji kanji #927
      '爺'        : ('爺',),
      # hyōgaiji kanji #928
      '鑓'        : ('鑓',),
      # hyōgaiji kanji #929
      '喩'        : ('喩',),
      # hyōgaiji kanji #930
      '揄'        : ('揄',),
      # hyōgaiji kanji #931
      '愈'        : ('愈',),
      # hyōgaiji kanji #932
      '楡'        : ('楡',),
      # hyōgaiji kanji #933
      '尤'        : ('尤',),
      # hyōgaiji kanji #934
      '釉'        : ('釉',),
      # hyōgaiji kanji #935
      '楢'        : ('楢',),
      # hyōgaiji kanji #936
      '猷'        : ('猷',),
      # hyōgaiji kanji #937
      '飫'        : ('飫',),
      # hyōgaiji kanji #938
      '輿'        : ('輿',),
      # hyōgaiji kanji #939
      '孕'        : ('孕',),
      # hyōgaiji kanji #940
      '妖'        : ('妖',),
      # hyōgaiji kanji #941
      '拗'        : ('拗',),
      # hyōgaiji kanji #942
      '涌'        : ('涌',),
      # hyōgaiji kanji #943
      '痒'        : ('痒',),
      # hyōgaiji kanji #944
      '傭'        : ('傭',),
      # hyōgaiji kanji #945
      '熔'        : ('熔',),
      # hyōgaiji kanji #946
      '瘍'        : ('瘍',),
      # hyōgaiji kanji #947
      '蠅'        : ('蠅',),
      # hyōgaiji kanji #948
      '沃'        : ('沃',),
      # hyōgaiji kanji #949
      '螺'        : ('螺',),
      # hyōgaiji kanji #950
      '萊'        : ('萊',),
      # hyōgaiji kanji #951
      '蕾'        : ('蕾',),
      # hyōgaiji kanji #952
      '洛'        : ('洛',),
      # hyōgaiji kanji #953
      '埒'        : ('埒',),
      # hyōgaiji kanji #954
      '拉'        : ('拉',),
      # hyōgaiji kanji #955
      '辣'        : ('辣',),
      # hyōgaiji kanji #956
      '瀾'        : ('瀾',),
      # hyōgaiji kanji #957
      '爛'        : ('爛',),
      # hyōgaiji kanji #958
      '鸞'        : ('鸞',),
      # hyōgaiji kanji #959
      '狸'        : ('狸',),
      # hyōgaiji kanji #960
      '裡'        : ('裡',),
      # hyōgaiji kanji #961
      '罹'        : ('罹',),
      # hyōgaiji kanji #962
      '籬'        : ('籬',),
      # hyōgaiji kanji #963
      '戮'        : ('戮',),
      # hyōgaiji kanji #964
      '慄'        : ('慄',),
      # hyōgaiji kanji #965
      '掠'        : ('掠',),
      # hyōgaiji kanji #966
      '笠'        : ('笠',),
      # hyōgaiji kanji #967
      '溜'        : ('溜',),
      # hyōgaiji kanji #968
      '榴'        : ('榴',),
      # hyōgaiji kanji #969
      '劉'        : ('劉',),
      # hyōgaiji kanji #970
      '瘤'        : ('瘤',),
      # hyōgaiji kanji #971
      '侶'        : ('侶',),
      # hyōgaiji kanji #972
      '梁'        : ('梁',),
      # hyōgaiji kanji #973
      '聊'        : ('聊',),
      # hyōgaiji kanji #974
      '菱'        : ('菱',),
      # hyōgaiji kanji #975
      '寥'        : ('寥',),
      # hyōgaiji kanji #976
      '蓼'        : ('蓼',),
      # hyōgaiji kanji #977
      '淋'        : ('淋',),
      # hyōgaiji kanji #978
      '燐'        : ('燐',),
      # hyōgaiji kanji #979
      '鱗'        : ('鱗',),
      # hyōgaiji kanji #980
      '屢'        : ('屢',),
      # hyōgaiji kanji #981
      '蛉'        : ('蛉',),
      # hyōgaiji kanji #982
      '蠣'        : ('蠣',),
      # hyōgaiji kanji #983
      '櫟'        : ('櫟',),
      # hyōgaiji kanji #984
      '礫'        : ('礫',),
      # hyōgaiji kanji #985
      '轢'        : ('轢',),
      # hyōgaiji kanji #986
      '煉'        : ('煉',),
      # hyōgaiji kanji #987
      '漣'        : ('漣',),
      # hyōgaiji kanji #988
      '憐'        : ('憐',),
      # hyōgaiji kanji #989
      '簾'        : ('簾',),
      # hyōgaiji kanji #990
      '鰊'        : ('鰊',),
      # hyōgaiji kanji #991
      '攣'        : ('攣',),
      # hyōgaiji kanji #992
      '賂'        : ('賂',),
      # hyōgaiji kanji #993
      '魯'        : ('魯',),
      # hyōgaiji kanji #994
      '濾'        : ('濾', '沪'),
      # hyōgaiji kanji #995
      '廬'        : ('廬',),
      # hyōgaiji kanji #996
      '櫓'        : ('櫓',),
      # hyōgaiji kanji #997
      '蘆'        : ('蘆', '芦'),
      # hyōgaiji kanji #998
      '鷺'        : ('鷺',),
      # hyōgaiji kanji #999
      '弄'        : ('弄',),
      # hyōgaiji kanji #1000
      '牢'        : ('牢',),
      # hyōgaiji kanji #1001
      '狼'        : ('狼',),
      # hyōgaiji kanji #1002
      '榔'        : ('榔',),
      # hyōgaiji kanji #1003
      '瘻'        : ('瘻',),
      # hyōgaiji kanji #1004
      '﨟'        : ('﨟',),
      # hyōgaiji kanji #1005
      '臘'        : ('臘',),
      # hyōgaiji kanji #1006
      '朧'        : ('朧',),
      # hyōgaiji kanji #1007
      '蠟'        : ('蠟', '蝋'),
      # hyōgaiji kanji #1008
      '籠'        : ('籠',),
      # hyōgaiji kanji #1009
      '聾'        : ('聾',),
      # hyōgaiji kanji #1010
      '肋'        : ('肋',),
      # hyōgaiji kanji #1011
      '勒'        : ('勒',),
      # hyōgaiji kanji #1012
      '漉'        : ('漉',),
      # hyōgaiji kanji #1013
      '麓'        : ('麓',),
      # hyōgaiji kanji #1014
      '窪'        : ('窪',),
      # hyōgaiji kanji #1015
      '歪'        : ('歪',),
      # hyōgaiji kanji #1016
      '猥'        : ('猥',),
      # hyōgaiji kanji #1017
      '隈'        : ('隈',),
      # hyōgaiji kanji #1018
      '或'        : ('或',),
      # hyōgaiji kanji #1019
      '罠'        : ('罠',),
      # hyōgaiji kanji #1020
      '椀'        : ('椀',),
      # hyōgaiji kanji #1021
      '碗'        : ('碗',),
      # hyōgaiji kanji #1022
      '彎'        : ('彎', '弯'),

      # ???
      '鬣'        : ('鬣',),

    })
    
# http://ja.wikipedia.org/wiki/%E6%8B%AC%E5%BC%A7
SYMB_PUNCTUATION = Name2Symbols(
    {"("         : ('(',),
     ")"        : (')',),
     "（"         : ('（',),
     "）"         : ('）',),
     "⎛"         : ('⎛',),
     "⎜"         : ('⎜',),
     "⎝"         : ('⎝',),
     "⎞"         : ('⎞',),
     "⎟"         : ('⎟',),
     "⎠"         : ('⎠',),
     "︵"         : ('︵',),
     "︶"         : ('︶',),
     "﴾"         : ('﴾',),
     "﴿"         : ('﴿',),
     "﹙"         : ('﹙',),
     "﹚"         : ('﹚',),
     "❨"         : ('❨',),
     "❩"         : ('❩',),
     "❪"         : ('❪',),
     "❫"         : ('❫',),
     "⁽"         : ('⁽',),
     "⁾"         : ('⁾',),
     "₍"         : ('₍',),
     "₎"         : ('₎',),
     
     "⦅"         : ('⦅',),
     "⦆"         : ('⦆',),
     "｟"         : ('｟',),
     "｠"         : ('｠',),
     "⸨"         : ('⸨',),
     "⸩"         : ('⸩',),
     
     "「"         : ('「',),
     "」"         : ('」',),
     "｢"         : ('｢',),
     "｣"         : ('｣',),
     "﹁"         : ('﹁',),
     "﹂"         : ('﹂',),

     "『"         : ('『',),
     "』"         : ('』',),
     "﹃"         : ('﹃',),
     "﹄"         : ('﹄',),

     "["         : ('[',),
     "]"         : (']',),
     "［"         : ('［',),
     "］"         : ('］',),
     "⎡"         : ('⎡',),
     "⎢"         : ('⎢',),
     "⎣"         : ('⎣',),
     "⎤"         : ('⎤',),
     "⎥"         : ('⎥',),
     "⎦"         : ('⎦',),
     "﹇"         : ('﹇',),
     "﹈"         : ('﹈',),

     "〚"         : ('〚',),
     "〛"         : ('〛',),
     "⟦"         : ('⟦',),
     "⟧"         : ('⟧',),

     "{"         : ('{',),
     "}"         : ('}',),
     "｛"         : ('｛',),
     "｝"         : ('｝',),
     "⎧"         : ('⎧',),
     "⎨"         : ('⎨',),
     "⎩"         : ('⎩',),
     "⎪"         : ('⎪',),
     "⎫"         : ('⎫',),
     "⎬"         : ('⎬',),
     "⎭"         : ('⎭',),
     "⎰"         : ('⎰',),
     "⎱"         : ('⎱',),
     "︷"         : ('︷',),
     "︸"         : ('︸',),
     "﹛"         : ('﹛',),
     "﹜"         : ('﹜',),
     "❴"         : ('❴',),
     "❵"         : ('❵',),

     "〔"         : ('〔',),
     "〕"         : ('〕',),
     "❲"         : ('❲',),
     "❳"         : ('❳',),
     "⟮"         : ('⟮',),
     "⟯"         : ('⟯',),
     "︹"         : ('︹',),
     "︺"         : ('︺',),

     "〘"         : ('〘',),
     "〙"         : ('〙',),
     "⟬"         : ('⟬',),
     "⟭"         : ('⟭',),

     "〈"         : ('〈',),
     "〉"         : ('〉',),
     "〈"         : ('〈',),
     "〉"         : ('〉',),
     "❬"         : ('❬',),
     "❭"         : ('❭',),
     "❰"         : ('❰',),
     "❱"         : ('❱',),
     "‹"         : ('‹',),
     "›"         : ('›',),
     "⧼"         : ('⧼',),
     "⧽"         : ('⧽',),
     "⟨"         : ('⟨',),
     "⟩"         : ('⟩',),
     "︿"         : ('︿',),
     "﹀"         : ('﹀',),

     "《"         : ('《',),
     "》"         : ('》',),
     "⟪"         : ('⟪',),
     "⟫"         : ('⟫',),
     "︽"         : ('︽',),
     "︾"         : ('︾',),

     "<"         : ('<',),
     ">"         : ('>',),

     "＜"         : ('＜',),
     "＞"         : ('＞',),
     "≪"         : ('≪',),
     "≫"         : ('≫',),

     "«"         : ('«',),
     "»"         : ('»',),
     "‹"         : ('‹',),
     "›"         : ('›',),

     "【"         : ('【',),
     "】"         : ('】',),
     "︻"         : ('︻',),
     "︼"         : ('︼',),

     "〖"         : ('〖',),
     "〗"         : ('〗',),
     "︗"         : ('︗',),
     "︘"         : ('︘',),

     # http://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%BC%E3%83%80%E3%83%BC_%28%E8%A8%98%E5%8F%B7%29
     "…"         : ('…',),
     "‥"         : ('‥',),
     "⋯"         : ('⋯',),
     "︙"         : ('︙',),
     "︰"         : ('︰',),
     "⁝"         : ('⁝',),
     "⁚"         : ('⁚',),

     # http://ja.wikipedia.org/wiki/%E8%AA%AD%E7%82%B9
     "、"         : ('、',),
     "､"         : ('､',),

     # http://ja.wikipedia.org/wiki/%E5%8F%A5%E7%82%B9
     "。"         : ('。',),
     "｡"         : ('｡',),
     "︒"         : ('︒',),

     # http://ja.wikipedia.org/wiki/%E4%B8%AD%E9%BB%92
     "·"         : ('·',),
     "·"         : ('·',),
     "•"         : ('•',),
     "∙"         : ('∙',),
     "⋅"         : ('⋅',),
     "・"         : ('・',),
     "･"         : ('･',),

     # http://ja.wikipedia.org/wiki/%E5%BA%B5%E7%82%B9
     "〽"         : ('〽',),

     # http://ja.wikipedia.org/wiki/%E6%B3%A2%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5
     "〜"         : ('〜',),

     # http://ja.wikipedia.org/wiki/%E6%84%9F%E5%98%86%E7%AC%A6
     "!"         : ('!',),
     "¡"         : ('¡',),
     "ǃ"         : ('ǃ',),
     "‼"         : ('‼',),
     "！"         : ('！',),

     # http://ja.wikipedia.org/wiki/%E7%96%91%E5%95%8F%E7%AC%A6
     "?"         : ('?',),
     "？"         : ('？',),
     "⁇"         : ('⁇',),
     "¿"         : ('¿',),

     '0'        : ('0',),
     '1'        : ('1',),
     '2'        : ('2',),
     '3'        : ('3',),
     '4'        : ('4',),
     '5'        : ('5',),
     '6'        : ('6',),
     '7'        : ('7',),
     '8'        : ('8',),
     '9'        : ('9',),

     "-"        : ('-',),

     # usual space :
     ' '        : (' ',),
     # ideographic space :
     '\u3000'   : ('\u3000',),
     '\n'       : ('\n',),
     '\r'       : ('\r',),
     '\t'       : ('\t',),

    })

SYMB_DIACRITICS = Name2Symbols(
    {"dakuten"          : ( chr(0x3099),),      # が 
     "handakuten"       : ( chr(0x309A),),      # ぱ̍
     })

#...............................................................................
# we calculate these tuples which are often used in order to speed up the code :
#...............................................................................
SYMB_DIACRITICS__DAKUTEN = SYMB_DIACRITICS['dakuten']
SYMB_DIACRITICS__HANDAKUTEN = SYMB_DIACRITICS['handakuten']

# we define these constants in order to avoir multiple calls to SYMB_DIACRITICS.get_default_symbol :
DEFAULTSYMB__CHOONPU = SYMB_CHOONPU.get_default_symbol('ー')
DEFAULTSYMB__DAKUTEN = SYMB_DIACRITICS.get_default_symbol('dakuten')
DEFAULTSYMB__HANDAKUTEN = SYMB_DIACRITICS.get_default_symbol('handakuten')
