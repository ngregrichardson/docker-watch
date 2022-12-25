import yaml

def load_config():
    try:
        with open("config.yml", "r") as yamlfile:
            return yaml.load(yamlfile, Loader=yaml.FullLoader)
    except FileNotFoundError:
        return None