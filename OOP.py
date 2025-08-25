
class Universe:
    def __init__(self, galaxies):
        self.galaxies = galaxies
        self.stars = galaxies * 100000000 # approx
    
    def CountUniverseItems(self):
        print(f"There are {self.galaxies:,} galaxies and {self.stars:,} stars")

Uni = Universe(200000000000)

print(Uni.CountUniverseItems())