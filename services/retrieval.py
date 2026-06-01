import chromadb

from services.embeddings import generate_embedding

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    "query_repository"
)

def retrieve_query(user_question):

    embedding = generate_embedding(
        user_question
    )

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results