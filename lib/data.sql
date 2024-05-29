DROP TABLE IF EXISTS players;

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    PointsPerGame FLOAT,
    AssistsPerGame FLOAT,
    ReboundsPerGame FLOAT,
    StealsPerGame FLOAT,
    BlocksPerGame FLOAT
);

-- Path: lib/data.sql

INSERT INTO players (name, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame) 
VALUES ('LeBron James', 25.3, 7.9, 7.4, 1.6, 0.7)
, ('Kevin Durant', 27.1, 4.1, 7.1, 1.1, 1.1)
, ('Kawhi Leonard', 26.9, 5.0, 7.3, 1.8, 0.6)
, ('Giannis Antetokounmpo', 29.6, 5.8, 13.7, 1.0, 1.0)
, ('James Harden', 34.4, 7.4, 6.4, 1.8, 0.9)
, ('Anthony Davis', 26.7, 3.1, 9.4, 1.5, 2.4)
, ('Luka Doncic', 28.8, 8.8, 9.4, 1.0, 0.2)
, ('Damian Lillard', 30.0, 8.0, 4.3, 1.1, 0.3)
, ('Nikola Jokic', 19.9, 7.0, 9.7, 1.2, 0.6)
, ('Jayson Tatum', 23.4, 3.0, 7.0, 1.4, 0.9)
, ('Kemba Walker', 20.4, 4.8, 3.9, 0.9, 0.5)
, ('Khris Middleton', 20.9, 4.3, 6.2, 1.0, 0.1)
, ('Devin Booker', 26.1, 6.6, 4.2, 0.7, 0.3)
, ('Donovan Mitchell', 24.0, 4.3, 4.4, 1.0, 0.2)
, ('Chris Paul', 17.6, 6.7, 5.0, 1.6, 0.1)
, ('Jimmy Butler', 19.9, 6.0, 6.7, 1.8, 0.6)
, ('Paul George', 21.5, 3.9, 5.7, 1.4, 0.5)
, ('Karl-Anthony Towns', 26.5, 4.4, 10.8, 0.9, 1.2)
, ('Zion Williamson', 22.5, 2.1, 6.3, 0.7, 0.4)
, ('Russell Westbrook', 27.2, 7.0, 7.9, 1.6, 0.4)
, ('DeMar DeRozan', 22.1, 5.6, 5.5, 1.0, 0.3)
, ('Trae Young', 29.6, 9.3, 4.3, 1.1, 0.1)
, ('Brandon Ingram', 23.8, 4.2, 6.1, 1.0, 0.6)
, ('Deandre Ayton', 18.2, 1.9, 11.5, 0.7, 1.5)
, ('Ben Simmons', 16.4, 8.0, 7.8, 2.1, 0.6)
, ('Pascal Siakam', 22.9, 3.5, 7.3, 1.0, 0.9)
, ('Kyle Lowry', 19.7, 7.7, 5.0, 1.4, 0.4);
