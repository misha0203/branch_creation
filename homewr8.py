# SQL - Structured Query Language
# СУБД - Система управления Базой Данных
# CRUD - Create, Read, Update, Delete
import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def select_all_students(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchmany(3)
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def delete_student(conn, id):
    try:
        sql = '''DELETE FROM students WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def update_student_mark_and_martial_status(conn, student):
    try:
        sql = '''UPDATE students SET mark=?, is_married=? WHERE id=?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


def update_student(conn, student):
    try:
        sql = '''UPDATE students SET mark=?, is_married=? WHERE id=?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


connection = create_connection(r"gr_23_3.db")
create_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''
if connection is not None:
    print("Connection Successfully")

    select_all_students(connection)

    # update_student_mark_and_martial_status(connection,(15.08,True,2))

    # delete_student(connection, 3)

    # create_table(connection, create_students_table)
    # create_student(connection,("Akyl Askarov",58.00,"Chess","2000-01-01",False))
    # create_student(connection, ("Akylbek u Arsen", 60.00, "Football", "2002-02-15", False))
    # create_student(connection, ("Bekberdi Sadyrbekov", 60.00, None, "2006-11-24", False))
    # create_student(connection, ("Adil Tashtanaliev", 58.00, "Books", "2008-06-03", False))
    # create_student(connection, ("Ruslan Aslanov", 58.00, None, "2006-07-13", False))
    # create_student(connection, ("Bektur Karimov", 58.00, "Walking", "2004-08-22", False))
    # create_student(connection, ("Kirill Savenko", 58.00, None, "2002-10-11", False))
    # create_student(connection, ("Iskender Zholdoshbaev", 58.00, "Driving car", "2000-03-19", False))
    print("Done!")
