# Calabash Metadata Webscraping Project

## Intro
*Calabash: a journal of Caribbean arts and letters* was an open access journal published from 2000-2008 by New York University's Graduate Program in Spanish & Portuguese Languages & Literatures. As part of a project to migrate the site to the Faculty Digital Archive, NYU Libraries' institutional repository, the journal's website will be scraped to produce preliminary metadata for each article.

## Spiders
This repository contains three spiders created using [Scrapy](https://docs.scrapy.org/en/latest/index.html). 

1. **vol1no1**: misleadingly named, since it actually works for volumes 1-3
2. **vol4-5**: works for volumes 4 and 5, but must be run separately for each issue
3. **contributors**: scrapes author names and bios from the contributor indexes

It also contains an earlier spider (**vol4**) that didn't catch all author names.

## Workflow
1. Run spiders to scrape data, with parameters -o {filename}.csv to output data. Files were named by volume and/or issue number.
2. Import individual CSV files for volumes 4 and 5 into their own OpenRefine projects and apply transformations (provided in this repository as JSON for documentation purposes). Export transformed files from OpenRefine to CSV.
3. Import transformed CSV files into a single Google Sheets workbook. Use the autofill feature to "fill up" cells so that the correct author's name is in the cell corresponding to their article. Export as a single CSV file containing all article rows.
4. Import combined csv into OpenRefine. Derive PDF filenames from scraped PDF links. Derive volume and issue numbers from issue URL. Split/cluster/combine author names. Add constant data (issn, journal title, dates, publisher). Export as a single CSV file.
5. Add DOIs, collection IDs, and rights statements. Rename columns to conform to DSpace template and delete extraneous columns.


 
