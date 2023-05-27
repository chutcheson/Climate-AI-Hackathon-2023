import os
import json
from copy import copy

import pandas as pd
from chromadb.config import Settings
import chromadb

from marvin import ai_fn

def create_collection():

    # Expand the tilde (~) to the user's home directory
    persistent_directory = os.path.expanduser("~/.diaita_data")

    # Expand the tilde (~) to the user's home directory
    data_file = os.path.expanduser("~/Projects/Climate-AI-Hackathon-2023/data/organic_data.csv")

    # Load the materials into a Pandas dataframe
    organic_df = pd.read_csv(data_file)

    # Create a Chroma client to store organic documents
    chroma_client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=str(persistent_directory)
    ))

    # Create collection to store organic data 
    organic_collection = chroma_client.create_collection(name="organic_data")

    # Create lists to store variables and metadata
    ids = []
    documents = []
    metadatas = []

    # Iterate over the evidence to store it in the database
    for record in organic_df.to_dict(orient='records'):
        
        # Retrieve the important fields from the email record
        citation = record['citation']
        content = record['content']

        # Find token length of the content
        content_length = len(content.split()) * 1.33

        # If the content length is > 1500, split it into chunks of 1500
        if content_length > 1500:

            # Split the content into the necessary chunks
            for i in range(int(content_length/1500)):

                # Save the organic data in the loop
                ids.append(f"{citation}_{i}")
                documents.append(" ".join(content.split()[i*1500:(i+1)*1500]))
                metadatas.append({ "citation" : citation, "kind" : "regulation"})

                # Perform AI summarization
                summary = summarize_document(" ".join(content.split()[i*1500:(i+1)*1500]))

                # Save the summarized organic data in the loop
                ids.append(f"{citation}_summary_{i}")
                documents.append(summary)
                metadatas.append({"citation" : citation, "kind" : "summary"})

        else:

            # Save the organic data in the loop
            ids.append(citation)
            documents.append(content)
            metadatas.append({ "citation" : citation, "kind" : "regulation"})

            # Perform AI summarization
            summary = summarize_document(content)

            # Save the summarized organic data in the loop
            ids.append(f"{citation}_summary")
            documents.append(summary)
            metadatas.append({"citation" : citation, "kind" : "summary"})

    # Add the organic data to the collection
    organic_collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    # Persist the collection to disk
    chroma_client.persist()

@ai_fn
def summarize_document(document: str) -> str:
    """
    You are an expert in USDA organic regulation. You are asked to summarize the requirements for a USDA organic auditor.

    Take the document, containing the regulation, and summarize it in bullet points that can be used by the auditor.

    The bullet points should be ordered by relevance.

    The bullet points should be terse and should omit unnecessary words.

    The bullet points should be complete and include all regulatory requirements.

    The bullet points should be easy to read.

    The bullet points should contain relevant citations.
    """

def load_collection():

    # Expand the tilde (~) to the user's home directory
    persistent_directory = os.path.expanduser("~/.diaita_data")

    # Create a chromadb client to access the collections
    chroma_client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=str(persistent_directory)
    ))

    # Create collection to store evidence
    organic_collection = chroma_client.get_collection(name="organic_data")

    return organic_collection


