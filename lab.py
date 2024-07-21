import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Бронь утилита')
app.geometry('600x600')
app.config(bg='#18161D')
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 13, 'bold')
font3 = ('Arial', 18, 'bold')

def add_to_treeview():
    tickets = database.get_tickets()
    tree.delete(*tree.get_children())
    for ticket in tickets:
        if ticket[2] > 0:
            tree.insert('', END, values = ticket)

def reservation(name, movie, quantity, price):
    customer_name = name
    movie_name = movie
    booked_quantity = quantity
    ticket_price = price
    total_price = ticket_price * booked_quantity

    frame = customtkinter.CTkFrame(app, bg_color = '#18161D', fg_color = '#292933', corner_radius = 10, border_width = 2, border_color = '#0f0', width = 200, height = 130)
    frame.place(x = 190, y = 450)

    name_label = customtkinter.CTkLabel(frame, font = font3, text = f'Имя: {customer_name}', text_color = '#fff', bg_color = '#292933')
    name_label.place(x = 10, y = 10)

    movie_label = customtkinter.CTkLabel(frame, font = font3, text = f'Фильм: {movie_name}', text_color = '#fff', bg_color = '#292933')
    movie_label.place(x = 10, y = 50)

    total_price_label = customtkinter.CTkLabel(frame, font = font3, text = f'Цена: {total_price}', text_color = '#fff', bg_color = '#292933')
    total_price_label.place(x = 10, y = 90)

    return total_price

def book():
    customer_name = name_entry.get()
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Ошибка!', 'Выберите билет для брони')
    elif not customer_name:
        messagebox.showerror('Ошибка!', 'Введите имя покупателя')
    else:
        row = tree.item(selected_item)['values']
        movie_name = row[1]
        ticket_price = row[3]
        booked_quantity = int(variable1.get())
        if booked_quantity > row[2]:
            messagebox.showerror('Ошибка!', 'Недостаточно билетов')
        else:
            database.update_quantity(row[0], booked_quantity)
            add_to_treeview()
            total_price = reservation(customer_name, movie_name, booked_quantity, ticket_price)
            with open('Tickets.txt', 'a') as file:
                file.write(f'Имя покупателя: {customer_name}\n')
                file.write(f'Название фильма: {movie_name}\n')
                file.write(f'Общая цена: {total_price}$\n=================\n')
            messagebox.showinfo('Успешно!', 'Билеты были забронированы!')

title1_label = customtkinter.CTkLabel(app, font = font1, text = 'Добро пожаловать! \n Выберите фильм для брони', text_color = '#fff', bg_color = '#18161D')
title1_label.place(x = 105, y = 20)

image1 = PhotoImage(file = 'C:\\Users\\Vladislav\\Desktop\\db\\1.jpg')
image1_label = Label(app, image = image1, bg = '#18161D')
image1_label.place(x = 40, y = 25)

name_label = customtkinter.CTkLabel(app, font = font3, text = 'Имя покупателя:', text_color = '#fff', bg_color = '#18161D')
name_label.place(x = 120, y = 300)

name_entry = customtkinter.CTkEntry(app, font = font3, text_color = '#000', fg_color = '#fff', border_color = '#AA04A7', border_width = 2, width = 160)
name_entry.place(x = 290, y = 300)

number_label = customtkinter.CTkLabel(app, font = font3, text = 'Кол-во билетов:', text_color = '#fff', bg_color = '#18161D')
number_label.place(x = 122, y = 350)

variable1 = StringVar()
options = ['1', '2', '3', '4', '5', '6']

duration_options = customtkinter.CTkComboBox(app, font = font3, text_color = '#000', fg_color = '#fff', dropdown_hover_color = '#AA04A7', button_color = '#AA04A7', button_hover_color = '#AA04A7', border_color = '#AA04A7', width = 160, variable = variable1, values = options, state = 'readonly')
duration_options.set('1')
duration_options.place(x = 290, y = 350)

book_button = customtkinter.CTkButton(app, command = book, font = font3, text_color = '#fff', text = 'Забронировать', fg_color = '#AA04A7', hover_color = '#6D006B', bg_color = '#18161D', cursor = 'hand2', corner_radius = 15, width = 200)
book_button.place(x = 190, y = 400)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font = font2, foreground = '#fff', background = '#000', fieldbackground = '#292933')
style.map('Treeview', background = [('selected', '#AA04A7')])

tree = ttk.Treeview(app, height = 8)

tree['columns'] = ('Ticket ID', 'Movie Name', 'Avilable Tickets', 'Ticket Price')

tree.column('#0', width = 0, stretch = tk.NO)
tree.column('Ticket ID', anchor = tk.CENTER, width = 100)
tree.column('Movie Name', anchor = tk.CENTER, width = 100)
tree.column('Avilable Tickets', anchor = tk.CENTER, width = 100)
tree.column('Ticket Price', anchor = tk.CENTER, width = 100)

tree.heading('Ticket ID', text = 'ID Билета')
tree.heading('Movie Name', text = 'Название фильма')
tree.heading('Avilable Tickets', text = 'Кол-во билетов')
tree.heading('Ticket Price', text = 'Цена')

tree.place(x = 90, y = 95)

add_to_treeview()

app.mainloop()