from endee_client import get_resume_index

index = get_resume_index()

def store_chunks(
    chunks,
    embeddings
):

    vectors = []

    for i, (chunk, emb) in enumerate(
        zip(chunks, embeddings)
    ):

        vectors.append(
            {
                "id": f"{i}_{hash(chunk)}",
                "vector": emb.tolist(),
                "meta": {
                    "text": chunk
                },
                "filter": {
                    "type": "resume"
                }
            }
        )

    index.upsert(vectors)