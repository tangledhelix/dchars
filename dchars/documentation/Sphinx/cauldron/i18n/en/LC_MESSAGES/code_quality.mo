??          T      ?       ?      ?      ?      ?                "  Q  .  D   ?  ?  ?  ?   \     ?     ?     ?                                        $CODE_QUALITY_TEXT$ $CODE_QUALITY_global_tests$ $CODE_QUALITY_unittests$ CODE_QUALITY_TITLE global tests unittesting Project-Id-Version: DChars 0.1.2
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2013-03-22 13:32
PO-Revision-Date: 2013-03-22 13:32
Last-Translator: Automatically generated
Language-Team: none
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: en_GB
Plural-Forms: nplurals=2; plural=(n != 1);
 Code quality matters : feel free to write the author to improve it ! We verify code's quality with two tests : |br| ``./header_please.py`` verifies that each file begins with a regular header |br| ``./pylint_tests`` launches Pylint and gives a mark to every file in the project. Pylint's configuration's file has been modified this way : |br| * max-line-length=100 |br| * disable=W0142 (used * or ** magic) |br| * max-public-methods=25 |br| * max-args=10 |br| * max-locals=20 This program uses ``nosetest`` for unit testing; unit tests are stored in ``/tests/``. To launch the unit tests : ``./unittests.sh`` code quality global tests unittesting 