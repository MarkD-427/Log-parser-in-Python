from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from config import db_config
from subprocess import call
import os.path
from tkinter import filedialog
from pathlib import Path
import re
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

def sal():
    file = filedialog.askopenfilename(filetypes=(("Лог-файлы", "*.log"),))
    # script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    # script = os.path.join(script_dir, file)
    path_to_file = Path(file)

    if selected.get() == 1:
          #auth_pochta
          def reader(filename):
            regexpmonth = r"^\w{3}"
            regexpday = r"\ \d{1,2}\ "
            regexptime = r"\d{2}:\d{2}:\d{2}"
            regexpuser = r" \w{4}$"

            with open(filename) as file:
                log = file.read()

                month_list = re.findall(regexpmonth, log, re.MULTILINE)
                day_list = re.findall(regexpday, log)
                time_list = re.findall(regexptime, log)
                user_list = re.findall(regexpuser, log, re.MULTILINE)
                month_list2 = []
                data_list = []

                for moni in range (len(month_list)):
                    match month_list[moni]:
                        case 'Jan': month_list2.insert(moni, "1")
                        case 'Feb': month_list2.insert(moni, "2")
                        case 'Mar': month_list2.insert(moni, "3")
                        case 'Apr': month_list2.insert(moni, "4")
                        case 'May': month_list2.insert(moni, "5")
                        case 'Jun': month_list2.insert(moni, "6")
                        case 'Jul': month_list2.insert(moni, "7")
                        case 'Aug': month_list2.insert(moni, "8")
                        case 'Sep': month_list2.insert(moni, "9")
                        case 'Oct': month_list2.insert(moni, "10")
                        case 'Nov': month_list2.insert(moni, "11")
                        case 'Dec': month_list2.insert(moni, "12")

                for i in range (len(month_list)):
                    data_list.insert(i, day_list[i].replace(" ","")+"-"+month_list2[i].replace(" ","")+"-"+"2024")

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
                try:
                    cursor = conn.cursor()
                    
                    for i in range(len(user_list)):
                        insert_in_table = """INSERT INTO auth_pochta (data, time, user, id_server) VALUES (%s,%s,%s,%s)"""
                        values = (data_list[i], time_list[i], user_list[i], 3)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

            return user_list, time_list, data_list
          messagebox.showinfo('Успешно', 'Лог auth почтового сервера загружен.')

            # if __name__ == '__main__':
            # # regpath = re.sub(r'\\', r'/', path_to_file)
            # # print(regpath)
            # # modul = import_module(path_to_file)
            #     reader(path_to_file)

    elif selected.get() == 2:
        #iredapd
        def reader(filename):
            regexpip = r'\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}'
            regexpmail_from = r' [-a-z0-9.-_]+@(?:[a-z0-9-A-Z]+\.)+[a-zA-z]{2,6} '
            regexpmail_to = r'> [-a-z0-9.-_]+@(?:[a-z0-9-A-Z]+\.)+[a-zA-z]{2,6}'
            regexpmails = r' [-a-z0-9.-_]+@(?:[a-z0-9-A-Z]+\.)+[a-zA-z]{2,6} -> [-a-z0-9.-_]+@(?:[a-z0-9-A-Z]+\.)+[a-zA-z]{2,6}'
            regexdata = r'\d{4}-\d{2}-\d{2}'
            regextime = r'\d{2}:\d{2}:\d{2}'

            with open(filename) as file:
                fin = file.read()

                ip_list = re.findall(regexpip, fin)
                data_list = re.findall(regexdata, fin)
                time_list = re.findall(regextime, fin)
                mails_list = re.findall(regexpmails,  fin)

                ip = []
                data = []
                time = []

                for i in range(2363):
                    ip.insert(i, ip_list[i])
                    data.insert(i, data_list[i])
                    time.insert(i, time_list[i])
                
                # print(len(ip), len(data), len(time))

                mail_from = re.findall(regexpmail_from, str(mails_list))
                mail_to = re.findall(regexpmail_to, str(mails_list))
                maillist_from = []
                maillist_to = []

                for i in range (len(mail_from)):
                    maillist_from.insert(i, mail_from[i].replace(" ",""))
                # print(len(maillist_from))

                for i in range (len(mail_to)):
                    maillist_to.insert(i, mail_to[i].replace("> ",""))
                # print(len(maillist_to))

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
                try:
                    # создание таблицы
                    cursor = conn.cursor()
                    # create_table_query = """
                    # CREATE TABLE iredapd (
                    # id INT AUTO_INCREMENT,
                    # ip VARCHAR(255) NOT NULL,
                    # data VARCHAR(255) NOT NULL,
                    # time VARCHAR(255) NOT NULL,
                    # mail_from VARCHAR(255) NOT NULL,
                    # mail_to VARCHAR(255) NOT NULL,
                    # id_server INT NOT NULL,
                    # PRIMARY KEY (id),
                    # FOREIGN KEY (id_server) REFERENCES server (id)
                    # )"""
                    # # query = """DROP TABLE iredapd;"""
                    # # cursor.execute(query)
                    # cursor.execute(create_table_query)
                    # conn.commit()


                    listD = []
                    
                    for i in range(len(ip)):
                        insert_in_table = """INSERT INTO iredapd(ip, data, time, mail_from, mail_to, id_server) VALUES (%s,%s,%s,%s,%s,%s)"""
                        values = (ip[i], data[i], time[i], maillist_from[i], maillist_to[i], 3)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

            return ip, data, time, maillist_from, maillist_to
        messagebox.showinfo('Успешно', 'Лог iredapd почтового сервера загружен.')

            # if __name__ == '__main__':
            #     reader(path_to_file)

    elif selected.get() == 3:
        # auth_openfire
        def reader(filename):
            regexpmonth = r"^\w{3}"
            regexpday = r"\  \d{1}\ "
            regexptime = r"\d{2}:\d{2}:\d{2}"
            regexpuser = r" \w{4}$"

            with open(filename) as file:
                log = file.read()

                month_list = re.findall(regexpmonth, log, re.MULTILINE)
                day_list = re.findall(regexpday, log)
                time_list = re.findall(regexptime, log)
                user_list = re.findall(regexpuser, log, re.MULTILINE)
                month_list2 = []
                data_list = []

                for moni in range (len(month_list)):
                    match month_list[moni]:
                        case 'Jan': month_list2.insert(moni, "1")
                        case 'Feb': month_list2.insert(moni, "2")
                        case 'Mar': month_list2.insert(moni, "3")
                        case 'Apr': month_list2.insert(moni, "4")
                        case 'May': month_list2.insert(moni, "5")
                        case 'Jun': month_list2.insert(moni, "6")
                        case 'Jul': month_list2.insert(moni, "7")
                        case 'Aug': month_list2.insert(moni, "8")
                        case 'Sep': month_list2.insert(moni, "9")
                        case 'Oct': month_list2.insert(moni, "10")
                        case 'Nov': month_list2.insert(moni, "11")
                        case 'Dec': month_list2.insert(moni, "12")

                for i in range (len(month_list)):
                    data_list.insert(i, day_list[i].replace(" ","")+"-"+month_list2[i].replace(" ","")+"-"+"2024")
                
                # DATA = [[None for _ in range(3)] for _ in range (len(user_list))]
                # with open ("oenfire_auth.txt", "w") as file:
                #     for i in range(len(user_list)):
                #         DATA[i][0] = data_list[i]
                #         DATA[i][1] = time_list[i]
                #         DATA[i][2] = user_list[i]
                #     for i in range(len(DATA)):
                #         for j in range(len(DATA[i])):
                #             file.writelines(str(DATA[i][j] + " "))
                #         file.writelines('\n')

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
                try:
                    # создание таблицы
                    cursor = conn.cursor()
                    # create_table_query = """
                    # CREATE TABLE auth_openfire (
                    # id INT AUTO_INCREMENT,
                    # data VARCHAR(255) NOT NULL,
                    # time VARCHAR(255) NOT NULL,
                    # user VARCHAR(255) NOT NULL,
                    # id_server INT NOT NULL,
                    # PRIMARY KEY (id),
                    # FOREIGN KEY (id_server) REFERENCES server (id)
                    # )"""
                    # # # query = """DROP TABLE iredapd;"""
                    # # # cursor.execute(query)
                    # cursor.execute(create_table_query)
                    # conn.commit()
                    
                    for i in range(len(user_list)):
                        insert_in_table = """INSERT INTO auth_openfire (data, time, user, id_server) VALUES (%s,%s,%s,%s)"""
                        values = (data_list[i], time_list[i], user_list[i], 2)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

            return user_list, time_list, data_list
        messagebox.showinfo('Успешно', 'Лог auth Openfire-сервера загружен.')

            # if __name__ == '__main__':
            #     reader(path_to_file)

    elif selected.get() == 4:
        # access_openfire
        def reader(filename):

            regexpip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            regexpdata = r'\d{2}/\w+/\d{4}'
            regexptime = r'\d{2}:\d{2}:\d{2}'
            regexpurl = r'http://.*?\"'

            with open(filename) as file:
                log = file.read()

                ip_list = re.findall(regexpip, log)
                data_list = re.findall(regexpdata, log)
                time_list = re.findall(regexptime, log)
                url_list = re.findall(regexpurl, log)
                url = []
                ip = []
                data = []
                time = []

                for i in range(102):
                    ip.insert(i, ip_list[i])
                    data.insert(i, data_list[i])
                    time.insert(i, time_list[i])

                for i in  range (len(url_list)):
                    url.insert(i, url_list[i].replace('"',''))

                print(len(ip_list), len(url))

                # DATA = [[None for _ in range(4)] for _ in range (len(ip))]
                # with open ("openfire_access.txt", "w") as file:
                #     for i in range(len(ip)):
                #         DATA[i][0] = ip[i]
                #         DATA[i][1] = data[i]
                #         DATA[i][2] = time[i]
                #         DATA[i][3] = url[i]
                #     for i in range(len(DATA)):
                #         for j in range(len(DATA[i])):
                #             file.writelines(str(DATA[i][j] + " "))
                #         file.writelines('\n')

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
                try:
                    # создание таблицы
                    cursor = conn.cursor()
                    # create_table_query = """
                    # CREATE TABLE access_openfire (
                    # id INT AUTO_INCREMENT,
                    # ip VARCHAR(255) NOT NULL,
                    # data VARCHAR(255) NOT NULL,
                    # time VARCHAR(255) NOT NULL,
                    # url VARCHAR(255) NOT NULL,
                    # id_server INT NOT NULL,
                    # PRIMARY KEY (id),
                    # FOREIGN KEY (id_server) REFERENCES server (id)
                    # )"""
                    # # query = """DROP TABLE iredapd;"""
                    # # cursor.execute(query)
                    # cursor.execute(create_table_query)
                    # conn.commit()

                    
                    for i in range(len(ip)):
                        insert_in_table = """INSERT INTO access_openfire(ip, data, time, url, id_server) VALUES (%s,%s,%s,%s,%s)"""
                        values = (ip[i], data[i], time[i], url[i], 2)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

            return ip_list, data_list, time_list, url
        messagebox.showinfo('Успешно', 'Лог access Openfire-сервера загружен.')


    elif selected.get() == 5:
        # auth_ftp
        def reader(filename):
            regexpmonth = r"^\w{3}"
            regexpday = r"\  \d{1}\ "
            regexptime = r"\d{2}:\d{2}:\d{2}"
            regexpuser = r" \w{4}$"

            with open(filename) as file:
                log = file.read()

                month_list = re.findall(regexpmonth, log, re.MULTILINE)
                day_list = re.findall(regexpday, log)
                time_list = re.findall(regexptime, log)
                user_list = re.findall(regexpuser, log, re.MULTILINE)
                month_list2 = []
                data_list = []

                for moni in range (len(month_list)):
                    match month_list[moni]:
                        case 'Jan': month_list2.insert(moni, "1")
                        case 'Feb': month_list2.insert(moni, "2")
                        case 'Mar': month_list2.insert(moni, "3")
                        case 'Apr': month_list2.insert(moni, "4")
                        case 'May': month_list2.insert(moni, "5")
                        case 'Jun': month_list2.insert(moni, "6")
                        case 'Jul': month_list2.insert(moni, "7")
                        case 'Aug': month_list2.insert(moni, "8")
                        case 'Sep': month_list2.insert(moni, "9")
                        case 'Oct': month_list2.insert(moni, "10")
                        case 'Nov': month_list2.insert(moni, "11")
                        case 'Dec': month_list2.insert(moni, "12")

                for i in range (len(month_list)):
                    data_list.insert(i, day_list[i].replace(" ","")+"-"+month_list2[i].replace(" ","")+"-"+"2024")

                # DATA = [[None for _ in range(3)] for _ in range (len(user_list))]
                # with open ("ftp_auth.txt", "w") as file:
                #     for i in range(len(user_list)):
                #         DATA[i][0] = data_list[i]
                #         DATA[i][1] = time_list[i]
                #         DATA[i][2] = user_list[i]
                #     for i in range(len(DATA)):
                #         for j in range(len(DATA[i])):
                #             file.writelines(str(DATA[i][j] + " "))
                #         file.writelines('\n')

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
                try:
                    # создание таблицы
                    cursor = conn.cursor()
                    # create_table_query = """
                    # CREATE TABLE auth_ftp (
                    # id INT AUTO_INCREMENT,
                    # data VARCHAR(255) NOT NULL,
                    # time VARCHAR(255) NOT NULL,
                    # user VARCHAR(255) NOT NULL,
                    # id_server INT NOT NULL,
                    # PRIMARY KEY (id),
                    # FOREIGN KEY (id_server) REFERENCES server (id)
                    # )"""
                    # # # query = """DROP TABLE iredapd;"""
                    # # # cursor.execute(query)
                    # cursor.execute(create_table_query)
                    # conn.commit()

                    
                    for i in range(len(user_list)):
                        insert_in_table = """INSERT INTO auth_ftp(data, time, user, id_server) VALUES (%s,%s,%s,%s)"""
                        values = (data_list[i], time_list[i], user_list[i], 1)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()

            return user_list, time_list, data_list
        messagebox.showinfo('Успешно', 'Лог auth FTP-сервера загружен.')

            # if __name__ == '__main__':
            #     reader(path_to_file)

    elif selected.get() == 6:
        # vsftpd
        def reader(filename):

            regexpip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            regexpmonth = r'\ \w{3}\ '
            regexpday = r'\ \d{1}\ '
            regexpyear = r'\ 20\d{2}\ '
            regextime = r'\d{2}:\d{2}:\d{2}'
            regexpstatus = r'\b\w[A-Z]+\s\w[A-Z]+|\w[A-Z]+\b'

            
            with open(filename) as file:
                log = file.read()

                # logs_list = re.findall(regexp1, log) + re.findall(regexp2, log)

                ip_list = re.findall(regexpip, log)
                day_list = re.findall(regexpday, log)
                month_list = re.findall(regexpmonth, log)
                year_list = re.findall(regexpyear, log)
                month_list2 = []
                time_list = re.findall(regextime, log)
                status_list = re.findall(regexpstatus, log)

                data_list = []

                for moni in range (len(month_list)):
                    match month_list[moni]:
                        case ' Jan ': month_list2.insert(moni, "1")
                        case ' Feb ': month_list2.insert(moni, "2")
                        case ' Mar ': month_list2.insert(moni, "3")
                        case ' Apr ': month_list2.insert(moni, "4")
                        case ' May ': month_list2.insert(moni, "5")
                        case ' Jun ': month_list2.insert(moni, "6")
                        case ' Jul ': month_list2.insert(moni, "7")
                        case ' Aug ': month_list2.insert(moni, "8")
                        case ' Sep ': month_list2.insert(moni, "9")
                        case ' Oct ': month_list2.insert(moni, "10")
                        case ' Nov ': month_list2.insert(moni, "11")
                        case ' Dec ': month_list2.insert(moni, "12")

                # print(ip_list, day_list, month_list2, year_list)
                for i in range (len(month_list)):
                    data_list.insert(i, day_list[i].replace(" ","")+"-"+month_list2[i].replace(" ","")+"-"+year_list[i].replace(" ",""))

                # DATA = [[None for _ in range(4)] for _ in range (len(ip_list))]
                # for i in range(len(ip_list)):
                #         DATA[i][0] = ip_list[i]
                #         DATA[i][1] = data_list[i]
                #         DATA[i][2] = time_list[i]
                #         DATA[i][3] = status_list[i]
                # for i in range(len(DATA)):
                #         for j in range(len(DATA[i])):
                #             file.writelines(str(DATA[i][j] + " "))
                #         file.writelines('\n')

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
                try:
                    # создание таблицы
                    cursor = conn.cursor()
                    # create_table_query = """
                    # CREATE TABLE vsftpd (
                    # id INT AUTO_INCREMENT,
                    # ip VARCHAR(255) NOT NULL,
                    # data VARCHAR(255) NOT NULL,
                    # time VARCHAR(255) NOT NULL,
                    # status VARCHAR(255) NOT NULL,
                    # id_server INT NOT NULL,
                    # PRIMARY KEY (id),
                    # FOREIGN KEY (id_server) REFERENCES server (id)
                    # )"""
                    # # # query = """DROP TABLE iredapd;"""
                    # # # cursor.execute(query)
                    # cursor.execute(create_table_query)
                    # conn.commit()

                    
                    for i in range(len(ip_list)):
                        insert_in_table = """INSERT INTO vsftpd(ip, data, time, status, id_server) VALUES (%s,%s,%s,%s,%s)"""
                        values = (ip_list[i], data_list[i], time_list[i], status_list[i], 1)
            
                        cursor.execute(insert_in_table, values)

                    conn.commit()

                except Error as error:
                    print(error)
                finally:
                    cursor.close()
                    conn.close()


            return ip_list, data_list, time_list, status_list
        messagebox.showinfo('Успешно', 'Лог vsftpd FTP-сервера загружен.')


            # if __name__ == '__main__':
            #     reader(path_to_file)

    if __name__ == '__main__':
        reader(path_to_file)

def back():
    window.destroy()
    call(["python", "C:\Python_diplom\Okna\select_and_scrap.py"])

conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                    db_config["mysql"]["user"],
                                    db_config["mysql"]["password"],
                                    "parser_db")

window = Tk()
window.title("Выбор лога")
window.geometry('700x700')
window.configure(bg="deep sky blue")
lbl = Label (window, text="Выберете лог", font=("Arial Bold", 30), bg="deep sky blue")
lbl.grid(column=0, row=0)
frame = Frame(window, width=600, height=250, bg="white")
frame.place(x=20, y=100, relwidth=0.9, relheight=0.7)

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
btn_load_and_scrap = Button(frame, text="Выбрать и загрузить", font=("Calibri", 14), bg="deep sky blue", fg="white",command=sal)
rad1.place(x=20, y=70)
rad1_1.place(x=20, y=100)
rad1_2.place(x=20, y=130)
rad2.place(x=20, y=160)
rad2_1.place(x=20, y=190)
rad2_2.place(x=20, y=220)
rad3.place(x=20, y=250)
rad3_1.place(x=20, y=280)
rad3_2.place(x=20, y=310)
btn_load_and_scrap.place(x=20, y=370)
btn_back = Button(window, text="Вернутся на окно выбора",  font=("Calibri", 14), bg="deep sky blue", fg="white",command=back)
btn_back.place(x=300, y=370)

window.mainloop()