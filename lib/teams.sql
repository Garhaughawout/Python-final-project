DROP TABLE IF EXISTS teams;

CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY,
    name TEXT,
    Wins INTEGER,
    Losses INTEGER,
    PointsPerGame FLOAT,
    AssistsPerGame FLOAT,
    ReboundsPerGame FLOAT,
    StealsPerGame FLOAT,
    BlocksPerGame FLOAT
);


INSERT INTO teams (name, Wins, Losses, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame)
VALUES ('Los Angeles Lakers', 42, 30, 109.5, 24.6, 44.7, 7.9, 5.4),
('Phoneix Suns', 51, 21, 115.3, 26.9, 43.1, 7.1, 4.0),
('Golden State Warriors', 39, 33, 113.7, 27.6, 45.0, 8.0, 4.8),
('Los Angeles Clippers', 47, 25, 114.7, 24.1, 44.1, 7.1, 4.6),
('Milwaukee Bucks', 46, 26, 120.1, 25.5, 48.2, 8.1, 4.8),
('Brooklyn Nets', 48, 24, 118.6, 26.8, 44.4, 6.7, 5.3),
('Dallas Mavericks', 42, 30, 112.4, 22.8, 44.0, 6.9, 4.3),
('Boston Celtics', 36, 36, 112.6, 23.5, 44.1, 7.6, 5.3),
('New York Knicks', 41, 31, 107.0, 21.9, 45.0, 7.6, 5.0),
('Denver Nuggets', 47, 25, 115.1, 26.8, 44.1, 8.1, 4.5),
('Sacramento Kings', 31, 41, 113.7, 25.5, 42.9, 7.6, 4.3),
('Houston Rockets', 17, 55, 108.9, 22.7, 42.9, 7.1, 4.0),
('Portland Trail Blazers', 42, 30, 116.1, 20.5, 44.7, 6.7, 5.0),
('New Orleans Pelicans', 31, 41, 114.6, 26.3, 45.2, 7.6, 4.3),
('Chicago Bulls', 31, 41, 110.7, 26.8, 44.7, 7.6, 4.3),
('Philadelphia 76ers', 49, 23, 113.6, 23.0, 45.5, 8.9, 6.1),
('Minnesota Timberwolves', 23, 49, 112.1, 24.7, 43.9, 8.6, 5.9),
('Washington Wizards', 34, 38, 116.6, 25.3, 44.2, 7.4, 4.3),
('Utah Jazz', 52, 20, 116.4, 23.7, 45.1, 6.9, 5.2),
('Atlanta Hawks', 41, 31, 113.7, 24.1, 45.1, 7.6, 4.8),
('San Antonio Spurs', 33, 39, 110.2, 24.5, 43.7, 7.2, 5.0),
('Charlotte Hornets', 33, 39, 110.7, 26.8, 44.7, 7.6, 4.3),
('Miami Heat', 40, 32, 108.0, 25.9, 42.8, 7.4, 4.0),
('Toronto Raptors', 27, 45, 111.6, 24.1, 41.6, 8.3, 5.5),
('Indiana Pacers', 34, 38, 115.3, 26.8, 44.7, 7.6, 4.3),
('Memphis Grizzlies', 38, 34, 113.3, 27.0, 46.1, 9.1, 5.0),
('Oklahoma City Thunder', 22, 50, 105.0, 22.7, 43.7, 7.6, 4.3),
('Detroit Pistons', 20, 52, 107.3, 24.1, 42.7, 7.6, 4.3),
('Cleveland Cavaliers', 22, 50, 103.8, 23.7, 42.8, 7.6, 4.3),
('Orlando Magic', 21, 51, 104.6, 22.8, 44.0, 6.9, 4.3);


