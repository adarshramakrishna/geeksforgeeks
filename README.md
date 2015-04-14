# Geeksforgeeks as Books

## Site

To read random post, head to [gfgreader.info](http://www.gfgreader.info/).

## What's new

### Bug fix

1. All articles now have titles. So table of content shows all articles.
2. Encoding problem has been fixed.

### New book

1. A book of Amazon interview questions under `goodies/interview_questions`
2. Several pdf books have been generated.


## Books

Look under subdirectory `goodies`. Each book under `geeksforgeeks` is generated with articles under a tag/category on [geeksforgeeks.org][1]. The book under leetcode is generated from the articles on [leetcode.com](http://leetcode.com/).

Here's how the books look like in the iBooks App and Kindle App on my iPad. Kindle hasn't been tested.

![Book covers](https://s-media-cache-ak0.pinimg.com/originals/25/15/f5/2515f556de2b199d4af8a8aacdebc7c3.jpg)
Book covers are made of word clouds based on the book content using [word_cloud](https://github.com/amueller/word_cloud)  

![On Ipad](https://s-media-cache-ak0.pinimg.com/originals/1d/28/d3/1d28d3e3148d2c91d22e837ace64c0ce.jpg)

![On Kindle App](https://s-media-cache-ak0.pinimg.com/originals/2b/86/53/2b8653eff7aaa191a80263de32c29651.jpg)

## Tools

Want to create a book from the `geeksforgeeks` site yourself? No problem. But you'll need some tools to get started. Apart from `Python 2.x` you also need the following tools.


### 1. Scrapy

[Scrapy][2] is used to download webpages from `geeksforgeeks` and `leetcode`. It makes it super easy to do so with its rules.

Install it with `pip install scrapy`

### 2. Boilerpipy

So you have the html files locally. But those html files have many other stuff you don't want. You only want... goodies.
No problem. Check out [boilerpipy][6], it can remove all the unnecessary stuff like header and comments, leaving you with only the article itself. It has the functionality of Pocket or Readability you might be familiar with.

However, I've found that it also removes the title of an article sometimes. So I had to do some post-processing with `lxml` after to add the title back.


### 3. Pandoc

[Pandoc][3] is used to convert html files or markdown files to epub, pdf and docx files. The latex engine used in Pandoc can't handle gif images so only a few pdf books have been generated so far.

### 4. Kindlegen

You'll need [kindlegen][4] to generate `mobi` files so you can read on your beloved Kindle or Kindle App. Download it from the linked Amazon webpage and install.

You just need to use `kindlegen awesome.epub` and it'll give you a file called `awesome.mobi`.

## How To

### 1. Crawling with Scrpay
Go to the `geeksforgeeks` subdirectory and run commands *like* `scrapy crawl geeksforgeeks -a category=category -a name=name`.

For example, running `scrapy crawl geeksforgeeks -a category=tag -a name=pattern-searching` will crawl from the page `http://www.geeksforgeeks.org/tag/pattern-searching/`. category and name are two arguments our spider takes. On geeksforgeeks, things can be organized by `tag` or `category`. Specify the category/tag and the name, Scrapy will do the rest for you.


### 2. Generate a book  

Following the example in 1, now go into the `geeksforgeeks-books` subdirectory and you should be able to find a directory called `pattern-searching`. Now run `python generate_book.py pattern-searching`. It will first clean the html files, concatenate the cleaned files into one, then use `pandoc` to create an epub file from the markdown file. In the end a mobi file is created using `kindlegen`.

Yay! Done!

## To Do

### Style the books

Style the books better. Those books are essentially styled via `css`. Therefore styling `<pre>` and `code` tag, for instance, will style the code of the `epub` books.

## Contribute

I've only worked on this project for a few days since I had the idea. It has huge room to improve. It's the first time I used `Scrapy` and `pandoc`.  

You can contribute in many ways. Besides contributing code to this project. You are more than welcome to contribute in the following ways.

### Book

Every tag or category on `geeksforgeeks.org` can be turned into a book. So you are welcome to add/suggest more books.

### Style

The style for generating `epub` books is under `styles` subdirectory. `epub` books are styled via `css`. Welcome to submit your stylesheets.

## License

The content in the books *doesn't* belong to me. I created the books so other people and me can read them offline on iPad or Kindle, and (hopefully) for a better reading experience.

The content on geeksforgeeks.org is licensed under Creative Commons
Attribution-NonCommercial-NoDerivs 2.5 India. See the license [here][7].

The content on `leetcode` belongs to the site.

The code in this project is licensed under Apache License, Version 2.0. See the
license [here][8].

## Authors

Jing Zhou, gnijuohz at gmail.com.


[1]:http://www.geeksforgeeks.org/
[2]:http://scrapy.org/
[3]:http://johnmacfarlane.net/pandoc/
[4]:http://www.amazon.com/gp/feature.html?docId=1000765211
[5]:https://github.com/gnijuohz/boilerpipy
[6]:https://github.com/harshavardhana/boilerpipy
[7]:http://creativecommons.org/licenses/by-nc-nd/2.5/in/deed.en_US
[8]:http://www.apache.org/licenses/LICENSE-2.0
