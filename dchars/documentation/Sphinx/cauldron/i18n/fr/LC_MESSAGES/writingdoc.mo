??          4      L       `      a      s   M  ?   C  ?                         $WRITINGDOC_TEXT$ WRITINGDOC_TITLE Project-Id-Version: Phoseg 0.3.6
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2012-12-16 10:45
PO-Revision-Date: 2012-12-16 10:45
Last-Translator: Automatically generated
Language-Team: none
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: fr
Plural-Forms: nplurals=2; plural=(n > 1);
 A partir des fichiers .rst de ``documentation/Sphinx/RSTsourcefiles/`` sont créés dans le même répertoire les fichiers .pot (templates) correspondants (``sphinx-build -b gettext . .``) . Chaque fichier .pot est converti en un fichier .po pour chaque langue et copié dans ``documentation/Sphinx/i18n/fr/`` (``msginit --no-translator --locale=fr_FR -i file.pot -o ../i18n/fr/file.po``). Le traducteur complète alors la traduction de chaque fichier .po. |br| Chaque fichier .po devient pendant la génération de la documentation (``./create_documentation.py``) un fichier .mo, placé dans ``documentation/Sphinx/i18n/fr/LC_MESSAGES/``. |br| |br| Un fichiers .rst est dynamiquement créé par ``./create_documentation.py`` : ``index.rst``. |br| |br| Attention : les anciens fichiers .po sont ÉCRASÉS avec la commande ``msginit`` ! écrire la documentation 