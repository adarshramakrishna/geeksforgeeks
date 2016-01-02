# Geeksforgeeks as Books


## Get the books

Complete books are located in the `book` [branch](https://github.com/gnijuohz/geeksforgeeks-as-books/tree/book).

Books will be updated regularly to keep up with [Geeksforgeeks.org](http://geeksforgeeks.org).

## App

There is an App now! [Geeksforgeeks Reader](https://itunes.apple.com/us/app/geekreader/id991254978?ls=1&mt=8) makes it easier to read on your iOS devices. This app just got started. Feature requests are welcome.

## Note

[Geeksforgeeks.org](http://geeksforgeeks.org) has (finally) updated its user interface lately and optimized for mobile devices. This project started when the old geeksforgeeks site was clumsy.

## Books
To get the latest version of the books, look under the directory called goodies. Each book under `geeksforgeeks-books` is generated with articles under a tag/category on [geeksforgeeks.org][1]. The book under `leetcode-book` is generated from the articles on [leetcode.com](http://leetcode.com/).

## Tools

If you want to generate the books yourself. Here is an incomplete guide.

### Requirements

1. install [Scrapy][2]. It's is used to download webpages from `geeksforgeeks` and `leetcode`. It follows the next page link and downloads webpages.

    Install it with `pip install scrapy`. I created two separate scrapy projects called `geeksforgeeks` and `leetcode` to download wepages from the sites.

2. [lxml][10] and [Boilerpipy][6] (or [BeautifulSoup][11]). After downloading the html files, you need to extract the articles from them, I'm using `Boilerpipy` because it can handle webpages with different layout. But if you are only interested in the `geeksforgeeks` site, you can just use `lxml` to extract the articles. It will probably be faster too.

    `Boilerpipy` also removes the title of an article sometimes. So I had to do some post-processing with `lxml` after to add the title back.

3. [Pandoc][3]. It's used to convert html files or markdown files to epub, pdf and docx format files. The latex engine used in Pandoc can't handle gif images so only a few pdf books have been generated so far.

4. [kindlegen][4] is needed to generate `mobi` files for reading on Kindle or the Kindle App.
5. [WordCloud][5]. The book covers are generated with `wordcloud` with a bit of meta in mind.

## How To

1. **Crawling with Scrpay.** Go to the `geeksforgeeks` subdirectory and run commands *like* `scrapy crawl geeksforgeeks -a category=category -a name=name`.

    For example, running `scrapy crawl geeksforgeeks -a category=tag -a name=pattern-searching` will crawl from the page `http://www.geeksforgeeks.org/tag/pattern-searching/`. category and name are two arguments the spider takes. On geeksforgeeks, things can be organized by `tag` or `category`. Specify the category/tag and the name, Scrapy will do the rest for you.

2. **Generate a book.** Now go into the `geeksforgeeks-books` subdirectory and you should be able to find a directory called `pattern-searching`. Now run `python generate_book.py pattern-searching 1.0`. It will clean the html files, concatenate the cleaned files into one html file, then use `pandoc` to create an epub and pdf format files from the it. In the end a mobi file is created using `kindlegen`.


## To Do

### Style the books
Style the books better. Those books are essentially styled via `css`. Therefore styling `<pre>` and `<code>`, for instance, will style the code of the `epub` books.

### Generate pdf format books
Convert `gif` images to `png` and use them instead so `pandoc` can handle them.

## Contribute

### Book

Every tag or category on `geeksforgeeks.org` can be turned into a book. So you are welcome to add/suggest more books.

### Style

The style for generating `epub` books is under `styles` subdirectory. `epub` books are styled via `css`. Welcome to submit your stylesheets.

## License

The content in the books *doesn't* belong to me. I created the books so that I can read them offline on iPad or Kindle, and (hopefully) for a better reading experience.

The content on geeksforgeeks.org is licensed under Creative Commons
Attribution-NonCommercial-NoDerivs 2.5 India. See the license [here][7].

The copyright of the content on `leetcode` belongs to the site and its owner.

The code in this project is licensed under Apache License, version 2.0. See the
license [here][8].


## Authors

Jing Zhou, gnijuohz at gmail.com.

## Contributors

@lebshah

## Issues

You can report issue right here.


[1]:http://www.geeksforgeeks.org/
[2]:http://scrapy.org/
[3]:http://johnmacfarlane.net/pandoc/
[4]:http://www.amazon.com/gp/feature.html?docId=1000765211
[5]:https://github.com/amueller/word_cloud
[6]:https://github.com/harshavardhana/boilerpipy
[7]:http://creativecommons.org/licenses/by-nc-nd/2.5/in/deed.en_US
[8]:http://www.apache.org/licenses/LICENSE-2.0
[9]:http://www.gfgreader.info/
[10]:http://lxml.de/
[11]:http://www.crummy.com/software/BeautifulSoup/
[12]:https://github.com/gnijuohz/geeksforgeeks-as-books/releases/latest
