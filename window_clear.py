from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from config import db_config
from subprocess import call
from tkinter import messagebox

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

def back():
    window.destroy()
    call(["python", "C:\Python_diplom\Okna\select_and_scrap.py"])

def clear():
        try:
            conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")
            if selected.get() == 1:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE auth_pochta;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица auth_pochta очищена")
                messagebox.showinfo('Успешно', 'Таблица auth_pochta почтового сервера очищен.')
            elif selected.get() == 2:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE iredapd;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица iredapd очищена")
                messagebox.showinfo('Успешно', 'Таблица iredapd почтового сервера очищен.')
            elif selected.get() == 3:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE auth_openfire;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица auth_openfire очищена")
                messagebox.showinfo('Успешно', 'Таблица auth_openfire Openfire-сервера очищен.')
            elif selected.get() == 4:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE access_openfire;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица openfire очищена")
                messagebox.showinfo('Успешно', 'Таблица access_openfire Openfire-сервера очищен.')
            elif selected.get() == 5:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE auth_ftp;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица auth_ftp очищена")
                messagebox.showinfo('Успешно', 'Таблица auth_ftp FTP-сервера очищен.')
            elif selected.get() == 6:
                cursor = conn.cursor()
                clear_table_query = """TRUNCATE vsftpd;"""
                cursor.execute(clear_table_query)
                conn.commit()
                # lbl_ok.configure(text="Таблица vsftpd очищена")
                messagebox.showinfo('Успешно', 'Таблица vsftpd FTP-сервера очищен.')
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")

window = Tk()
window.title("Очистка нужной таблицы в БД")
window.geometry('800x700')
window.configure(bg="deep sky blue")
lbl = Label (window, text="Выберете таблицу", font=("Arial Bold", 30), bg="deep sky blue")
lbl.grid(column=0, row=0)
frame = Frame(window, width=600, height=250, bg="white")
frame.place(x=20, y=100, relwidth=0.9, relheight=0.7)

lbl_serv = Label (frame, text="Меню таблиц", font=("Arial Bold", 20), bg="deep sky blue")
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
btn_clear = Button(frame, text="Очистить", font=("Calibri", 14), bg="deep sky blue", fg="white",command=clear)
rad1.place(x=20, y=70)
rad1_1.place(x=20, y=100)
rad1_2.place(x=20, y=130)
rad2.place(x=20, y=160)
rad2_1.place(x=20, y=190)
rad2_2.place(x=20, y=220)
rad3.place(x=20, y=250)
rad3_1.place(x=20, y=280)
rad3_2.place(x=20, y=310)
btn_clear.place(x=20, y=370)

# lbl_ok = Label (window, text="Выберете таблицу", font=("Arial Bold", 30), bg="deep sky blue")
# lbl_ok.place(x=250, y=300)
btn_back = Button(window, text="Вернутся на окно выбора",  font=("Calibri", 14), bg="deep sky blue", fg="white",command=back)
btn_back.place(x=300, y=370)

window.mainloop()