import csv
import yaml
import unittest
import os.path

#Checking if main config file exists

_config = 'auditor.example.conf.yaml'

class check_do_check_config(unittest.TestCase):
    def test_check_config(self):
        self.assertTrue(os.path.isfile(_config))
unittest.main()
        #    self.assertTrue(filecmp.cmp(tst_path, ref_path, shallow=False),'Result is Unexpected')
