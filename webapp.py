from flask import Flask,render_template,request
from article import save_posts,fetch_posts,create_file
from content import get_posts
from article_w import fetch_art
web=Flask(__name__,template_folder="template")
web.config["SECRET_KEY"]="pepcraper"
@web.route("/",methods=["GET","POST"])
def main():
    posts=[]
    if request.method=="POST":
        url=request.form.get("url")
        word=request.form["word"]
        sel=request.form["option"]
        if sel=="norm":
            
            posts.append(fetch_posts(url,word))
        else: 
            print("no")

    return render_template("menu.html",posts=posts)
if __name__=="__main__":
    web.run(debug=True)