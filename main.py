#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as sqlite
import sys
import logging

"""[application description here]"""
__appname__ = "[sqlite3 connection]"
__author__  = "MassiH"
__version__ = "0.1"

log = logging.getLogger(__name__)


def connect():
    con = sqlite.connect('payment.db')
    with con:
        cursor = con.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        data = cursor.fetchone()
        print('SQLite version is %s'% data)


def main():
    connect()

if __name__ == '__main__':
    main()
