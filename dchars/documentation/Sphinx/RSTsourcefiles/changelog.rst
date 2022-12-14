===============
CHANGELOG_TITLE
===============

------------------
0.6.5 [2014_08_19]
------------------

  * (bod) updated syllabic_structure.py::CHILTON_LIST : added (None, None, 'A')

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.6.4 [2014_08_14]
------------------

  * (bod) improved the InternalStructures.seems_to_be_a_pure_tibetan_string() function, whicn now uses two methods, the standard one (grammatical analysis) or the one's based on Chilton list (see  http://www.tibet.columbia.edu/iats/it/IATS-X_Chilton_slides.pdf, slide 32)

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.6.3 [2014_08_14]
------------------

  * (bod) InternalStructures.seems_to_be_a_pure_tibetan_string() now calls .seems_to_be_a_sanskrit_string() with strict_answer equal to True.

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.6.2 [2014_08_14]
------------------

  * (bod) improved InternalStructures.seems_to_be_a_pure_tibetan_string() : the stack of consonants must now be adequate to http://www.thlib.org/reference/transliteration/tibstacks.php and the function seems_to_be_a_sanskrit_string() is called.

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.6.1 [2014_08_14]
------------------

  * (bod) new functions *.seems_to_be_a_pure_tibetan_string() 

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.6.0 [2014_08_13]
------------------

  * improved documentation
  * (all languages) added a family of functions called by the Logotheras project : set_to_its_most_visual_form()
  * (all languages) fixed a bug DStringMotherClass.open/.readlines
  * (grc) one more test; remove_any_orthographic_soft_breathing_on_a_vowel() > rm_soft_breathing_on_vowels();  DStringGRC.remove_any_orthographic_soft_breathing_on_a_vowel()
  * (jpn) modified DStringJPN.sortingvalue() : fixed the way the sorting value is computed : some special cases were missing.

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok

------------------
0.5.9 [2014_01_21]
------------------

  * new language : ?????????/Japanese (ang) and its transliteration's method "shepburn" (simplified Hepburn)
  * Old English (ang) : sorting method 'default' is ok (thorn character has been taken in account)
  * no more dummies string copies with [:]

  * code quality :

    * header_please_test.py ok
    * 194 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.8 [2014_01_08]
------------------

  * new language : Old English (ang)

  * code quality :

    * header_please_test.py ok
    * 176 tests, all ok
    * Pylint's worst mark : 9.47

--------------------
OLDER_VERSIONS_TITLE
--------------------

------------------
0.5.7 [2013_12_21]
------------------

  * added to DCharacterGRC.get_sourcestr_representation() the 'ignore_makron' parameter
  * added new function DStringGRC.get_sourcestr_representation() overloading DString.get_sourcestr_representation() to take the 'ignore_markron' parameter in account

  * code quality :

    * header_please_test.py ok
    * 158 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.6 [2013_11_29]
------------------

  * new functions : DStringMotherClass.endswith(), .startswith() + tests

  * code quality :

    * header_please_test.py ok
    * 157 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.5 [2013_11_28]
------------------

  * new function : DStringGRC.endsWithABareiaAccent()

  * code quality :

    * header_please_test.py ok
    * 147 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.4 [2013_11_24]
------------------

  * added DStringMotherClass.__add__() method
  * added clone() method for all languages
  * added DStringMotherClass.__getitem__() method
  * moved tests/ to root directory, beside dchars/ directory

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.3 [2013_09_26]
------------------

  * the way DChars compute the alphabetical order has been checked and modified to be the same for all languages.

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.2 [2013_08_23]
------------------

  * new list of "usefull characters"

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.1 [2013_08_21]
------------------

  * new option for grc.gutenberg : "ignore makron and brakhu"
  * fixed a bug in ConfigValue.__repr__()
  * new function : (config_ini_data.py)ConfigValuesForOneLanguage.get_configvalue_for_this_optionname()

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.5.0 [2013_08_20]
------------------

  * lot of small fixes thanks to Pylint
  * bool options defined by "yes"/"no", not by a bool anymore.
  * trans__directions added to every DString*** object in order to verify if a transliteration's method is available in both direction ( transliteration <-> text ) or not.
  * AVAILABLE_DIRECTIONS defined for every transliteration.

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok
    * Pylint's worst mark : 9.47

------------------
0.4.9 [2013_08_12]
------------------

  * (config_ini.py) modified write_config_ini() so that the option's name appears in the config.ini file as a commentary.
  * new attribute for ConfigValue class : the 'optionname' stores the name of the option in dchars.py::LANGUAGE
  * (grc.gutenberg) : new option "hh becomes h" (patch from Frank Zago !)

------------------
0.4.8 [2013_08_01]
------------------

  * new function : Transformation.is_ready_to_be_applied()
  * Transformation.result if set by default to "" (and not None)
  * languages_name.py::LANGUAGES_AND_TRANSLITERATIONS define "ewts" and "bodsan" as 
    transliteration methods; there's no 'default' method for Tibetan.

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok

------------------
0.4.7 [2013_07_30]
------------------

  * modified dchars.py to take in account the strange behaviour of the configparser module which needs to open (on Windows systems) the file utf-8 files with a call to codecs.open .
  * SuccessiveTransformations.apply : new argument 'limit_to_the_number_of_transformations'
  * added commentaries in DString*:__init__ about the three attributes iss639_3_name, transliteration_method, options
  * Transformation.direction can be set to +1 or -1 and not to strings anymore
  * fixed some relative paths so that they become absolute
  * added some files to setup.py needed by dchars
  * added to project_files.py some forgotten files
  * modified .gitignore so that doc/ and dchars/documentation/ directories are not added to git files.

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok

------------------
0.4.6 [2013_07_17]
------------------

  * "DEVANAGARI LETTER " > ""
  * no more "DStringCharacterGRC" in the comments > "DCharacterGRC"
  * (all languages) get_usefull_combinations() for all transliteration's methods
  * (all languages) one directory per transliteration method.
  * (grc) in transliterations' method, symbols.py doesn't use anymore unused dchar_base like "??2".
  * (grc) fixed a bug concerning ?? and ??, no longer 'base_char'

  * code quality :

    * header_please_test.py ok
    * 136 tests, all ok

------------------
0.4.5 [2013_07_13]
------------------

  * added timestamp to the header of config.ini
  * ConfigValue.subsection must be filled every time the subsection is different from "".

  * code quality :

    * header_please_test.py ok
    * 131 tests, all ok

------------------
0.4.4 [2013_07_13]
------------------

  * config_ini.py::check() checks if names and values correspond to config_ini_data.DATA
  * fixed a bug in projects_files.py : config_ini and config_ini_data are not dev-only files.

  * code quality :

    * header_please_test.py ok
    * 131 tests, all ok

------------------
0.4.3 [2013_07_07]
------------------

  * new file : dchars/config_ini.py with the function write_config_ini()
  * (Pylint, name too long) "dstring__trans__get_transliteration" > dstring__trans__get_trans
  * dchars.py/write_config_ini() creates the config.ini file
  * new file : dchars/config_ini_data.py with the informations relative to the config.ini file

  * code quality :

    * header_please_test.py ok
    * 131 tests, all ok

------------------
0.4.2 [2013_07_05]
------------------

  * if a wrong transliteration method's name is passed to new_dstring(), an exception is raised.
  * new file : dchars/languages_name.py, defining LANGUAGES_NAME and LANGUAGES_AND_TRANSLITERATIONS
  * new file : successivetransformations.py (in order to automate successive transliterations from a source text)
  * new function : dchars.py::sort_a_list_of_words()
  * (bod) alert__dchars_have_changed() > update_istructs()
  * (bod) alert__istructs_have_changed() > update_dchars()
  * no more triggerlists in the project : they were used by several files for Tibetan
  * (bod) no more automatic updates for istructs when dchars have changed neither automatic updates for dchars when istructs have changed.

------------------
0.4.1 [2013_06_27]
------------------

  * (bod) new function : ListOfInternalStructures.contains_unknown_character()
  * (bod) no more words stored in the buffers with unknown characters.
  * (bod) new buffers : words stored in the buffers are now stored with their real_indexes and indexes. The two buffers are bigger (2 x 400.000)

------------------
0.4.0 [2013_06_25]
------------------

  * (config.ini, grc:gutenberg) new possibility for [grc.gutenberg]transliteration for upsilon = u or y (tested)
  * setup.py (thank you Frank Zago !) : DChars can be installed via the usual setup.py procedure.

------------------
0.3.9 [2013_06_24]
------------------

  * (grc) added a dstring__trans__get_transliteration(dstring_object) function to
    all transliteration methods.
  * (grc) first draft for the 'gutenberg' transliteration method (see http://www.pgdp.net/wiki/Greek)
  * (grc) new options : gutenberg:ignore accents, gutenberg:ignore iota subscript, ...

------------------
0.3.8 [2013_06_21]
------------------

  * rewrote documentation for (bod)internalstructure.py::get_intstruct_from_str()
  * added some documentations to roadmap.rst (DChars' "map" concerning Tibetan)
  * sort.py : version 0.3.8-sort#[2|3|4], fixed several bugs concerning Tibetan

------------------
0.3.7 [2013_06_17]
------------------

  * sort.py has the same version as DChars
  * ListOfInternalStructures.seems_to_be_a_sanskrit_string got the 'strict_answer' argument,
    used by sort.py.
  * dchars/symbols.py has been moved to dchars/symbols/symbols.py
  * dchars/dicttools.py, dchars/lstringtools.py, dchars/name2symbols.py,
    dchars/orderedset.py, dchars/regexstring.py dchars/sortingvalue.py,
    dchars/triggerlist.py have been moved to dchars/utilities
  * no more useless print()
  * get rid of lot of $$$ and ??? strings, replaced by ad hoc comments.

------------------
0.3.6 [2013_06_04]
------------------

  * (bod) ... superfix letter ! Fixed this old mistake : until this version DChars didn't
    know what a superfix was... hem... hem...
  * (all languages) a lot of new tests in order to test comparisons.
  * (all languages) ./sort.py : a program to sort files.
  * (lat, grc) changed letter's name in order to be shorter (e.g. '?????????' > '??')
  * (all languages) added the six rich comparison ordering methods to DStringMotherClass :
    lt/le, gt/ge, eq/ne.  Except eq/ne, those methods call the sortingvalue() function.
  * (all languages) added five rich comparison ordering methods to DCharacterMotherClass :
    lt/le, gt/ge, ne (but NOT __eq__, defined in the derived classes). Those methods
    call the sortingvalue() function.
  * (lat) base_char contains always "a", not "A" as before (and 'b', not 'B' and so on)
  * (all languages) added a new option : "sorting method"
  * (all languages) in DCharacter* classes, the .dstring_object attribute belongs now
    to the mother class dchars/dcharacter.py::DCharacterMotherClass

  * code quality :

    * header_please_test.py ok
    * 130 tests, all ok
    * Pylint's worst mark : 9.47

0.3.5 [2013_04_27]
------------------

  * (bod.bodsan) fixed a bug concerning the presence of the tsheg symbol after each
    Sanskrit syllable.
  * (all languages) delete the function add_the_unrecognized_characters() and rewrote
    the init_from_src() functions.
  * (all languages) new option : "anonymize the unknown characters"

  * code quality :

    * header_please_test.py ok
    * 111 tests, all ok
    * Pylint's worst mark : 9.47

0.3.4 [2013_04_26]
------------------

  * (bod) new transliteration's method : "bodsan" (Tibetan <-> Sanskrit)
  * (bod) fixed a bug concerning the oM symbol.
  * modified dicttools.py in order to show more explicit error message
  * added more explicit comments in config.ini
  * (bod) fixed several bugs in bod__create_buffers.py
  * (bod) added a bunch of new ewts words (places' names) to ewts_words
    (dchars/languages/bod/transliteration/ewts_words.txt) in order to add new
    syllables to the buffers. Buffers were updated.
  * delete the ISO15919/ directory

  * code quality :

    * header_please_test.py ok
    * 111 tests, all ok
    * Pylint's worst mark : 9.47

0.3.3 [2013_04_25]
------------------

  * (bod) fixed a bug in the EWTS transliteration of "H" and "M" : "labH" but "khaMs",
    H after the suffix, M after the main vowel.
  * (bod) fixed a bug in the transliteration of "always Sanskrit" Tibetan string :
    ??????????????? is "basgrada", not "bsgrada" (I forgot to add the 'a' vowel to the prefix)
  * fixed a bug in new_dstring : I forgot to duplicate the options : the different DString*
    don't have to share the same dictionary of options !

  * code quality :

    * header_please_test.py ok
    * 110 tests, all ok
    * Pylint's worst mark : 9.47

0.3.2 [2013_04_25]
------------------

  * added config.ini, a file describing the default values of DString* objects
  * (bod) in bod_tests.py, test_problematicstring() > test_problematicstrings()
  * (bod) TESTSDStringBOD.test_pickle() tests the functions used to format ListOfInternalStructures object into a "pickle-compliant" string.
  * (bod) two functions can now use buffers in order to return quickly the entries already computed :
    ewts.py::get_intstruct_from_str() and ewts.py::get_intstruct_from_trans_str()
  * (bod) modified the name of the letters in order to spare time and memory (e.g. "LETTER KHA" -> "KH")

  * code quality :

    * header_please_test.py ok
    * 110 tests, all ok
    * Pylint's worst mark : 9.47

0.3.1 [2013_04_24]
------------------

  * (bod) new option : "expected structure" :
        "always Sanskrit", "always Tibetan", "Tibetan or Sanskrit"
  * added default options to every DString created by new_dstring()
  * (bod) rewrote large parts of get_intstruct_from_trans_str() and of get_intstruct_from_str()
    using a new function, ListOfInternalStructures.get_the_complete_records
  * (bod) added a bunch of EWTS words to the tests (file ewts_words)
  * no more dstring.err(), dstring.errors, dstring.validity; if an error occurs, an exception
    will be raised.
  * (bod) added new strings for tests
  * (bod) fixed a bug concerning rnam bcad/anusvara/halanta place in transliteration.
  * (bod) fixed a bug concerning words ending with a suffix and the rnam bcad symbol (e.g. ????????? labH)

  * code quality :

    * header_please_test.py ok
    * 109 tests, all ok
    * Pylint's worst mark : 9.47


0.3.0 [2013_04_21]
------------------
  * (bod) "dependentvowel" > "vowel"
  * (bod) "TIBETAN xxx" > "xxx" (e.g. "TIBETAN LETTER LA" -> "LETTER LA")
  * (bod) new file : bod/syllabic_structure.py
  * (bod) DString's type is now TriggerList.
  * (bod) new function : InternalStructrure.check_default_value() in order to simplify comparisons
    betwwen InternalStructrure objects.
  * (bod) new suffixes supported : 'i, 'is, 'u, 'o, 'ang and 'am. Damn, it wasn't easy...
  * (bod) added a new test (TESTSDStringBOD.test_intstruct) in order to test the internal structure taken from an EWTS string and from a unicode string.
  * (bod) fix OrderedSet.__eq__ so that the an OrderedSet object can be compared to None
  * (bod) DStringBOD has now a (ListOfInternalStructures) self.istructs attribute
  * (bod) fixed a minor bug in functions like dstring__init_from_translit_str() : these functions do not return the dstring object but may return anything else (e.g. with bod
    functions, it's an ListOfInternalStructures object which may be returned)
  * (bod) added new tests to EWTS from http://www.thlib.org/reference/transliteration/wyconverter.php
  * added LANGUAGES_LOADED to dchars.py in order to avoid to import several times the
    same module.

  * code quality :

    * header_please_test.py ok
    * 108 tests, all ok
    * Pylint's worst mark : 9.47

0.2.9 [2013_04_13]
------------------

  * new tests for strings with unknown character; the code was deeply analysed and sometimes
    rewritten to achieve the expected results.
  * languages modules are dynamically loaded by dchars/dchars.py::new_dstring
  * new file : dchars/symbols.py defines the UNKNOW_CHAR_SYMBOL symbol.
  * all the languages use the UNKNOWN_CHAR_SYMBOL for the get_the_transliteration() functions.
  * added the UNKNOWN_CHAR_SYMBOL symbol to all DChar* objects in order to show the presence of
    unknown characters.
  * fixed a typo in DStringMotherClass.__repr__ : "characters" > "character(s)"

  * code quality :

    * header_please_test.py ok
    * 100 tests, all ok
    * Pylint's worst mark : 9.47


0.2.8 [2013_04_12]

  * (all the code) "specialpoints" > "specialpoint"
  * (san) deleted the useless pseudo-sign "@VIRAMA" and "@NUKTA"
  * fixed a big bug concerning regex' patterns (?P<name>(a|b|c))? != (?P<name>(a|b|c)?)
  * fixed a lot of small bugs in all languages : I checked that we have trans->unicode->trans
    for all languages.
  * delete some old and big .txt~ files
  * (bod) added a test in order to check abnormal use of diacritics (e.g. "?????????" has two anusvara-s)

  * code quality :

    * header_please_test.py ok
    * 87 tests, all ok
    * Pylint's worst mark : 9.47

0.2.7 [2013_04_10]

  * (bod, ewts) : modified transliterations for 'TIBETAN LETTER GHA' : 'g+h' (before : 'gh')
                  same thing for "b+h" (before : 'bh') and "d+h" (before : 'dh')
                  (according to http://www.thlib.org/reference/transliteration/#!essay=/thl/ewts/4/)
  * (bod, ewts) : all Unicode compound forms (e.g. chr(0x0F90) + chr(0x0FB5), chr(0x0FB9)  ?????? ->  ??? ) are
    now defined in bod/dstring.py::INIT_FROM_STR__SUBSTITUTIONS . DChars uses the
    unique character (0x0FB9), not the compounds characters but know how to read them.
  * (bod, ewts) added 'TIBETAN LETTER KSSA'  : 'k+Sh' to ewts.py
  * (bod, ewts) added 'TIBETAN LETTER DZHA'  : 'dz+h' to ewts.py

  * code quality :

    * header_please_test.py ok
    * 69 tests, all ok
    * Pylint's worst mark : 9.47

0.2.6 [2013_04_10]

  * (bod, ewts) fixed a bug with ??? = oM in order to accept, e.g., ????????? = yoM too.
  * (bod, ewts) 'TIBETAN SIGN RJES SU NGA RO' (?????? = saM) accepted
  * (bod, ewts) 'TIBETAN SIGN NYI ZLA NAA DA' (?????? = sa~M`) accepted
  * (bod, ewts) 'TIBETAN SIGN SNA LDAN' (?????? = sa~M) accepted
  * (bod, ewts) fixed a bug with +C (C being a consonant)
  * (bod, ewts) halanta is accepted, like in "??????"="k?"

  * code quality :

    * header_please_test.py ok
    * 69 tests, all ok
    * Pylint's worst mark : 9.47

0.2.5 [2013_04_09]

  * (bod, ewts) rnam bcad is accepted, like in "????????????"="gtiH"
  * (lstringtool.py::isort_a_lstrings_bylen_nodup) modify the function in order to treat empty entry.
  * (bod, ewts) "??????" = "fa", "??????" = "va" are accepted
  * (bod, ewts) "??????" = "k+Sha" is accepted
  * (bod, ewts) oM is accepted
  * (bod, ewts) D+ha, Sha are accepted
  * (bod, ewts) +C (C being a consonant) is accepted

  * code quality :

    * header_please_test.py ok
    * 68 tests, all ok
    * Pylint's worst mark : 9.47

0.2.4 [2013_04_08]

  * (bod) unicode->EWTS seems functional for standard Tibetan (not for Sanskrit Tibetan)
  * (bod/internalstructure.py) get_internal_structure() -> get_intstructures_from_dstring()
  * new fake-function : DCharacterMotherClass.reset() (this function must be overloaded)
  * (bod) ListOfAssumptions > ListOfInternalStructures, Assumptions > InternalStructure
  * (bod) assumptions.py has been placed in internalstructure.py

  * code quality :

    * header_please_test.py ok
    * 68 tests, all ok
    * Pylint's worst mark : 8.82

0.2.3 [2013_04_05]

  * DStringMotherClass.open() can only be used to read files.
  * modify DStringMotherClass in order to allow :

        .. code-block:: python

            import dchars.dchars as dchars
            DSTRING_SAN = dchars.new_dstring(language='???????????????????????????', transliteration_method="itrans")

            # example with read() :
            with DSTRING_SAN().open(sourcefile, 'r') as src:
                print( src.read().get_transliteration() )

            # example with readlines() :
            with DSTRING_SAN().open(sourcefile, 'r') as src:
                for line in src.readlines():
                    print( line.get_transliteration() )

  * (bod) add COMMON_CONSONANTS_STACK to internalstructure.py in order to treat strings like
    "????????????"="sat+t+wa".
  * (bod, ewts) : one Tibetan syllable can now have two vowels (e.g. "????????????"="rdo+e")
  * (documentation) modify index.po
  * (documentation) fix a typo in grc.rst

  * code quality :

    * header_please_test.py ok
    * 66 tests, all ok
    * Pylint's worst mark : 8.82

0.2.2 [2013_04_03]

  * read and checked every call to DCharsError
  * (bod) GetInternalStructure() > get_internal_structure()
  * default transliteration method is defined in dchars.dchars.py::LANGUAGES
  * no more "logotheras" string in .py files ("logotheras" -> "dchars")
  * all languages accept the new interface to the DString classes : new_dstring(language, transliteration_method)
  * (san) find a big bug in iso15919_tests.py (test test_init_from_transliteration1 was ineffective)
  * (san) better support for candrabindu

  * code quality :

    * header_please_test.py ok
    * 66 tests, all ok
    * Pylint's worst mark : 8.82

0.2.1 [2013_03_29]

  * fixed a bug in (bod)dchars.py : vowels TIBETAN VOWEL SIGN II and
    TIBETAN VOWEL SIGN UU are now well recognized.
  * (bod) bodsan module uses the internal structure computed by
    GetInternalStructure() to transliterate tibetan into sanskrit.


0.2.0 [2013_03_29]

  * (bod) new files : internalstructure.py, assumptions.py
  * no more "bot" (instead of 'bod') anymore in the code.

0.2.0 [2013_03_29]

  * bod : unicode->EWTS has been improved
  * update dchars/tests/languages/bod/transliterations/ewts_tests.py
  * first steps with bodsan.py (tibetan <-> sanskrit)


0.1.9 [2013_03_28]

  * bod : unicode->EWTS seems to work on all "pure tibetan" words.

0.1.8 [2013_03_25]

  * bod : unicode->EWTS well advanced
  * bod : first steps with EWTS->unicode

0.1.7 [2013_03_24]

  * first steps with bod (Tibetan)
  * index.rst has been modified : let's hope this page is now easier to read !
  * fixed typos in sans.rst, lat.rst, howto_use.rst

  * code quality :

    * header_please_test.py ok
    * 61 tests, all ok
    * Pylint's worst mark : 9.47

(DChars presented on linuxfr.org)

0.1.6 [2013_03_22]

  * Sphinx' documentation ok.
  * remove the old dchars/languages/hbo/transliterations/default.py
  * speed up the code by removing some calls to get_default_symbol()
  * test functions test_from_srcstr_2_srcstr() are now much harder (reciprocal identity used)
  * remove some unused lines of code in san/translations/itrans.py concerning nukta point.
  * fix a bug in iso15919.py : dchar.dependentvowel = None instead of the stupid " = False"

  * code quality :

    * header_please_test.py ok
    * 61 tests, all ok
    * Pylint's worst mark : 9.47

0.1.5 [2013_03_22]

  * Sphinx's documentation : not for Sanskrit and no translations.
  * bug fixed : san/dchars.py knows how to handle the "a" vowel in order to pass the srcstr_2_srcstr test.
  * repr_as_a_string() renamed as source_string_representation()
  * bug fixed in DString.__str__ : "".join(), not "\n".join().
  * add to all languages the DStringXXX.get_transliteration() function in order to
    use the DEFAULT_TRANSLITERATION_METHOD if no method if given to the function.
  * remove the useless "import traceback" in dchars/errors/errors.py
  * functions' names has been harmonized : ...trans_lstring > ...translit_str, ...transli_string > ...translit_str, ...translistring > ...translit_str
  * transliteration's "default" method (lat,hbo,grc) renamed as "basic"

  * code quality :

    * header_please_test.py ok
    * 55 tests, 55 ok
    * Pylint's worst mark : 9.47

0.1.4 [2013_03_19]

  * "DIGIT" > "OTHER_SYMBOL"
  * PUNCTUATION and DIGITS are now separated objects : a digit is not a punctuation
    sign anymore. (tested)
  * the validity attribute is checked in every test of every language
  * problem with hbo multiple cantillation's marks solved (E.g : Psalm 18.12)
  * dchar__get_translistring > dchar__get_trans_lstring
  * dchar_init_from_translistring > dchar_init_from_trans_lstring
  * (lat) : check if "y" + diacritics works (ok)

  * code quality :

    * 57 tests, 57 ok
    * Pylint's worst mark : 9.47

0.1.3 [2013_03_18]

  * code cleaning
  * tests with Pylint

  * code quality :

    * 53 tests, 52 ok
    * Pylint's worst mark : 9.47

0.1.2 [2013_03_18]

  * new regex' pattern for san:iso15919 : it works.

  * 53 tests, all ok

0.1.1 [2013_03_11]

  * working on iso15919 : not yet ready
  * san/itrans : nukta ok
  * DEFAULT_TRANSLITERATION_METHOD for all languages
  * trans_equivalences for all languages (e.g. in san/itrans : "RRi" == "R^i")
  * more documentation about san/itrans
  * DCharacterXXX.reset cleaned up

0.1.0 [2013_03_11]

  * (san)itrans ok
  * new structure for DCharacterSAN : hiatus ok

  * 44 tests, all ok

0.0.9 [2013_03_09]

  * Sanskrit/Devanagari : in progress
  * Latin (lat) ok
  * Name2Symbols.num2name > defaultsymbol2name
  * fixed a bug concerning the hbo.transliteration.default of ???? (shin + daghesh)
  * fixed a but in grc/dchars.py::DCharacterGRC.__eq__ : I forgot capital_letter.

0.0.8 [2013_03_06]

  * hbo : transliteration ok
  * hbo : DCharacterHBO, DStringHBO tested.
  * (grc, hbo) a lot of code has been factorized to the motherclasses DCharacter, DString
  * grc: new test file (text003_Euripides_Bacchae_1_104.txt)

  * 26 tests, all ok.

0.0.7 [2013_03_05]

  * Ancient Hebrew (hbo) : DCharacterHBO, DStringHBO, not tested
  * new Greek characters : digamma, kai, ...

  * 16 tests, all are ok.

0.0.6 [2013_03_04]

  * new structure for the directories
  * new transliteration for Ancient Greek : perseus

  * 14 tests, all are ok.

0.0.5 [2013_03_04]

  * dchars/stringtools.py
  * languages/grc/transliteration/default.py
  * fixed a lot of bugs in grc module.
  * two available translitteration for Ancient Greek : default, betacode

  * 11 tests, all are ok.

0.0.4 [2013_03_03]

  * dchars/regexstring.py
  * languages/grc/symbols.py
  * class Name2Symbols in dchars/name2symbols.py

  * 7 tests, all are ok.

0.0.3 [2013_03_02]

  * class Name2Symbols
  * Ancient Greek is nearly ok.

  * 5 tests, all ok

0.0.2 [2013_02_28]

  * DCharacterGRC::self.error
  * 4 tests, 2 failures

0.0.1 [2013_02_27]

  * classes DCharacter, DCharacterString
  * classes DCharacterGRC, DCharacterStringGRC
  * no tests
