from enum import Enum

# WCD = WikiCitations Database


class WCDItem(Enum):
    WIKIPEDIA_REFERENCE = "Q4"
    WIKIPEDIA_PAGE = "Q6"
    ENGLISH_WIKIPEDIA = "Q3"


class WCDProperty(Enum):
    """Mapping for WikiCitations Wikibase"""

    ACCESS_DATE = "P37"
    ARCHIVE_DATE = "P39"
    ARCHIVE_URL = "P38"
    AUTHOR = "P7"
    AUTHOR_NAME_STRING = "P15"
    DOI = "P33"
    EDITOR = "P6"
    EDITOR_NAME_STRING = "P40"
    FAMILY_NAME = "P5"
    GIVEN_NAME = "P4"
    CITATIONS = "P19"
    FULL_WORK_AVAILABLE_AT_URL = "P23"
    HASH = "P30"
    HOST_STRING = "P47"
    INSTANCE_OF = "P10"
    INTERVIEWER_STRING = "P48"
    ISBN_10 = "P28"
    ISBN_13 = "P32"
    ISSUE = "P24"
    LAST_UPDATE = "P43"
    LUMPED_AUTHORS = "P46"
    MEDIAWIKI_PAGE_ID = "P18"
    NAME_MASK = "P45"
    ORCID = "P31"
    PAGES = "P25"
    PMID = "P34"
    PUBLICATION_DATE = "P12"
    PUBLISHED_IN = "P17"
    RETRIEVED_DATE = "P29"
    PAGE_REVISION_ID = "P42"  # string
    SERIES_ORDINAL = "P14"  # aka author position # quantity
    SOURCE_WIKIPEDIA = "P9"
    STRING_CITATIONS = "P36"
    TEMPLATE_NAME = "P8"
    TITLE = "P20"  # monolingual text
    TRANSLATOR_NAME_STRING = "P41"
    URL = "P2"
    VOLUME = "P27"
    WEBSITE = "P13"
    WEBSITE_STRING = "P35"
    WIKIDATA_QID = "P44"  # external id
