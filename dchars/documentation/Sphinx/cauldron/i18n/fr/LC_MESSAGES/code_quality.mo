??          T      ?       ?      ?      ?      ?                "  M  .  U   |  ?  ?  ?   ?          #     4                                        $CODE_QUALITY_TEXT$ $CODE_QUALITY_global_tests$ $CODE_QUALITY_unittests$ CODE_QUALITY_TITLE global tests unittesting Project-Id-Version: DChars 0.1.2
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2013-03-22 13:32
PO-Revision-Date: 2013-03-22 13:32
Last-Translator: Automatically generated
Language-Team: none
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Language: fr
Plural-Forms: nplurals=2; plural=(n > 1);
 La qualité du code compte : n'hésitez pas à contacter l'auteur pour l'améliorer ! La qualité du code est vérifiée grâce à deux tests : |br| |br| ``./header_please.py`` vérifie que chaque fichier a une en-tête correcte. |br| |br| ``./pylint_tests`` lance Pylint qui note chaque fichier du projet. Le fichier de configuration de Pylint est modifié de la façon suivante : |br| * max-line-length=100 |br| * disable=W0142 (used * or ** magic) |br| * max-public-methods=25 |br| * max-args=10 |br| * max-locals=20 Ce programme utilise ``nosetest`` pour ses tests unitaires, regroupés dans ``/tests/``. Pour lancer les tests unitaires : ``./unittests.sh`` qualité du code tests généraux unit testing 