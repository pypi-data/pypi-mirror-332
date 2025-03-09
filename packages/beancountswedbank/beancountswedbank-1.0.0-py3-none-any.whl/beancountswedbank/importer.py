#!/usr/bin/env python3
import csv
import re
from itertools import islice

from beangulp import mimetypes
from beangulp.importers import csvbase


class SwedbankCSVReader(csvbase.CSVReader):
    encoding = 'iso-8859-15'
    skiplines = 1

    HEAD = re.compile(r'^\* Transaktioner Period ([0-9]{4}-[0-9]{2}-[0-9]{2}).([0-9]{4}-[0-9]{2}-[0-9]{2}) Skapad ([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2}) ([+-][0-9]{2}:[0-9]{2}|CES?T)$')
    FIELDS = ['Radnummer',
              'Clearingnummer',
              'Kontonummer',
              'Produkt',
              'Valuta',
              'Bokföringsdag',
              'Transaktionsdag',
              'Valutadag',
              'Referens',
              'Beskrivning',
              'Belopp',
              'Bokfört saldo',
              ]

    def read(self, filepath):
        columns = {'date': csvbase.Date(self.FIELDS[5], "%Y-%m-%d"),
                   'amount': csvbase.Amount(self.FIELDS[10]),
                   'currency': csvbase.Column(self.FIELDS[4]),
                   'narration': csvbase.Column(self.FIELDS[9]),
                   'payee': csvbase.Column(self.FIELDS[8]),
                   'balance': csvbase.Amount(self.FIELDS[11]),
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


class CSVImporter(csvbase.Importer, SwedbankCSVReader):
    """The actual importer protocol for CSV exported reports from Swedbanken online banking"""

    def __init__(self, bankaccount, account, currency, flag='*'):
        super().__init__(account, currency, flag)
        self.bankaccount = bankaccount

    def identify(self, filepath):
        mimetype, _ = mimetypes.guess_type(filepath)
        if mimetype != 'text/csv':
            return False
        with open(filepath, 'rt', encoding=SwedbankCSVReader.encoding) as fd:
            try:
                line = fd.readline()
                if not SwedbankCSVReader.HEAD.match(line):
                    return False
            except:
                pass

            line = fd.readline().strip()
            if not line.startswith(','.join(SwedbankCSVReader.FIELDS)):
                return False
            reader = csv.reader(fd)
            row = next(reader)
            return self.bankaccount in {row[2], row[3]}

