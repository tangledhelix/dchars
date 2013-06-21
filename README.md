----
----

*DChars* : [Check out the homepage !](http://94.23.197.37/dchars/)

----
----

*D(etailed)* *char(acter)s* *for* *Biblical* *Hebrew*, *Ancient* *Greek*, *Sanskrit*, *Latin* *and* *Tibetan*

DChars (Detailed Characters) is a **Python3** module aiming to modify easily the diacritics signs of complex unicode characters and to get their transliteration. DChars’ code is licensed under the **GPLv3** licence and is free. Current available languages are Ancient Greek, Latin, Biblical Hebrew, Sanskrit (devanāgarī) and Tibetan.

----
----

*How* *to* *use* *it* :

```python
# Let's use by instance the Sanskrit module :

# we import the "new_dstring" object in order to set DSTRING_SAN :
from dchars.dchars import new_dstring
DSTRING_SAN = new_dstring(language='san', transliteration_method="iso15919")

# We set the string from a source-string :
# this is the first part of the first verse of the Rig-Veda :
string = DSTRING_SAN("अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म् ।")

# and this is the second part :
string += DSTRING_SAN("होता॑रं रत्न॒धात॑मम् ॥")

# transliteration :
print(string.get_transliteration())         # -> a̱gnimī́ḷē pu̱rōhítaṁ ya̱jñasyá dē̱vamr̥̱tvijám .hōtā́raṁ ratna̱dhātámam ..

# Let's inspect and modify this string :
print(string[0])                            # -> अ॒
print(string[-1].punctuation)               # -> True
print(string[0].base_char)                  # -> "A"
print(string[1].base_char)                  # -> "DEVANAGARI LETTER GA"
print(string[0].anudatta)                   # -> True
string[0].anudatta = False
string[0].accent = "DEVANAGARI STRESS SIGN UDATTA"
print(string.get_transliteration())         # -> "ágnimī́ḷē pu̱rōhítaṁ ya̱jñasyá dē̱vamr̥̱tvijám .hōtā́raṁ ratna̱dhātámam .."

# Let's read a file and display its transliteration, line by line :
with DSTRING_SAN().open(sourcefile, 'r') as src:
    for line in src.readlines():
        print( line.get_transliteration() )
```
----
