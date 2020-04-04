import yaml


with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'webserver': {
            'host': '127.0.0.1'
        }
    }, yaml_file)

