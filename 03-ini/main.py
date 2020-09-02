#!/usr/bin/env python3

import os
from configparser import ConfigParser

root = os.path.abspath(os.curdir)

config = ConfigParser()
config.read(['config.ini'])

print(config)
print(os.path.abspath('config.ini'));
print(os.path.isfile(os.path.abspath('config.ini')))
print ("Sections : ", config.sections())
print ("Sections : ", config.has_section('settings'))


# config.set('Settings', 'year','2050') #Updating existing entry
# config.set('Settings', 'day','sunday') #Writing new entry
# # config.write(configFile.open("w"))
#
# #
# year = config['Settings']['year']
# print(year)
