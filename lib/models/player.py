from __init__ import CURSOR
class players():

    def __init__(self, name, ppg, apg, rpg, spg, bpg, team, id=None):
        self.id = id
        self.name = name
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg
        self.team = team

    def save(self):
        if self.id:
            CURSOR.execute('UPDATE players SET name = ?, PointsPerGame = ?, AssistsPerGame = ?, ReboundsPerGame = ?, StealsPerGame = ?, BlocksPerGame = ?, Team = ? WHERE id = ?', (self.name, self.ppg, self.apg, self.rpg, self.spg, self.bpg, self.team, self.id))
        else:
            CURSOR.execute('INSERT INTO players (name, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame, Team) VALUES (?, ?, ?, ?, ?, ?, ?)', (self.name, self.ppg, self.apg, self.rpg, self.spg, self.bpg, self.team))
            self.id = CURSOR.lastrowid

for row in CURSOR.execute('SELECT * FROM players'):
    player = players(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
    print(player.name)


