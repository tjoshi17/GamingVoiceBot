import sqlite3

conn = sqlite3.connect(
    "database/gaming.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
player_id INTEGER PRIMARY KEY,
player_name TEXT,
country TEXT,
registration_date DATE,
player_level INTEGER,
vip_status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS games(
game_id INTEGER PRIMARY KEY,
game_name TEXT,
genre TEXT,
release_year INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions(
session_id INTEGER PRIMARY KEY,
player_id INTEGER,
game_id INTEGER,
login_time TIMESTAMP,
logout_time TIMESTAMP,
hours_played REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
txn_id INTEGER PRIMARY KEY,
player_id INTEGER,
game_id INTEGER,
amount REAL,
txn_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS achievements(
achievement_id INTEGER PRIMARY KEY,
player_id INTEGER,
achievement_name TEXT,
achievement_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboards(
leaderboard_id INTEGER PRIMARY KEY,
player_id INTEGER,
game_id INTEGER,
rank INTEGER,
score INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS query_repository(
query_id INTEGER PRIMARY KEY,
question TEXT,
sql_query TEXT,
category TEXT
)
""")

conn.commit()
conn.close()