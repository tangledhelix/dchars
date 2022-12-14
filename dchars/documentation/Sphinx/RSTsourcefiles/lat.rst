.. |br| raw:: html

   <br />

=========
LAT_TITLE
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
    DSTRING_LAT = new_dstring(language="latīna")

    # -------------------------------------------
    # let's start with a Latin string :
    # -------------------------------------------
    # let's take the first sentence from Cicero's Ōrātiō in Catilīnam :
    string = DSTRING_LAT("Quō usque tandem abūtēre, Catilīna, patientiā nostrā?")
    # is this DString object valid (i.e. no problem with the Latin string ?)
    print(string.validity)                  # -> True (no problem with the original text)
    # get the (default) transliteration :
    print(string.get_transliteration())     # -> "Quo_ usque tandem abu_te_re, [...]"
    # is there a stress accent on the character number #11 ?
    print(string[11].stress)                # -> False
    # what's the basic character of the character number #0 ?
    print(string[0].base_char)              # -> "Q"
    # let's add a stress accent on the character number #11 :
    string[11].stress = True
    print(string)                           # -> "Quō usque tándem [...] :

    # is the last character a punctuation sign ?
    print(string[-1].punctuation)           # -> True, since we read "?".

    # --------------------------------------------------------------------------
    # now, let's use with a transliterated string (using the default method) :
    # --------------------------------------------------------------------------
    string = DSTRING_LAT().init_from_transliteration("Ro_ma")
    # we have a DSTRING_LAT object whose length is equal to 4 (4 DCharacterLAT objects) :
    print(len(string), string)              # -> 4
    # let's add the vowels' quantity :
    string[1].length = "short"
    string[-1].length = "long"
    # the string we get is now...
    print(string)                           # -> "Rŏmā"
    print(string.get_transliteration())     # -> "Ro*ma_"

-----------------------
TRANSLITERATION_METHODS
-----------------------

$TRANSLITERATION_METHODS_TXT$

BASIC_METHOD
--------------

$BASIC_METHOD_TXT$

.. code-block:: none

    * Ōrātiō in Catilīnam, I :
      Quō usque tandem abūtēre, Catilīna, patientiā nostrā? quam diū etiam furor iste tuus nōs ēlūdet? quem ad fīnem sēsē effrēnāta jactābit audācia?
      Quo_ usque tandem abu_te_re, Catili_na, patientia_ nostra_? quam diu_ etiam furor iste tuus no_s e_lu_det? quem ad fi_nem se_se_ effre_na_ta jacta_bit auda_cia?

    * transliterated characters defining one DCharacterLAT are defined in this order : base_char | stress | length | diaeresis
      (confer lat/transliterations/basic.py::PATTERN)
      E.g. : "a/_+" for "ǟ́"

-------------
POSSIBILITIES
-------------

$POSSIBILITIES_TXT$

.. code-block:: none

    * the module knows how to handle diaeresis.
    * Vowels' length can be defined as "long"(ā), "short"(ŏ) or None(a,o)

    * a DCharacterLAT is defined by the following attributes (confer dchars/languages/lat/dchars.py::DCharacterLAT.__init__) :
      * unknown_char                    : bool
      * base_char                       : None or a string
      * punctuation                     : True, False
      * capital_letter                  : True, False
      * length                          : None or a string ("short", "long")
      * stress                          : bool
      * diaeresis                       : bool

------------
HOW_IT_WORKS
------------

$HOW_IT_WORKS_TXT$

.. code-block:: none

    ############################################################################
    #
    # (0)   general remarks on DStringLAT and DCharacterLAT
    #
    # (1)   reciprocal functions : DStringLAT.init_from_str <> DStringLAT.get_sourcestr_representation
    # (1.1) DStringLAT.init_from_str("Rōma")
    # (1.2) DStringLAT.get_sourcestr_representation()
    #
    # (2)   transliterations
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
    # (0)   general remarks on DStringLAT and DCharacterLAT
    ############################################################################

    * From a string like "Rōma" you can build a DStringHBO object by writing :
    string = DStringHBO("Rōma"); you modify this object and then you get the
    corresponding string by calling DStringHBO.get_sourcestr_representation()
    * You can initialize a DStringHBO with a transliterated string :
    DStringHBO().init_from_transliteration("Ro_ma"); you can modify this
    object and then you get the new transliterated string by calling
    DStringHBO.get_the_transliteration().

    * A DStringLAT is an object derived from DString, i.e. a list of DCharacterLAT
    objects. You can access a DStringLAT as a list made of characters.
    * A DStringLAT object has the (bool)".validity" attribute set to False if
    something is wrong after a call to DStringLAT.init_from_str(); in this
    case the (list)".errors" attribute contains some informations about the error.
    * CAVEAT : THE "validity" ATTRIBUTE IS NOT SET AFTER A CALL TO
    DStringLAT.init_from_transliteration()

    * use print(string) or print(str(string)) to display the original text in a
    DStringLAT object and print(repr(string)) to get the very detailed informations
    about the string.

    * to initialize a DStringLAT object you need :
      * either a source-string like "abūtēre" : DStringLAT("abūtēre").
        Conversely, you can get this source-string by a call to the function
        DStringLAT.get_sourcestr_representation().
        * you have the identities :
              DStringLAT.get_sourcestr_representation( DStringLAT( src ) ) = src
          and DStringLAT( DStringLAT.get_sourcestr_representation (src ) ) = src

          ONLY FOR A SUBSET OF THE CHARACTERS AVAILABLE. See the documentation and
          the code to see which characters can do that; typically this module
          uses compact unicode characters when they exist : these characters should
          be prefered to the (uncompact) compounds of characters.
          This identities are controlled in the test files by the functions named
          test_from_srcstr_2_srcstr().

      * either a transliterated string like "abu_te_re" (see below the format of this
        string, depending to the choosed transliterations's method), by calling :
        DStringLAT().init_from_transliteration("abu_te_re"). Conversely you can
        get the transliterated string by calling DStringLAT.get_the_transliteration()

    ############################################################################
    # (1)   reciprocal functions : DStringLAT.init_from_str <> DStringLAT.get_sourcestr_representation
    ############################################################################

    * characters are divided into SYMB_UPPER_CASE, SYMB_LOWER_CASE, SYMB_PUNCTUATION, SYMB_DIACRITICS

    * dchars/languages/lat/symbols.py::SYMB_UPPER_CASE, SYMB_LOWER_CASE, ... ... are Name2Symbols

    * dchars/languages/lat/dchars.py::stringLAT.pattern = re.compile("((?P<letter>{0})(?P<diacritics>({1})*))

      * pattern_letters = SYMB_UPPER_CASE, SYMB_LOWER_CASE, SYMB_PUNCTUATION
      * pattern_diacritics = SYMB_DIACRITICS

    * As expected with reciprocal function, we have init_from_str( get_sourcestr_representation( src ) ) = src
    and get_sourcestr_representation( init_from_str( src ) ) = src if src is made of certain characters.

    ############################################################################
    # (1.1) DStringLAT.init_from_str("Rōma")
    ############################################################################

    This function initializes a DStringLAT object from a string.

    * DStringLAT("Rōma")

      * DStringLAT.init_from_str("Rōma")
        * src ---> NFD -----> src
        * for element in re.finditer(DStringLAT.pattern, src)
          * new_character = DCharacterLAT(unknown_char = False,
                                          base_char = base_char,
                                          punctuation = punctuation,
                                          capital_letter = capital_letter,
                                          length = length,
                                          stress = stress,
                                          diaeresis = diaeresis)

    ############################################################################
    # (1.2) DStringLAT.get_sourcestr_representation()
    ############################################################################

    This function gives the representation string corresponding to a DStringLAT object.

    * DStringLAT.get_sourcestr_representation("Rōma")
      * [...]
        if self.stress:
            res.append( SYMB_DIACRITICS.get_default_symbol('stress' ) )

        if self.length == 'short' or self.length == 'long':
            res.append( SYMB_DIACRITICS.get_default_symbol(self.length) )


        [...]
      * res ----> NFC ----> res

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

    These functions initialize a DStringLAT object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringLAT.init_from_transliteration()

    IN GENERAL :
    * DStringLAT().init_from_transliteration(src, method="basic") => basic.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterLAT.init_from_transliteration(method = "basic")
      => basic.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "á" = base_char="a", stress=True, ...)
    * PATTERN2 is a regex used to cut a string into some complex characters ( e.g : "bá" -> /b/ + /á/ )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringLAT().init_from_transliteration("ba", method="basic")

      * dchars/languages/lat/transliterations/basic.py::dstring__init_from_translit_str(src="á")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "basic")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * basic.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("á")
                * element = re.match(PATTERN, src)
                * [...]
                  dchar.stress = element.group('trans_stress') != ''
                  dchar.diaeresis = element.group('trans_diaeresis') != ''
                  [...]

    ############################################################################
    # (2.1.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterLAT object.
    This function is called by DCharacterLAT.get_transliteration(), this last function
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
              if dchar.stress:
                  res.append( DIACRITICS['stress'] )

              if dchar.length is not None:
                  res.append( DIACRITICS[dchar.length] )

              if dchar.diaeresis:
                  res.append( DIACRITICS['diaeresis'] )
              [...]

    ############################################################################
    # (3)   exceptions
    ############################################################################

    As a module of the DChars project, the code may raise a DCharsError exception
    defined in dchars/errors/errors.py .
