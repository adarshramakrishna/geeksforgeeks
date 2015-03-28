"""
generate a book. takes two arguments: book name and version number.
"""
import re
import sys
import glob
from subprocess import call

from clean import clean_html_files
from generate_covers import generate_cover

def custom_comparator(name1, name2):
    numbers1 = re.findall("\d+", name1)
    if not numbers1:
        return -1
    numbers2 = re.findall("\d+", name2)
    if not numbers2:
        return -1
    return int(numbers1[0])-int(numbers2[0])


def generate(book, version):
    if book[-1] != "/":
        book = book + "/"
    version = "_" + version
    print "cleaning html files,", "this might take a while..."
    clean_html_files(book)
    cleaned_html = sorted(glob.glob(book + "*_cleaned.html"), cmp=custom_comparator)
    md_file = book + book[:-1] + version + ".md"
    html_file = book + book[:-1] + version + ".html"
    epub_file = book + book[:-1] + version + ".epub"
    cover_image = "covers/" + book[:-1] + ".png"
    print "generating", html_file, "..."
    call("cat " + "../bookcopyright/copyright.html " + " ".join(cleaned_html) + " > " + html_file, shell=True)
    generate_cover(book[:-1], version[1:])
    print "generating", epub_file, "this might take a while..."
    call(['pandoc', '-o', epub_file, html_file, '--epub-metadata='+book+'metadata.xml', "--toc", "--toc-depth=2", "--epub-stylesheet=../styles/buttondown.css", "-f", "html-native_divs", "--epub-cover-image="+cover_image])
    print "generating", book + book[:-1] + version + ".mobi", "..."
    call(['kindlegen', epub_file])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "this program takes two arguments"
        sys.exit()
    book = sys.argv[1]
    version = sys.argv[2]
    generate(book, version)
