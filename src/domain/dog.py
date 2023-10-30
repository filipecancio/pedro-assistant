import array as arr
class Dog:
    hunger = [],
    thirst = [],
    
    def __init__(self, name):
        self.name = name
        self.hunger = ["🍪"],
        self.thirst = ["🥛","🥛","🥛","🥛","🥛"],

    def drink(self):
        size = len(self.thirst)
        while size > 5:
            self.thirst.append("🥛")
            size += 1
        return f'🐶 {self.name} is drinking water'
    
    def eat(self):
        size = len(self.hunger)
        while size > 5:
            self.hunger.append("🍪")
            size += 1
        return f'🐶 {self.name} is eating food'
    
    def poop(self):
        try:
            self.hunger.pop(1)
            return f'🐶 {self.name} pooped 💩'
        except(IndexError):
            self.onHungry()
    
    def peed(self):
        try:
            self.thirst.pop()
            return f'🐶 {self.name} peed 💦'
        except(IndexError):
            self.onThirsty()
    
    def onHungry(self):
        return f'🐶 {self.name} is very hungry 😭😭😭'
    
    def onThirsty(self):
        return f'🐶 {self.name} is very thirsty 😭😭😭'
    
    def seeThirsty(self):
        return f'🐶 {self.name} hungry: {self.thirst}'
    
    def seeHungry(self):
        return f'🐶 {self.name} thirsty: {self.hunger}'