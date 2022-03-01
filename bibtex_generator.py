import pandas as pd
import bibtexparser
from tqdm import tqdm
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import  convert_to_unicode

delete_items = [
    'issn',
    'doi',
    'month',
    'eprint',
    'abstract',
    'archiveprefix',
    'keywords',
    'file',
    'eprinttype',
    'shorttitle',
    'address',
    'isbn',
    'langid',
    'publisher',
]


def replace_content(text,abbr_df):
    for index,row in abbr_df.iterrows():
        text = text.replace(f"{row[0]}",f"{row[1]}")
    
    if 'arxiv' in text.lower():
        arxiv_num = "".join(list(filter(str.isdigit, text)))
        text = f"arXiv:{arxiv_num[0:4]}.{arxiv_num[4:]}"

    ' '.join(text.split())
    return text

def arxiv_check(entry):
    if 'journal' in entry:
        if 'arxiv' in entry['journal'].lower():

            arxiv_num = "".join(list(filter(str.isdigit, entry['journal'])))
            entry['journal'] = f"arXiv:{arxiv_num[0:4]}.{arxiv_num[4:]}"
            ' '.join(entry['journal'].split())
            entry['year'] = entry['year']+f". [Online]. Available: http://arxiv.org/abs/{arxiv_num[0:4]}.{arxiv_num[4:]}"

    return entry



if __name__ =="__main__":

    abbr_df = pd.read_excel(r'./abbr_list.xlsx')
    with open('My Library.bib',encoding='UTF-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file,parser)
        for entry in tqdm(bib_database.entries):
            for item in delete_items:
                if item in entry:
                    del entry[item]
            if 'journal' in entry:
                entry['journal'] = replace_content(entry['journal'],abbr_df)
            if 'booktitle' in entry:
                entry['booktitle'] = replace_content(entry['booktitle'],abbr_df)
            
            entry = arxiv_check(entry)


    writer = BibTexWriter()
    writer.indent = '    '
    writer.comma_first = False
    with open('My Library.bib', 'w') as bibfile:
        bibfile.write(writer.write(bib_database))


