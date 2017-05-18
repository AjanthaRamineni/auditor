import csv
import yaml
import unittest
import os.path

#Checking if LookUp file exists

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
        for key in new_headers.keys():
            header_data = new_headers[key]
            self.assertTrue(os.path.isfile(header_data['lookup_file']))
            print(os.path.isfile(header_data['lookup_file']))
unittest.main()
