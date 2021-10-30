# importing tkinter module
from tkinter import *

# importing random modules
import random

# Importing base64 for Encryption and Decryption
import base64

# ============================================================================================

# creating root object
root = Tk()

# Size of the window
root.geometry("1200x800")

# Title of window
root.title("Message Encryption and Decryption Tool")

Tops = Frame(root, width=1200, relief=GROOVE)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=GROOVE)
f1.pack(side=LEFT)

# ============================================================================================

labelInfo = Label(Tops, font=('Comic Sans MS', 30, 'bold'), text="SECRET MESSAGING \n Vigenère Cipher", fg="Black", bd=10, anchor='w')
labelInfo.grid(row=0, column=0)

# Initializing variables
Message = StringVar()
Key = StringVar()
Mode = StringVar()
Result = StringVar()

# ============================================================================================

# Label & Entry box for the Message
labelMessage = Label(f1, font=('Raleway Medium', 16, 'bold'), text="MESSAGE", bd=16, anchor="w")
labelMessage.grid(row=1, column=0)

textMessage = Entry(f1, font=('Courier New', 16), textvariable=Message, bd=10, insertwidth=4, bg="powder blue", justify='right')
textMessage.grid(row=1, column=1)


# Label & Entry box for the Key
labelKey = Label(f1, font=('Raleway Medium', 12, 'bold'), text="KEY (Integer Value Only )", bd=16, anchor="w")
labelKey.grid(row=2, column=0)

textKey = Entry(f1, font=('Courier New', 16), textvariable=Key, bd=10, insertwidth=4, bg="powder blue", justify='right')
textKey.grid(row=2, column=1)

# Label & Entry box for the Mode
labelMode = Label(f1, font=('Raleway Medium', 12, 'bold'), text="MODE('E' to Encrypt, 'D' to Decrypt)", bd=16, anchor="w")
labelMode.grid(row=3, column=0)

textMode = Entry(f1, font=('Courier New', 16), textvariable=Mode, bd=10, insertwidth=4, bg="powder blue", justify='right')
textMode.grid(row=3, column=1)

# Label & Entry box for the Result
labelResult = Label(f1, font=('Raleway Medium', 16, 'bold', 'underline'), text="Result :", bd=16, anchor="w")
labelResult.grid(row=1, column=2)

textResult = Entry(f1, font=('Courier New', 16, 'bold'), textvariable=Result, bd=10, insertwidth=4, bg="powder blue", justify='right')
textResult.grid(row=1, column=3)

# ============================================================================================

# Vigenere cipher
# Function to Encode the Message
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode the Message
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)
        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)

# Function to Show the Results
def Results():
    msg = Message.get()
    k = Key.get()
    m = Mode.get()

    if m == 'E':
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))

# Function to Exit the Window
def qExit():
    root.destroy()

# Window Reset Function
def Reset():
    Message.set("")
    Key.set("")
    Mode.set("")
    Result.set("")

# ============================================================================================

# Show Messgae, Reset & Exit Buttons
btnShow = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times New Roman', 16), width=10, text="Show Message", bg="green", command=Results)
btnShow.grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times New Roman', 16, 'italic'), width=10, text="Reset", bg="sky blue", command=Reset)
btnReset.grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times New Roman', 16), width=10, text="Exit", bg="red", command=qExit)
btnExit.grid(row=7, column=3)

# ============================================================================================

root.mainloop()

# ======================================== END of CODE =======================================