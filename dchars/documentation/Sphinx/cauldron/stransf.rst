================================
SUCCESSIVE_TRANSFORMATIONS_TITLE
================================

.. code-block:: python

    from dchars.dchars import new_dstring
    from dchars.successivetransformations import SuccessiveTransformations

    DSTRING_GRC = new_dstring(language="Ἑλληνικὴ γλῶττα",
                              transliteration_method = "basic",
                              options = {"anonymize the unknown characters" : False,
                                         "gutenberg:ignore smooth breathing" : True,
                                         "gutenberg:ignore accents" : True,
                                         "gutenberg:ignore iota subscript" : True,
                                         "gutenberg:ignore diaeresis" : True,
                                         "gutenberg:transliteration for upsilon" : "u",
                                        },
                              )

    strans = SuccessiveTransformations()
    strans.add( DSTRING_GRC, "transliteration->text" )
    strans.add( DSTRING_GRC, "text->transliteration" )
    strans.add( DSTRING_GRC, "transliteration->text" )
    strans.add( DSTRING_GRC, "text->transliteration" )
    strans.apply( "p/ama" )

    print(strans)
