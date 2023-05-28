import json

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from prompts import compliance_assistant_cot_prompt, compliance_assistant_prompt 
from diaita.docs import query_documents

# Get compliance assistant answer
def assistant(question, collection):

    # Get the related documents
    docs = query_documents(question, collection, "regulation", n_results=2)

    # Consolidate the documents
    docs = "\n".join([doc for idx, doc in docs])

    # Get the reasoning
    chat_reasoning = reasoning(question, docs)

    # Extract the answer
    chat_answer = answer(question, chat_reasoning)

    return chat_answer

# Get reasoning
def reasoning(actor_question, query_documents):

    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        SystemMessage(content="You are an expert in USDA Organic complaince and you are helping a company to understand the requirements."),
        HumanMessage(content=compliance_assistant_cot_prompt.format(question=actor_question, documents=query_documents))
    ]

    # Get the reasoning
    res = chat(messages).content

    return res

# Get answer
def answer(actor_question, chat_reasoning):

    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create messages
    messages = [
        HumanMessage(content=compliance_assistant_prompt.format(question=actor_question, reasoning=chat_reasoning))
    ]

    # Get the reasoning
    res = chat(messages).content

    return res
