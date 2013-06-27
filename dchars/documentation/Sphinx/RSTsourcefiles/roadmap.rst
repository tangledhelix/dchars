=============
ROADMAP_TITLE
=============

.. code-block:: none

  * (28) pas moyen de trier grc : dstring.sortingvalue ?
  * (27) nom de la méthode pour trier : (bod) default ou basic ? voir *tables*.py

  * (26) bodsan : http://www.virtualvinodh.com/tibetan

    अनिरोधम् अनुत्पादम् अनुच्छेदम् अशाश्वतम् ।

    अनेकार्थम् अनानार्थम् अनागमम् अनिर्गमम् ॥

    यः प्रतीत्यसमुत्पादं प्रपञ्चोपशमं शिवम् ।

    देशयामास संबुद्धस्तं वन्दे वदतां वरम् ॥


    transliterated as :

    
    ཨནིརོདྷམ྄ ཨནུཏྤཱདམ྄ ཨནུཙྪེདམ྄ ཨཤཱཤྭཏམ྄ ། 

    ཨནེཀཱརྠམ྄ ཨནཱནཱརྠམ྄ ཨནཱགམམ྄ ཨནིརྒམམ྄ ༎ 

    ཡཿ པྲཏཱིཏྱསམུཏྤཱདཾ པྲཔཉྩོཔཤམཾ ཤིཝམ྄ ། 

    དེཤཡཱམཱས སཾབུདྡྷསྟཾ ཝནྡེ ཝདཏཱཾ ཝརམ྄ ༎ 

(The Sample text is the invocatory verse of Nagarajuna's Mulamadhyamaka Karika :
The non-ceasing and the non-arising, the non-annihilation and the non-permanence,
The non-identity and the non-difference, the non-appearance and the non-disappearance,
The dependent arising, the appeasement of obsessions and the auspicious
I salute him, the fully enlightened Buddha, the best of speakers, who preached them

ref : https://groups.google.com/forum/#!msg/grantha-lipi/a3jWe5gvdTs/CkGu2_Te36EJ
)

  * (23) bodsan
  * (22) http://94.23.197.37/dchars/doc/en/howto_use.html : un par langue
  * (21) donner un exemple pour sort.py
  * (19) "सिद्धि", "སི་དདྷི་" = + prefix : vérifier que l'on a bien le préfixe
  * (18) bodsan : l'Illuminator contient des exemples intéressants de translittérations.
  * (17) (bod) utiliser des tables annexes pour alléger le code !
  * (16) vérifier comment le "jh" sanskrit est translittéré en tibétain.
  * (15) "DEVANAGARI " > "" (bod + san)
  * (14) ko+o = kau selon http://www.thlib.org/reference/transliteration/wyconverter.php
  * (13) ཁས khas sans tsheg : toujours ajouter tsheg pour "always Sanskrit" ?
  * (12) option : use ca cha ja jha instead of tsa tsha dza dzha = no
  * (11) (lat) e dans l'o, e dans l'a
  * (10) (bod) new test : TESTSDStringBOD.test_different_structures
  * (09) "ཏནདྲ" tandra / ཏནདར tand.ra/ problème avec shamba'i'i
  * (07) fixed form for R ?
  * (06) documenter les langues (sauf bod, !! revoir l'ordre des diacritiques à partir du code !!! :
         même ordre dans get_sourcestr_representation() et dchar__get_translit_str()
  * (05) (toutes langues) accélérer le code : accélérer len(constante) > len_constante
  * (04) (bod) quid de KAKE_A ?
  * (03) (bod.ewts) vérifier que la liste suivant est bien traitée par le programme :
    # anusvara = 0F7E TIBETAN SIGN RJES SU NGA RO
    # visarga  = 0F7F TIBETAN SIGN RNAM BCAD
    # chandrabindu = 0F83 TIBETAN SIGN SNA LDAN
    # virama = 0F84 TIBETAN MARK HALANTA
    # avagraha = 0F85 TIBETAN MARK PALUTA
    # jihvamuliya = 0F88 TIBETAN SIGN LCE TSA CAN [NON]
    # upadhmaniya = 0F89 TIBETAN SIGN MCHU CAN [NON]
  * (02) virer les print(), les $$$ et ???
  * (01) bod.bodsan
  * (00) Old Norse (?)

  * (bod)DOC :

    * même si ce n'est pas un mot valide, gyaka est accepté (pas seulement gyag) (??? à vérifier)
    * pour afficher, utiliser par exemple https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/Jomolhari-ID-a3d.zip

  * doc : expliquer en général ce qu'est une DString : repr(dstring), str(dstring)
  * différence indexes et real_indexes :
    rnya : r/n/y/a pour real_indexes
           r/ny/a/ pour indexes

  * (bod) à propos de oM : peut être représenté par 0x0F00 ou par 0x0F68 + 0x0F7C + 0x0F7E
    dans les deux cas, au final, le signe est pas analysé comme une signe de ponctuation, non pas comme voyelle + M.
    la représentation interne est donc celle d'un signe de ponctuation.

  *      doc pour DCharacter* : si unknown character, le caractère inconnu est stocké dans .base_char

  * (bod) si un caractère est inconnu, unknown_character = True et le caractère est contenu dans punctuation_or_other_symbol

  * (bod) les deux buffers ne sont utilisés que pour "expected structure" = "Tibetan or Sanskrit"


DOC : toutes langues : Le DChar de chaque langue doit avoir une fonction sortingvalue().

DOC : au niveau d'un DCharacter, objet SortingValue renvoyé par .sortingvalue(); au niveau d'une
DString, list de SortingValue 


DOC:
"क" ------------ 

           <--(1b)----           -----(2b)--->
(EWTS)"ka" ---(1a)---> .istructs <----(2a)---- (Tibetan script, unicode, utf-8)"ཀ"
                         |    /\
                         |     |
                        (3a) (3b)
                         |     |
                         \/    |
                     list of DCharacterBOD

(1a)  DStringBOD.init_from_transliteration > ewts.py::get_intstruct_from_trans_str
(1b)  ewts.py::dstring__get_translit_str()
(2a)  DStringBOD.init_from_str() > istructs::get_intstruct_from_str
(2b)  istructs.get_the_corresponding_string() > [ istruct.get_the_corresponding_string() ]
(3a)  istructs.get_the_corresponding_dchars() > [ istruct.get_the_corresponding_dchars() ]
(3b)  internalstructure.py::get_intstructures_from_dstring()


DOC:
visarga :
        "high"          : visarga > visarga
        "normal"        : visarga > 0 [@@BOD2SAN-NORM-001]
        "low"           : visarga > 0 [@@BOD2SAN-LOW-001]

व(va) :
        "high"          : व(va) > व(va)
        "normal"        : व(va) > ब(ba) [@@BOD2SAN-NORM-002]
        "low"           : व(va) > ब(ba) [@@BOD2SAN-LOW-002]

ओ(ō) :
        dependent vowels :
        "high"          : ओ(ō) > ओ(ō)
        "normal"        : ओ(ō) > औ(au) [@@BOD2SAN-NORM-003]
        "low"           : ओ(ō) > औ(au) [@@BOD2SAN-NORM-003]

        independent vowels :
        "high"          : ओ(ō) > ओ(ō)
        "normal"        : ओ(ō) > औ(au) [@@BOD2SAN-NORM-004]
        "low"           : ओ(ō) > औ(au) [@@BOD2SAN-NORM-004]

long vowels (ā, ī, ū) :
        dependent vowels :
        "high"          : long vowels > long vowels
        "normal"        : long vowels > long vowels
        "low"           : long vowels > short vowels [@@BOD2SAN-LOW-005]

        independent vowels :
        "high"          : long vowels > long vowels
        "normal"        : long vowels > long vowels
        "low"           : long vowels > short vowels [@@BOD2SAN-LOW-006]

retroflex consonant :
        "high"          : retroflex consonant > retroflex consonant
        "normal"        : retroflex consonant > retroflex consonant
        "low"           : retroflex consonant > non-retroflex consonant
                          retroflex consonant + aspiration > non-retroflex consonant without aspiration
                          [@@BOD2SAN-LOW-007]

DOC :
"sra" : (consonant)S + (subfix)R [@@BOD-INTERNALSTRUCTURE-001]
"rla" : (consonant)R + (subfix)L [@@BOD-INTERNALSTRUCTURE-002]
"sla" : (consonant)S + (subfix)L [@@BOD-INTERNALSTRUCTURE-003]
"rwa" : (consonant)R + (subfix)W [@@BOD-INTERNALSTRUCTURE-004]
"lwa" : (consonant)L + (subfix)W [@@BOD-INTERNALSTRUCTURE-005]
"swa" : (consonant)S + (subfix)W [@@BOD-INTERNALSTRUCTURE-006]

DOC::(bod) pour les mots considérés comme tirés du sanskrit, préfixe, superfix et subfix ok; ainsi "སི་དདྷི་" (siddhi) représentant "सिद्धि" utilise bien un préfixe.

DOC::(bod) @@BOD-INTERNALSTRUCTURE-007
'SIGN RNAM BCAD',       # "gtiH" and not "gatiH", so rnam bcad isn't an evidence of a Sanskrit word

DOC::(bod) @@BOD-INTERNALSTRUCTURE-008
'SIGN RJES SU NGA RO', # ཁསཾ = "khaMs" and not "khasaM", so rjes su nga ro isn't an evidence of a Sanskrit word

DOC::(bod) @@BOD-INTERNALSTRUCTURE-009a : sorting method = 'basic'
attention : 
ཀ་ཏྱྰ་ཡ་ན་ནོག་ཅན (ka t+y+'a ya na nog can)
ཀ་ཏྱྰའི་བུ་ཆེན་པོ (ka t+y+'a'i bu chen po)           : absence de suffixe grammatico-sémantique (dans ka t+y+'a) < suffixe 'i (dans ka t+y+'a'i)



DOC:comment trier les mots 
from dchars.languages.bod.dstring import DStringBOD
words = list(map(DSTRING_BOD, ("པ","ཀ","ས")))
sorted_words = sorted(words, key=DStringBOD.sortingvalue)

