#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as sqlite
import logging
import argparse
from datetime import date, datetime

"""[application description here]"""
__appname__ = "[working_hours]"
__author__ = "MassiH"
__version__ = "0.1"

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


def arg_parser():
    parser = argparse.ArgumentParser(description='A simple app to keep track of working hours!')
    parser.add_argument('hours', metavar='H', type=int, help='working hours')
    parser.add_argument('--date', '-d', default=date.today(), type=validate_date,
                        help='the target date (default: today) yyyy-mm-dd')
    args = parser.parse_args()
    return args


def print_table(all_data):
    all_data.sort(reverse=True)
    print('-'*20)
    print("\n".join(['| {0} | {1} | {2} |'.format(row[0], row[1], row[2]) for row in all_data]))
    print('-' * 20)
    print('Total Komp Hour: {}'.format(sum([row[2] for row in all_data])))


def validate_date(args_date):
    try:
        return datetime.strptime(args_date, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid date: {}, please use YYYY-MM-DD style".format(args_date))


def main():
    args = arg_parser()
    connect(args.date, args.hours)


if __name__ == '__main__':
    main()
