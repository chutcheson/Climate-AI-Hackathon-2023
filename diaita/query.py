import json

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

from prompts import compliance_assistant_cot_prompt, compliance_assistant_prompt 
from diaita.docs import query_documents

# Get compliance assistant answer
def assistant(question, collection):

    # Get the related documents
    docs = query_documents(question, collection, "regulation", n_results=2)

    # Consolidate the documents
    docs = "\n".join([doc[1] for idx, doc in docs])

    print(docs)

    # Get the reasoning
    chat_reasoning = reasoning(question, docs)

    # Extract the answer
    chat_answer = answer(question, chat_reasoning)

    return chat_answer

# Get reasoning
def reasoning(question, documents):
    
    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        SystemMessage(content="You are an expert in USDA Organic complaince and you are helping a company to understand the requirements."),
        compliance_assistant_cot_prompt.format(question=question, documents=documents)
    ]

    # Get the reasoning
    res = chat(messages).content

    print(res)

    return res

# Get answer
def answer(question, reasoning):

    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        SystemMessage(content="You are an expert in USDA Organic complaince and you are helping a company to understand the requirements."),
        compliance_assistant_prompt.format(question=question, reasoning=reasoning)
    ]

    # Get the reasoning
    res = chat(messages).content

    print(res)

    return res
