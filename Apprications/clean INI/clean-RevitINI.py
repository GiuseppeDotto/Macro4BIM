
import os
import shutil

base = os.path.join(os.getenv('APPDATA'), 'Autodesk', 'Revit')
temp_file = os.path.join(os.getenv('APPDATA'), 'Revit.INI')

# SNOOP EVERYTHING
for dirpath, dirnames, filenames in os.walk(base):
    if 'Revit.ini' in filenames:
        ini_file = os.path.join(dirpath, 'Revit.ini')
        with open(ini_file, 'r+', encoding='utf-16') as file:
            all_text = file.read()
            if 'Recent File List' in all_text:
                partial_text = all_text[all_text.index('Recent File List'):]
                to_remove = partial_text[partial_text.index(']')+1:partial_text.index('[')-1]
                if to_remove:
                    # print( to_remove )
                    with open(temp_file, 'w', encoding='utf-16') as temp:  temp.write( all_text.replace(to_remove, '') )
                    print('CLEANED\t\t:\t'+ini_file)
                    shutil.copy(temp_file, os.path.dirname(ini_file))
                else:
                    print('NOTHING TO CLEAN\t:\t'+ini_file)
            else:
                print('NADA\t\t:\t'+ini_file)

input('')