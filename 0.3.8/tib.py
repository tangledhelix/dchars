from dchars.dchars import new_dstring
DSTRING_BOD = new_dstring(language="བོད་ཡིག", transliteration_method='ewts')

for txt, trans_ewts in (
                        ("ཀ"    , 'ka'),
                        ("ཀྲ"    , 'kra'),
                        ("ཀྭ",   'kwa'),
                        ("ཀྱ",   'kya'),
                        ("རྐ",   'rka'),
                        ("ཉ",   'nya'),
                        ("རྙ",   'rnya'),
                        ("ཀི",   'ki'),
                        ("ཀུ",   "ku"),
                        ("ཀེ",   "ke"),
                        ("ཀོ",  "ko"),
                        ('ཨི', "i"),
                        ("ཀོང", "kong"),
                        ("བསྒྲིབས", "bsgribs"),
                        ("མགོན", "mgon"),

                        ("ཁམ་", "kham "),
                        ("ཁམས", "khams"),

                        # three-letters syllable without sa suffix :
                        ("འཇམ", "'jam"),

                        ("སྤྲུལ", "sprul"),
                        ("བློ", "blo"),
                        ("གྲོས", "gros"),

                        ("མཐའ་ཡས", "mtha' yas"),

                        # titles from http://www.rigpawiki.org/index.php?title=Jamg%C3%B6n_Kongtrul_Lodr%C3%B6_Tay%C3%A9 :
                        ("འཇམ་མགོན་ཀོང་སྤྲུལ་བློ་གྲོས་མཐའ་ཡས་", "'jam mgon kong sprul blo gros mtha' yas "),
                        ("ཤེས་བྱ་ཀུན་ཁྱབ་མཛོད་", "shes bya kun khyab mdzod "),
                        ("གདམས་ངག་མཛོད་", "gdams ngag mdzod "),
                        ("རིན་ཆེན་གཏེར་མཛོད་ཆེན་མོ་", "rin chen gter mdzod chen mo "),
                        ("རྒྱ་ཆེན་བཀའ་མཛོད་", "rgya chen bka' mdzod "),
                        ("ངེས་དོན་སྒྲོན་མེ་", "nges don sgron me "),

                        # from http://www.rigpawiki.org/index.php?title=Mandala
                        ("དཀྱིལ་འཁོར་", "dkyil 'khor "),

                        # from http://www.rigpawiki.org/index.php?title=Tantra
                        ("རྒྱུད་", "rgyud "),
                        ("རྩ་རྒྱུད་", "rtsa rgyud "),
                        ("བཤད་རྒྱུད་", "bshad rgyud "),
                        # from http://www.rigpawiki.org/index.php?title=Nine_yanas
                        ("ཐེག་པ་དགུ་", "theg pa dgu "),
                        # from http://www.rigpawiki.org/index.php?title=Nine_yanas
                        ("ཐེག་པ་རིམ་པ་དགུ་", "theg pa rim pa dgu "),
                        # from http://www.rigpawiki.org/index.php?title=Seven_Points_of_Mind_Training
                        ("བློ་སྦྱོངས་དོན་བདུན་མ་", "blo sbyongs don bdun ma "),
                        # from http://www.rigpawiki.org/index.php?title=Kama :
                        ("རྙིང་མ་བཀའ་མ་", "rnying ma bka' ma "),
                        # from http://www.rigpawiki.org/index.php?title=Terma :
                        ("གཏེར་མ་", "gter ma "),

                        # imaginary words :
                        ("བྲག", "brag"),
                        ("བརག", "b.rag"),

                        # http://en.wikipedia.org/wiki/Wylie_transliteration
                        ("གྱང", "gyang"),
                        ("གཡང", "g.yang"),

                        # # # Quelques exemples de noms propres tirés du sanskrit ou du chinois, pour rigoler...
                        ("ཏཱ་ལའི་བླ་མ", "tA la'i bla ma"), # the Dalaï-Lama

                        ("ཏཱ་ར་ནཱ་ཐ", "tA ra nA tha"),

                        # # des exemples un peu plus vaches:
                        ("བའི", "ba'i"),
                        ("པའོ", "pa'o"),
                        ("མཚོའི", "mtsho'i"),

                        ("མཇ", "mja"),

                        ("རྐ", "rka"),

                        ("འོད", "'od"),
                        ("ཡིད", "yid"),
                        ("གཡུག", "g.yug"),
                        ("ཁྱིའུ", "khyi'u"),
                        ("བམའི", "bma'i"),
                        ("བམའ", "bma'"),
                        ("མའི" ,"ma'i" ),

                        ("དབྱངས", "dbyangs"),

                        ("པའོ" , "pa'o" ),
                        ("ཨའ", "a'"),

                        ("གྱཀ", "gyaka"),
                        ("གཡག", "g.yag"),

                        ("མང", "mang"),
                        ("བརྒྱུད", "brgyud"),
                        ("བཀའ་བརྒྱུད་སྔགས་མཛོད་", "bka' brgyud sngags mdzod "),

                        ("ཀརྨ་པ་", "karma pa "),

                        ("ཨ་ཁུ", "a khu"),
                        ("ཨུག་པ", "ug pa"),
                       ):

    # print("*"*80)
    # print("*"*80)
    # print("*"*80)
    # print()
    print(txt)
    print([hex(ord(c)) for c in txt], trans_ewts)
    string = DSTRING_BOD(txt)
    if string.get_sourcestr_representation() != txt:
        print("!!!!src->src", txt, string.get_sourcestr_representation())
        break
    trans = string.get_transliteration()
    if trans != trans_ewts:
        print("!!!!trans", "<"+trans_ewts+">")
        print("!!!!trans", "<"+trans+">")
        break
