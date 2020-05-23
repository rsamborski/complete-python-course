# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __repr__(self):
        return "Club {}: {}".format(self.name, self.players)

    def __str__(self):
        return "Club {} with {} players".format(self.name, len(self))


some_club = Club("Aresenal")
some_club.players.append("Giorgo Armani")
some_club.players.append("Son of Sons")
some_club.players.append("Master of puppets")

print(some_club)
