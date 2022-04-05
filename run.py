from printy import printy
import pyfiglet as pyf
from termcolor import colored,cprint
from article import save_posts,fetch_posts
from content import get_posts
from article_w import fetch_art
from tkinter import filedialog as fdialog
import tkinter as tk
cprint(pyf.figlet_format("PEP",font="isometric1"),"blue")
print(colored("[ lower case Mode]","yellow"))
def inputs():
    url=input(">>BASE URL ~ ")
    key_wrd=input(">>KEY WORD ~ ")
    return url,key_wrd
def exemption():
    print(colored(">> failed to scrap","red"))
    sel=input("Do you wish to try the other approach[y or n]")
    if sel=="y" or sel=="Y":
        menu()
    else:
        print(colored("%%%%%%%%%%%% Exiting.... %%%%%%%%%%%","red"))
        exit()

def menu():
    print(colored("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%","blue"))
    print(colored("1.             Norm set (Recommended)       ","green"))
    print(colored("2.             Distorted                    ","green"))
    print(colored("3.             Delicate                    ","green"))
    print(colored("4.             Exit","red"))
    print(colored("=====================================================================","blue"))
    opt=input(">>select option [1-3] ~")
    opt=int(opt)
    printy("=====================================================================","rBU")
    if opt==1:
        url,word=inputs()
        try:
            save_posts(fetch_posts(url,word))
            menu()
        except Exception as e:
            print(e)
            exemption()
    elif opt==2:
        url,word=inputs()
        try:
            save_posts(get_posts(url,word))
            menu()
        except:
            exemption()
    elif opt==3:
        url,word=inputs()
        save_posts(fetch_art(url,word))
        menu()
     
menu()