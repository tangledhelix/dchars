find dchars/ -name "*.py" -exec sed -i "s/from dchars.dicttools/from dchars.utilities.dicttools/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.lstringtools/from dchars.utilities.lstringtools/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.name2symbols/from dchars.utilities.name2symbols/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.orderedset/from dchars.utilities.orderedset/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.regexstring/from dchars.utilities.regexstring/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.sortingvalue/from dchars.utilities.sortingvalue/g" {} \;
find dchars/ -name "*.py" -exec sed -i "s/from dchars.triggerlist/from dchars.utilities.triggerlist/g" {} \;


