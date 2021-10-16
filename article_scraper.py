import requests
from bs4 import BeautifulSoup
from newspaper import Article
import csv
import nltk
import ssl
""" create the word cloud """
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "monospace"
import numpy as np

FEEDS = [
    "https://vice.com/rss",
    "https://www.wired.com/rss/",
    "https://www.theguardian.com/business/economics/rss",
    "https://www.theguardian.com/world/rss",
    "http://rss.slashdot.org/Slashdot/slashdotMain",
    ]

ARTICLES = []
DATA = []

for feed in FEEDS:
    response = requests.get(feed)
    #print(response.status_code)
    webpage = response.content
    soup = BeautifulSoup(webpage, features="xml")
    items = soup.find_all("item")
    for item in items:
        link = item.find("link").text
        ARTICLES.append(link)
#print(ARTICLES)
for url in ARTICLES:
    info = Article(url)
    info.download()
    info.parse()
    info.nlp()
    keywords = info.keywords
    text = info.text
    save = [url, keywords, text]
    DATA.append(save)
with open("scraped_articles.csv", "w") as csv_file:
    LABEL = ["URL", "Keywords", "Text"]
    writer = csv.writer(csv_file)
    writer.writerow(LABEL)
    writer.writerows(DATA)
    csv_file.close()


""" converters reconverts large list of strings as list
    eval is function which valuates a large string """
DATA_FRAME = pd.read_csv("scraped_articles.csv", converters={"Keywords":eval})

# print(DATA_FRAME.shape[0])
# print(DATA_FRAME.head())
#text = DATA_FRAME.Text[0] # full text
# print(DATA_FRAME.URL[4]) # url 
# print(text)
stopwords = set(STOPWORDS)
stopwords.update(["vice", "guardian", "wired"])
# print(stopwords)

""" loop through every list, take all keywords, make one big list """
keywords = [j for i in DATA_FRAME.Keywords for j in i]
sorted_keywords = " ".join(i for i in keywords)
#print(sorted_keywords)

""" collocations takes care of phrases """
word_cloud = WordCloud(stopwords=stopwords, max_words=150, background_color="white", collocations=False).generate(sorted_keywords)
plt.figure(figsize=[10,10])
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
