import tkinter as Tiki
from tkinter.ttk import Button, Label
import ttkbootstrap as ttk
import requests
import webbrowser

def Instagram1():
    webbrowser.open_new("https://www.instagram.com")
def Twitter1():
    webbrowser.open_new("https://www.twitter.com")
def Facebook1():
    webbrowser.open_new("https://www.facebook.com")
def Youtube1():
    webbrowser.open_new("https://www.youtube.com")

window= Tiki.Tk()
window.geometry('1080x1080')
window.title("LinkTree", )
window.configure(bg='pink')

Label1= Tiki.Label(window, text= "LinkTree", font= ("Elephant", 30, "bold"))
Label1.pack()

Button1= Tiki.Button(text= "Instagram", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Instagram1, background= "orange", foreground= "black")
Button1.pack(padx= 10, pady=10)

Button2= Tiki.Button(text= "Twitter", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Twitter1, background= "blue", foreground= "white")
Button2.pack(padx= 10, pady=10)

Button3= Tiki.Button(text= "Facebook", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Facebook1, background= "dark blue", foreground= "white")
Button3.pack(padx= 10, pady=10)

Button4= Tiki.Button(text= "Youtube", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Youtube1, background= "red", foreground= "white")
Button4.pack(padx= 10, pady=10)


window.mainloop()