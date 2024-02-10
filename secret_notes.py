import tkinter
import pybase64
from tkinter import messagebox
from PIL import ImageTk, Image

def encrypt():
    # Get text from text box
    secret = gizli_not.get(1.0, tkinter.END)
    # Clear the text box
    gizli_not.delete(1.0, tkinter.END)

    # Logic for password
    if master_key_girisi.get() == "ozay":
        # convert to byte
        secret = secret.encode("ascii")
        # Convert to base64
        secret = pybase64.b64encode(secret)
        # Convert it back to ascii
        secret = secret.decode("ascii")
        # Print to text box
        gizli_not.insert(tkinter.END, secret)
    else:
        # Flash a message if wrong password
        messagebox.showwarning("Incorrect!, Incorrect Password, Try Again")

def decrypt():
    # Get text from text box
    secret = gizli_not.get(1.0, tkinter.END)
    # Clear the screen
    gizli_not.delete(1.0, tkinter.END)
    # Logic for password
    if master_key_girisi.get() == "ozay":

        # convert to byte
        secret = secret.encode("ascii")
        # Convert to base64
        secret = pybase64.b64decode(secret)
        # Convert it back to ascii
        secret = secret.decode("ascii")
        # Print to text box
        gizli_not.insert(tkinter.END, secret)
    else:
        # Flash a message if wrong password
        messagebox.showwarning("Incorrect!, Incorrect Password, Try Again")

window = tkinter.Tk()
window.title("Secret Notes")
window.geometry("350x650")
window.config(padx=10, pady=10, bg="light grey")

resim = ImageTk.PhotoImage(Image.open("top_secret1.png"))
label = tkinter.Label(image=resim, width=155, height=155)

label.pack()

baslik = tkinter.Label(text="Enter your title")
baslik.config(padx=5, pady=2)
baslik.place(x=116, y=180)

baslik_girisi = tkinter.Entry()
baslik_girisi.config(width=26)
baslik_girisi.place(x=80, y=205)

gizli_not_basligi = tkinter.Label(text="Enter your secret")
gizli_not_basligi.config(padx=5, pady=2)
gizli_not_basligi.place(x=110, y=235)

gizli_not = tkinter.Text(width=33, height=15)
gizli_not.place(x=25, y=260)

master_key_basligi = tkinter.Label(text="Enter master key")
master_key_basligi.config(padx=5, pady=2)
master_key_basligi.place(x=110, y=515)

master_key_girisi = tkinter.Entry()
master_key_girisi.config(width=26, show="*")
master_key_girisi.place(x=80, y=540)

encrypt_buton = tkinter.Button(text="Save & Encrypt", command=encrypt)
encrypt_buton.config(padx=5, pady=2)
encrypt_buton.place(x=113, y=565)

decrypt_buton = tkinter.Button(text="Decrypt", command=decrypt)
decrypt_buton.config(padx=5, pady=2)
decrypt_buton.place(x=132, y=595)

with open("text1.txt", mode="w") as f:
    secret = gizli_not.get(1.0, tkinter.END)
    f.write(secret)

window.mainloop()