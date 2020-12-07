import base64
from tkinter import *
import io
from PIL import Image, ImageTk
with open('file.txt', 'r') as file:
    contents = file.read()
   

decoded = base64.b64decode(contents)

#with open(r"C:\Users\Public\Recorded TV\Pictures\Sample Pictures\Tulips.jpg", 'rb') as file:
#    contents = file.read()

#with open('file.txt', 'wb') as file:
 #   file.write(base64.b64encode(contents))

root = Tk()

buf = io.BytesIO(decoded)
img = Image.open(buf)
#img.show()
pic = ImageTk.PhotoImage(img)
label = Label(root, image = pic)
label.pack()

root.mainloop()