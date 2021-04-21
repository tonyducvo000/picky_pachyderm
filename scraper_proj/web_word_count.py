import time
from data_source import urlpage
import re
import pandas as pd
from common_words import rem_words
from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def scrape(urlpage):
        pd.set_option('display.max_rows', None)
        spc_chars = "+?.:%',$[]&"
        spc_char_list = ['.', ',', '\n', '(', ')', '[', ']', '+', '&', '\\', ':', '-', '•', '•', '•', '?', '™', '', '|', '👩', '©']

        res = []

        opts = Options()
        opts.headless = True

        driver = webdriver.Firefox(options=opts)
        driver.get(urlpage)
        #time.sleep(60)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        source = driver.page_source
        driver.close()

        # f = open("scratch.txt", "w", encoding="utf-8")
        # f.write(source)
        # f.close()

        soupSrc = BeautifulSoup(source, features="html.parser")
        for script in soupSrc(["script","style"]):
                script.decompose()

        strips = list(soupSrc.stripped_strings)
        strips = list([word for line in strips for word in line.split()])

        # st = open("strips.txt", "w", encoding="utf-8")
        #
        # st.write("+++++++++++++++++++++++++++++++\n")
        # st.write(urlpage + "\n")
        #
        # for index in strips:
        #         st.write(str(index)+"\n")
        # st.close()

        for char in spc_char_list:
                if char in strips:
                        strips.remove(char)

        trans_table = str.maketrans('', '', spc_chars)
        res = [s.translate(trans_table) for s in strips]

        #remove numbers in list
        #res = [x for x in res if not (x.isdigit())]
        #print(res)

        #remove numbers from res list
        pat_num = "^(\d+)$"
        num_filt = list(filter(lambda x: not re.match(pat_num, x), res))

        #remove simple one word (i.e., 'a' or 'A')
        #or two letter words (e.g., 'As', 'by', 'go', etc), these don't hold much significance
        #keep two capitalized letters (US, UN, EU, etc) since these have meaning
        pat_word = "^(\w{1})$|^([A-Z][a-z])$|^([a-z]{2})$"
        full_filt = list(filter(lambda x: not re.match(pat_word, x), num_filt))

        #remove other common words
        for index_rm in rem_words:
                for index_f in full_filt:
                        if re.match(index_rm, index_f):
                                full_filt.remove(index_f)

        #Any item filtered from above becomes '' in list, remove ''
        for index in full_filt:
                if index == '' or index == '--' or index == '—':
                        full_filt.remove(index)

        print(full_filt)
        #res = [index.lower() for index in res ]

        with open("scratch.txt", "w", encoding="utf-8") as scratch:
                for index in full_filt:
                        scratch.write(str(index) + "\n")

        scratch.close()

        #get count for the words, sort it by count, and put in dataframe
        count = Counter(full_filt).most_common()
        countSorted = sorted(count, key=lambda x: x[1], reverse=True)

        df = pd.DataFrame.from_records(countSorted, columns=['Word', 'Count'], index=None)

        file = open("result.txt", "w", encoding="utf-8")
        file.write(urlpage)
        file.write("\n")
        file.write(str(df))
        file.write("\n\n++++++++++++++++++++++++++++++++\n\n")
        file.close()

        print(f'Building {urlpage} table...')

scrape(urlpage)
# for index in urllist:
#         scrape(index)