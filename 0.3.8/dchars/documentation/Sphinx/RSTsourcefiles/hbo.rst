.. |br| raw:: html

   <br />

=========
HBO_TITLE
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
    DSTRING_HBO = new_dstring(language="עִבְֿרִיתֿ מִקְרָאִיתֿ")

    # -------------------------------------------
    # let's start with a Biblical Hebrew string :
    # -------------------------------------------
    # let's take the first sentence from Genesis :
    string = DSTRING_HBO("בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃")
    # is this DString object valid (i.e. no problem with the Biblical Hebrew string ?)
    print(string.validity)                  # -> True (no problem with the original text)
    # get the (default) transliteration :
    print(string.get_transliteration())     # -> "bərēʾši<HEBREW ACCENT TIPEHA>yṯ [...]"
    # what's the vowel of the first character ?
    print(string[0].vowel)                  # -> "HEBREW POINT SHEVA"
    # what's the consonant of the first character ?
    print(string[0].base_char)              # -> "ב"
    # has this consonant a "DAGHESH" point ?
    print(string[0].daghesh_mapiq)          # -> True
    # let's change the vowel of the first character from "HEBREW POINT SHEVA" to "HEBREW POINT HIRIQ" :
    string[0].vowel = "HEBREW POINT HIRIQ"
    # is the last character a punctuation sign ?
    print(string[-1].punctuation)           # -> True "׃" (SOF PASUQ)
    # the transliteration is now...
    print(string.get_transliteration())     # -> "birēʾši<HEBREW ACCENT TIPEHA>yṯ [...]"

    # --------------------------------------------------------------------------
    # now, let's use with a transliterated string (using the default method) :
    # --------------------------------------------------------------------------
    string = DSTRING_HBO().init_from_transliteration("ba")
    # we have a DSTRING_HBO object whose length is equal to one (one DCharacterHBO object) :
    print(len(string))                      # -> 1
    # let's change the consonant of the first (and unique) character from "בּ" to "ב" :
    string[0].daghesh_mapiq = False
    # the transliteration is now...
    print(string.get_transliteration())     # -> "ḇa"

-----------------------
TRANSLITERATION_METHODS
-----------------------

$TRANSLITERATION_METHODS_TXT$

BASIC_METHOD
--------------

$BASIC_METHOD_TXT$

.. code-block:: none

    * (Genesis, I.1) :
      בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃
      bərēʾši<HEBREW ACCENT TIPEHA>yṯ bārā<HEBREW ACCENT MUNAH>ʾ ʾĕlōhi<HEBREW ACCENT ETNAHTA>ym ʾē<HEBREW ACCENT MERKHA>ṯ haŠāma<HEBREW ACCENT TIPEHA>yim wəʾē<HEBREW ACCENT MERKHA>ṯ hāʾā|reṣ:

    * transliterated characters defining one DCharacterHBO are defined in this order : base_char | vowel | methegh | raphe | special points | cantillation_mark
      (confer hbo/transliterations/basic.py::PATTERN)
      E.g. : "ba|-" for ba + methegh + raphe

-------------
POSSIBILITIES
-------------

$POSSIBILITIES_TXT$

.. code-block:: none

    * some diacritics are normally used only with some consonants (e.g. "HEBREW POINT HOLAM HASER FOR VAV")
      but the code DOESN'T CHECK IF THESE DIACRITICS ARE CORRECTLY USED !
    * the module reads 05D0 and 2135 ('א' and 'ℵ'), 05D1 and 2136 ('ב' and 'ℶ'), 05D2 and 2137 ('ג' and 'ℷ')
      as equivalent characters but writes only the expected characters 'א','ב','ג'
      (confer dchars/languages/hbo/symbols.py::SYMB_LETTERS)
    * all cantillation marks defined by the Unicode norm are known
    * a DCharacterHBO can have zero, one or two cantilation marks (see Psalm 18.12 for a character with two cantilation marks)
    * a DCharacterHBO object doesn't differentiate between a daghesh dot and a mapiq dot
    * alternative characters defined in http://www.unicode.org/charts/PDF/UFB00.pdf,
      from FB2A שׁ HEBREW LETTER SHIN WITH SHIN DOT to FB4E פֿ HEBREW LETTER PE WITH RAFE
      are read and used as output characters by this module.

    * a DCharacterHBO is defined by the following attributes (confer dchars/languages/hbo/dchars.py::DCharacterHBO.__init__) :
      * unknown_char                    : bool
      * base_char                       : None or a string
      * contextual_form                 : None or a string ("initial+medium+final", "final")
      * punctuation                     : True, False
      * shin_sin_dot                    : None or a string ("HEBREW POINT SHIN DOT", "HEBREW POINT SIN DOT")
      * daghesh_mapiq                   : bool
      * methegh                         : bool
      * specialpoints                   : None or a string ("HEBREW MARK UPPER DOT", "HEBREW MARK LOWER DOT")
      * vowel                           : None or string like 'HEBREW POINT SHEVA' (see symbols.py::SYMB_VOWELS)
      * raphe                           : bool
      * cantillation_mark               : None or a list of strings (see symbols.py::SYMB_CANTILLATION_MARKS)

------------
HOW_IT_WORKS
------------

$HOW_IT_WORKS_TXT$

.. code-block:: none

    ############################################################################
    #
    # (0)   general remarks on DStringHBO and DCharacterHBO
    #
    # (1)   reciprocal functions : DStringHBO.init_from_str <> DStringHBO.get_sourcestr_representation
    # (1.1) DStringHBO.init_from_str('א')
    # (1.2) DStringHBO.get_sourcestr_representation()
    #
    # (2)   transliteration
    #
    # (2.1)   transliteration's method : "basic" : reciprocal functions
    # (2.1.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.1.2) dchar__get_translit_str()
    #
    # (3)   exceptions
    #
    ############################################################################

    ABBREVIATIONS :
    * NFC = unicodedata.normalize('NFC', string)
    * NFD = unicodedata.normalize('NFD', string)

    ############################################################################
    # (0)   general remarks on DStringHBO and DCharacterHBO
    ############################################################################

    * From a string like 'א' you can build a DStringHBO object by writing :
    string = DStringHBO('א'); you modify this object and then you get the
    corresponding string by calling DStringHBO.get_sourcestr_representation()
    * You can initialize a DStringHBO with a transliterated string :
    DStringHBO().init_from_transliteration("ba"); you can modify this
    object and then you get the new transliterated string by calling
    DStringHBO.get_the_transliteration().

    * A DStringHBO is an object derived from DString, i.e. a list of DCharacterHBO
    objects. You can access a DStringHBO as a list made of characters.
    * A DStringHBO object has the (bool)".validity" attribute set to False if
    something is wrong after a call to DStringHBO.init_from_str(); in this
    case the (list)".errors" attribute contains some informations about the error.
    * CAVEAT : THE "validity" ATTRIBUTE IS NOT SET AFTER A CALL TO
    DStringHBO.init_from_transliteration()

    * use print(string) or print(str(string)) to display the original text in a
    DStringHBO object and print(repr(string)) to get the very detailed informations
    about the string.

    * to initialize a DStringHBO object you need :
      * either a source-string like "בְּרֵאשִׁ֖ית" : DStringHBO("בְּרֵאשִׁ֖ית").
        Conversely, you can get this source-string by a call to the function
        DStringHBO.get_sourcestr_representation().
        * you have the identities :
              DStringHBO.get_sourcestr_representation( DStringHBO( src ) ) = src
          and DStringHBO( DStringHBO.get_sourcestr_representation (src ) ) = src

          ONLY FOR A SUBSET OF THE CHARACTERS AVAILABLE. See the documentation and
          the code to see which characters can do that; typically this module
          uses compact unicode characters when they exist : these characters should
          be prefered to the (uncompact) compounds of characters.
          This identities are controlled in the test files by the functions named
          test_from_srcstr_2_srcstr().

      * either a transliterated string like "bərēʾši" (see below the format of this
        string, depending to the choosed transliterations's method), by calling :
        DStringHBO().init_from_transliteration("bərēʾši"). Conversely you can
        get the transliterated string by calling DStringHBO.get_the_transliteration()

    ############################################################################
    # (1)   reciprocal functions : DStringHBO.init_from_str <> DStringHBO.get_sourcestr_representation
    ############################################################################

    * characters are divided into SYMB_LETTERS, SYMB_OTHER_SYMBOLS, SYMB_PUNCTUATION,
      SYMB_VOWELS, SYMB_POINTS, SYMB_SPECIAL_POINTS and SYMB_CANTILLATION_MARKS.

    * dchars/languages/hbo/symbols.py::SYMB_LETTERS, SYMB_VOWELS, ... are Name2Symbols

    * dchars/languages/hbo/dchars.py::stringHBO.pattern = re.compile("((?P<basechar>{0})(?P<diacritics>({1})*))

      * pattern_basechar = SYMB_LETTERS + SYMB_OTHER_SYMBOLS + SYMB_PUNCTUATION
      * pattern_diacritics = SYMB_VOWELS + SYMB_POINTS + SYMB_SPECIALPOINTS + SYMB_CANTILLATION_MARKS

    * As expected with reciprocal function, we have init_from_str( get_sourcestr_representation( src ) ) = src
    and get_sourcestr_representation( init_from_str( src ) ) = src if src is made of certain characters.

    ############################################################################
    # (1.1) DStringHBO.init_from_str('א')
    ############################################################################

    This function initializes a DStringHBO object from a string.

    * DStringHBO('א')

      * DStringHBO.init_from_str('א')
        * src ---> NFD -----> src
        * for element in re.finditer(DStringHBO.pattern, src)
          * new_character = DCharacterHBO(unknown_char = False,
                                          base_char = base_char,
                                          contextual_form = contextual_form,
                                          punctuation = punctuation,
                                          shin_sin_dot = shin_sin_dot,
                                          daghesh_mapiq = daghesh_mapiq,
                                          methegh = methegh,
                                          specialpoints = specialpoints,
                                          vowel = vowel,
                                          raphe = raphe,
                                          cantillation_mark = cantillation_mark)

    ############################################################################
    # (1.2) DStringHBO.get_sourcestr_representation()
    ############################################################################

    This function gives the representation string corresponding to a DStringHBO object.

    * DStringHBO.get_sourcestr_representation('א')
      * [...]
        if self.base_char is not None:
            res.append( self.base_char )

        if self.shin_sin_dot is not None:
            res.append( SYMB_POINTS.get_default_symbol(self.shin_sin_dot) )

        [...]
      * res ----> COMPLETE_NORMALIZE_NFC ---> res

    ############################################################################
    # (2)   transliterations
    ############################################################################

    Unknown characters are silently ignored.

    ############################################################################
    # (2.1)   transliteration's method : "basic" : reciprocal functions
    ############################################################################

    ############################################################################
    # (2.1.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    ############################################################################

    These functions initialize a DStringHBO object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringHBO.init_from_transliteration()

    IN GENERAL :
    * DStringHBO().init_from_transliteration(src, method="basic") => basic.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterHBO.init_from_transliteration(method = "basic")
      => basic.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "ba" = base_char="b", vowel="a", methegh=False, ...)
    * PATTERN2 is a regex used to cut a string into some complex characters ( e.g : "bama" -> /ba/ + /ma/ )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringHBO().init_from_transliteration("ba", method="basic")

      * dchars/languages/hbo/transliterations/basic.py::dstring__init_from_translit_str(src="ba")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "basic")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * basic.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("ba")
                * element = re.match(PATTERN, src)
                * [...]
                  dchar.methegh = element.group('trans_methegh') != ""
                  dchar.raphe = element.group('trans_raphe') != ""
                  [...]

    ############################################################################
    # (2.1.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterHBO object.
    This function is called by DCharacterHBO.get_transliteration(), this last function
    being called by DString.get_transliteration().

    * DString.get_transliteration :
      for dchar in self:
          res.append( dchar.get_transliteration(method = "basic") )

          * --------------------------------------------------------------------
          * dchar.get_transliteration(method = "basic") calls in fact
          * basic.py::dchar__get_translit_str(), id est :
          * --------------------------------------------------------------------
          * dchar__get_translit_str(dchar)

            * [...]
              if dchar.vowel is not None:
                  res.append( VOWELS[dchar.vowel] )

              if dchar.methegh:
                res.append( POINTS["HEBREW POINT METEG"] )

              if dchar.raphe:
                res.append( POINTS["HEBREW POINT RAFE"] )
              [...]

    ############################################################################
    # (3)   exceptions
    ############################################################################

    As a module of the DChars project, the code may raise a DCharsError exception
    defined in dchars/errors/errors.py .
