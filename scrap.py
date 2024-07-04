from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from config import db_config
from tkinter.ttk import Combobox


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

window = Tk()
window.title("Подготовка")
window.geometry('600x500')
window.configure(bg="deep sky blue")

frame = Frame(window, width=500, height=300, bg="white")
frame.place(x=20, y=100, relwidth=0.85)
lbl_title = Label(frame, text="Выполняйте действия последвательно", font=("Arial Bold", 20))
lbl_title.place(x=0, y=0)

lbl_clear = Label(frame, text="Сначала очистите БД", font=("Calibri", 14))
lbl_clear.place(x=5, y=40)
btn = Button (frame, text="Очистить БД", font=("Calibri", 14), bg="deep sky blue", fg="white")
btn.place(x=5, y=80)
lbl_newtake = Label(frame, text="Теперь загрузите новый log-файл", font=("Calibri", 14))
lbl_newtake.place(x=5, y=130)
btn = Button (frame, text="Загрузить log-файл", font=("Calibri", 14), bg="deep sky blue", fg="white")
btn.place(x=5, y=170)
lbl_newtake = Label(frame, text="Теперь загрузите новый log-файл", font=("Calibri", 14))
lbl_newtake.place(x=5, y=130)
btn = Button (frame, text="Загрузить log-файл", font=("Calibri", 14), bg="deep sky blue", fg="white")
btn.place(x=5, y=170)

window.mainloop()