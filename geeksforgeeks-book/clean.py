# -*- coding: utf-8 -*-
"""
clean local html files
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
    cleaned_file = os.path.splitext(basename)[0] + "_cleaned.html"
    # don't clean files that already have been cleaned
    if os.path.isfile(cleaned_file):
        return
    content = codecs.open(file_name, "r", 'utf-8').read()

    head_pos = content.find('<head>')

    # insert the encoding of the file
    content = content[:head_pos+6] + '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">' + content[head_pos+6:]
    article = Extractor(content, loglevel = logging.INFO).extracted()

    if article is None:
        print "Error processing html file"
        sys.exit(1)
    html_parser = html.HTMLParser(encoding="utf-8")
    html_doc = html.fromstring(content, parser=html_parser)
    head_doc = html_doc.find('head')
    source_url = head_doc.cssselect('meta[property="og:url"]')[0].get('content')
    title = html_doc.find('.//title').text_content()

    # if the title is unfortunately removed by boilerpipy, then add it back in
    if "h2" not in article:
        article = "<h1>" + title[:title.rfind('-')] + "</h1>" + article

    reconstructed_body = "<html><body>" + article.replace("<h2", "<h1").replace("</h2>", "</h1>") + "</body></html>"
    source_header_string = "<h3>Source</h3>"
    source_link = "<p><a href='" + source_url +"' rel='tag'>" + source_url + "</a></p>"
    # further remove useless stuff
    body_doc = html.fromstring(reconstructed_body).find('body')
    for bad in body_doc.xpath("//div[@class='comments-main']"):
        bad.getparent().remove(bad)
    for ad_by_google in body_doc.xpath("//ins[@class='adsbygoogle']"):
        ad_by_google.getparent().remove(ad_by_google)
    for bad_h3 in body_doc.xpath("//h3"):
        bad_h3.getparent().remove(bad_h3)
    for pre_tag in body_doc.xpath("//pre"):
        if 'class' in pre_tag.attrib:
            pre_tag.attrib.pop('class')
        if 'title' in pre_tag.attrib:
            pre_tag.attrib.pop('title')

    post_content_doc = body_doc.xpath("//div[@class='entry-content']")[0]
    post_content_doc.append(lxml.etree.XML(source_header_string))
    post_content_doc.append(lxml.etree.XML(source_link))
    basename = os.path.basename(file_name)
    result = html.tostring(body_doc)
    # replace <code> with <code><pre> for styling later.
    result = result.replace('<pre>', '<pre> <code>').replace('</pre>', '</code> </pre>')
    with open(directory + cleaned_file, 'w') as cleaned_file_handle:
        cleaned_file_handle.write(result.encode('utf-8'))

def clean_html_files(directory = ""):
    for html_file in sorted(glob.glob(directory + '*.html'), key=os.path.getmtime):
        if 'clean' not in html_file:
            try:
                clean(html_file, directory)
            except:
                print "WARNING: failed to clean", html_file

if __name__ == "__main__":
    clean(sys.argv[1])
    #clean_html_files("")
