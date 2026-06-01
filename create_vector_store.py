import sqlite3
import chromadb
import ollama

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_or_create_collection(
    name="query_repository"
)

conn = sqlite3.connect("database/gaming.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
query_id,
question,
sql_query,
category
FROM query_repository
""")

rows = cursor.fetchall()

for row in rows:

    query_id = str(row[0])
    question = row[1]
    sql_query = row[2]
    category = row[3]

    embedding_text = f"""
    Question: {question}
    Category: {category}
    """

    embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=embedding_text
    )["embedding"]

    collection.add(
        ids=[query_id],
        embeddings=[embedding],
        documents=[question],
        metadatas=[{
            "sql_query": sql_query,
            "category": category
        }]
    )

print("Vector DB Created")