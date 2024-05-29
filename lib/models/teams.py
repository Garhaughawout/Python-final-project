from player import players
from .__init__ import CURSOR, CONN
class team(players):

    def __init__(self, name, wins, losses, ppg, apg, rpg, spg, bpg):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg

    def addPlayerToTeam():
        pass