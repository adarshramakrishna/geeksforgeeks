import os
import glob
import sys
import string
from subprocess import call

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

stopwords = set()
single_letters = set(string.letters)
program_related = {'null', 'also', 'arr', 'char', 'child', 'code', 'col', 'cpp', 'data', 'driver', 'element', 'else', 'example', 'false', 'first', 'float', 'following', 'fun', 'function', 'given', 'idx', 'if', 'include', 'int', 'left', 'long', 'main', 'mid', 'new', 'newnode', 'newtnode', 'next', 'node', 'notranslate', 'number', 'one', 'org', 'output', 'output', 'point', 'print', 'printf', 'problem', 'program', 'return', 'right', 'root', 'row', 'second', 'sizeof', 'solution', 'struct', 'tags', 'tNode', 'temp', 'time', 'title', 'true', 'two', 'utility', 'unsigned', 'variable', 'void', 'want', 'will', 'stdio', 'stdlib', 'please', 'snode', 'brush', 'getchar', 'prints', 'functions', 'fun2', 'using', 'question'}
stopwords |= STOPWORDS
stopwords |= single_letters
stopwords |= program_related


def generate_cover(book_name):
    html_file = book_name + "/" + book_name + ".html"
    plain_text = book_name + "/" + book_name + ".txt"
    image_name = "covers/" + book_name + ".png"

    if not os.path.exists(plain_text):
        call("pandoc " + html_file + " -t plain -o " + plain_text, shell=True)

    text = open(plain_text).read()
    fig = plt.figure(frameon=False)
    fig.set_size_inches(4, 6)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    wordcloud = WordCloud(font_path='/Users/jing/Library/Fonts/Verdana.ttf', width=800, height=1200, stopwords=stopwords).generate(text)
    plt.imshow(wordcloud, aspect='normal')

    #plt.axis("off")
    plt.savefig(image_name, dpi=300)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        generate_cover(sys.argv[1])
