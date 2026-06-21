from endee import Endee

client = Endee()

index = client.get_index(
    name="resume_index"
)

index.upsert([
    {
        "id": "test1",
        "vector": [0.1] * 384,
        "meta": {
            "text": "Hello Endee"
        }
    }
])

print("Inserted")