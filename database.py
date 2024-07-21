import sqlite3

def create_table():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
            ticket_id TEXT PRIMARY KEY,
            movie_name TEXT,
            ticket_quantity INTEGER,
            ticket_price INTEGER)''')
    
    conn.commit()
    conn.close()

def insert_Tickets():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()

    Tickets_data = [
        #('Код','Наз-ие фильма', Кол-во билетов, Цена)
        ('D1', 'Битлджус 2', 4, 200),
        ('D2', 'Тихое место: День первый', 1, 200),
        ('D3', 'Дюна: Часть 2', 6, 200),
        ('D4', 'Я не киллер', 9, 200),
        ('D5', 'Каскадеры', 2, 200),
        ('Y2', 'Жизнь Пи', 10, 150)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id, movie_name, ticket_quantity, ticket_price) VALUES(?, ?, ?, ?)', Tickets_data)

    conn.commit()
    conn.close()

def get_tickets():
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets = cursor.fetchall()
    conn.close()

    return tickets

def update_quantity(id, reserved_quantity):
    conn = sqlite3.connect('Reservation.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Tickets SET ticket_quantity = ticket_quantity - ? Where ticket_id = ?', (reserved_quantity, id))
    conn.commit()
    conn.close()

create_table()
insert_Tickets()