import json

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

from prompts import compliance_system_template, compliance_assistant_cot_prompt, compliance_assistant_prompt 
from diaita.docs import query_documents

# Get compliance assistant answer
def assistant(question, collection):

    # Get the related documents
    docs = query_documents(query, collection, kind, n_results=2)

    # Get the reasoning
    reasoning = reasoning(question, docs)

    # Extract the answer
    answer = answer(question, reasoning)

    return answer

# Get reasoning
def reasoning(question, documents):
    
    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        SystemMessage(content=compliance_system_template),
        compliance_assistant_cot_prompt.format(question=question, documents=documents)
    ]

    # Get the reasoning
    res = chat(messages).content

    return res

# Get answer
def answer(question, reasoning):

    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        SystemMessage(content=compliance_system_template),
        compliance_assistant_prompt.format(question=question, reasoning=reasoning)
    ]

    # Get the reasoning
    res = chat(messages).content

    return res
