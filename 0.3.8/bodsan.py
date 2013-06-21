from htmltable import HtmlTable
from dchars.dchars import new_dstring

DSTRING_BOD = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Sanskrit"})

DSTRING_BODSAN = new_dstring(language="བོད་ཡིག",
                             transliteration_method='bodsan',
                             options = {"expected structure" : "always Sanskrit",}
                            )

DSTRING_SAN = new_dstring(language='संस्कृतम्', transliteration_method="iso15919")

table = HtmlTable( header = ["source",
                             "→ DSTRING_BODSAN()",
                             "→ DSTRING_SAN()",
                             "expected result",
                             ])

data = (
        ("༠",   "०"),
        ("ཨ",   "अ"),
        ("ཨི",   "इ"),
        ("ཨཿ",  "अः"),
        ("ཀ",   "क"),
        ("ཀི",   "कि"),
        ("ཀཱི",   "की"),
        ("ཀཱ",   "का"),
        ("པེ",   "पे"),
        ("པོ",   "पो"),
        ("ཝ",   "व"),
        ("?", "पो"),
        ("?", "पौ"),
        ("ཀཀ", "कक"),
        ("ཀ་ཀ", "क क"),
        ("ཀརྨ",  "कर्म"),
        ("ཀརྨཀརྨ",  "कर्मकर्म"),
        ("ཁས", "खस"),
        ("ཁསཾ", "खसं"),
        ("ཁ་ས་", "खस"),
        ("ཁ་སཾ་", "खसं"),
        # http://en.wikipedia.org/wiki/Om_mani_padme_hum :
        ("ཨོཾ་མ་ཎི་པ་དྨེ་ཧཱུྃ",    "ओं म णि प द्मे   हूँ"),
       )

for bod, san in data:

    # print("***", bod)
    # print([hex(ord(c)) for c in bod])

    bodsan_dstring = DSTRING_BODSAN(bod)
    san_dstring = DSTRING_SAN(bodsan_dstring.get_transliteration())

    table.append(
            (bod+" ("+DSTRING_BOD(bod).get_transliteration()+")",
             str(bodsan_dstring)+" ("+bodsan_dstring.get_transliteration()+")",
             str(san_dstring)+" ("+san_dstring.get_transliteration()+")",
             san+" ("+DSTRING_SAN(san).get_transliteration()+")",
            ))

print(table.get_html())

table = HtmlTable( header = ["source",
                             "→ DSTRING_BODSAN()",
                             "→ DSTRING_SAN()",
                             "expected result",
                             ])

for bod, san in data:

    # print("***", bod)
    # print([hex(ord(c)) for c in bod])

    bodsan_dstring = DSTRING_BODSAN().init_from_transliteration(san)
    san_dstring = DSTRING_SAN(bodsan_dstring.get_transliteration())

    table.append(
            (san+" ("+DSTRING_SAN(san).get_transliteration()+")",
             str(bodsan_dstring)+" ("+bodsan_dstring.get_transliteration()+")",
             str(san_dstring)+" ("+san_dstring.get_transliteration()+")",
             san+" ("+DSTRING_SAN(san).get_transliteration()+")",
            ))

print(table.get_html())
