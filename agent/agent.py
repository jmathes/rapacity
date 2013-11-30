import random

class Agent(object):
    def __init__(self, name):
        if name is None:
            name = random.choice(["Pat", "Sam", "Casey", "Alex", "Devin", "Corey"])
        self.id = random.randint(-9223372036854775808, 9223372036854775807)
        self._contacts = {}


    def act(self):
        pass

    def react(self, interaction):
        pass
