"""
generate a book. takes two arguments: book name and version number.
"""
import re
import os
import sys
import glob
from subprocess import call

from clean import clean_html_files
from generate_covers import generate_cover

def custom_comparator(name1, name2):
    """
    cutom comparison function for sorting
    """
    numbers1 = re.findall("\d+", name1)
    numbers2 = re.findall("\d+", name2)
    if not numbers1 and not numbers2:
        return name1 > name2
    if not numbers1:
        return -1
    if not numbers2:
        return -1
    return int(numbers1[0])-int(numbers2[0])


def generate(book, version):
    """
    generate a book with a certain version
    """
    if book[-1] != "/":
        book = book + "/"
    version = "_" + version
    md_file = book + book[:-1] + version + ".md"
    html_file = book + book[:-1] + version + ".html"
    epub_file = book + book[:-1] + version + ".epub"
    cover_image = "covers/" + book[:-1] + ".png"
    print "cleaning html files,", "this might take a while..."
    clean_html_files(book)
    cleaned_html = sorted(glob.glob(book + "*_cleaned.html"), key=os.path.getmtime)
    print "generating", html_file, "..."
    call("cat " + "../bookcopyright/copyright.html " + " ".join(cleaned_html) + " > " + html_file, shell=True)
    generate_cover(book[:-1], version[1:])
    call('pandoc --latex-engine=xelatex ' + html_file + ' -o ' + html_file.replace('html', 'docx'), shell=True)
    print "generating", epub_file, "this might take a while..."
    call(['pandoc', '-o', epub_file, html_file, '--epub-metadata='+book+'metadata.xml', "--toc", "--toc-depth=2", "--epub-stylesheet=../styles/buttondown.css", "-f", "html-native_divs", "--epub-cover-image="+cover_image])
    print "generating", book + book[:-1] + version + ".mobi", "..."
    call(['kindlegen', epub_file])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "this program takes two arguments: a book name and a version"
        sys.exit()
    book = sys.argv[1]
    version = sys.argv[2]
    generate(book, version)
