import configparser


config = configparser.ConfigParser(allow_no_value=True)
config.read('config')

current_vps = config['current']['vps']
print(config[current_vps])
