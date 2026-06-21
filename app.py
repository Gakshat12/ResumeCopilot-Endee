import os
import streamlit as st

from resume_parser import extract_text
from embeddings import get_embedding
from matcher import compute_match_score
from chunker import chunk_text
from skills import extract_skills
from analyzer import generate_feedback
from scoring import calculate_final_score
from vector_store import store_chunks
from retriever import retrieve_chunks

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

st.set_page_config(
    page_title="ResumeCopilot-Endee",
    layout="wide"
)

st.title("🚀 ResumeCopilot-Endee")

st.write(
    "Upload a Resume and compare it with a Job Description"
)

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if resume_file is None:

        st.error(
            "Please upload a resume."
        )

        st.stop()

    if len(job_description.strip()) == 0:

        st.error(
            "Please paste a Job Description."
        )

        st.stop()

    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume_file.name
    )

    with open(file_path, "wb") as f:

        f.write(
            resume_file.getbuffer()
        )

    with st.spinner(
        "Extracting Resume..."
    ):

        resume_text = extract_text(
            file_path
        )

    chunks = chunk_text(
        resume_text
    )

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    missing_skills = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    with st.spinner(
        "Generating Embeddings..."
    ):

        resume_embedding = get_embedding(
            resume_text
        )

        jd_embedding = get_embedding(
            job_description
        )

    chunk_embeddings = []

    for chunk in chunks:

        emb = get_embedding(
            chunk
        )

        chunk_embeddings.append(
            emb
        )

    with st.spinner(
        "Storing Resume Chunks in Endee..."
    ):

        store_chunks(
            chunks,
            chunk_embeddings
        )

    with st.spinner(
        "Searching Endee..."
    ):

        top_chunks = retrieve_chunks(
            jd_embedding,
            top_k=3
        )

    score = compute_match_score(
        resume_embedding,
        jd_embedding
    )

    final_score = calculate_final_score(
        score,
        resume_skills,
        jd_skills,
        top_chunks
    )

    feedback = generate_feedback(
        final_score,
        missing_skills
    )

    st.success(
        "Analysis Complete ✅"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📊 Match Score"
        )

        st.metric(
            "Resume Match %",
            f"{final_score}%"
        )

        st.progress(
            min(
                int(final_score),
                100
            )
        )

    with col2:

        st.subheader(
            "📈 Resume Statistics"
        )

        st.metric(
            "Characters",
            len(resume_text)
        )

        st.metric(
            "Chunks Created",
            len(chunks)
        )

    st.divider()

    st.subheader(
        "🛠 Resume Skills"
    )

    st.write(
        resume_skills
    )

    st.subheader(
        "📋 JD Skills"
    )

    st.write(
        jd_skills
    )

    st.subheader(
        "❌ Missing Skills"
    )

    if missing_skills:

        st.error(
            ", ".join(
                missing_skills
            )
        )

    else:

        st.success(
            "No Missing Skills Found"
        )

    st.subheader(
        "💡 Suggestions"
    )

    for item in feedback:

        st.write(
            item
        )

    st.divider()

    st.subheader(
        "🎯 Relevant Resume Sections (Endee)"
    )

    shown = set()

    for i, chunk in enumerate(top_chunks, start=1):

        if chunk in shown:
            continue

        shown.add(chunk)

        st.markdown(
            f"### Result {i}"
        )

        st.info(
            chunk[:600]
        )

        st.divider()

    st.subheader(
        "📄 Resume Preview"
    )

    st.text_area(
        "",
        resume_text[:5000],
        height=350
    )