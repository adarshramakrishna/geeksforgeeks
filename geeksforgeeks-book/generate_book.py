import re
import os
import sys
import glob
from subprocess import call
from datetime import datetime

from clean import clean_html_files
from generate_covers import generate_cover

def generate(book):
    if book[-1] != "/":
        book = book + "/"
    print("generating " + book[:-1])
    md_file = book + book[:-1]  + ".md"
    html_file = book + book[:-1]  + ".html"
    epub_file = book + book[:-1]  + ".epub"
    cover_image = "covers/" + book[:-1] + ".png"
    print "cleaning html files,", "this might take a while..."
    clean_html_files(book)
    cleaned_html = sorted(glob.glob(book + "*_cleaned.html"), key=lambda x: datetime.strptime(x.split('_')[-2], '%Y-%m-%dT%H:%M:%S'))
    print "generating", html_file, "..."
    call("cat " + "../bookcopyright/copyright.html " + " ".join(cleaned_html) + " > " + html_file, shell=True)
    try:
        generate_cover(book[:-1])
    except:
        print "can't generate cover for", book[:-1]
    call('pandoc --latex-engine=xelatex ' + html_file + ' -o ' + html_file.replace('html', 'docx'), shell=True)
    print "generating", epub_file, "this might take a while..."
    call(['pandoc', '-o', epub_file, html_file, '--epub-metadata='+book+'metadata.xml', "--toc", "--toc-depth=2", "--epub-stylesheet=../styles/buttondown.css", "-f", "html-native_divs", "--epub-cover-image="+cover_image])
    print "generating", book + book[:-1] + ".mobi", "..."
    call(['kindlegen', epub_file])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "this program takes a book name"
        sys.exit()
    book = sys.argv[1]
    generate(book)
