from article import init_scrap
from termcolor import colored
def fetch_art(url,key_wrd):
    article=init_scrap(url)
    heads=["h1","h2","h3","h4"]
    all_posts=[]
    for art in article.find_all(heads):
        if art.text=="Forbidden":
            print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
            print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
            print(colored(".....Access Denied.....","red"))
            print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
            print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
            exit()
        if art.find("a")==None:
            pass
        else:
            
            if list(map(lambda x:x.lower(),art.find("a").text.strip().split(" "))).count(key_wrd)>0:
                
                posts=init_scrap(url+art.find("a").get("href"))
                posts_=[]
                for post in posts.find_all("p"):
                    posts_.append(post.text.strip())
                all_posts.append(posts_)
    if len(all_posts)==0:
        print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
        print(colored("           No articles matching your key word ","red"))
        print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","red"))
    return all_posts
