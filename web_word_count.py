import time
import pandas as pd
from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

urlpage = 'https://www.cnn.com'
spc_chars = '-.,\n()[]+&' #special chars
res = []

opts = Options()
opts.headless = True

driver = webdriver.Firefox(options=opts)
driver.get(urlpage)
#time.sleep(60)

#grab source via selenium driver
source = driver.page_source
driver.close()

# f = open("scratch.txt", "w", encoding="utf-8")
# f.write(source)
# f.close()

#remove <script> and <style> tags and make the list
soupSrc = BeautifulSoup(source, features="html.parser")
for script in soupSrc(["script","style"]):
        script.decompose()

strips = list(soupSrc.stripped_strings)

#make translation table, mapping special characters to None then
#translate special characters to blank
trans_table = str.maketrans('', '', spc_chars)
res = [s.translate(trans_table) for s in strips]

#get count for the words, sort it by count, and put in dataframe
count = Counter(res).most_common()
countSorted = sorted(count, key=lambda x: x[1], reverse=True)
df = pd.DataFrame.from_records(countSorted, columns=['Word', 'Count'], index=None)

print(df)
print('Closing program now!!!')

