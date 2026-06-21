import os
import streamlit as st

from resume_parser import extract_text
from embeddings import get_embedding
from matcher import compute_match_score
from chunker import chunk_text
from skills import extract_skills
from analyzer import generate_feedback
from endee_client import EndeeVectorStore
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

st.markdown(
    """
    Upload your Resume and compare it against a Job Description.
    """
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

    store = EndeeVectorStore()

    for chunk in chunks:

        embedding = get_embedding(
            chunk
        )

        store.add(
            chunk,
            embedding
        )

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    missing_skills = list(
        set(jd_skills) -
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

        top_chunks = store.search(
            jd_embedding
        )

    score = compute_match_score(
        resume_embedding,
        jd_embedding
    )

    feedback = generate_feedback(
        score,
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
            f"{score}%"
        )

        st.progress(
            min(int(score), 100)
        )

        if score >= 80:
            st.success(
                "Excellent Match"
            )

        elif score >= 60:
            st.warning(
                "Good Match"
            )

        else:
            st.error(
                "Needs Improvement"
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

    if resume_skills:
        st.write(
            resume_skills
        )
    else:
        st.warning(
            "No skills detected."
        )

    st.subheader(
        "📋 JD Skills"
    )

    if jd_skills:
        st.write(
            jd_skills
        )
    else:
        st.warning(
            "No JD skills detected."
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
        "📄 Resume Preview"
    )

    st.text_area(
        "",
        resume_text[:5000],
        height=350
    )
    st.subheader(
    "Relevant Resume Sections"
    )

    for chunk in top_chunks:

        st.write(chunk)

        st.divider()