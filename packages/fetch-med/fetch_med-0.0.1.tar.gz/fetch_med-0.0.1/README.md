# Pubmed-Paper-Fetcher-and-Processor

Tools Used - ChatGPT https://chatgpt.com/, Stackoverflow http://stackoverflow.com/

*This package is designed for searching the PubMed database and retrieving data, including the paper’s ID, title, publication date, non-academic authors, and their metadata.*

**WITH** command-line syntax:
--
- -h,--help  : show this help message and exit
- -d,--debug : debug the program
- -q,--query : query to get papers
- -f,--file  : path of the output file
- --force    : force article to be added even if author is not present
- -c,--count : max number of articles to fetch and parse. By default all
- -e,--ext   : supports: .json, .csv and .xlsx

For Example:

`get-papers-list --debug --query covid-19 --force -c 2`

**WITHOUT** command-line syntax:
--
Run: `get-papers-list`


_____
Note :
- *If no file or incorrect file path is given then output will be printed on console*
- *Dont include -e or --ext to run the program or it will give you list of supported extentions*



