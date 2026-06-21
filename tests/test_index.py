from endee import Endee, Precision

client = Endee()

client.create_index(
    name="resume_index",
    dimension=384,
    space_type="cosine",
    precision=Precision.INT8
)

print("Index Created Successfully")