class EndeeVectorStore:

    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, text, vector):

        self.texts.append(text)
        self.vectors.append(vector)

    def search(self, query_vector):

        return self.texts[:5]