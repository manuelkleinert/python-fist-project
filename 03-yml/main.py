import os
import yaml

root_dir = os.path.dirname(__file__)

config_path = os.path.join(root_dir, 'config.yml')
config = open(config_path, 'r')

data = yaml.load(config, Loader=yaml.FullLoader)

print(data['floors'])

for floor in data['floors']:
        print('floors ', floor)
