from faker import Faker
from pathlib import Path
import random
import sqlite3

fake=Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "gaming.db"
conn = sqlite3.connect(db_path)

cursor=conn.cursor()

for i in range(10000):
    cursor.execute("""
    INSERT INTO players
    VALUES (?,?,?,?,?,?)
    """,(
    i+1,
    fake.name(),
    fake.country(),
    fake.date_between(
        start_date="-3y",
        end_date="today"
    ),
    random.randint(1,100),
    random.choice(
        ["Gold","Silver","Bronze"]
    )
    ))

conn.commit()
conn.close()