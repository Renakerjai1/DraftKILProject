import tkinter as tk
import PIL
from PIL import ImageTk,Image
class AppWindow:
    """
    make product a tuple or a list and make a recycler style view that shows a certain number of images, less than 10,
    with one or two videos

    need to find a way to create a revolving list of products that preview photos and videos

    """
    def __init__(self,product):
        appwindow=tk.Tk()
        appwindow.title('Ten second ads')
        appwindow.geometry("640x600")
        like=tk.Button(text="like",width="5",height="2",bg="red",fg="white")
        entry=tk.Entry(fg="white",bg="blue",width=50)
        img=ImageTk.PhotoImage(product.photo)
        entry.pack(),like.pack()