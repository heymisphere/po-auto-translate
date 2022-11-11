from argparse import ArgumentParser
from polib import pofile
from pylingva import pylingva
translator = pylingva()

ap = ArgumentParser(description="Auto-translate PO files")
ap.add_argument("--file", '-f', nargs=1, required=True, help="File", metavar='/path/to/file')
ap.add_argument("--source", '-s', nargs=1, required=False, metavar='lang', help="Source language, default: en")
ap.add_argument("--destination", '-d', nargs=1, required=True, metavar='lang', help="Destination language")

args = ap.parse_args()

src = args.source
if src == None:
    src = 'en'
else:
    src = src[0]

des = args.destination[0]
file = pofile(args.file[0])

for entry in file.untranslated_entries():
    l = entry.msgstr = translator.translate(src, des, entry.msgid)
    entry.msgstr = l

file.save(args.file[0]+'-translated')