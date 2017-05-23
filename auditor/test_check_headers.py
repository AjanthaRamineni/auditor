import csv
import yaml
import unittest
import os.path
import filecmp

_config = 'auditor.example.conf.yaml'
_file = 'Testdata.csv'
class check_lookupfile_headers(unittest.TestCase):
    def test_lookupfile_exists(self):
        with open(_config, 'r') as config_file:
            global config
            config = yaml.load(config_file.read())

        csv_file = open(_file, 'r')
        data = csv.reader(csv_file, **config['csv_conf'])

        new_headers = config.get('new_headers')
        new_rows = []
        for key in new_headers.keys():
            header_data = new_headers[key]
            with open(header_data['lookup_file'], 'r') as lookup_file:
                lookup_data = yaml.load(lookup_file.read())
            for index, row in enumerate(data):
                if index == 0:
                    old_headers = row
                    row.append(new_headers[key]['name'])
                    try:
                        new_rows[index] = row
                    except IndexError:
                        new_rows.append(row)
                else:
                    lookup_key = row[old_headers.index(header_data['key'])]
                    lookup_value = lookup_data.get(lookup_key) or header_data['default'] or ''
                    row.append(lookup_value)
                    try:
                        new_rows[index] = row
                    except IndexError:
                        new_rows.append(row)
        for index, row in enumerate(new_rows):
            print row
unittest.main()
