#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import csv
import unittest
from docopt import docopt
import sys
from auditor import do_add_headers
import json
import yaml
from auditor.mappings import Mappings


import yaml
#from auditor.mappings import Mappings
_file = 'Workbook1.csv'
_config = 'blacklist.config.yaml'
_output = 'output.csv'
_verbose = 'blacklisted'
import pdb

class Test(unittest.TestCase):

	# def __init__(self, config, **kwargs):
	# 	self.bad_data = config['error_strings']['bad_data']
	# 	self.empty_cell = config['error_strings']['empty_cell']
	# 	self.blacklisted = config['error_strings']['blacklisted']

	# 	self.blacklists = {}
	# 	for item in config['blacklist']:
	# 		with open(item['vals_file_path']) as values_file:
	# 			self.blacklists[item['header_name']] = self.parse(values_file)


        

	# def test_do_add_headers(self):
	# 	with open(_config, 'r') as config_file:
	# 		global config
	# 		config = yaml.load(config_file.read())
	# 	csv_file = open(_file, 'r')
	# 	data = csv.reader(csv_file, **config['csv_conf'])
	# 	data1 = do_add_headers(data, config.get('new_headers'))
		
	# 	print(data1)
	# 	with open(_output, 'w') as outputfile:
	# 		wr = csv.writer(outputfile, dialect='excel')
	# 		wr.writerows(data1)

       
	# 	with open('expected.csv',mode = 'r') as expectedfile:
	# 		reader = csv.DictReader(expectedfile)
	# 		r = reader.fieldnames
	# 	with open(_output, 'r') as outputfile:
	# 		reader1 = csv.DictReader(outputfile)
	# 		r1 = reader1.fieldnames
	# 		print(r)
	# 		print(r1)
	# 	self.assertListEqual(r,r1)


	# def is_blacklist(self, **kwargs):
 #        item = kwargs.get('item')
 #        header = kwargs.get('header')
 #        try:
 #            if item == '':
 #                return self.empty_cell
 #            else:
 #            	return self.blacklisted if item in self.blacklists.get(header) else item
 #        except Exception as ex:
 #            if self.verbose:
 #                print('is_blacklist exception')
 #                print(ex)
 #        	return self.bad_data

	def test_blacklisted(self):
		with open(_config, 'r') as config_file:
			global config
			config = yaml.load(config_file.read())

		mappings = Mappings(config,verbose=_verbose)

		header = config.get('new_headers')
		cell = row[index]
		for mapping in config['mappings']:
			if headers[index] == mapping['header']:
				for map_index, my_map in enumerate(mapping['maps']):
					kwargs = {
                        'item': cell,
                        'headers': headers,
                        'header': headers[index],
                        'index': index,
                        'row': row,
                        'map': mapping['maps'][map_index]
                    }

			csv_file = open(_file, 'r')
			data = csv.reader(csv_file, **config['csv_conf'])
			data1 = Mappings.is_blacklist(**kwargs)
		
			print(data1)
unittest.main()




