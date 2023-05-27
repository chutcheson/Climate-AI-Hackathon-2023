from marvin import ai_fn

from diaita.load import load_collection 

def query_documents(text, kind, n_results):
    collection = load_collection()
    res = collection.query(query_texts=[text], where={"kind":kind}, n_results=n_results)
    metadata = res['metadata'][0]
    docs = res['documents'][0]
    return [(datum['citation'], doc) for datum, doc in zip(metadata, docs)]
