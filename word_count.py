import re
import pandas as pd
from collections import Counter

text = open("textfile.txt", "r", encoding='utf-8')
text = text.read()

spc_chars = '-.,\n()[]' #special chars

#remove special chars and numbers
for char in spc_chars:
    text = text.replace(char, '')
text = text.lower()
text = re.sub(r'[0-9]+', '', text)

text = text.split()

count = Counter(text).most_common()

wordSorted = sorted(count, key=lambda x: x[1], reverse=True)

df = pd.DataFrame.from_records(wordSorted, columns=['Word', 'Count'], index=None)
print(df)