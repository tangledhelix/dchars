#find dchars/languages/bod -name "*.py" -exec sed -i "s/'KA'/'K'/g" {} \;

src = {
        'KA'            : (chr(0x0F40),),
        'KHA'           : (chr(0x0F41),),
        'GA'            : (chr(0x0F42),),
        'GHA'           : (chr(0x0F43),),
        'NGA'           : (chr(0x0F44),),
        'CA'            : (chr(0x0F45),),
        'CHA'           : (chr(0x0F46),),
        'JA'            : (chr(0x0F47),),
        'NYA'           : (chr(0x0F49),),
        'TTA'           : (chr(0x0F4A),),
        'TTHA'          : (chr(0x0F4B),),
        'DDA'           : (chr(0x0F4C),),
        'DDHA'          : (chr(0x0F4D),),
        'NNA'           : (chr(0x0F4E),),
        'TA'            : (chr(0x0F4F),),
        'THA'           : (chr(0x0F50),),
        'DA'            : (chr(0x0F51),),
        'DHA'           : (chr(0x0F52),),
        'NA'            : (chr(0x0F53),),
        'PA'            : (chr(0x0F54),),
        'PHA'           : (chr(0x0F55),),
        'BA'            : (chr(0x0F56),),
        'BHA'           : (chr(0x0F57),),
        'MA'            : (chr(0x0F58),),
        'TSA'           : (chr(0x0F59),),
        'TSHA'          : (chr(0x0F5A),),
        'DZA'           : (chr(0x0F5B),),
        'DZHA'          : (chr(0x0F5C),),
        'WA'            : (chr(0x0F5D),),
        'ZHA'           : (chr(0x0F5E),),
        'ZA'            : (chr(0x0F5F),),
        '-A'            : (chr(0x0F60),),
        'YA'            : (chr(0x0F61),),
        'RA'            : (chr(0x0F62),),
        'LA'            : (chr(0x0F63),),
        'SHA'           : (chr(0x0F64),),
        'SSA'           : (chr(0x0F65),),
        'SA'            : (chr(0x0F66),),
        'HA'            : (chr(0x0F67),),
        'KSSA'          : (chr(0x0F69),),
        'FIXED-FORM RA' : (chr(0x0F6A),),

        'KKA'           : (chr(0x0F6B),),
        'RRA'           : (chr(0x0F6C),),
      }

import os
for _key in src:
    key = _key[:-1]

    order = 'find dchars/languages/bod -name "*.py" -exec sed -i ' + \
            '"s/{0}/{1}/g" {2} \;'.format( "'"+_key+"'", "'"+key+"'", {})

    print(order)

    order = 'find dchars/languages/bod -name "*.py" -exec sed -i ' + \
            '"s/{0}/{1}/g" {2} \;'.format( '\\"'+_key+'\\"', '\\"'+key+'\\"', {})

    print(order)

    order = 'find dchars/tests/languages/bod -name "*.py" -exec sed -i ' + \
            '"s/{0}/{1}/g" {2} \;'.format( "'"+_key+"'", "'"+key+"'", {})

    print(order)

    order = 'find dchars/tests/languages/bod -name "*.py" -exec sed -i ' + \
            '"s/{0}/{1}/g" {2} \;'.format( '\\"'+_key+'\\"', '\\"'+key+'\\"', {})

    print(order)






