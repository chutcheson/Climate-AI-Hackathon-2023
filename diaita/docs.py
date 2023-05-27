from marvin import ai_fn

from diaita.load import load_collection 

def query_document(text, kind, n_results):
    collection = load_collection()
    res = collection.query(query_texts=[text], where={"kind":kind}, n_results=n_results)
    ids = res['ids'][0]
    docs = res['documents'][0]
    return [(idx, doc) for idx, doc in zip(ids, docs)]
