#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import csv
import unittest
from docopt import docopt
import sys
from auditor import do_add_headers


import yaml
#from auditor.mappings import Mappings
_file = 'Workbook1.csv'
_config = 'auditor.example.conf.yaml'
_output = 'output.csv'
import pdb

class Test(unittest.TestCase):

	def test_do_add_headers(self):
		print('test')
		with open(_config, 'r') as config_file:
			global config
			config = yaml.load(config_file.read())
		csv_file = open(_file, 'r')
		data = csv.reader(csv_file, **config['csv_conf'])
		data1 = do_add_headers(data, config.get('new_headers'))
		
		print(data1)
		with open(_output, 'w') as outputfile:
			wr = csv.writer(outputfile, dialect='excel')
			wr.writerows(data1)

       
		with open('expected.csv',mode = 'r') as expectedfile:
			reader = csv.DictReader(expectedfile)
			r = reader.fieldnames
		with open(_output, 'r') as outputfile:
			reader1 = csv.DictReader(outputfile)
			r1 = reader1.fieldnames
			print(r)
			print(r1)
		self.assertListEqual(r,r1)
unittest.main()

 
