import pybase64
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Secret Notes")
window.geometry("500x750")

#photo
img = ImageTk.PhotoImage(Image.open("top-secret.jpg").resize((100, 90)))
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
    master_key = entry_key.get().strip()

    combined = master_key + "|" + text_get
    encoded = pybase64.b64encode(combined.encode("utf-8")).decode("utf-8")

    if not text_get or not entry_get:
        messagebox.showinfo("Error", "Please enter both title and text")
        return

    elif master_key == "":
        messagebox.showinfo("Error", "Please enter master key")
        return
    else:
        try:
            with open("MySecret.txt", "a", encoding="utf-8") as f:
                f.write(f"{entry_get}\n{encoded}")
        except FileNotFoundError:
            with open("MySecret.txt", "w", encoding="utf-8") as f:
                f.write(f"\n{entry_get}\n{encoded}")
        finally:
            entry_title.delete(0, END)
            text.delete("1.0", END)
            entry_key.delete(0, END)

        messagebox.showinfo("Secret Notes", "Secret Notes saved successfully!")

def decrypt():
    text_get = text.get("1.0", END).strip()
    master_key = entry_key.get().strip()

    try:
        decoded_text = pybase64.b64decode(text_get).decode("utf-8")
        defined_key, text_get = decoded_text.split("|",1)

        if defined_key == master_key:
            text.delete("1.0", END)
            text.insert(END, text_get)
        else:
            messagebox.showinfo("Error", "Wrong master key")
    except (ValueError, UnicodeDecodeError):
        messagebox.showinfo("Error", "Invalid encoded text")

#save & encrypt
button_save_encrypt = Button(window, text="Save & Encrypt", command= import_file)
button_save_encrypt.pack(pady=(10, 0))

#Decrypt
button_decrypt = Button(text="Decrypt", command=decrypt)
button_decrypt.pack(pady=(10, 0))

window.mainloop()
