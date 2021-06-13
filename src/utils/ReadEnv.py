import configparser

class ReadEnv:

    def __init__(self, configFile:str = "bot.config"):
        self.configFile = configFile
        self.SECRET = ""
        self.TOKEN = ""
        self.grabEnv()

    def grabEnv(self):
        section = "bot-config"
        config = configparser.ConfigParser()
        config.read(self.configFile)
        botConfigs = config[section]

        self.SECRET = botConfigs["SECRET"]
        self.TOKEN = botConfigs["TOKEN"]

    def getSecret(self):
        return self.SECRET

    def getToken(self):
        return self.TOKEN

