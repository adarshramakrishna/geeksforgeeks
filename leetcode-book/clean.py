# -*- coding: utf-8 -*-
"""
clean local html files via boilerpipy. the tool removes the title of an article occasionally.
"""

import glob
import sys
import codecs
import os
import logging
import HTMLParser
from subprocess import call

import lxml.etree
import lxml.html as html
from bs4 import UnicodeDammit

from boilerpipy import (Extractor, isvalidhtml)


def insert_content(doc, html_doc, insert_string, insert_type):
    to_insert = html_doc.find('.//'+insert_type)
    doc.append(to_insert)
    return doc

def clean(file_name, directory="."):

    content = codecs.open(file_name, "r", 'utf-8').read()

    article = Extractor(content, loglevel = logging.INFO).extracted()

    if article is None:
        print "Error processing html file"
        sys.exit(1)
    html_parser = html.HTMLParser(encoding="utf-8")
    html_doc = html.fromstring(content, parser=html_parser)
    head_doc = html_doc.find('head')
    source_url = head_doc.cssselect('link[rel="canonical"]')[0].get('href')
    title = html_doc.find('.//title').text_content()

    # if the title is unfortunately removed by boilerpipy, then add it back in
    if "h2" not in article:
        article = "<h1>" + title[:title.rfind('-')] + "</h1>" + article

    reconstructed_body = "<html><body>" + article.replace("<h2", "<h1").replace("</h2>", "</h1>") + "</body></html>"
    source_header_string = "<h3>Source</h3>"
    source_link = "<p><a href='" + source_url +"' rel='tag'>" + source_url + "</a></p>"
    # further remove useless stuff
    body_doc = html.fromstring(reconstructed_body).find('body')
    try:
        post_content_doc = body_doc.xpath("//div[@class='post-content']")[0]
        post_content_doc.append(lxml.etree.XML(source_header_string))
        post_content_doc.append(lxml.etree.XML(source_link))
    except:
        print file_name

    basename = os.path.basename(file_name)
    cleaned_file = os.path.splitext(basename)[0] + "_cleaned.html"
    result = html.tostring(body_doc)
    with open(directory + cleaned_file, 'w') as cleaned_file_handle:
        cleaned_file_handle.write(result.encode('utf-8'))

def clean_html_files(directory = ""):
    for html_file in glob.glob(directory + '*.html'):
        if 'clean' not in html_file:
            try:
                clean(html_file, directory)
            except:
                print "WARNING: failed to clean", html_file

if __name__ == "__main__":
    clean(sys.argv[1])
    #clean_html_files("")
