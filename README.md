# WikiCitations Import Bot
This bot is capable of fetching and storing 
reference information from Wikipedia pages as structured data 
in a Wikibase instance. 

This bot has been developed by James Hare (version 1.0.0) 
and Dennis Priskorn (version 2) as part of the 
Turn All References Blue project which is led by 
Mark Graham head of The 
Wayback Machine department of the Internet Archive.

A Wikibase with millions of references and edges between 
them and the Wikipedia page(s) they are used on is useful
 for both Wiki(p|m)edians and researchers who wish to understand
 which websites are linked to which pages and used as references.

This is part of a wider initiative help raise the quality of sources in 
Wikipedia to and enable everyone in the world to make
 decisions based on trustworthy information that is sourced by 
trustworthy sources.

# What is Wikibase?
Wikibase is a FLOSS graph database which enables users to store large
amounts of information and query them using SPARQL.
Wikibase has been created by Wikimedia Deutchland and is 
maintained by them as of this writing.

# Why store the data about references in a graph database?
The advantages of having access to this data in a graph are many.
* Overview and visualization of references across (whole categories) of Wikipedia pages becomes possible.
* Overview of most cited websites in the world
* Using SPARQL it becomes easy to e.g. pinpint pages with less trustworthy sources
* Using the data over time can help follow and understand changes in patterns of referencing.
* and more...

# Supported templates
There are a lot of templates in use in the different Wikipedias. For now 
the bot only supports templates and parameters from English Wikipedia 
but intention is to code it in a way that avoids hardcoding of 
enwp specific templates and parameters.

## English Wikipedia templates
English Wikipedia has hundreds of special reference templates in use 
and a handful of widely used generic templates.

Currently the focus is on supporting the most widely used reference 
templates in English Wikipedia.

### List of currently supported templates
supported_templates = [
    "citation",  # see https://en.wikipedia.org/wiki/Template:Citation
    "cite q",
    "citeq",
    "isbn",
    "url",
    # CS1 templates:
    "cite arxiv",
    "cite av media notes",
    "cite av media",
    "cite biorxiv",
    "cite book",
    "cite cite seerx",
    "cite conference",
    "cite encyclopedia",
    "cite episode",
    "cite interview",
    "cite journal",
    "cite magazine",
    "cite mailing list" "cite map",
    "cite news",
    "cite newsgroup",
    "cite podcast",
    "cite press release",
    "cite report",
    "cite serial",
    "cite sign",
    "cite speech",
    "cite ssrn",
    "cite techreport",
    "cite thesis",
    "cite web",
]

# Running the bot in AWS
Because of security limitations of SSDB it is recommended 
to only run the bot on the same server as the SSDB instance.

Log into the AWS server via putty or a virtual terminal in Linux/Mac OSX. 
You will need to generate a public SSH key and have 
an account set up before being able to log in. 

Start GNU screen (if you want to have a persisting session)
`$ screen -D -RR`

Now you are ready to install and setup the bot.

# Installation
Clone the git repo:

`$ git clone https://github.com/internetarchive/wcdimportbot.git`

# Setup
Install the dependencies:

`$ pip install -r requirements.txt`

[Generate a botpassword](https://wikicitations.wiki.opencura.com/w/index.php?title=Special:UserLogin&returnto=Special%3ABotPasswords&returntoquery=&force=BotPasswords)

Copy config.py.sample -> config.py 
`$ cp config.py.sample config.py`
and 
enter your botpassword credentials. E.g. user: "test" and password: "q62noap7251t8o3nwgqov0c0h8gvqt20"
`$ nano config.py`

If you want to delete items from the Wikibase, ask an administrator of the Wikibase to become admin.


# Features
Currently the bot can be used to import pages one by one and to rinse the imported items from the Wikibase.
## Import a page
The bot can import any Wikipedia page (in English Wikipedia)

`$ python wcdimportbot.py --import "title of page"` 

## Rinse all items from the Wikibase
To delete all the imported items e.g. 
after changes in the data model run

`$ python wcdimportbot.py --rinse`

# Help
```
usage: wcdimportbot.py [-h] [-i IMPORT_TITLE] [--rinse]

    WCD Import Bot imports references and pages from Wikipedia

    Example adding one page:
    '$ wcdimportbot.py --import-title "Easter Island"'

    Example rinsing the Wikibase and the cache:
    '$ wcdimportbot.py --rinse'


optional arguments:
  -h, --help            show this help message and exit
  -i IMPORT_TITLE, --import-title IMPORT_TITLE
                        Title to import from a Wikipedia (Defaults to English Wikipedia for now)
  --rinse               Rinse all page and reference items and delete the cache
```