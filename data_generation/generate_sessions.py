from faker import Faker
from pathlib import Path
import random
import sqlite3

fake=Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "gaming.db"
conn = sqlite3.connect(db_path)

cursor=conn.cursor()

for i in range(500000):
    player_id=random.randint(
        1,10000
    )

    game_id=random.randint(
        1,10
    )

    hours_played=round(
        random.uniform(0.5,6),
        2
    )

    login=fake.date_time_this_year()

    cursor.execute("""
    INSERT INTO sessions
    VALUES (?,?,?,?,?,?)
    """,(
    i+1,
    player_id,
    game_id,
    login,
    login,
    hours_played
    ))

conn.commit()
conn.close()
