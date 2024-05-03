from configparser import ConfigParser

config = ConfigParser()
config.read('/etc/conf/gaian/mobius-gpt-service/config.ini')

print(config)

consul_service_url = config['CONSUL']['consul service url']
print(consul_service_url)



#database
host = config['DATABASE']['host']
database = config['DATABASE']['database']
username = config['DATABASE']['username']
password = config['DATABASE']['password']

