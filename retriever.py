from endee_client import get_resume_index

index = get_resume_index()

def retrieve_chunks(
    query_embedding,
    top_k=3
):

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k
    )

    chunks = []

    for item in results:

        if "meta" in item:
            chunks.append(
                item["meta"]["text"]
            )

    return chunks