import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        db = sqlite3.connect('mail.db')
        return db
    except Error:
        print(Error)


def create_table(con):
    try:
        cur = con.cursor()
        cur.execute('''CREATE TABLE mail(
        id INTEGER PRIMARY KEY,
        sender INTEGER,
        receiver INTEGER,
        headline TEXT,
        mailtext TEXT,
        date TEXT);''')
        con.commit()
        print('The table is created successfully')
    except Error:
        print(Error)


def insert_data(con, entities):
    
    query = """INSERT INTO mail (id, sender, receiver, headline, mailtext, date) VALUES(?,?,?,?,?,?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Error:
        print(Error)


def add_data(con):
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO mail VALUES(2, 'David', 'Tom', 'Dev', 'text2', '2020-06-01')")
        cur.execute("INSERT INTO mail VALUES(3, 'Tom', 'Alan', 'Manager', 'text3','2018-03-02')")
        cur.execute("INSERT INTO mail VALUES(4, 'Alan', 'David', 'Dev', 'text4','2019-04-15')")
        con.commit()
        print("The records added successfully")
    except Error:
        print(Error)


def select_all(con):
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM employees')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def update_data(con, salary, id):
    try:
        cur = con.cursor()
        cur.execute("UPDATE mail SET mailtext = ?  WHERE id = ?", ('mailtext', id))
        con.commit()
        print("The record updated successfully")
    except Error:
        print(Error)


def delete_record(con, sender):
    """ Delete the given record
    """
    query = "DELETE FROM mail WHERE sender = ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (sender,))
        con.commit()
        print("The record deleted successfully")
    except Error:
        print(Error)


def main():
    con = sql_connection()
    create_table(con)
    entities = (1, 'Anna', 'Thomas', 'IT','text1', '2020-02-09')
    insert_data(con, entities)
    add_data(con)
    select_all(con)
    update_data(con, 'changedtext1', 1)
    delete_record(con, "Alan")
    con.close()


if __name__ == "__main__":
    main()