.. |br| raw:: html

   <br />

=====================
DIRECTSTRUCTURE_TITLE
=====================

.. code-block:: none

   ./create_documentation.py    : create the documentation, has as --upload argument
   ./header_please.py           : check the header of all files named in ./project_files.py
   ./header_template.txt        : template used by ./header_please.py
   ./make_devversion.py         : create the global backup.
   ./nosetetests_setup.cfg      : configuration file for nosetests
   ./projects_files.py          : list of all files in the project
   ./pylint.rc                  : configuration file for pylint
   ./pylint_tests.py            : launch the Pylint's tests for all files named in ./project_files.py
   ./RSTconf_template.txt       : template for conf.py, a file created for Sphinx
   ./RST_template.txt           : template for .rst files created for Sphinx
   ./unittests.sh               : launch the unit tests with nosetest

   ./dchars/                    : main directory
   ./dchars/dchars.py           : mother-classes DCharacter and DString
   ./dchars/documentation       : ... and specially documentation/Sphinx/RSTsourcefiles
   ./dchars/dicttools.py        : utilities for dictionaries
   ./dchars/errors/             : class DCharsError
   ./dchars/languages/          : [see below]
   ./dchars/lstringtools.py     : utilities for list of strings.
   ./dchars/name2symbols.py     : class Name2Symbols
   ./dchars/symbols.py/         : symbol(s) used by every languages
   ./dchars/system              : (numversion and program's name defined in communia.py)
   ./dchars/tests               : unit tests

   and for each language in ./dchars/languages/xxx :
   ./dchars/languages/xxx/dchars.py     : DCharacterXXX and DStringXXX
   ./dchars/languages/xxx/symbols.py    : Name2Symbols objects (SYMB_CONSONANTS, ...)

   and for each transliteration's method defined in ./dchars/languages/xxx/transliteration :
   ./dchars/languages/xxx/transliteration/methodxxx.py

