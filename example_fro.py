from dchars.dchars import new_dstring
DSTRING_FRO = new_dstring(language='fro')

string = DSTRING_FRO().init_from_transliteration("abc")
print(str(string))
print(string.get_transliteration())

string = DSTRING_FRO().init_from_transliteration("a\\")
print(str(string))
print(string.get_transliteration())
