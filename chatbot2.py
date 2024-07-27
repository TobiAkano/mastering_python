from tkinter import *
import time 
# GUI
root = Tk()
root.title("Chatbot")
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
 
# function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
 
    if (user == "hello" or "hi" or "hey" or "sup"):
        txt.insert(END, "\n" + "Bot -> Hi there,i am Maxio")
        
        txt.insert(END, "\n" + "Bot -> let me give a few catergories")
        txt.insert(END, "\n" + "Bot -> Action , Scifi , anime , romance , slice of life ")
        


 
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
 
    e.delete(0, END)
 
 
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Maxio", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)
 
root.mainloop()