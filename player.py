class Player:
    def __innit__(self, name, Health, Strength, Level):
        self.name = name
        self.Health = Health
        self.Strength = Strength
        self.Level = Level
    def print_person_info(self):
        print(self.name, self.Health, self.Strength, self.Level)
