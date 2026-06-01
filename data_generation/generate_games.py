from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "gaming.db"
conn = sqlite3.connect(db_path)

cursor=conn.cursor()

games = [
("Battle Royale X","Shooter"),
("Dragon Kingdom","RPG"),
("Speed Racers","Racing"),
("Zombie Arena","Survival"),
("Fantasy Quest","Adventure"),
("War Legends","Strategy"),
("Soccer Masters","Sports"),
("Cricket Heroes","Sports"),
("Cyber Strike","Shooter"),
("Galaxy Fighters","Sci-Fi")
]

for idx, game in enumerate(games):
    cursor.execute("""
    INSERT INTO games
    VALUES (?,?,?,?)
    """,(
        idx+1,
        game[0],
        game[1],
        2020
    ))

conn.commit()
conn.close()