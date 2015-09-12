import os
import glob
from subprocess import call

def scrapy_all():
    for dir_name in glob.glob('../geeksforgeeks-book/*'):
        if os.path.isdir(dir_name) and dir_name.split('/')[-1] not in ["covers", ".ipynb_checkpoints"]:
            book_name = dir_name.split('/')[-1]
            if book_name in {"advance-data-structures", "backtracking", "amazon", "Array", "BinarySearchTree", "divide-and-conquer", "dynamic-programming", "Greedy-Algorithm", "Hashing", "Heap", "LinkedList", "MathematicalAlgo", "Matrix", "microsoft", "Misc", "pattern-searching", "Queue", "recursion", "Stack", "tree-travera"}:
                call('scrapy crawl geeksforgeeks -a name=' + book_name + ' -a category=tag', shell=True)
            else:
                call('scrapy crawl geeksforgeeks -a name=' + book_name + ' -a category=category', shell=True)
scrapy_all()
