from tkinter import *
from pytube import YouTube, streams
from pytube.cli import on_progress

root = Tk()
root.title ("Youtube Download Videos")

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=20, pady=20)

def link():
    link_video = caixa.get()
    print(link_video)


#define buttons

myLabel1 = Label(frame, text="Downloader")
myLabel2 = Label(frame, text="Link:")
button_download = Button(frame, text="Download", padx=10, pady=10, command=link)
caixa = Entry(frame, width=35, borderwidth=5)
caixa.get()

#put the buttons on the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
button_download.grid(row=2, column=1)
caixa.grid(row=1, column=1, columnspan=3, padx=10, pady=10)



root.mainloop()