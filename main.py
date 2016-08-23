#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sqlite
import sys
import logging
from datetime import date

"""[application description here]"""
__appname__ = "[working_hours]"
__author__ = "MassiH"
__version__ = "0.1"

log = logging.getLogger(__name__)


def connect():
    _date = date.today()
    _table_name = 'table_{}'.format(_date.year)
    con = sqlite.connect('payment.db')
    with con:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS {}(WDate TEXT PRIMARY KEY, Normal_hour INTEGER, Komp_hour INTEGER)".format(_table_name))
        _hours = input('hours for today %s' % date.today())
        cursor.execute('INSERT INTO {}(WDate,Normal_hour,Komp_hour) VALUES (?, ?, ?)'.format(_table_name), (_date, _hours, 0))
        cursor.execute('SELECT * FROM {}'.format(_table_name))
        data = cursor.fetchone()
        print('SQLite version is %s' % str(data))


def main():
    print(date.today().year)
    connect()


if __name__ == '__main__':
    main()
