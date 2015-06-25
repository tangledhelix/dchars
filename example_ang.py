from dchars.dchars import new_dstring
DSTRING_ANG = new_dstring(language='ang')

#string = DSTRING_ANG().init_from_transliteration("a*_")
#print(str(string))
#print(string.get_transliteration())

string = DSTRING_ANG().init_from_transliteration("a_*")
print(str(string))
print(string.get_transliteration())

string += string[0]
print(str(string))
print(string.get_transliteration())
