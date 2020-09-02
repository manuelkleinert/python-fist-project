#!/usr/bin/env python3

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

print(config)
print ("Sections : ", config.sections())
print ("Sections : ", config.has_section('settings'))


# config.set('Settings', 'year','2050') #Updating existing entry
# config.set('Settings', 'day','sunday') #Writing new entry
# # config.write(configFile.open("w"))
#
# #
# year = config['Settings']['year']
# print(year)
