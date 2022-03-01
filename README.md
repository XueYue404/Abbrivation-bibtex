# Abbrivation-bibtex
For Bibtex citations used in LaTex, I write a simple script to convert names of journals and conferences into abbreviations. Common abbreviations are found in the IEEE-reference-guide, but you can customize any abbreviation that you want by adding/modifying the excel file! ArXiv articals were treated specifically in the code.

## Dependency 
1. pandas  
2. bibtexparser  
3. tqdm
  
## Usage
0. Generate the .bib file using any document management tool, Zotero for example. 
1. Put the excel file and the python script in the same folder, as well as your .bib file.  
2. Change the name of .bib file in the python script, and run it. （It will overwrite the original .bib file）
3. Enjoy!
