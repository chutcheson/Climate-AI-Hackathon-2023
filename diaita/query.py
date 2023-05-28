from typing import Dict, List

from marvin import ai_fn

from diaita.docs import query_documents

def query(query, kind):
    docs = query_documents(query, kind=kind, n_results=5)
    if kind == "auditor":
        return query_auditor(query, docs)
    elif kind == "farmer":
        return query_farmer(query, docs)

@ai_fn
def query_auditor(question: str, documents: Dict[str, str]) -> str:
    """
    You are an expert in USDA organic accreditation and auditing.

    Answer the question using the documents provided.

    Include citations for propositions inline, at the end of each sentence.

    """

@ai_fn
def query_farmer(query: str, documents: Dict[str, str]) -> str:
    """
    You are an expert in USDA organic accreditation and auditing. You are responding to a question from a farmer looking to explore USDA organic certification.

    Using the relevant documents, you should answer the question. 
    """
