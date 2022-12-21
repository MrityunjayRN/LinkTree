import tkinter as Tiki
from tkinter.ttk import Button, Label, Entry
import ttkbootstrap as ttk
import webbrowser
window1= Tiki.Tk()
window1.geometry('1080x1080')
window1.title("Entry")
label_entry= Tiki.Label(window1, text= "Instagram")
label_entry.pack()
entry1= Entry(window1)
entry1.pack()
label2_entry= Tiki.Label(window1, text= "Twitter")
label2_entry.pack()
entry2= Entry(window1)
entry2.pack()
label3_entry= Tiki.Label(window1, text= "Facebook")
label3_entry.pack()
entry3= Entry(window1)
entry3.pack()
label4_entry= Tiki.Label(window1, text= "YouTube")
label4_entry.pack()
entry4= Entry(window1)
entry4.pack()

print(entry1, entry2, entry3, entry4)

entry1= entry1.get()
entry2= entry2.get()
entry3= entry3.get()
entry4= entry4.get()

print(entry1, entry2, entry3, entry4)

def Instagram1():
    webbrowser.open_new(entry1)
def Twitter1():
    webbrowser.open_new(entry2)
def Facebook1():
    webbrowser.open_new(entry3)
def Youtube1():
    webbrowser.open_new(entry4)


def Linktree():
    window= Tiki.Tk()
    window.geometry('1080x1080')
    window.title("LinkTree")
    window.configure(bg='pink')

    Label1= Tiki.Label(window, text= "LinkTree", font= ("Elephant", 30, "bold"))
    Label1.pack()

    Button1= Tiki.Button(window, text= "Instagram", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Instagram1, background= "orange", foreground= "black")
    Button1.pack(padx= 10, pady=10)

    Button2= Tiki.Button(window, text= "Twitter", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Twitter1, background= "blue", foreground= "white")
    Button2.pack(padx= 10, pady=10)

    Button3= Tiki.Button(window, text= "Facebook", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Facebook1, background= "dark blue", foreground= "white")
    Button3.pack(padx= 10, pady=10)

    Button4= Tiki.Button(window, text= "Youtube", font= ("Century Gothic", 20, "bold"), width="50", height= "2", command= Youtube1, background= "red", foreground= "white")
    Button4.pack(padx= 10, pady=10)

    def Add_Button():
        label_entry_add= Tiki.Label(window, text= "Button Name")
        label_entry_add.pack()
        entry_add= Entry(window)
        entry_add.pack()
        label_entry_add1= Tiki.Label(window, text= "Link")
        label_entry_add1.pack()
        entry2_add= Entry(window)
        entry2_add.pack()

        entry2_add= str(entry2_add)

        def button():
            webbrowser.open_new(entry2_add)
            Button6= Tiki.Button(window, text= "Add Button", font= ("Century Gothic", 20, "bold"), width="5", height= "2", command= button, background= "red", foreground= "white")
            Button6.pack()

    Button5= Tiki.Button(window, text= "Add Button", font= ("Century Gothic", 20, "bold"), width="5", height= "2", command= Add_Button, background= "red", foreground= "white")
    Button5.pack()

button1= Tiki.Button(text="Form Linktree", command= Linktree)
button1.pack()

window1.mainloop()