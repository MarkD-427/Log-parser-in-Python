from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from config import db_config
from tkinter.ttk import Combobox
from subprocess import call


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

def find():
    try:
    # создание таблицы
            conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")
            if combo.get() == 'IP':
                for colm in table.get_children():
                    table.delete(colm)
                cursor = conn.cursor(buffered=True)
                select_table_query = f"""select * from access_openfire where ip like '%{what_find.get()}';"""
                cursor.execute(select_table_query)
                for colm in cursor.fetchall():
                    table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
                conn.commit()
            elif combo.get() == 'Дата':
                for colm in table.get_children():
                    table.delete(colm)
                cursor = conn.cursor(buffered=True)
                select_table_query = f"""select * from access_openfire where data like '%{what_find.get()}';"""
                cursor.execute(select_table_query)
                for colm in cursor.fetchall():
                    table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
                conn.commit()
            elif combo.get() == 'Время':
                for colm in table.get_children():
                    table.delete(colm)
                cursor = conn.cursor(buffered=True)
                select_table_query = f"""select * from access_openfire where time like '%{what_find.get()}';"""
                cursor.execute(select_table_query)
                for colm in cursor.fetchall():
                    table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
                conn.commit()
            elif combo.get() == 'URL':
                for colm in table.get_children():
                    table.delete(colm)
                cursor = conn.cursor(buffered=True)
                select_table_query = f"""select * from access_openfire where url like '%{what_find.get()}';"""
                cursor.execute(select_table_query)
                for colm in cursor.fetchall():
                    table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
                conn.commit()

    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def all_view():
    try:
    # создание таблицы
        conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")
        for colm in table.get_children():
                table.delete(colm)
        cursor = conn.cursor(buffered=True)
        select_table_query = """select * from access_openfire;"""
        cursor.execute(select_table_query)
        for colm in cursor.fetchall():
            table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
        conn.commit()

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
window.title("Авторизация на почте")
window.geometry('1000x500')
window.configure(bg="deep sky blue")
# window.resizable(width=False, height=False)
btn_back = Button(window, text="Вернутся на окно выбора", command=back)
btn_back.place(relx = 0.1, rely = 0.6)

frame_founder = Frame(window, width=200, height=200, bg="white")
frame_results = Frame(window, width=400, height=200, bg="white")
frame_founder.place(x=20, y=100, relwidth=0.35)
frame_results.place(relx=0.4, y=100, relwidth=0.5)
# frame_founder.grid(column=0, row=0, padx=50)
# frame_results.grid(column=1, row=0, padx=50)

label_title = Label(window, text="Openfire", font=("Arial Bold", 30), bg="deep sky blue")
label_title.grid(column=0, row=0)

scrollbar = Scrollbar(frame_results)
scrollbar.pack( side = RIGHT, fill = Y )
table = ttk.Treeview(frame_results)
# heads = ['id', 'data', 'time', 'user']
# table['columns'] = [0, 1, 2, 3]
table["columns"] = ("1", "2", "3", "4", "5")
table['show'] = 'headings'
table.column("1", width=30, anchor='c')
table.column("2", width=80, anchor='c')
table.column("3", width=80, anchor='c')
table.column("4", width=80, anchor='c')
table.column("5", width=200, anchor='c')
table.heading("1", text="id")
table.heading("2", text="ip")
table.heading("3", text="data")
table.heading("4", text="time")
table.heading("5", text="url")
table.pack()
scrollbar.config( command = table.yview )
# scrollbar.set(0.2, 0.5)
cursor = conn.cursor()
# view_info_query = """SELECT * FROM auth_pochta"""
try:
    # создание таблицы
    cursor = conn.cursor(buffered=True)
    select_table_query = """select * from access_openfire;"""
    cursor.execute(select_table_query)
    for colm in cursor.fetchall():
        table.insert("", 'end', iid=colm[0], values=(colm[0],colm[1],colm[2],colm[3],colm[4]))
    conn.commit()

except Error as error:
    print(error)
finally:
    cursor.close()
    conn.close()
# for row in '''SELECT * FROM auth_pochta''':
#        table.insert('', 'end', values=row)

lbl_finder = Label(frame_founder, text="Ищем по:", font=(20), bg="ivory2")
lbl_finder.grid(column=0, row=0, padx=10, pady=10)
combo = Combobox (frame_founder)
combo['values'] = ('IP', 'Дата', 'Время', 'URL')
combo.grid(column=0, row=1)
lbl_what_find = Label(frame_founder, text="Что ищем:", font=(20), bg="ivory2")
lbl_what_find.grid(column=0, row=2, padx=10, pady=10)
what_find = Entry(frame_founder, width=20)
what_find.grid(column=0, row=3)
btn = Button(frame_founder, text = "Поиск", command=find, font=("Calibri", 14), bg="deep sky blue", fg="white",)
btn.grid(column=0, row=4)
btn_all = Button(frame_founder, text = "Вывести все данные", command=all_view, font=("Calibri", 14), bg="deep sky blue", fg="white",)
btn_all.grid(column=1, row=4)

window.mainloop()