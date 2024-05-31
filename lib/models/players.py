from models.__init__ import CURSOR, CONN

class players():
    
    all = []
    
    def __init__(self, name, ppg, apg, rpg, spg, bpg, team, id=None):
        self.id = id
        self.name = name
        self.ppg = ppg
        self.apg = apg
        self.rpg = rpg
        self.spg = spg
        self.bpg = bpg
        self.team = team
        players.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return print("Invalid input must be a string")

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

    @property
    def team(self):
        return self._team
    
    @team.setter
    def team(self, team):
        if isinstance(team, str):
            self._team = team
        else:
            return print("Invalid input must be a string")


    def save(self):
        CURSOR.execute(
            """INSERT INTO players (name, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame, Team) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (self.name, self.ppg, self.apg, self.rpg, self.spg, self.bpg, self.team))
        CONN.commit()
        print(f"{self.name} have been created")

    @classmethod
    def create(cls):
        new_name = input("Enter the player's name: ")
        new_ppg = float(input("Enter the player's points per game: "))
        new_apg = float(input("Enter the player's assists per game: "))
        new_rpg = float(input("Enter the player's rebounds per game: "))
        new_spg = float(input("Enter the player's steals per game: "))
        new_bpg = float(input("Enter the player's blocks per game: "))
        new_team = input("Enter the player's team: ")
        new_player = cls(new_name, new_ppg, new_apg, new_rpg, new_spg, new_bpg, new_team)
        new_player.save()

    @classmethod
    def find_by_player_name(cls):
        search_name = input("Enter the name of the player you are looking for: ")
        CURSOR.execute('SELECT * FROM players WHERE name = ?', (search_name,))
        row = CURSOR.fetchone()
        if row:
            return print(f'Name: {row[1]}, \nPointsPerGame: {row[2]}, \nAssistsPerGame: {row[3]}, \nReboundsPerGame: {row[4]}, \nStealsPerGame: {row[5]}, \nBlocksPerGame: {row[6]}, \nTeam: {row[7]}')
        return print("Player not found")
    
    @classmethod
    def deletebyName(cls,):
        chosen_name = input("Enter the name of the player you want to delete: ")
        CURSOR.execute('DELETE FROM players WHERE name = ?', (chosen_name,))
        CONN.commit()
        print(f"{chosen_name} has been deleted")


for row in CURSOR.execute('SELECT * FROM players'):
    player = players(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])


