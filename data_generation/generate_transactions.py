from faker import Faker
from pathlib import Path
import random
import sqlite3

fake=Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "gaming.db"
conn = sqlite3.connect(db_path)

cursor=conn.cursor()

for i in range(100000):

    cursor.execute("""
    INSERT INTO transactions
    VALUES (?,?,?,?,?)
    """,(

    i+1,

    random.randint(
        1,10000
    ),

    random.randint(
        1,10
    ),

    round(
        random.uniform(
            50,
            5000
        ),
        2
    ),

    fake.date_this_year()
    ))

conn.commit()
conn.close()