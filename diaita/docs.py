from marvin import ai_fn

from diaita.load import load_collection 

def query_document(text, n_results):
    collection = load_collection()
    res = collection.query(query_texts=[text], n_results=n_results)
    ids = res['ids'][0]
    docs = res['documents'][0]
    return [(idx, doc) for idx, doc in zip(ids, docs)]

def query_summarized_documents(text, n_results):
    res = []
    docs = query_document(text, n_results)
    for idx, doc in docs:
        print("Citiation: ", idx)
        print("Document: ", doc)
        res.append({ "citation" : idx, "document" : summarize_document(doc)})
    return res

@ai_fn
def summarize_document(document: str) -> str:
    """
    You are an expert in USDA organic regulation. You are asked to summarize the requirements for a USDA organic auditor.

    Take the document and summarize it in bullet points that can be used by the auditor.
    """


