#!/usr/bin/env python3
import csv
from decimal import Decimal
from itertools import islice

from beangulp import mimetypes
from beangulp.importers import csvbase


class NLBalance(csvbase.Column):
    def parse(self, value):
        value = value.replace('.', '').replace(',', '.')
        return Decimal(value)


class NLAmount(csvbase.Column):
    def parse(self, *values):
        amount, kind = values
        multiplier = 1
        if kind == 'Debet':
            multiplier = -1
        amount = amount.replace('.', '').replace(',', '.')
        return multiplier * Decimal(amount)


class TriodosCSVReader(csvbase.CSVReader):
    encoding = 'iso-8859-15'

    def read(self, filepath):
        columns = {'date': csvbase.Date(0, "%d-%m-%Y"),
                   'amount': NLAmount(2, 3, default=None),
                   'narration': csvbase.Column(7),
                   'payee': csvbase.Column(4),
                   'balance': NLBalance(8),
                  }
        with open(filepath, encoding=self.encoding) as fd:
            lines = islice(fd, self.skiplines, None)
            reader = csv.reader(lines)

            headers = {name.strip(): index
                       for index, name in enumerate(next(reader))}
            row = type('Row', (tuple,), {k: property(v.getter(headers))
                                         for k, v in columns.items()})
            for csvrow in reader:
                yield row(csvrow)


class CSVImporter(csvbase.Importer, TriodosCSVReader):
    """The actual importer protocol for CSV exported reports from Triodos online banking"""

    def __init__(self, bankaccount, account, currency='EUR', flag='*'):
        super().__init__(account, currency, flag)
        self.bankaccount = bankaccount

    def identify(self, filepath):
        mimetype, _ = mimetypes.guess_type(filepath)
        if mimetype != 'text/csv':
            return False
        with open(filepath, 'rt', encoding=TriodosCSVReader.encoding) as fd:
            reader = csv.reader(fd)
            try:
                row = next(reader)
            except:
                return False
            return len(row) == 9 and self.bankaccount == row[1]
