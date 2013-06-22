.. |br| raw:: html

   <br />

=========
GRC_TITLE
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
    DSTRING_GRC = new_dstring(language="Ἑλληνικὴ γλῶττα")

    # ------------------------------------------
    # let's start with an Ancient Greek string :
    # ------------------------------------------
    # let's take the first verse from Iliad :
    string = DSTRING_GRC("μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος")
    # is this DString object valid (i.e. no problem with the Ancient Hebrew string ?)
    print(string.validity)                  # -> True : no problem

    # get the (default) transliteration :
    print(string.get_transliteration())     # -> "m/\ênin )/aeide the\a Pêlêi:/adeô )Akhil/\êos"

    # is there a stress accent on the character number #1 ?
    print(string[1].tonos)                  # -> "περισπωμένη"
    # what's the basic character of the character number #1 ?
    print(string[1].base_char)              # -> "η"
    # # let's modify the stress accent on the character number #1 :
    string[1].tonos = "ὀξεῖα"
    print(string)                           # -> "μήνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"

    # is the last character a punctuation sign ?
    print(string[-1].punctuation)           # -> False, since we have a final sigma

    # ----------------------------------------
    # let's use another Ancient Greek string :
    # ----------------------------------------
    # we build the relative pronoun (dative, singular, m/n) :
    string = DSTRING_GRC("ω")
    string[0].tonos = "περισπωμένη"
    string[0].pneuma = "δασὺ"
    string[0].hypogegrammene = True
    print(string)                          # -> "ᾧ"

    # ------------------------------------------------------------------------
    # now, let's use with a transliterated string (using the default method) :
    # ------------------------------------------------------------------------
    string = DSTRING_GRC().init_from_transliteration("m/\ênin")
    # we have a DSTRING_GRC object whose length is equal to 5 (5 DCharacterGRC objects) :
    print(len(string), string)              # -> 5
    # let's add two characters : space + ἄ
    string += DSTRING_GRC(" ἄ")
    # the string we get is now...
    print(string)                           # -> "μῆνιν ἄ"
    print(string.get_transliteration())     # -> "m/\ênin )/a"

-----------------------
TRANSLITERATION_METHODS
-----------------------

$TRANSLITERATION_METHODS_TXT$

BASIC_METHOD
------------

$BASIC_METHOD_TXT$

.. code-block:: none

    * Hippocrates, De aere aquis et locis, I.1 :
      "ἰητρικὴν ὅστις βούλεται ὀρθῶς ζητεῖν, τάδε χρὴ ποιεῖν: πρῶτον μὲν ἐνθυμεῖσθαι τὰς ὥρας τοῦ ἔτεος, ὅ τι δύναται ἀπεργάζεσθαι ἑκάστη:"
      ")iêtrik\ên (/ostis bo/uletai )orth/\ôs zête/\in, t/ade khr\ê poie/\in: pr/\ôton m\en )enthume/\isthai t\as (/ôras to/\u )/eteos, (/o ti d/unatai )aperg/azesthai (ek/astê:"

    * transliterated characters defining one DCharacterGRC are defined in this order : pneuma|tonos|base_char|hypogegrammene|dialutika|mekos
      (confer grc/transliterations/basic.py::PATTERN)
      E.g. : "/\\u:_" for "ῧ̄"

    * upper case and lower case are distinguished this way : "δ" = "d' and "Δ" = "D"

BETACODE_METHOD
---------------

$BETACODE_METHOD_TXT$

.. code-block:: none

    * Hippocrates, De aere aquis et locis, I.1 :
      "ἰητρικὴν ὅστις βούλεται ὀρθῶς ζητεῖν, τάδε χρὴ ποιεῖν: πρῶτον μὲν ἐνθυμεῖσθαι τὰς ὥρας τοῦ ἔτεος, ὅ τι δύναται ἀπεργάζεσθαι ἑκάστη:"
      "I)HTRIKH\N O(/STIS BOU/LETAI O)RQW=S ZHTEI=N, TA/DE XRH\ POIEI=N:: PRW=TON ME\N E)NQUMEI=SQAI TA\S W(/RAS TOU= E)/TEOS, O(/ TI DU/NATAI A)PERGA/ZESQAI E(KA/STH::"

    * transliterated characters defining one DCharacterGRC are defined in this order : *|base_char|pneuma|tonos|hypogegrammene|dialutika|mekos
      (confer grc/transliterations/betacode.py::PATTERN)
      E.g. : "*(=W|" for "ᾯ"

    * upper case and lower case are distinguished this way : "δ" = "D' and "Δ" = "*D"

PERSEUS_METHOD
--------------

$PERSEUS_METHOD_TXT$

.. code-block:: none

    * Hippocrates, De aere aquis et locis, I.1 :
      "ἰητρικὴν ὅστις βούλεται ὀρθῶς ζητεῖν, τάδε χρὴ ποιεῖν: πρῶτον μὲν ἐνθυμεῖσθαι τὰς ὥρας τοῦ ἔτεος, ὅ τι δύναται ἀπεργάζεσθαι ἑκάστη:"
      "i)htrikh\n o(/stis bou/letai o)rqw=s zhtei=n, ta/de xrh\ poiei=n: prw=ton me\n e)nqumei=sqai ta\s w(/ras tou= e)/teos, o(/ ti du/natai a)perga/zesqai e(ka/sth:"

    * transliterated characters defining one DCharacterGRC are defined in this order : *|base_char|pneuma|tonos|hypogegrammene|dialutika|mekos
      (confer grc/transliterations/perseus.py::PATTERN)
      E.g. : "*(=w|" for "ᾯ"

    * upper case and lower case are distinguished this way : "δ" = "d' and "Δ" = "*d"

-------------
POSSIBILITIES
-------------

$POSSIBILITIES_TXT$

.. code-block:: none


    * the module knows how to handle diaeresis : see dialutika below
    * some equivalent characters are accepted : e.g. 'ϑ' for 'θ'
      (see san/symbols.py::SYMB_LOWER_CASE and SYMB_UPPER_CASE)

    * a DCharacterGRC is defined by the following attributes (confer dchars/languages/grc/dchars.py::DCharacterGRC.__init__) :
      * unknown_char                    : bool
      * base_char                       : None or a string
      * contextual_form                 : None or a string ("initial+medium+final"+"initial", "initial+medium", "final", "medium+final")
      * punctuation                     : True, False
      * capital_letter                  : True, False
      * mekos(μῆκος)                    : None, "βραχύ", "μακρόν"
      * tonos(τόνος)                    : None, "ὀξεῖα", "βαρεῖα", "περισπωμένη"
      * pneuma(πνεῦμα)                  : None, "ψιλὸν", "δασὺ"
      * hypogegrammene(ὑπογεγραμμένη)   : True, False
      * dialutika(διαλυτικά)            : True, False

------------
HOW_IT_WORKS
------------

$HOW_IT_WORKS_TXT$

.. code-block:: none

    ############################################################################
    #
    # (0)   general remarks on DStringGRC and DCharacterGRC
    #
    # (1)   reciprocal functions : DStringGRC.init_from_str <> DStringGRC.get_sourcestr_representation
    # (1.1) DStringGRC.init_from_str("Ἀχιλῆος")
    # (1.2) DStringGRC.get_sourcestr_representation()
    #
    # (2)   transliterations
    #
    # (2.1)   transliteration's method : "basic" : reciprocal functions
    # (2.1.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.1.2) dchar__get_translit_str()
    #
    # (2.2)   transliteration's method : "betacode" : reciprocal functions
    # (2.2.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.2.2) dchar__get_translit_str()
    #
    # (2.3)   transliteration's method : "perseus" : reciprocal functions
    # (2.3.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    # (2.3.2) dchar__get_translit_str()
    #
    # (3)   exceptions
    #
    ############################################################################

    ABBREVIATIONS :
    * NFC = unicodedata.normalize('NFC', string)
    * NFD = unicodedata.normalize('NFD', string)

    ############################################################################
    # (0)   general remarks on DStringGRC and DCharacterGRC
    ############################################################################

    * From a string like "Ἀχιλῆος" you can build a DStringGRC object by writing :
    string = DStringGRC("Ἀχιλῆος"); you modify this object and then you get the
    corresponding string by calling DStringGRC.get_sourcestr_representation()
    * You can initialize a DStringGRC with a transliterated string :
    DStringGRC().init_from_transliteration("ba"); you can modify this
    object and then you get the new transliterated string by calling
    DStringGRC.get_the_transliteration().

    * A DStringGRC is an object derived from DString, i.e. a list of DCharacterGRC
    objects. You can access a DStringGRC as a list made of characters.
    * A DStringGRC object has the (bool)".validity" attribute set to False if
    something is wrong after a call to DStringGRC.init_from_str(); in this
    case the (list)".errors" attribute contains some informations about the error.
    * CAVEAT : THE "validity" ATTRIBUTE IS NOT SET AFTER A CALL TO
    DStringGRC.init_from_transliteration()

    * use print(string) or print(str(string)) to display the original text in a
    DStringGRC object and print(repr(string)) to get the very detailed informations
    about the string.

    * to initialize a DStringGRC object you need :
      * either a source-string like "Ἀχιλῆος" : DStringGRC("Ἀχιλῆος").
        Conversely, you can get this source-string by a call to the function
        DStringGRC.get_sourcestr_representation().
        * you have the identities :
              DStringGRC.get_sourcestr_representation( DStringGRC( src ) ) = src
          and DStringGRC( DStringGRC.get_sourcestr_representation (src ) ) = src

          ONLY FOR A SUBSET OF THE CHARACTERS AVAILABLE. See the documentation and
          the code to see which characters can do that; typically this module
          uses compact unicode characters when they exist : these characters should
          be prefered to the (uncompact) compounds of characters.
          This identities are controlled in the test files by the functions named
          test_from_srcstr_2_srcstr().

      * either a transliterated string like "poiei=n:" (see below the format of this
        string, depending to the choosed transliterations's method), by calling :
        DStringGRC().init_from_transliteration("poiei=n:"). Conversely you can
        get the transliterated string by calling DStringGRC.get_the_transliteration()

    ############################################################################
    # (1)   reciprocal functions : DStringGRC.init_from_str <> DStringGRC.get_sourcestr_representation
    ############################################################################

    * characters are divided into SYMB_LOWER_CASE, SYMB_UPPER_CASE, SYMB_OTHER_SYMBOLS,
      SYMB_PUNCTUATION and SYMB_DIACRITICS.

    * dchars/languages/grc/symbols.py::SYMB_LOWER_CASE, SYMB_UPPER_CASE, ... are Name2Symbols

    * dchars/languages/grc/dchars.py::stringGRC.pattern = re.compile("((?P<basechar>{0})(?P<diacritics>({1})*))

      * pattern_basechar = SYMB_LOWER_CASE, SYMB_UPPER_CASE, SYMB_OTHER_SYMBOLS + SYMB_PUNCTUATION
      * pattern_diacritics = SYMB_DIACRITICS

    * As expected with reciprocal function, we have init_from_str( get_sourcestr_representation( src ) ) = src
    and get_sourcestr_representation( init_from_str( src ) ) = src if src is made of certain characters.

    ############################################################################
    # (1.1) DStringGRC.init_from_str("Ἀχιλῆος")
    ############################################################################

    This function initializes a DStringGRC object from a string.

    * DStringGRC("Ἀχιλῆος")

      * DStringGRC.init_from_str("Ἀχιλῆος")
        * src ---> NFD -----> src
        * for element in re.finditer(DStringGRC.pattern, src)
          * new_character = DCharacterGRC(unknown_char = False,
                                          base_char = base_char,
                                          contextual_form = contextual_form,
                                          punctuation = punctuation,
                                          capital_letter = capital_letter,
                                          tonos = tonos,
                                          pneuma = pneuma,
                                          hypogegrammene = hypogegrammene,
                                          dialutika = dialutika,
                                          mekos=mekos)


    ############################################################################
    # (1.2) DStringGRC.get_sourcestr_representation()
    ############################################################################

    This function gives the representation string corresponding to a DStringGRC object.

    * DStringGRC.get_sourcestr_representation("Ἀχιλῆος")
      * [...]
        if self.mekos == 'βραχύ':
            res.append( SYMB_DIACRITICS.get_default_symbol('μῆκος.βραχύ') )
        elif self.mekos == 'μακρόν':
            res.append( SYMB_DIACRITICS.get_default_symbol('μῆκος.μακρόν') )

        if self.hypogegrammene == True:
            res.append( SYMB_DIACRITICS.get_default_symbol('ὑπογεγραμμένη') )

        if self.dialutika == True:
            res.append( SYMB_DIACRITICS.get_default_symbol('διαλυτικά') )
        [...]
      * res ----> NFC ----> res
      * res --> COMPLETE_NORMALIZE_NFC --> res (we help NFC in some difficult
        cases)

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

    These functions initialize a DStringGRC object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringGRC.init_from_transliteration()

    IN GENERAL :
    * DStringGRC().init_from_transliteration(src, method="basic") => basic.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterGRC.init_from_transliteration(method = "basic")
      => basic.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "a/" = base_char="α", tonos="περισπωμένη", ...)
    * PATTERN2 is a regex used to cut a string into some complex characters ( e.g : "ba/ma" -> "b" + "a/" + "m" +"a" )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringGRC().init_from_transliteration("ba", method="basic")

      * dchars/languages/grc/transliterations/basic.py::dstring__init_from_translit_str(src="ba")
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
                  dchar.hypogegrammene = element.group('trans_hypogegrammene') != ''
                  dchar.dialutika = element.group('trans_dialutika') != ''
                  [...]

    ############################################################################
    # (2.1.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterGRC object.
    This function is called by DCharacterGRC.get_transliteration(), this last function
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
              if dchar.unknown_char:
                  res.append( TRANS__UNKNOWN_CHARACTER )

              if dchar.pneuma is not None:
                  res.append( DIACRITICS[dchar.pneuma] )

              if dchar.tonos is not None:
                  res.append( DIACRITICS[dchar.tonos] )
              [...]

    ############################################################################
    # (2.2)   transliteration's method : "betacode" : reciprocal functions
    ############################################################################

    ############################################################################
    # (2.2.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    ############################################################################

    These functions initialize a DStringGRC object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringGRC.init_from_transliteration()

    IN GENERAL :
    * DStringGRC().init_from_transliteration(src, method="betacode") => betacode.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterGRC.init_from_transliteration(method = "betacode")
      => betacode.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "A/" = base_char="α", tonos="περισπωμένη", ...)
    * PATTERN is a regex used to cut a string into some complex characters
      ( e.g : "BA/MA" -> "B" + "A/" + "M" +"A" )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringGRC().init_from_transliteration("BA", method="betacode")

      * dchars/languages/grc/transliterations/betacode.py::dstring__init_from_translit_str(src="BA")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "betacode")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * betacode.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("BA")
                * element = re.match(PATTERN, src)
                * [...]
                  dchar.hypogegrammene = element.group('trans_hypogegrammene') != ''
                  dchar.dialutika = element.group('trans_dialutika') != ''
                  [...]

    ############################################################################
    # (2.2.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterGRC object.
    This function is called by DCharacterGRC.get_transliteration(), this last function
    being called by DString.get_transliteration().

    * DString.get_transliteration :
      for dchar in self:
          res.append( dchar.get_transliteration(method = "betacode") )

          * --------------------------------------------------------------------
          * dchar.get_transliteration(method = "betacode") calls in fact
          * betacode.py::dchar__get_translit_str(), id est :
          * --------------------------------------------------------------------
          * dchar__get_translit_str(dchar)

            * [...]
                if dchar.unknown_char:
                    res.append( TRANS__UNKNOWN_CHARACTER )

                else:

                    if dchar.punctuation:
                        # punctuation :
                        res.append( PUNCTUATION[dchar.base_char] )

                    elif dchar.base_char in OTHER_SYMBOLS:
                        res.append( OTHER_SYMBOLS[dchar.base_char] )

                    else:

                        if dchar.capital_letter:
                            # upper case letter :
                            res.append( '*' )

                            if dchar.pneuma is not None:
                                res.append( DIACRITICS[dchar.pneuma] )
                            [...]

                        else:
                            # lower case letter :
                            res.append( LOWER_CASE[dchar.base_char] )

                            if dchar.pneuma is not None:
                                res.append( DIACRITICS[dchar.pneuma] )
                            [...]


                        if dchar.hypogegrammene == True:
                            res.append( DIACRITICS['ὑπογεγραμμένη'] )

                        if dchar.dialutika == True:
                            res.append( DIACRITICS['διαλυτικά'] )

                        if dchar.mekos is not None:
                            res.append( DIACRITICS[dchar.mekos] )
              [...]

    ############################################################################
    # (2.3)   transliteration's method : "perseus" : reciprocal functions
    ############################################################################

    ############################################################################
    # (2.3.1) dstring__init_from_translit_str(), dchar__init_from_translit_str()
    ############################################################################

    These functions initialize a DStringGRC object from a transliterated string.
    The function dstring__init_from_translit_str() is called by DStringGRC.init_from_transliteration()

    IN GENERAL :
    * DStringGRC().init_from_transliteration(src, method="perseus") => perseus.py::dstring__init_from_translit_str
    * ... calling for each character DCharacterGRC.init_from_transliteration(method = "perseus")
      => perseus.py::dchar__init_from_translit_str()

    IN DETAILS :
    * PATTERN is a regex used to cut one complex character into its element
      ( "a/" = base_char="α", tonos="περισπωμένη", ...)
    * PATTERN is a regex used to cut a string into some complex characters
      ( e.g : "ba/ma" -> "b" + "a/" + "m" +"a" )
    * TRANS_EQUIVALENCES is a list of substitutions for the transliterated strings, if we want to treat
      similarly two different transliterated strings.

    * DStringGRC().init_from_transliteration("ba", method="perseus")

      * dchars/languages/grc/transliterations/perseus.py::dstring__init_from_translit_str(src="ba")
        * src ---> TRANS_EQUIVALENCES ---> src
        * for element in re.finditer(PATTERN2, _src):
              string = element.string[element.start():element.end()]
              new_character = dcharactertype().init_from_transliteration(string, "perseus")

              * -----------------------------------------------------------------
              * dcharactertype().init_from_transliteration calls in fact
              * perseus.py::dchar__init_from_translit_str(), id est :
              * -----------------------------------------------------------------
              * dchar__init_from_trans_lstring("ba")
                * element = re.match(PATTERN, src)
                * [...]
                  dchar.hypogegrammene = element.group('trans_hypogegrammene') != ''
                  dchar.dialutika = element.group('trans_dialutika') != ''
                  [...]

    ############################################################################
    # (2.3.2) dchar__get_translit_str()
    ############################################################################

    This function gives the representation string corresponding to a DCharacterGRC object.
    This function is called by DCharacterGRC.get_transliteration(), this last function
    being called by DString.get_transliteration().

    * DString.get_transliteration :
      for dchar in self:
          res.append( dchar.get_transliteration(method = "perseus") )

          * --------------------------------------------------------------------
          * dchar.get_transliteration(method = "perseus") calls in fact
          * perseus.py::dchar__get_translit_str(), id est :
          * --------------------------------------------------------------------
          * dchar__get_translit_str(dchar)

            * [...]
                if dchar.unknown_char:
                    res.append( TRANS__UNKNOWN_CHARACTER )

                else:

                    if dchar.punctuation:
                        # punctuation :
                        res.append( PUNCTUATION[dchar.base_char] )

                    elif dchar.base_char in OTHER_SYMBOLS:
                        res.append( OTHER_SYMBOLS[dchar.base_char] )

                    else:

                        if dchar.capital_letter:
                            # upper case letter :
                            res.append( '*' )

                            if dchar.pneuma is not None:
                                res.append( DIACRITICS[dchar.pneuma] )
                            [...]

                        else:
                            # lower case letter :
                            res.append( LOWER_CASE[dchar.base_char] )

                            if dchar.pneuma is not None:
                                res.append( DIACRITICS[dchar.pneuma] )
                            [...]


                        if dchar.hypogegrammene == True:
                            res.append( DIACRITICS['ὑπογεγραμμένη'] )

                        if dchar.dialutika == True:
                            res.append( DIACRITICS['διαλυτικά'] )

                        if dchar.mekos is not None:
                            res.append( DIACRITICS[dchar.mekos] )
              [...]

    ############################################################################
    # (3)   exceptions
    ############################################################################

    As a module of the DChars project, the code may raise a DCharsError exception
    defined in dchars/errors/errors.py .


