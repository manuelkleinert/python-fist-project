try:
    import os
    import yaml
except ImportError:
    print('yaml not install')
    exit(1)

class Config:
    def __init__(self, main_file):
        root_dir = os.path.dirname(main_file)
        config_path = os.path.join(root_dir, 'config\config.yml')
        self.config = open(config_path, 'r')

    def get(self):
        return yaml.load(self.config, Loader=yaml.FullLoader) 
