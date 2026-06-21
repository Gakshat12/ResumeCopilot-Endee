from endee import Endee

client = Endee()

index = client.get_index(
    name="resume_index"
)

results = index.query(
    vector=[0.1] * 384,
    top_k=3
)

print(results)