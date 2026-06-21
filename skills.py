SKILLS = [
"python",
"java",
"c++",
"machine learning",
"deep learning",
"nlp",
"sql",
"mongodb",
"react",
"nodejs",
"docker",
"kubernetes",
"aws",
"azure",
"fastapi",
"flask",
"rag",
"vector database",
"faiss",
"pytorch",
"tensorflow"
]

def extract_skills(text):


    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return found

