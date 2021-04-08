# picky_pachyderm

Various python scripts, that I have made to satisy my curiosity.

word_count.py
This script reads in a file, and then "cleans" the text; basically removing any occurence of special characters and numbers.  Then the text is split and stored in a python list.  Then using the Counter library, a list of tuples containing the word and the count is generated [(word, count),...,(word, count)].  This list of tuples gets sorted via the sorted() function using the count as the key to sort (key=lambda x: x[1]).  Finally, a pandas dataframe is generated from this sorted list of tuples.  The dataframe presents the data in row and column format for easier reading. 
