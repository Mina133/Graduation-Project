from tkinter import *
from PIL import Image, ImageTk

# create a top-level window
top = Toplevel()

# create a PIL Image object from an image file
img = Image.open("select.png")
tkimg = ImageTk.PhotoImage(img)

# create a button and set its image
btn = Button(top, image=tkimg)
btn.pack()

# start the main event loop
top.mainloop()
