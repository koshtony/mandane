import streamlit as st
from PIL import Image
import time
from article import save_posts,fetch_posts
from content import get_posts
from article_w import fetch_art
st.get_option("theme.textColor")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
rad=st.sidebar.radio("scrap approach",["Normal","Distorted","Delicate"])
col1,col2=st.columns((1,1))
url=col1.text_input("Base URL")
key_word=col1.text_input("Key Word")
def join_posts(obj):
    len_posts=len(obj)
    posts_num=str(len_posts)+" post(s) found"
    col2.write(posts_num)
    all=[]
    for i in range(len_posts):
        all.append(" ".join(obj[i]))
    return all
def errors():
    col2.error("Failed to Scrap")
    col2.write("Try another approach")
if rad=="Normal":
    if col1.button("Normal Scrap"):
        try:
            progress=col2.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i+1)
            all,titles=fetch_posts(url,key_word)
            all=join_posts(all)
            col2.write(all)
            col1.header("TITLES")
            col1.write(titles)
        except:
            errors()
elif rad=="Distorted":
    if col1.button("Distorted Scrap"):
        try:
            progress=col2.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i+1)
            all_p=join_posts(get_posts(url,key_word))
            col2.write(all_p)
        except:
            errors()
elif rad=="Delicate":
    if col1.button("Delicate Scrap"):
        try:
            progress=col2.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i+1)
            all_a=join_posts(fetch_art(url,key_word))
            col2.write(all_a)
        except:
            errors()
rep=st.sidebar.text_input("Report failed URL")
def report(txt):
    txt=str(txt)+"\n"
    if st.sidebar.button("send"):
        try:
            files=open("report.txt","a")
            files.write(txt)
            files.close()
            st.sidebar.info("sent successfully")
        except:
            st.sidebar.error("Failed to send")
        
report(rep)
background = Image.open('hqdefault.jpg')
st.sidebar.image(background, width=300)









