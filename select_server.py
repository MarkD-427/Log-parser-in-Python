from tkinter import *
from tkinter import ttk

def serv_select():  
    lbl2.configure(text=selected.get())

window = Tk()
window.title("Выберете сервер")
window.geometry('500x400')
window.configure(bg="lightblue")
lbl = Label (window, text="Выберете сервер", font=("Arial Bold", 30), bg="lightblue")
lbl.grid(column=0, row=0)
frame = Frame(window, width=400, height=250, bg="white")
frame.place(x=20, y=100, relwidth=0.5)

lbl_serv = Label (frame, text="Меню серверов", font=("Arial Bold", 20), bg="lightblue")
# lbl_serv.pack(anchor='center')
lbl_serv.place(x=10, y=20)

selected = IntVar()
rad1 = Radiobutton(frame, text='Почта', value=1, variable=selected)  
rad2 = Radiobutton(frame, text='Openfire', value=2, variable=selected)  
rad3 = Radiobutton(frame, text='FTP', value=3, variable=selected)
btn = Button(frame, text="Продолжить", command=serv_select)
# rad1.pack(anchor='center')
# rad2.pack(anchor='center')
# rad3.pack(anchor='center')
# btn4.pack(anchor='center')
menu = Menu(window)
new_item = Menu(menu, tearoff=0)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Изменить')  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  
rad1.place(x=20, y=70)
rad2.place(x=20, y=90)
rad3.place(x=20, y=110)
btn.place(x=20, y=140)

window.mainloop()