try:
    import yaml
except ImportError:
    print 'yaml not install'
    exit()

class config_func:
    def __init__(self):
        self.root_dir = os.path.dirname(__file__)
        self.config_path = os.path.join(root_dir, 'config.yml')
        self.config = open(config_path, 'r')
        print(self.root_dir)
