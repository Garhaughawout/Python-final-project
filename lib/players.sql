DROP TABLE IF EXISTS players;

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    PointsPerGame FLOAT,
    AssistsPerGame FLOAT,
    ReboundsPerGame FLOAT,
    StealsPerGame FLOAT,
    BlocksPerGame FLOAT,
    Team TEXT
);

-- Path: lib/data.sql

INSERT INTO players (name, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame, Team)
VALUES ('LeBron James', 25.3, 7.9, 7.4, 1.2, 0.9, 'Los Angeles Lakers'),
('Kevin Durant', 27.0, 5.9, 7.1, 1.1, 1.2, 'Phoneix Suns'),
('Stephen Curry', 30.1, 6.7, 5.4, 1.6, 0.2, 'Golden State Warriors'),
('Kawhi Leonard', 26.9, 4.9, 7.3, 1.8, 0.6, 'Los Angeles Clippers'),
('Giannis Antetokounmpo', 29.5, 5.6, 13.6, 1.0, 1.0, 'Milwaukee Bucks'),
('James Harden', 34.3, 7.5, 6.6, 2.0, 0.8, 'Brooklyn Nets'),
('Anthony Davis', 26.1, 3.2, 9.3, 1.5, 2.3, 'Los Angeles Lakers'),
('Luka Doncic', 28.8, 8.6, 9.4, 1.0, 0.2, 'Dallas Mavericks'),
('Damian Lillard', 28.8, 7.5, 4.2, 1.0, 0.3, 'Milwaukee Bucks'),
('Jaylen Brown', 24.7, 3.4, 6.0, 1.2, 0.6, 'Boston Celtics'),
('Julius Randle', 24.1, 6.0, 10.2, 0.9, 0.3, 'New York Knicks'),
('Kemba Walker', 19.3, 4.9, 3.6, 0.9, 0.4, 'Boston Celtics'),
('Klay Thompson', 21.5, 2.4, 3.8, 0.8, 0.6, 'Golden State Warriors'),
('Deandre Ayton', 18.2, 1.9, 11.5, 0.6, 1.2, 'Phoneix Suns'),
('Ben Simmons', 14.3, 7.2, 7.2, 1.6, 0.6, 'Philadelphia 76ers'),
('Jamal Murray', 21.2, 4.8, 4.0, 1.0, 0.3, 'Denver Nuggets'),
('DeAaron Fox', 25.2, 7.2, 3.5, 1.5, 0.5, 'Sacramento Kings'),
('John Wall', 20.6, 6.9, 3.2, 1.1, 0.8, 'Houston Rockets'),
('Kristaps Porzingis', 20.1, 1.8, 8.9, 0.7, 1.3, 'Dallas Mavericks'),
('CJ McCollum', 23.1, 4.8, 3.9, 0.8, 0.5, 'Portland Trail Blazers'),
('Brandon Ingram', 23.8, 4.9, 4.9, 0.8, 0.7, 'New Orleans Pelicans'),
('Devin Booker', 26.6, 4.3, 4.2, 0.8, 0.3, 'Phoneix Suns'),
('Zach LaVine', 27.4, 4.9, 5.0, 1.0, 0.5, 'Chicago Bulls'),
('Joel Embiid', 28.5, 2.8, 10.6, 1.0, 1.4, 'Philadelphia 76ers'),
('Nikola Jokic', 26.4, 8.3, 10.8, 1.6, 0.7, 'Denver Nuggets'),
('Kyrie Irving', 27.4, 6.4, 4.8, 1.4, 0.5, 'Brooklyn Nets'),
('Paul George', 21.5, 3.9, 5.7, 1.4, 0.5, 'Los Angeles Clippers'),
('Jimmy Butler', 21.5, 6.9, 6.9, 2.1, 0.6, 'Miami Heat'),
('Devin Booker', 26.6, 4.3, 4.2, 0.8, 0.3, 'Phoneix Suns'),
('Jayson Tatum', 26.4, 4.3, 7.4, 1.2, 0.9, 'Boston Celtics'),
('Zion Williamson', 27.0, 3.7, 7.2, 1.0, 0.6, 'New Orleans Pelicans'),
('Karl-Anthony Towns', 24.8, 4.5, 10.8, 0.8, 1.2, 'Minnesota Timberwolves'),
('Bradley Beal', 31.3, 4.4, 4.7, 1.2, 0.4, 'Washington Wizards'),
('Russell Westbrook', 22.2, 11.5, 11.5, 1.3, 0.3, 'Washington Wizards'),
('Donovan Mitchell', 26.4, 5.2, 4.4, 1.0, 0.3, 'Utah Jazz'),
('Trae Young', 25.3, 9.4, 3.9, 1.1, 0.2, 'Atlanta Hawks'),
('DeMar DeRozan', 21.6, 6.9, 4.2, 1.0, 0.3, 'San Antonio Spurs'),
('Chris Paul', 16.4, 8.9, 4.5, 1.4, 0.2, 'Phoneix Suns'),
('Khris Middleton', 20.4, 5.4, 6.0, 1.0, 0.2, 'Milwaukee Bucks'),
('Rudy Gobert', 14.3, 1.2, 13.5, 0.5, 2.7, 'Utah Jazz'),
('Jrue Holiday', 17.7, 6.1, 4.5, 1.6, 0.6, 'Milwaukee Bucks'),
('Tobias Harris', 19.5, 3.5, 6.8, 0.9, 0.6, 'Philadelphia 76ers'),
('Mike Conley', 16.2, 6.0, 3.5, 1.4, 0.1, 'Utah Jazz'),
('Gordon Hayward', 19.6, 4.1, 6.5, 1.1, 0.4, 'Charlotte Hornets'),
('Kyle Lowry', 17.2, 7.3, 5.4, 1.0, 0.3, 'Toronto Raptors'),
('Bam Adebayo', 18.7, 5.4, 9.0, 1.0, 1.0, 'Miami Heat'),
('Fred VanVleet', 19.6, 6.3, 4.3, 1.7, 0.7, 'Toronto Raptors'),
('Pascal Siakam', 20.1, 4.8, 7.2, 1.0, 0.7, 'Toronto Raptors'),
('LaMelo Ball', 15.7, 6.1, 5.9, 1.6, 0.4, 'Charlotte Hornets'),
('Lonzo Ball', 14.6, 5.7, 4.8, 1.3, 0.6, 'New Orleans Pelicans'),
('DAngelo Russell', 19.0, 5.6, 3.9, 1.0, 0.3, 'Minnesota Timberwolves'),
('Shai Gilgeous-Alexander', 23.7, 5.9, 4.7, 1.1, 0.7, 'Oklahoma City Thunder'),
('Collin Sexton', 24.3, 4.4, 3.1, 1.0, 0.1, 'Cleveland Cavaliers'),
('Christian Wood', 21.0, 1.3, 9.6, 0.9, 1.2, 'Dallas Mavericks'),
('John Collins', 17.6, 1.3, 7.4, 0.5, 1.0, 'Atlanta Hawks'),
('Jerami Grant', 22.3, 2.8, 4.6, 0.7, 1.0, 'Detroit Pistons'),
('Darius Garland', 17.4, 6.1, 2.4, 1.2, 0.1, 'Cleveland Cavaliers'),
('Zach Collins', 10.3, 1.3, 5.2, 0.5, 1.0, 'Portland Trail Blazers'),
('Dennis Schroder', 15.4, 5.8, 3.5, 1.1, 0.2, 'Los Angeles Lakers'),
('Malcolm Brogdon', 21.2, 6.5, 4.7, 1.2, 0.2, 'Indiana Pacers'),
('Buddy Hield', 19.2, 3.1, 4.6, 1.0, 0.3, 'Sacramento Kings'),
('RJ Barrett', 17.6, 3.0, 5.8, 1.0, 0.3, 'New York Knicks'),
('Jaren Jackson Jr.', 17.4, 1.4, 4.6, 0.7, 1.0, 'Memphis Grizzlies'),
('Aaron Gordon', 14.6, 3.2, 6.6, 0.9, 0.7, 'Denver Nuggets'),
('Evan Fournier', 17.1, 3.4, 3.0, 1.0, 0.2, 'Boston Celtics'),
('Kelly Oubre Jr.', 15.4, 1.5, 6.0, 1.0, 0.7, 'Golden State Warriors');
-- Path: lib/data.sql