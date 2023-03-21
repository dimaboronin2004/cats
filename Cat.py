class Cat:
    def __init__(self, name):
        self.__name = name
        self.energy = 50
        self.mood = 50

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def play(self, time):
        self.mood += 1 * time
        self.energy -= 1 * time
        if self.energy < 0 or self.mood > 100:
            raise ValueError('Mood or energy out of range')
