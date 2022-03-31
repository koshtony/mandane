from bs4 import BeautifulSoup as bs
import requests
import os
def init_scrap(url):
    web=requests.get(url)
    web_cont=bs(web.text,'lxml')
    return web_cont

def fetch_posts(url,key_wrd):
    article=init_scrap(url)
    heads=["h1","h2","h3","h4"]
    all_posts=[]
    for art in article.find_all("a"):
        if art.find(heads)==None:
            pass
        else:
            if list(map(lambda x:x.lower(),art.find(heads).text.strip().split(" "))).count(key_wrd):
                #mini_art=init_scrap(art.text)
                posts=init_scrap(url+art.get("href"))
                posts_=[]
                for post in posts.find_all("p"):
                    posts_.append(post.text.strip())
                all_posts.append(posts_)
    return all_posts

def save_posts(obj):
    if len(obj)>0:
        print(str(obj)+" posts found")
        fnam=input("filename>>")
        create_file(fnam,obj)
def create_file(name,obj):
    for i in range(len(obj)):
        post_i=" ".join(obj[i])
        f_names=name+str(i)+".doc"
        files=open(f_names,"w",encoding="utf-8")
        files.write(post_i)
        files.close()
    print("=====files saved in: ",os.getcwd())
    
save_posts(fetch_posts(url,key_wrd))