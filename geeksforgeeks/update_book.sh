# this is a cron job script
cd ~/Awesome/github/geeksforgeeks-books/geeksforgeeks
python scrapy_books.py
cd ../geeksforgeeks-book
python batch_generate_book.py
python copy_to_goodies.py
git add -A
git commit -m"updating books"
git push
