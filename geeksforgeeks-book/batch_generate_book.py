import os
import glob
import sys
import datetime
from generate_book import generate

if __name__ == "__main__":
    with open('../bookcopyright/copyright.html', 'w') as f:
        f.write("""<h1> Copyright </h1>

        <div class="copyright-content">
            <p>
            The content of this book comes from <a href="http://geeksforgeeks.org">geeksforgeeks.org</a> and it's licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/2.5/in/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 2.5 India</a>
            </p>
        </div>

        <div class="book-maker">
            <p>
            Made by <a href="http://www.jing-zhou.me/">Jing</a>. 2015.
            </p>
            <p> Updated on """ + datetime.date.today().strftime("%B %d, %Y") +
            """
            <p>
            <p>
            Head over to <a href="https://github.com/gnijuohz/geeksforgeeks-as-books">this
                github repo</a> to report issues or contribute.
            </p>
        </div>""" )
    for dir_name in glob.glob('*'):
        if os.path.isdir(dir_name) and dir_name not in ["covers", ".ipynb_checkpoints"]:
            generate(dir_name)
