??          4      L       `      a      s   Q  ?   ?  ?     ?                    $WRITINGDOC_TEXT$ WRITINGDOC_TITLE Project-Id-Version: Phoseg 0.3.6
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2012-12-16 10:45
PO-Revision-Date: 2012-12-16 10:45
Last-Translator: Automatically generated
Language-Team: none
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: en_EN
Plural-Forms: nplurals=2; plural=(n != 1);
 By converting .rst files presents in ``documentation/Sphinx/RSTsourcefiles/`` we create the corresponding .pot (template) files in the same directory (``sphinx-build -b gettext . .``). Every .pot file for every language is converted (``msginit --no-translator --locale=fr_FR -i file.pot -o ../i18n/fr/file.po``) into a .po file and copied in ``documentation/Sphinx/i18n/fr/``. The translator fills in every .po file. |br| During the documentation's generation (``./create_documentation.py``) every .po file becomes a .mo file, placed in ``documentation/Sphinx/i18n/fr/LC_MESSAGES/``. |br| |br| One .rst files is dynamically created by ``./create_documentation.py`` : ``index.rst``. |br| |br| Beware ! Old .po files are OVERWRITTEN by the command ``msginit`` ! how to write the documentation 