import sqlite3
import pandas as pd
from pathlib import Path

def execute_sql(sql_query):

    BASE_DIR = Path(__file__).resolve().parent.parent
    db_path = BASE_DIR / "database" / "gaming.db"
    conn = sqlite3.connect(db_path)

    df = pd.read_sql_query(
        sql_query,
        conn
    )

    conn.close()

    return df