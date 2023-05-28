from typing import Dict, List

from marvin import ai_fn

from diaita.docs import query_documents

def query(query, col, actor='farmer', kind='regulation'):
    docs = query_documents(query, col, kind, n_results=2)
    if actor == "auditor":
        return query_auditor(query, docs)
    elif actor == "farmer":
        return query_farmer(query, docs)

@ai_fn
def query_auditor(question: str, documents: Dict[str, str]) -> str:
    """
    You are an expert in USDA organic accreditation and auditing.

    Answer the question. You may use the provided documents for context.

    At end of the response, include a list of useful citations.
    """

@ai_fn
def query_farmer(query: str, documents: Dict[str, str]) -> str:
    """
    You are an expert in USDA organic accreditation and auditing. You are responding to a question from a farmer looking to explore USDA organic certification.

    Answer the question, You may use the provided documents for context.
    """
