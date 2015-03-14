# -*- encoding: utf-8 -*-

# Export Better BibTex, bibtexparser assumes ascii input

import bibtexparser
import os

# Change the default encoding to utf8
#import sys
#reload(sys)
#sys.setdefaultencoding('UTF8')

inputfile = os.path.join('data','Exported Items.bib')
print(inputfile)
a_file = open(inputfile, encoding='utf-8')
bibtex_str = a_file.read()

'''
with open(inputfile) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
    print(bib_database)

print(bib_database)
print(bib_database.entries)
'''

'''
with open(inputfile) as bibtex_file:
    print(bibtex_file)
    bibtex_str = bibtex_file.read()

'''
bib_database = bibtexparser.loads(bibtex_str)
print(bib_database)

print('\n*** Entries ***\n')
print(bib_database.entries)

print('\n*** Fields ***\n')
print(type(bib_database.entries))

for key, value in bib_database.entries[0].items() :
    print(key)
    print('\t',value,'\n')


