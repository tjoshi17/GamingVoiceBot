import ollama
import json

def rerank_question(
        user_question,
        candidate_questions):

    prompt = f"""
You are a semantic matching expert.

User Question:
{user_question}

Candidate Questions:
{candidate_questions}

Instructions:

1. Select the BEST matching candidate.
2. Return confidence score between 0 and 100.
3. Be strict.
4. If unsure give confidence below 90.

Return ONLY JSON.

Example:

{{
    "selected_index":0,
    "confidence":96
}}
"""

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    content = response["message"]["content"]

    return json.loads(content)