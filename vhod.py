from tkinter import *
from login import login_in_prog
from subprocess import call
from tkinter import messagebox

def click():
    if login.get() == (login_in_prog["login"]) and pasw.get() == (login_in_prog["password"]):
            window.destroy()      
            call(["python", "C:\Python_diplom\Okna\select_and_scrap.py"])
    else:
        messagebox.showerror('Внимание:', 'Неверный логин или пароль')


window = Tk()
window.title("Вход")
window.geometry('500x370')
window.configure(bg="deep sky blue")
frame = Frame(window, width=400, height=250, bg="white")
frame.place(x=100, y=100, relwidth=0.5)

lbl = Label (window, text="Вход в приложение", font=("Arial Bold", 30), bg="deep sky blue")
lbl.grid(column=0, row=0)

lbl_login = Label (frame, text="Логин", font=("Arial Bold", 20), bg="ivory2")
lbl_login.place(x=75, y=5)
login = Entry(frame, width=30, font=("Arial", 20))
login.place(x=10, y=50)

lbl_pasw = Label (frame, text="Пароль", font=("Arial Bold", 20), bg="ivory2")
lbl_pasw.place(x=65, y=95)
pasw = Entry(frame, width=30, font=("Arial", 20), show="*")
pasw.place(x=10, y=140)

btn = Button (frame, text="Вход", font=("Arial Bold", 20), bg="deep sky blue", fg="white", command=click)
btn.place(x=70, y=185)

window.mainloop()