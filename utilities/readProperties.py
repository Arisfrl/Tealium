import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\Configurations\\" + "config.ini")
print(os.path.abspath(os.curdir))


class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password
