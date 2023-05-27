from diaita.load import load_collection 

def query_document(text):
    collection = load_collection()
    docs = collection.query(query_texts=[text], n_results=3)
    print(docs)

