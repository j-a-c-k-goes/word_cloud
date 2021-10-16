from newspaper import Article
import nltk
import ssl

#_create_unverified_https_context = ssl._create_unverified_context
#ssl._create_default_https_context = _create_unverified_https_context
#nltk.download()


article = Article("https://www.cnbc.com/2021/02/02/5-freelance-jobs-where-you-can-earn-100000-or-more-during-pandemic.html")
article.download()
article.parse()
article.nlp()

title = article.title
link = article.url
authors = article.authors
date = article.publish_date
image = article.top_image
summary = article.summary
text = article.text

print("@"*20)
print(f"title: {title}")
print(f"link: {link}")
print(f"authors: {authors}")
print(f"publish date: {date}")
print(f"top image: {image}")
print(f"summary: ")
print(summary)
print("@"*20)
