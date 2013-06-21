from htmltable import HtmlTable
from dchars.dchars import new_dstring

htmlt = HtmlTable( header = ("(source:ewts or bod)",
                             "",
                             "always Tibetan",
                             "Tibetan or Sanskrit",
                             "always Sanskrit",) )


DSTRING_BOD_s = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Sanskrit",
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_t = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "always Tibetan",
                                     "look up in the buffers" : False},
                          )
DSTRING_BOD_o = new_dstring(language="བོད་ཡིག",
                          transliteration_method='ewts',
                          options = {"expected structure" : "Tibetan or Sanskrit",
                                     "look up in the buffers" : False},)

for ewts, bod in ( ("ma", "མ"),
                   ("tA", "ཏཱ"),
                   ("bsgrad", "བསྒྲད"),
                   ("karma", "ཀརྨ"),
                   ("karmaM", "ཀརྨཾ"),
                   ("d+harma", "དྷརྨ"),
                   ("kaurabaH", "ཀཽརབཿ"),
                   ("dAyag", "དཱཡག"),
                   ("shamba'i'i", "ཤམབའིའི"),
                   ("panDi", "པནཌི")
                   ):

    s = DSTRING_BOD_s().init_from_transliteration(ewts)
    t = DSTRING_BOD_t().init_from_transliteration(ewts)
    o = DSTRING_BOD_o().init_from_transliteration(ewts)

    htmlt.append( (ewts,
                   "",
                   "{0}({1})".format( str(t), t.get_transliteration() ),
                   "{0}({1})".format( str(o), o.get_transliteration() ),
                   "{0}({1})".format( str(s), s.get_transliteration() ),
                   ))

    s = DSTRING_BOD_s(bod)
    t = DSTRING_BOD_t(bod)
    o = DSTRING_BOD_o(bod)

    htmlt.append( (bod,
                   "",
                   "{0}({1})".format( str(t), t.get_transliteration() ),
                   "{0}({1})".format( str(o), o.get_transliteration() ),
                   "{0}({1})".format( str(s), s.get_transliteration() ),
                   ))

print(htmlt.get_html())

