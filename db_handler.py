#!/usr/bin/python3

"""
"""

# -*- coding: utf-8 -*-
import sqlite3 as sqlite

log = logging.getLogger(__name__)

def connect(_date, _hours):
    _table_name = 'table_{}'.format(_date.year)
    _month = _date.month

    con = sqlite.connect('payment.db')
    with con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}"
                       "(WDate TEXT PRIMARY KEY,"
                       " Normal_hour INTEGER, "
                       "Komp_hour INTEGER)"
                       .format(_table_name))
        cursor.execute('INSERT INTO {}(WDate,Normal_hour,Komp_hour) VALUES (?, ?, ?)'.format(_table_name),
                       (_date, _hours, _hours-8))
        cursor.execute('SELECT * FROM {}'.format(_table_name))
        all_data = cursor.fetchall()
        print_table(all_data)


def insert_update():
    pass


def print_table(_data):
    pass
