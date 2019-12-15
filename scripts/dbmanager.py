import sqlite3
import hashlib
import argparse
import random


''' This function is the one that checks if an already
    existing database is present in the repository.
    If not, it will create a table with SQL '''


def check_or_create():

    global conn
    global cursor
    conn = sqlite3.connect("ourdatabase.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        '''Create table'''
        cursor.execute('''CREATE TABLE user
                      (username CHAR(256),
                       hasha CHAR(256),
                       salt CHAR(256),
                       PRIMARY KEY (hasha))''')


''' Here, we are passing three arguments that
    the programm will ask the user to insert '''


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument("-p", help="the username password",
                        required=True)
    parser.add_argument("-c", help="Check username and password",
                        required=False)
    return parser.parse_args()


''' Once the user has inserted the username
    and the password, his data will be saved
    in the database that we have before hand created '''


def save_new_username(username, password):
    global conn
    global cursor

    salt = str(random.random())
    hasha = salt + password

    for i in range(100000):
        hasha = hashlib.sha256(hasha.encode('utf-8')).hexdigest()

    cursor.execute("DELETE FROM user WHERE username=?", (username,))
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, hasha, salt))
    conn.commit()
    print("The user {} has correctly inserted to ourdatabase".format(username))


''' This function check if the data of the
    user are contained in ourdatabase. If yes,
    the user is allowed to have access to the data '''


def check_for_username(username, password):
    global conn
    global cursor

    conn = sqlite3.connect("ourdatabase.db")
    cursor = conn.cursor()
    salt = cursor.execute("SELECT salt FROM user WHERE username=?",
                          (username,)).fetchall()

    conn.commit()

    hasha = str(salt[0][0]) + password

    for i in range(100000):
        hasha = hashlib.sha256(hasha.encode('utf-8')).hexdigest()

    rows = cursor.execute("SELECT * FROM user WHERE username=? and hasha=?",
                          (username, hasha))

    conn.commit()
    results = rows.fetchall()
    '''NOTE: this could be done more efficiently with a JOIN'''
    if results:
        print("User is present, password is valid")
    else:
        print("User is not present, or password is invalid")

    cursor.close()
    conn.close()


args = parse_args()
check_or_create()


if args.a and args.p:
    save_new_username(args.a, args.p)
elif args.c and args.p:
    check_for_username(args.c, args.p)

conn.close()
