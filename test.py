from tkinter import *
from tkinter import messagebox
#from tkinter import messagebox

class erfun:
    def addtolist():
        ad = adde.get()
        if len(ad) != 0:
            if ad not in listi:
                listi.append(ad)
                listi.sort()
                for i in range(li.size()):
                    li.delete(0)
                for i in listi:
                    li.insert(END,i)
                for i in range(len(adde.get())):
                    adde.delete('0')
            else:
                messagebox.showinfo('error', 'Item in list')
                for i in range(len(adde.get())):
                    adde.delete('0')
    
    def DElete():
        itemnumber = li.curselection()
        if len(itemnumber)>0:
            itemname=li.get(itemnumber)
            if itemname != "no":
                a = listi.index(itemname)
                listi.pop(a)
                for i in range(li.size()):
                    li.delete(0)
                for i in listi:
                    li.insert(END,i)

    def Search():
        sear = seae.get()
        se = []
        if len(sear) == 0:
            for i in range(li.size()):
                li.delete(0)
            for i in listi:
                li.insert(END,i)
        else:
            for i in listi:
                if sear in i:
                    se.append(i)
            if len(se) == 0:
                se.append("no")
            for i in range(li.size()):
                li.delete(0)
            for i in se:
                li.insert(END,i)
            for i in range(len(seae.get())):
                    seae.delete('0')
        

listi = []





root = Tk()
li = Listbox(root,font = ("Times 14",20),bg = 'pink',fg = 'red');li.place(y = 0,x = 249,width = 250,height = 400)
# li.bind('<Double-1>', erfun._delete_)
add = Button(root,text = "Add" , font = ("Times 14",20),bg = "blue",command = erfun.addtolist);add.place(x = 429,y = 401,height = 50)
adde = Entry(root,font = ("Times 14",20),bg = "green",bd = 2,fg = 'yellow');adde.place(x = 249,y = 401,height = 48,width = 180)
sea = Button(root,text = "Sea" , font = ("Times 14",20),bg = "blue",command = erfun.Search);sea.place(x = 429,y = 451,height = 50)
seae = Entry(root,font = ("Times 14",20),bg = "green",bd = 2,fg = 'yellow');seae.place(x = 249,y = 451,height = 48,width = 180)
Delete = Button(root,text = "Delete" , font = ("Times 14",20),bg = "blue",command = erfun.DElete);Delete.place(x =145,y = 0,height = 50)
root.title("erfun")
root.geometry("500x500+200+50")
root.resizable(False , False)
root.config(bg = "black")


root.mainloop()