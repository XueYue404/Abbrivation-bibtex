# BibTex Abbrivation Converter
For Bibtex citations used in LaTex, I wrote a simple script to convert names of journals and conferences into abbreviations to fit the journal's requirements. Common abbreviations were found in the IEEE-reference-guide, but you can customize any abbreviation you want by modifying the excel file! Also, arXiv articles were treated specially in the code.

## Dependency 
1. pandas  
2. bibtexparser  
3. tqdm
  
## Usage
0. Generate the .bib file using any document management tool, Zotero for example. 
1. Put the excel file and the python script in the same folder, as well as your .bib file.  
2. Run the script as: 
```python 
python bibtex_generator.py -i example.bib -o output.bib # -h for help
```
3. Enjoy!
