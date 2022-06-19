import tkinter as tk
window =tk.Tk()
window.geometry("640x600")
greeting=tk.Label(text="10 second ads",foreground="white",background="black")
like=tk.Button(
    text="like",width="5",height="2",bg="red",fg="white"
)
entry=tk.Entry(fg="white",bg="blue",width=50)
greeting.pack(),entry.pack(),like.pack()