from bs4 import BeautifulSoup as bf 
import requests
import sys
import os
from article import init_scrap,save_posts
print("=================================")
print("=============POST SCRAPER========")

def get_posts(url,key_word):
    resp_cont=init_scrap(url)
    heads=["h1","h2","h3","h4"]
    story=[]
    for head in resp_cont.find_all(heads):
        if list((map(lambda x: x.lower(),head.text.strip().split(" ")))).count(key_word)>0:
            print("============Available Story Links ==========")
            print(head.text.strip())
            print("=============================================")
            posts=requests.get(head.find("a").get("href"))
            results=bf(posts.text,'lxml')
            ps=[]
            for post in results.find_all("p"):
                ps.append(post.text.strip())
            
            story.append(ps)
    return story
save_posts(get_posts(url,key_wrd))
