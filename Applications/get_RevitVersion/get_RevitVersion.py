
import os


print('HOW-TO:\tInput the folder path containing the .rvt and/or the .rfa files you want to inspect.\n\n')

dir_path = input('Input the folder and press ENTER: ')
dir_path = dir_path.replace('"','')

print('\n##########\n')

# search = 'B\x00u\x00i\x00l\x00d'
# search = lambda s: 'Build' in s.replace('\\x00','')
# search = lambda s: 'B' in s and 'u' in s and 'i' in s and 'd' in s and ':' in s and '2' in s
search = lambda l: 'Build' in str(l).replace('\\x00', '')
out = []


for dirpath, dirnames, filenames in os.walk(dir_path):
	rvt_files = [f for f in filenames if '.rvt' in f.lower() or '.rfa' in f.lower()]
	for f in rvt_files:
		file = os.path.join(dirpath, f)
		with open(file, "rb") as reader:
			for n, line in enumerate(reader.readlines()):
				try:
					if search(line):
						out.append('{}\n\t{}'.format(f, previous))
						print('----------')
						print('{}\n\t{}'.format(f, previous[:]))
						break
					else:
						end = str(line).index('\\r\\x00\\n')
						previous = str(line)[2:end].replace('\\x00','').replace('Format', 'Revit Version')
				except:
					pass
	break


if len(out) < 1:
	print('NO .RVT/.RFA FILES FOUND.')
else:
	print('----------')

print('\n##########\n')

print('© 2023, All rights reserved, Macro4BIM (www.macro4bim.com)')

input('\npress ENTER to close the window.')