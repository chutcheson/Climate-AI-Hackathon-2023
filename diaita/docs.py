from diaita.load import load_collection 

def query_documents(text, col, kind, n_results):
    res = col.query(query_texts=[text], where={"kind":kind}, n_results=n_results)
    metadata = res['metadatas'][0]
    docs = res['documents'][0]
    return [(datum['citation'], doc) for datum, doc in zip(metadata, docs)]
