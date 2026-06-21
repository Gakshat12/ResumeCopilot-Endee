SKILLS = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "nlp",
    "sql",
    "docker",
    "fastapi",
    "flask",
    "rag",
    "faiss",
    "tensorflow",
    "sentence transformers",
    "semantic search",
    "retrieval",
    "recommendation",
    "embeddings",
    "vector database"
]

SKILL_GROUPS = {
    "vector database": [
        "faiss",
        "pinecone",
        "qdrant",
        "weaviate",
        "milvus",
        "chroma",
        "opensearch",
        "elasticsearch",
        "semantic search",
        "retrieval"
    ]
}


def extract_skills(text):

    text = text.lower()

    found = set()

    for skill in SKILLS:

        if skill in text:
            found.add(skill)

    for parent_skill, children in SKILL_GROUPS.items():

        if any(child in text for child in children):
            found.add(parent_skill)

    return sorted(list(found))