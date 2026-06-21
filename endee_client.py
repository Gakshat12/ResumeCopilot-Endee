from endee import Endee, Precision

client = Endee()

INDEX_NAME = "resume_index"

def get_resume_index():

    indexes = client.list_indexes()

    existing = [
        idx["name"]
        for idx in indexes["indexes"]
    ]

    if INDEX_NAME not in existing:

        client.create_index(
            name=INDEX_NAME,
            dimension=384,
            space_type="cosine",
            precision=Precision.INT8
        )

    return client.get_index(
        name=INDEX_NAME
    )