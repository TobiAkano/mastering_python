from tkinter import *
window=Tk()
# widgets 
lbl=Label(window, text="MAXIO", fg='black', font=("Comfortaa",30 ))
lbl.place(x=60, y=50)
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=85, y=100)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=120, y=150)
#widgets


window.title(' maxio')
window.geometry("300x500+10+20")
window.mainloop()