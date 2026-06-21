# reset_index.py

from endee_client import client

try:
    client.delete_index("resume_index")
except:
    pass

client.create_index(
    name="resume_index",
    dimension=384,
    space_type="cosine"
)

print("Fresh index created")