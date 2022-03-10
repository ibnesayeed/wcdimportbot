from typing import Optional

from src.models.wikimedia.wikipedia.templates.wikipedia_page_reference import WikipediaPageReference


class CiteNews(WikipediaPageReference):
    """This models the template cite news in English Wikipedia
    https://en.wikipedia.org/wiki/Template:Cite_news"""
    last1: Optional[str]
    first1: Optional[str]
    author_link1: Optional[str]
    last2: Optional[str]
    first2: Optional[str]
    author_link2: Optional[str]
    last3: Optional[str]
    first3: Optional[str]
    author_link3: Optional[str]
    last4: Optional[str]
    first4: Optional[str]
    author_link4: Optional[str]
    last5: Optional[str]
    first5: Optional[str]
    author_link5: Optional[str]
    display_authors: Optional[str]
    author_mask: Optional[str]
    name_list_style: Optional[str]
    date: Optional[str]
    year: Optional[str]
    orig_date: Optional[str]
    title: Optional[str]
    script_title: Optional[str]
    trans_title: Optional[str]
    url: Optional[str]
    url_status: Optional[str]
    format: Optional[str]
    editor1_last: Optional[str]
    editor1_first: Optional[str]
    editor1_link: Optional[str]
    editor2_last: Optional[str]
    editor2_first: Optional[str]
    editor2_link: Optional[str]
    editor3_last: Optional[str]
    editor3_first: Optional[str]
    editor3_link: Optional[str]
    editor4_last: Optional[str]
    editor4_first: Optional[str]
    editor4_link: Optional[str]
    editor5_last: Optional[str]
    editor5_first: Optional[str]
    editor5_link: Optional[str]
    display_editors: Optional[str]
    department: Optional[str]
    work: Optional[str]
    type: Optional[str]
    series: Optional[str]
    language: Optional[str]
    volume: Optional[str]
    issue: Optional[str]
    others: Optional[str]
    edition: Optional[str]
    location: Optional[str]
    publisher: Optional[str]
    publication_date: Optional[str]
    agency: Optional[str]
    page: Optional[str]
    pages: Optional[str]
    at: Optional[str]
    no_pp: Optional[str]
    arxiv: Optional[str]
    asin: Optional[str]
    bibcode: Optional[str]
    doi: Optional[str]
    doi_broken_date: Optional[str]
    isbn: Optional[str]
    issn: Optional[str]
    jfm: Optional[str]
    jstor: Optional[str]
    lccn: Optional[str]
    mr: Optional[str]
    oclc: Optional[str]
    ol: Optional[str]
    osti: Optional[str]
    pmc: Optional[str]
    pmid: Optional[str]
    rfc: Optional[str]
    ssrn: Optional[str]
    zbl: Optional[str]
    id: Optional[str]
    archive_url: Optional[str]
    archive_date: Optional[str]
    access_date: Optional[str]
    via: Optional[str]
    quote: Optional[str]
    postscript: Optional[str]
    ref: Optional[str]
    first: Optional[str]
    editor: Optional[str]
    last: Optional[str]
