.. |br| raw:: html

   <br />

=========
SAN_TITLE
=========

------------
WHAT_IS_THIS
------------

$WHAT_IS_THIS_TXT$

---------------
SIMPLE_EXAMPLES
---------------

$SIMPLE_EXAMPLES_TXT$

.. code-block:: python

    from dchars.dchars import new_dstring
    DSTRING_SAN = new_dstring(language='संस्कृतम्')

    # ------------------------------------
    # let's start with a Sanskrit string :
    # ------------------------------------
    # let's take the first verse from the Rig-Veda :
    string = DSTRING_SAN("अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।")
    # is this DString object valid (i.e. no problem with the Sanskrit string ?)
    print(string.validity)                  # -> True : no problem

    # get the (default) transliteration :
    print(string.get_transliteration())     # -> "a̱gnimī́ḷē pu̱rōhítaṁ ya̱jñasyá dē̱vamr̥̱tvijám ."

    # is there an anuudatta on the character #0 ?
    print(string[0].anudatta)               # -> True
    # what's the basic character of the character #0 ?
    print(string[0].base_char)              # -> "A"
    # what's the basic character of the character #1 ?
    print(string[1].base_char)              # -> "DEVANAGARI LETTER GA"
    # what's the dependent vowel of the character #1 ?
    print(string[1].dependentvowel)         # -> None
    # what's the basic character of the character #2 ?
    print(string[2].base_char)              # -> "DEVANAGARI LETTER NA"
    # what's the dependent vowel of the character #2 ?
    print(string[2].dependentvowel)         # -> "I"

    # let's add a stress accent to character #0 :
    string[0].accent = "DEVANAGARI STRESS SIGN UDATTA"
    print(string)                           # -> अ॒॑ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।
    print(string.get_transliteration())     # -> á̱gnimī́ḷē pu̱rōhítaṁ ya̱jñasyá dē̱vamr̥̱tvijám .

    # is the last character a punctuation sign ?
    print(string[-1].punctuation)           # -> True, since we read "।" (danda)

    # --------------------------------------------------------------------------
    # now, let's start with a transliterated string (using the default method) :
    # --------------------------------------------------------------------------
    string = DSTRING_SAN().init_from_transliteration('ya̱jñasyá')
    # we have a DSTRING_SAN object whose length is equal to 5 (5 DCharacterSAN objects) :
    print(len(string), string)              # -> 5
    # let's add two characters : space + pu̱
    string += DSTRING_SAN(" पु॒")
    # the string we get is now...
    print(string)                           # -> "य॒जञसय॑ पु॒"
    print(string.get_transliteration())     # -> "ya̱jñasyá pu̱"

-----------------------
TRANSLITERATION_METHODS
-----------------------

$TRANSLITERATION_METHODS_TXT$

ISO15919_METHOD
---------------

$ISO15919_TXT$

.. code-block:: none

    * (Rig-Veda, I.1) :
      अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् । होता॑रं रत्न॒धात॑मम् ॥
      a̱gnimī́ḷē pu̱rōhítaṁ ya̱jñasyá dē̱vamr̥̱tvijám . hōtā́raṁ ratna̱dhātámam ..

    * transliterated characters defining one DCharacterSAN are defined in this order : base_char | accent | anudatta | nukta | anusvara_candrabindu
      (confer san/transliterations/iso15919.py::PATTERN)
      E.g. : "१॒॑" (१(0x0967) + anudatta(0x0952) + udatta(0x0951)) => "1̱́" ('1' + 0x0331anudatta + 0x0301=accent)

    * "SHORT E" and "E", "SHORT O" and "O" are different vowels; "E" and "O" are the natural vowels of Sanskrit and are rendered as ē and ō.
    * r̥(0072+0325) is a vowel, not ṛ(1E5B).
    * vowels in hiatus are preceded by a ":" ('रआ' = "ra:ā")
    * visarga is transliterated by a "ḥ" ("कं॒ः" = 'ka̱ṁḥ')
    * chandrabindu is transliterated by a "m̐" ('माँ' = 'mām̐') ALWAYS PLACED AFTER THE CHARACTER,
      ignoring a rule followed by ISO15919 (see NOTE-ISO15919-1 below)
    * the module knows how to handle consonants with nutka : "क़॒॑" = "qá̱"

    * Nepali r̆ (ONE/TWO-WAY URPHA OPTION) has not been taken in account.
    * r- (adscript consonant) has been ignored
    * no vowels ligatures (dr̥, ru, rū, hr̥) or half consonants ligatures.
    * the program reads r̥̄ = r + 0325 + 0304 AND r + 0304 + 0325.
    * the program reads l̥̄ = l + 0325 + 0304 AND l + 0304 + 0325.
    * the program reads 'ḥ' [0068+0323] AND 'ḥ' [1E25]
    * udatta + anudatta : the program produces 0x0331 + 0x0301 (not 0x0301 + 0x0331)
    * udatta + anudatta : the program reads 0x0331 + 0x0301 AND 0x0301 + 0x0331
    * the program produces r̥̄ = r + 0325 + 0304, not r + 0304 + 0325.
    * the program produces l̥̄= l + 0325 + 0304, not l + 0304 + 0325
    * the program produces 'ḥ' [1E25]
    * consonants with anudatta : the program produces compact symbols like
      ḵ (1E35), not k + 0331
    * consonants with anudatta : the program reads compact symbols like
      ḵ (1E35) AND uncompact symbols like k + 0331
    * consonants with dot like ṛ : the program produces compact symbols like
      ṛ (1E5B), not r+0x0323
    * consonants with dot like ṛ : the program reads compact symbols like
      ṛ (1E5B) AND uncompact symbols r+0x0323.
    * anusvara & candrabindu : ISO 15919 has two options about anusvāra and this
      program always uses the "simplified nasalization option" : "ṁ"
    * e and ē, o and ō are different; Sanskrit has ē and ō.
    * DEVANAGARI SIGN INVERTED CANDRABINDU ignored

    * (NOTE-ISO15919-1) (ignored rule) : When used with a semi-vowel (y, r, l, ḷ or v),
      candrabindu is placed before the semi-vowel. For example, यँ is written m̐ya and not yam̐.

ITRANS_METHOD
-------------

$ITRANS_TXT$

.. code-block:: none

    * (Rig-Veda, I.1) :
      "अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् । होता॑रं रत्न॒धात॑मम् ॥"
      a\_gnimI\'Le pu\_rohi\'taM ya\_j~nasya\' de\_vamR^i\_tvija\'m . hotA\'raM ratna\_dhAta\'mam ..

    * transliterated characters defining one DCharacterSAN are defined in this order : base_char | anudatta | accent | virama | anusvara_candrabindu
      (confer san/transliterations/itrans.py::PATTERN)
      * e.g. : "१॒॑" = "1\\_\\'"
      * e.g. : 'रआ' = "ra/A"

    * "SHORT E" and "E", "SHORT O" and "O" are different vowels; "E" and "O" are the natural vowels of Sanskrit and are rendered as "e" and "o".
    * r̥(0072+0325) is a vowel, not ṛ(1E5B).
    * some vowels in hiatus are preceded by a "+" and some vowels by "/" (see san/transliterations/itrans.py::VOWELS_IN_HIATUS)
    * visarga is transliterated by a "H" ("कं॒ः" = 'ka\\_MH')
    * chandrabindu is transliterated by a ".N" ("कं॒ः" = 'ka\\_MH')
    * the module knows how to handle consonants with nutka : "क़" = "qa"
    * a R^i vowel in hiatus seems to be transliterated as R^i
      (according to text003_rigveda_samhita_1_1.itrans.txt :
       e.g.: ##1.044.03c##  dhU\_make\'tu\_M bhAR^i\'jIka\_M vyu\'ShTiShu ya\_j~nAnA\'madhvara\_shriya\'m ..)
    * if a vowel is in hiatus but have the anusvara or a candrabindu character,
      it's transliterated as a hiatus but as a stand-alone vowel (???, according to
      according by text003_rigveda_samhita_1_1.itrans.txt)

    * this transliteration method is based on two documents :
      * (1) http://www.aczoom.com/itrans/#itransencoding (reproduced below)
      * (2) http://www.detlef108.de/RV-D-IT.txt <-> http://www.detlef108.de/RV-D-UTF8.html

    *   -----------------------------------------------------------
        Extract from http://www.aczoom.com/itrans/#itransencoding :
        -----------------------------------------------------------
          "
          " Vowels (dependent and independent):
          " -------
          " a     aa / A       i      ii / I       u     uu / U
          " RRi / R^i    RRI / R^I    LLi / L^i    LLI / L^I
          " e     ai     o     au     aM    aH
          "
          " Consonants:
          " -----------
          " k     kh     g     gh     ~N
          " ch    Ch     j     jh     ~n
          " T     Th     D     Dh     N
          " t     th     d     dh     n
          " p     ph     b     bh     m
          " y     r      l     v / w
          " sh    Sh     s     h      L
          " x / kSh     GY / j~n / dny     shr
          " R (for marathi half-RA)
          " L / ld (marathi LLA)
          " Y (bengali)
          "
          " Consonants with a nukta (dot) under them (mainly for Urdu devanagari):
          " -----------------------------------------
          " k  with a dot:      q
          " kh with a dot:      K
          " g  with a dot:      G
          " j  with a dot:      z / J
          " p  with a dot:      f
          " D  with a dot:      .D
          " Dh with a dot:      .Dh
          "
          " Specials/Accents:
          " -----------------
          " Anusvara:       .n / M / .m  (dot on top of previous consonant/vowel)
          " Avagraha:       .a    (`S' like symbol basically to replace a after o)
          " Ardhachandra:   .c    (for vowel sound as in english words `cat' or `talk')
          " Chandra-Bindu:  .N    (chandra-bindu on top of previous letter)
          " Halant:		.h    (to get half-form of the consonant - no vowel - virama)
          " Visarga:        H     (visarga - looks like a colon character)
          " Om:		OM, AUM (Om symbol)
          "
          " [As shown, many codes have multiple choices, example "RRi / R^i" implies you
          "  can use either "RRi" or "R^i"]

-------------
POSSIBILITIES
-------------

$POSSIBILITIES_TXT$

.. code-block:: none

    * metric symbols : digits+anusvara+udatta are ok (see NOTE1 below, e.g. : "१॒॑") but not special characters
      belonging to the so-called "Devanagari extended" (A8E0–A8FF).

    * a DCharacterSAN is defined by the following attributes (confer dchars/languages/san/dchars.py::DCharacterSAN.__init__) :
      * unknown_char                    : bool
      * base_char                       : None or a string with the NAME of the character,
      *                                   not the character itself.
      * accent                          : None or a string :
                                                  ("DEVANAGARI STRESS SIGN UDATTA",
                                                   "DEVANAGARI GRAVE ACCENT"
                                                   "DEVANAGARI ACUTE ACCENT"
                                                  )
                                                  but not "DEVANAGARI STRESS SIGN ANUDATTA", see anudatta below.
      * punctuation                     : bool
      * nukta                           : bool
      * anusvara_candrabindu            : None, or a string
                                                  ("DEVANAGARI SIGN ANUSVARA",
                                                   "DEVANAGARI SIGN INVERTED CANDRABINDU",
                                                   'DEVANAGARI SIGN CANDRABINDU'
                                                  )
      * virama                          : bool
      * anudatta                        : bool
      * is_an_independent_vowel         : bool
      * dependentvowel                  : None, or a string (see symbol.SYMB_DEPENDENT_VOWELS)

    * (NOTE1) : from, http://en.wikipedia.org/wiki/Vedic_accent : "If an independent svarita syllable
      is next before an udātta syllable, instead of putting the anudātta mark and the svarita mark on
      the same syllable, a figure 1 (if the svarita vowel is short) or a figure 3 (if the svarita
      vowel is long) is written between, and that figure has the svarita mark and the anudātta mark."

------------
HOW_IT_WORKS
------------

$HOW_IT_WORKS_TXT$

.. code-block:: none

    ############################################################################
    #
    # (0)   general remarks on DStringSAN and DCharacterSAN
    #
    # (1)   reciprocal functions : DStringSAN.init_from_str <> DStringSAN.get_sourcestr_representation
    # (1.1) DStringSAN.init_from_str("अ॒ग्निमी॑ळे")
    # (1.2) DStringSAN.get_sourcestr_representation()
    #
    # (2)   transliterations
    #
    # (2.1)   transliteration's method : "iso15919" : reciprocal functions
    # (2.1.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.2.2) dchar__get_translit_str()
    #
    # (2.2)   transliteration's method : "itrans" : reciprocal functions
    # (2.2.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.2.2) dchar__get_translit_str()
    #
    # (3)   exceptions
    #
    ############################################################################

    ABBREVIATIONS :
    * NFC = unicodedata.normalize('NFC', string)
    * NFD = unicodedata.normalize('NFD', string)

    ############################################################################
    # (0)   general remarks on DStringSAN and DCharacterSAN
    ############################################################################

    * From a string like "अ॒ग्निमी॑ळे" you can build a DStringSAN object by writing :
    string = DStringSAN("अ॒ग्निमी॑ळे"); you modify this object and then you get the
    corresponding string by calling DStringSAN.get_sourcestr_representation()
    * You can initialize a DStringSAN with a transliterated string :
    DStringSAN().init_from_transliteration("ba"); you can modify this
    object and then you get the new transliterated string by calling
    DStringSAN.get_the_transliteration().

    * A DStringSAN is an object derived from DString, i.e. a list of DCharacterSAN
    objects. You can access a DStringSAN as a list made of characters.
    * A DStringSAN object has the (bool)".validity" attribute set to False if
    something is wrong after a call to DStringSAN.init_from_str(); in this
    case the (list)".errors" attribute contains some informations about the error.
    * CAVEAT : THE "validity" ATTRIBUTE IS NOT SET AFTER A CALL TO
    DStringSAN.init_from_transliteration()

    * use print(string) or print(str(string)) to display the original text in a
    DStringSAN object and print(repr(string)) to get the very detailed informations
    about the string.

    * to initialize a DStringSAN object you need :
      * either a source-string like "अ॒ग्निमी॑ळे" : DStringSAN("अ॒ग्निमी॑ळे").
        Conversely, you can get this source-string by a call to the function
        DStringSAN.get_sourcestr_representation().
        * you have the identities :
              DStringSAN.get_sourcestr_representation( DStringSAN( src ) ) = src
          and DStringSAN( DStringSAN.get_sourcestr_representation (src ) ) = src

          ONLY FOR A SUBSET OF THE CHARACTERS AVAILABLE. See the documentation and
          the code to see which characters can do that; typically this module
          uses compact unicode characters when they exist : these characters should
          be prefered to the (uncompact) compounds of characters.
          This identities are controlled in the test files by the functions named
          test_from_srcstr_2_srcstr().

      * either a transliterated string like "a̱gnimī́ḷē" (see below the format of this
        string, depending to the choosed transliterations's method), by calling :
        DStringSAN().init_from_transliteration("a̱gnimī́ḷē"). Conversely you can
        get the transliterated string by calling DStringSAN.get_the_transliteration()

    ############################################################################
    # (1)   reciprocal functions : DStringSAN.init_from_str <> DStringSAN.get_sourcestr_representation
    ############################################################################

    * characters are divided into SYMB_CONSONANTS, SYMB_INDEPENDENT_VOWELS, SYMB_DEPENDENT_VOWELS,
      SYMB_OTHER_SYMBOLS, SYMB_PUNCTUATION, SYMB_DIACRITICS

    * dchars/languages/san/symbols.py::SYMB_CONSONANTS, SYMB_INDEPENDENT_VOWELS, ... are Name2Symbols

    * dchars/languages/san/dchars.py::stringSAN.pattern = re.compile("((?P<basechar>{0})((?P<dependentvowel>{1})?)(?P<diacritics>({2})*))")

      * pattern_basechar = SYMB_CONSONANTS + SYMB_INDEPENDENT_VOWELS + SYMB_OTHER_SYMBOLS + SYMB_PUNCTUATION
      * pattern_dependentvowel = SYMB_DEPENDENT_VOWELS
      * pattern_diacritics = SYMB_DIACRITICS

    * As expected with reciprocal function, we have init_from_str( get_sourcestr_representation( src ) ) = src
    and get_sourcestr_representation( init_from_str( src ) ) = src if src is made of certain characters.

    ############################################################################
    # (1.1) DStringSAN.init_from_str("अ॒ग्निमी॑ळे")
    ############################################################################

    This function initializes a DStringSAN object from a string.

    * DStringSAN("अ॒ग्निमी॑ळे")

      * DStringSAN.init_from_str("अ॒ग्निमी॑ळे")
        * src ---> NFD -----> src
        * for element in re.finditer(DStringSAN.pattern, src)
          * new_character = DCharacterSAN(unknown_char = False,
                                          base_char = base_char,
                                          accent = accent,
                                          punctuation = punctuation,
                                          nukta = nukta,
                                          anusvara_candrabindu = anusvara_candrabindu,
                                          virama = virama,
                                          anudatta = anudatta,
                                          is_a_vowel = is_a_vowel,
                                          dependentvowel = dependentvowel)

    ############################################################################
    # (1.2) DStringSAN.get_sourcestr_representation()
    ############################################################################

    This function gives the representation string corresponding to a DStringSAN object.
    The transliterated character(s) corresponding to the "a" vowel are deleted at the
    end of the function.

    * DStringSAN.get_sourcestr_representation("अ॒ग्निमी॑ळे")
      * [...]
        if self.accent is not None:
            res.append( SYMB_DIACRITICS.get_default_symbol(self.accent) )

        if self.nukta:
            res.append( SYMB_DIACRITICS.get_default_symbol("DEVANAGARI SIGN NUKTA") )

        if self.anusvara_candrabindu is not None:
            res.append( SYMB_DIACRITICS.get_default_symbol(self.anusvara_candrabindu) )
        [...]

      * res = res.replace(FAKE_A__SYMBOL, "")
      * res ----> COMPLETE_NORMALIZE_NFC ----> res
      * res ----> NFC ----> res

    ############################################################################
    # (2)   transliterations
    ############################################################################

    Unknown characters are silently ignored.

    ############################################################################
    # (2.1)   transliteration's method : "iso15919" : reciprocal functions
    ############################################################################

    transliterated string -> srcstring : the dependent vowel of a consonant is
    not set by dchar__init_from_translit_str() but by dstring__init_from_translit_str()
    Since "ka" isn't "कऄ" but "क" the choice of the right devanagari character
    belongs to a function able to analyze a string of characters, not a stand-alone
    character.

    ############################################################################
    # (2.1.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    ############################################################################

    These functions initialize a DStringSAN object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringSAN.init_from_transliteration()

    IN GENERAL :
    * DStringSAN().init_from_transliteration(src, method="iso15919") => iso15919.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterSAN.init_from_transliteration(method = "iso15919")
      => iso15919.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "ba" = base_char="b", dependent_vowel="a" ...)
    * PATTERN2 is a regex used to cut a string into some complex characters ( e.g : "bama" -> /ba/ + /ma/ )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringSAN().init_from_transliteration("ba", method="iso15919")

      * dchars/languages/san/transliterations/iso15919.py::dstring__init_from_translit_str(src="ba")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "iso15919")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * iso15919.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("ba")
                * element = re.match(PATTERN, src)
                * [...]
                    accent = element.group('accent')
                    if accent == '':
                        dchar.accent = None
                    else:
                        dchar.accent = DIACRITICS_INVERSED[accent]
                  [...]

    ############################################################################
    # (2.1.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterSAN object.
    This function is called by DCharacterSAN.get_transliteration(), this last function
    being called by DString.get_transliteration().

    * DString.get_transliteration :
      for dchar in self:
          res.append( dchar.get_transliteration(method = "iso15919") )

          * --------------------------------------------------------------------
          * dchar.get_transliteration(method = "iso15919") calls in fact
          * iso15919.py::dchar__get_translit_str(), id est :
          * --------------------------------------------------------------------
          * dchar__get_translit_str(dchar)

            * [...]
                if dchar.accent is not None:
                    res.append( DIACRITICS[dchar.accent] )

                if dchar.anudatta:
                    res.append( DIACRITICS['DEVANAGARI STRESS SIGN ANUDATTA'] )
              [...]

              res ----> NFC ---> res

    ############################################################################
    # (2.2)   transliteration's method : "itrans" : reciprocal functions
    ############################################################################

    ############################################################################
    # (2.2.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    ############################################################################

    These functions initialize a DStringSAN object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringSAN.init_from_transliteration()

    IN GENERAL :
    * DStringSAN().init_from_transliteration(src, method="itrans") => itrans.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterSAN.init_from_transliteration(method = "itrans")
      => itrans.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "ba" = base_char="b", dependent_vowel="a" ...)
    * PATTERN2 is a regex used to cut a string into some complex characters ( e.g : "bama" -> /ba/ + /ma/ )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringSAN().init_from_transliteration("ba", method="itrans")

      * dchars/languages/san/transliterations/itrans.py::dstring__init_from_translit_str(src="ba")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "itrans")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * itrans.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("ba")
                * element = re.match(PATTERN, src)
                * [...]
                    accent = element.group('accent')
                    if accent == '':
                        dchar.accent = None
                    else:
                        dchar.accent = DIACRITICS_INVERSED[accent]
                  [...]

    ############################################################################
    # (2.2.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterSAN object.
    This function is called by DCharacterSAN.get_transliteration(), this last function
    being called by DString.get_transliteration().

    * DString.get_transliteration :
      for dchar in self:
          res.append( dchar.get_transliteration(method = "itrans") )

          * --------------------------------------------------------------------
          * dchar.get_transliteration(method = "itrans") calls in fact
          * itrans.py::dchar__get_translit_str(), id est :
          * --------------------------------------------------------------------
          * dchar__get_translit_str(dchar)

            * [...]
               if dchar.anudatta:
                    res.append( DIACRITICS['DEVANAGARI STRESS SIGN ANUDATTA'] )

                if dchar.accent is not None:
                    res.append( DIACRITICS[dchar.accent] )
              [...]

    ############################################################################
    # (3)   exceptions
    ############################################################################

    As a module of the DChars project, the code may raise a DCharsError exception
    defined in dchars/errors/errors.py .
