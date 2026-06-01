from faker import Faker
from pathlib import Path
import random
import sqlite3

fake = Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "gaming.db"
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

achievement_names = [
    "First Win",
    "Master Shooter",
    "Legend Player",
    "Top Scorer",
    "Elite Warrior",
    "Survivor",
    "Champion",
    "Headshot King",
    "Dungeon Master",
    "Battle Hero",
    "Treasure Hunter",
    "Speed Runner",
    "Ultimate Winner",
    "MVP Player",
    "Conqueror"
]

batch_size = 1000
records = []

for i in range(50000):

    records.append((
        i + 1,                                    # achievement_id
        random.randint(1, 10000),                # player_id
        random.choice(achievement_names),        # achievement_name
        fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    ))

    # Insert in batches for better performance
    if len(records) == batch_size:
        cursor.executemany("""
            INSERT INTO achievements(
                achievement_id,
                player_id,
                achievement_name,
                achievement_date
            )
            VALUES (?, ?, ?, ?)
        """, records)

        conn.commit()
        records = []

# Insert remaining records
if records:
    cursor.executemany("""
        INSERT INTO achievements(
            achievement_id,
            player_id,
            achievement_name,
            achievement_date
        )
        VALUES (?, ?, ?, ?)
    """, records)

    conn.commit()

conn.close()