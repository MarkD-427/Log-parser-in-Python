from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from config import db_config
from subprocess import call
from tkinter import messagebox
# from window_auth_pochta import window_auth_pochta
# from pathlib import Path

def create_connection_mysql_db(db_host, user_name, user_password, db_name = None):
            connection_db = None
            try:
                connection_db = mysql.connector.connect(
                    host = db_host,
                    user = user_name,
                    password = user_password,
                    database = db_name
                    )
                print("Подключение к MySQL успешно выполнено")
            except Error as db_connection_error:
                print("Возникла ошибка: ", db_connection_error)
            return connection_db

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")

def serv_select():
    if selected.get() == 1:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_auth_pochta.py"])
    elif selected.get() == 2:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_iredapd.py"])
    elif selected.get() == 3:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_auth_openfire.py"])
    elif selected.get() == 4:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_openfire.py"])
    elif selected.get() == 5:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_auth_ftp.py"])
    elif selected.get() == 6:
        window.destroy()
        call(["python", "C:\Python_diplom\Okna\window_vsftpd.py"])

def clear():
    window.destroy()
    call(["python", "C:\Python_diplom\Okna\window_clear.py"])

def newtake():
    window.destroy()
    call(["python", "C:\Python_diplom\Okna\select_and_load.py"])

window = Tk()
window.title("Выбор сервера")
window.geometry('800x700')
window.configure(bg="deep sky blue")
lbl = Label (window, text="Выберете сервер", font=("Arial Bold", 30), bg="deep sky blue")
lbl.grid(column=0, row=0)
frame = Frame(window, width=600, height=250, bg="white")
frame.place(x=20, y=100, relwidth=0.9, relheight=0.7)

lbl_serv = Label (frame, text="Меню серверов", font=("Arial Bold", 20), bg="deep sky blue")
# lbl_serv.pack(anchor='center')
lbl_serv.place(x=10, y=20)

selected = IntVar()
rad1 = Label(frame, text="Почта", font=("Calibri", 14), bg="ivory2")
rad1_1 = Radiobutton(frame, text='Авторизация на почте', value=1, variable=selected)
rad1_2 = Radiobutton(frame, text='Iredapd', value=2, variable=selected)
rad2 = Label(frame, text="Openfire", font=("Calibri", 14), bg="ivory2")
rad2_1 = Radiobutton(frame, text='Авторизация Openfire', value=3, variable=selected)
rad2_2 = Radiobutton(frame, text='Access Openfire', value=4, variable=selected)   
rad3 = Label(frame, text="FTP", font=("Calibri", 14), bg="ivory2")
rad3_1 = Radiobutton(frame, text='Авторизация FTP', value=5, variable=selected)
rad3_2 = Radiobutton(frame, text='Vsftpd', value=6, variable=selected)
btn1 = Button(frame, text="Продолжить", font=("Calibri", 14), bg="deep sky blue", fg="white",command=serv_select)
# rad1.pack(anchor='center')
# rad2.pack(anchor='center')
# rad3.pack(anchor='center')
# btn4.pack(anchor='center')
# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)  
# new_item.add_command(label='Новый')  
# new_item.add_separator()  
# new_item.add_command(label='Изменить')  
# menu.add_cascade(label='Файл', menu=new_item)  
# window.config(menu=menu)  
rad1.place(x=20, y=70)
rad1_1.place(x=20, y=100)
rad1_2.place(x=20, y=130)
rad2.place(x=20, y=160)
rad2_1.place(x=20, y=190)
rad2_2.place(x=20, y=220)
rad3.place(x=20, y=250)
rad3_1.place(x=20, y=280)
rad3_2.place(x=20, y=310)
btn1.place(x=20, y=370)

lbl_clear = Label(frame, text="Сначала очистите БД", font=("Calibri", 14))
lbl_clear.place(x=300, y=40)
btn_clear = Button (frame, text="Очистить БД", font=("Calibri", 14), bg="deep sky blue", fg="white", command=clear)
btn_clear.place(x=300, y=80)
lbl_newtake = Label(frame, text="Теперь выберете и загрузите новый log-файл в БД", font=("Calibri", 14))
lbl_newtake.place(x=300, y=130)
btn_newtake = Button (frame, text="Выбрать и загрузить log-файл", font=("Calibri", 14), bg="deep sky blue", fg="white", command=newtake)
btn_newtake.place(x=300, y=170)
# lbl_newtake = Label(frame, text="Добавьте log-файл в БД", font=("Calibri", 14))
# lbl_newtake.place(x=300, y=220)
# btn4 = Button (frame, text="Добавить log-файл", font=("Calibri", 14), bg="deep sky blue", fg="white")
# btn4.place(x=300, y=260)
# wap = os.startfile(r"C:/Python_diplom/Okna/window_auth_pochta.py")
# Toplevel(wap)

window.mainloop()