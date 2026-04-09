from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Secret Notes")
window.geometry("500x750")

#photo
img = ImageTk.PhotoImage(Image.open("top-secret.jpg").resize((100, 80)))
panel = Label(window, image=img, width=100, height=100)
panel.pack(pady=(20, 0))

#label title
label_title = Label(text="Enter your title", font=("Arial", 12, "bold"))
label_title.pack(pady=(30, 0))

#entry title
entry_title = Entry(width=40)
entry_title.pack()

#label message
label_title = Label(text="Enter your secret", font=("Arial", 12, "bold"))
label_title.pack(pady=(20, 0))

#text
text = Text(width=40, height=20)
text.pack()

#label master key
label_key = Label(text="Enter master key", font=("Arial", 12, "bold"))
label_key.pack(pady=(20, 0))

#entry master key
entry_key = Entry(width=40)
entry_key.pack()

#save & encrypt
button_save_encrypt = Button(text="Save & Encrypt")
button_save_encrypt.pack(pady=(10, 0))

#Decrypt
button_decrypt = Button(text="Decrypt")
button_decrypt.pack(pady=(10, 0))

window.mainloop()
