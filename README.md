
Repo for my collection of python scripts.

1.  word_count.py  
This script reads in a file, and then "cleans" the text; basically removing any occurence of special characters and numbers.  Then the text is split and stored in a python list.  Then using the Counter library, a list of tuples containing the word and the count is generated [(word, count),...,(word, count)].  This list of tuples gets sorted via the sorted() function using the count as the key to sort (key=lambda x: x[1]).  Finally, a pandas dataframe is generated from this sorted list of tuples.  The dataframe presents the data in row and column format for easier reading. 

2.  web_word_count.py  
A web scraper using Selenium, Beautiful Soup, and Pandas.  This script scrapes all text for a given URL and outputs the data in a pandas dataframe.
Using `urllib.request.urlopen()` will only retrieve the raw html file from the server, with dynamic elements unrendered by the 
browser. Thus, any text found withn these dynamic features will not be captured.  

    A solution to this problem is to have the dynamic features rendered by the browser, then capture the text
using selenium using `driver.get(urlpage)`.  Once the text is captured, the <script> and <style> tags are removed with Beautiful Soup, as they 
are not necessary.  Special characters can be filtered by using a translation table, `str.maketrans('','',spc_chars)`
where the special characters are mapped to ''.  Then each character will be scanned, and if a special character is found, it is translated to '' 
using `s.translate()`.  
  
    Finally the words are counted using `Counter().most_common` and stored as a Python list of (word, count) tuples. 
The list can be sorted by count number using `key=lambda x: x[1]` as a parameter to the `Sorted()` function.
The sorted list is then placed in a Pandas dataframe for presentation.
