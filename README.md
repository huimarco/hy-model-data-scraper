# Description
A tool that web scrapes previous day financial markets data used for the high yield model:
* ICE BofA US High Yield Index Total Return Index Value
* NASDAQ Composite Price
* Value Line Geometric Index Price
* NYSE Advances
* NYSE Declines
* Crude Oil WTI Futures Prices 

Scraped numbers are pasted to the last row in a specified Excel file; it will not overwrite existing cells.

# Instructions
Create a ```config.json``` file and populate it with the following piece of code:
```
{
    "excel_file_path": [YOUR EXCEL FILEPATH]
}  
```
Once that is done, run ```main.py```.
