class Player:
    def __init__(self, name, Health, Strength, Level):
        self.name = name
        self.Health = Health
        self.Strength = Strength
        self.Level = Level
    def show_stats(self):
        print(f"Name -> {self.name}")
        print(f"Health -> {self.Health}")
        print(f"Strength -> {self.Strength}")
        print(f"Level -> {self.Level}")