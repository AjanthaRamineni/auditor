#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import csv
import unittest
from docopt import docopt
import sys
import auditor

import yaml
#from auditor.mappings import Mappings
_file = 'Workbook1.csv'
_config = 'auditor.example.conf.yaml'
#_output = '--output'
import pdb

class Test(unittest.TestCase):
	def test_do_add_headers(self):
		print('test')
		with open(_config, 'r') as config_file:
			global config
			config = yaml.load(config_file.read())
		csv_file = open(_file, 'r')
		data = csv.reader(csv_file, **config['csv_conf'])
		data1 = auditor.do_add_headers(data, config.get('new_headers'))
		print(data1)
    

	#def test_do_add_headers(self):

	#	with open('expected.csv',mode = 'r') as expectedfile:
	#		reader = csv.DictReader(csvfile)
	#		reader1 = csv.DictReader(open('output.csv'))
	#		r = reader.fieldnames
	#		r1 = reader1.fieldnames
	#		for row in r:
	#			print(row)
	#		print(r)
	#		print(r1)
	#	self.assertListEqual(r,r1)

unittest.main()




 
