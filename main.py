from tkinter import *
from tkinter import messagebox
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

def import_file():
    entry_get = entry_title.get().strip()
    text_get = text.get("1.0", END).strip()

    if not text_get or not entry_get:
        messagebox.showinfo("Error", "Please enter both title and text")
        return

    file_name = "MySecret.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(entry_get)
        f.write("\n")
        f.write(text_get)
    messagebox.showinfo("Secret Notes", "Secret Notes saved successfully!")
    window.destroy()

#save & encrypt
button_save_encrypt = Button(window, text="Save & Encrypt", command=import_file)
button_save_encrypt.pack(pady=(10, 0))

#Decrypt
button_decrypt = Button(text="Decrypt")
button_decrypt.pack(pady=(10, 0))


window.mainloop()
