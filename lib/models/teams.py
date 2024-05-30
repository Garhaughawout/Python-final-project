from models.players import players
from models.__init__ import CURSOR, CONN
class teams(players):
    teamlist = []

    def __init__(self, name, wins, losses, ppg, apg, rpg, spg, bpg):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg
        teams.add_to_teamlist(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return print("Invalid input. must be a string")

    @property
    def wins(self):
        return self._wins
    
    @wins.setter
    def wins(self, wins):
        if isinstance(wins, int):
            self._wins = wins
        else:
            return print("Invalid input must be an Integer")
    
    @property
    def losses(self):
        return self._losses
    
    @losses.setter
    def losses(self, losses):
        if isinstance(losses, int):
            self._losses = losses
        else:
            return print("Invalid input must be an Integer")
    
    @property
    def ppg(self):
        return self._ppg
    
    @ppg.setter
    def ppg(self, ppg):
        if isinstance(ppg, float):
            self._ppg = ppg
        else:
            return print("Invalid input must be a float")

    @property
    def apg(self):
        return self._apg

    @apg.setter
    def apg(self, apg):
        if isinstance(apg, float):
            self._apg = apg
        else:
            return print("Invalid input must be a float")
    
    @property
    def rpg(self):
        return self._rpg
    
    @rpg.setter
    def rpg(self, rpg):
        if isinstance(rpg, float):
            self._rpg = rpg
        else:
            return print("Invalid input must be a float")
        
    @property
    def spg(self):
        return self._spg
    
    @spg.setter
    def spg(self, spg):
        if isinstance(spg, float):
            self._spg = spg
        else:
            return print("Invalid input must be a float")
    
    @property
    def bpg(self):
        return self._bpg
    
    @bpg.setter
    def bpg(self, bpg):
        if isinstance(bpg, float):
            self._bpg = bpg
        else:
            return print("Invalid input must be a float")

    @classmethod
    def add_to_teamlist(cls, self):
        cls.teamlist.append(self)

    @classmethod
    def find_by_name(cls):
        input_name = input("Enter the name of the team you are looking for: ")
        CURSOR.execute('SELECT * FROM teams WHERE name = ?', (input_name,))
        row = CURSOR.fetchone()
        if row:
            return print(f'Name: {row[1]},\nWins: {row[2]},\nLosses: {row[3]},\nPointsPerGame: {row[4]},\nAssistsPerGame: {row[5]},\nReboundPerGame: {row[6]},\nStealsPerGame: {row[7]},\nBlocksPerGame: {row[8]}')
        else:
            return print("Team not found")
    
    def save(self):
        CURSOR.execute(
            """INSERT INTO teams (name, wins, losses PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?), (self.name, self.wins, self.losses, self.ppg, self.apg, self.rpg, self.spg, self.bpg)""")
        CONN.commit()

    @classmethod
    def create(cls, name, wins, losses, ppg, apg, rpg, spg, bpg):
        new_name = input("Enter the team's name: ")
        new_wins = input("Enter the team's wins: ")
        new_losses = input("Enter the team's losses: ")
        new_ppg = input("Enter the team's points per game: ")
        new_apg = input("Enter the team's assists per game: ")
        new_rpg = input("Enter the team's rebounds per game: ")
        new_spg = input("Enter the team's steals per game: ")
        new_bpg = input("Enter the team's blocks per game: ")
        new_team = cls(new_name, new_wins, new_losses, new_ppg, new_apg, new_rpg, new_spg, new_bpg)
        new_team.save()

    @classmethod
    def grab_Players_By_Team(cls):
        new_team = input("Enter the name of the team you want to grab the players from: ")
        CURSOR.execute('SELECT * FROM players WHERE team = ?', (new_team,))
        players = CURSOR.fetchall()
        return print(players)
    
    @classmethod
    def deletebyName(cls,):
        chosen_name = input("Enter the name of the team you want to delete: ")
        CURSOR.execute('DELETE FROM teams WHERE name = ?', (chosen_name,))
        CONN.commit()
        print(f"{chosen_name} has been deleted")

for team in CURSOR.execute('SELECT * FROM teams'):
    new_team = teams(team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8])


     