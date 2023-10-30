from general_functions import  getJson

class Assistant():    
    def __init__(self):
        self.settings = getJson("/util/data/config.json")
        self.ASSISTANT_NAME = self.settings["assistant_name"]

    def doComand(self, command):
        if not self.isCorrectAssitant(command[0]):
            return "Nome de assistente incorreto."
        elif self.hasCommandList(command) != None:
            command_list = self.hasCommandList(command)
            command_phrase = self.hasCommand(command_list,command)
            return command_phrase
        else:
            return "Comando não encontrado."
        
    def isCorrectAssitant(self, name):
        return name == self.ASSISTANT_NAME
    
    def isValidCommand(self, action, target):
        for settings_action in self.settings["action"]:
            if settings_action["name"] == action:
                if target in settings_action["target"]:
                    return True
                
        return False
    
    def foundAnimalType(self, animal_type, prhase_array):
        if animal_type in prhase_array:
            return animal_type
        else :
            return False
        
    def hasCommandList(self, prhase_array):
        for settings_action in self.settings["actions"]:
            if settings_action["target"] == self.foundAnimalType(settings_action["target"], prhase_array):
                return settings_action["commands"]
            else :
                return None
        return None
    
    def hasCommand(self, command_list, prhase_array):
        for command in command_list:
            if command["target"] == self.foundAnimalType(command["target"], prhase_array):
                return command["command"]
        return None