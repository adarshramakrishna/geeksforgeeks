import sys
import glob
from subprocess import call

if __name__ == "__main__":
    for book_format in ['mobi', 'epub', 'docx']:
        for book in glob.glob("./*/*." book_format):
            call("cp " + book + " ../goodies/geeksforgeeks/" + book_format, shell=True)
