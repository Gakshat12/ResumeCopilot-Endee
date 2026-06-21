# 🚀 ResumeCopilot-Endee

An AI-powered Resume Intelligence Platform built using **Endee Vector Database**, **Sentence Transformers**, and **Streamlit** for semantic resume-job matching.

---

# 📌 Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching.

This creates several issues:

* Strong candidates get rejected because they use different terminology.
* Semantic relationships between skills are ignored.
* Recruiters spend significant time manually reviewing resumes.
* Candidate-job matching becomes inaccurate.

ResumeCopilot-Endee solves this problem using semantic retrieval and vector search.

Instead of only checking whether keywords exist, the system understands the meaning of resume content and retrieves the most relevant sections for a given Job Description.

---

# 🎯 Project Objective

Build an AI-powered resume analysis system that:

* Extracts text from resumes.
* Generates semantic embeddings.
* Stores resume chunks inside Endee Vector Database.
* Performs semantic retrieval against job descriptions.
* Identifies relevant resume evidence.
* Calculates candidate-job match scores.
* Highlights skill gaps and recommendations.

---

# 🏗 System Architecture

Resume PDF
↓
PDF Parsing
↓
Resume Text
↓
Chunking
↓
Sentence Transformer Embeddings
↓
Endee Vector Database
↓
Vector Upsert
↓
Job Description Embedding
↓
Semantic Search
↓
Relevant Resume Sections
↓
Skill Analysis
↓
Match Scoring

---

# ⚡ Features

## 1. Resume Upload

* Supports PDF resumes.
* Extracts complete resume content.

## 2. Resume Chunking

Large resumes are divided into smaller semantic chunks.

Benefits:

* Better retrieval quality.
* More precise matching.
* Faster vector search.

## 3. Embedding Generation

Uses Sentence Transformers to convert text into dense vector embeddings.

Capabilities:

* Semantic understanding.
* Context-aware similarity.
* Better than keyword matching.

## 4. Endee Vector Database Integration

The project uses Endee as the vector storage layer.

Each resume chunk is:

* Embedded
* Stored inside Endee
* Indexed for retrieval

Example:

```python
index.upsert(...)
```

## 5. Semantic Retrieval

Job descriptions are converted into embeddings.

The system queries Endee to retrieve:

* Most relevant experience
* Matching projects
* Relevant technical skills

Example:

```python
results = index.query(
    vector=query_embedding,
    top_k=3
)
```

## 6. Skill Analysis

The system:

* Extracts resume skills
* Extracts JD skills
* Detects missing skills
* Provides recommendations

## 7. Match Score

Calculates candidate-job similarity using:

* Semantic similarity
* Skill overlap
* Retrieved evidence

---

# 🛠 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI & NLP

* Sentence Transformers
* HuggingFace
* Semantic Embeddings

## Vector Database

* Endee

## Search & Retrieval

* Vector Search
* Semantic Retrieval

## Machine Learning

* Scikit-Learn

---

# 📂 Project Structure

ResumeCopilot-Endee/

├── app.py

├── resume_parser.py

├── embeddings.py

├── matcher.py

├── chunker.py

├── skills.py

├── analyzer.py

├── scoring.py

├── endee_client.py

├── vector_store.py

├── retriever.py

├── requirements.txt

├── README.md

└── uploads/

---

# 🔄 Workflow

Step 1:

User uploads resume PDF.

Step 2:

Resume text is extracted.

Step 3:

Resume is split into chunks.

Step 4:

Embeddings are generated.

Step 5:

Chunks are stored inside Endee.

Step 6:

Job description is embedded.

Step 7:

Endee retrieves relevant chunks.

Step 8:

Resume-JD similarity is calculated.

Step 9:

Results are displayed.

---

# 💡 Why Endee?

Endee was selected because it provides:

* High-performance vector retrieval
* Semantic similarity search
* Scalable indexing
* Metadata support
* Retrieval-focused architecture

The project demonstrates how Endee can be used as the retrieval layer for recruitment intelligence systems.

---

# 🚀 Future Improvements

* Multi-resume ranking
* Recruiter dashboard
* Candidate recommendation engine
* Hybrid retrieval (BM25 + Vector Search)
* LLM-based feedback generation
* Resume optimization suggestions
* Automated interview question generation

---

# 👨‍💻 Author

Akshat Gupta

B.Tech CSE (AI)

Maharaja Agrasen Institute of Technology

GitHub: https://github.com/Gakshat12

LinkedIn: https://linkedin.com/in/akshat-gupta-000503282

---

# ⭐ Endee Integration Highlights

✅ Endee SDK Integration

✅ Index Creation

✅ Vector Upsert

✅ Semantic Search

✅ Resume Retrieval

✅ Candidate-JD Matching

This project demonstrates a complete AI retrieval pipeline powered by Endee Vector Database.
