import os
import streamlit as st

from streamlit_mic_recorder import mic_recorder

from services.speech_to_text import transcribe_audio
from services.retrieval import retrieve_query
from services.sql_executor import execute_sql


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Gaming Analytics Voice Bot",
    layout="wide"
)

st.title("🎮 Gaming Analytics Voice Bot")

# ==================================================
# VOICE INPUT
# ==================================================

audio = mic_recorder(
    start_prompt="🎤 Start",
    stop_prompt="⏹ Stop",
    key="voice_recorder"
)

# ==================================================
# GET QUESTION
# ==================================================

user_question = None

if audio:

    os.makedirs(
        "temp",
        exist_ok=True
    )

    audio_path = "temp/audio.wav"

    with open(audio_path, "wb") as f:
        f.write(audio["bytes"])

    st.success("Audio received")

    with st.spinner(
        "Transcribing..."
    ):

        user_question = transcribe_audio(
            audio_path
        )

# ==================================================
# PROCESS QUERY
# ==================================================

if user_question:

    st.subheader(
        "Recognized Question"
    )

    st.write(
        user_question
    )

    # ==============================================
    # RETRIEVAL
    # ==============================================

    with st.spinner(
        "Searching Query Repository..."
    ):

        result = retrieve_query(
            user_question
        )

    # ==============================================
    # RAW DEBUG
    # ==============================================

    documents = result["documents"][0]

    distances = result["distances"][0]

    metadatas = result["metadatas"][0]

    # ==============================================
    # ALWAYS PICK BEST MATCH
    # ==============================================

    selected_index = 0

    matched_question = \
        documents[selected_index]

    sql_query = \
        metadatas[selected_index][
            "sql_query"
        ]

    # ==============================================
    # DISPLAY MATCH
    # ==============================================

    st.subheader(
        "Matched Repository Question"
    )

    st.success(
        matched_question
    )

    st.subheader(
        "Retrieved SQL"
    )

    st.code(
        sql_query,
        language="sql"
    )

    # ==============================================
    # EXECUTE SQL
    # ==============================================

    try:

        df = execute_sql(
            sql_query
        )

        st.subheader(
            "Database Result"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"SQL Execution Failed: {e}"
        )