import os
import json
from copy import copy

import pandas as pd
from chromadb.config import Settings
import chromadb

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

    chroma_client.delete_collection(name="organic_data")

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

        # Save the organic data in the loop
        ids.append(citation)
        documents.append(content)
        metadatas.append({ "citation" : citation })

    # Add the organic data to the collection
    organic_collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

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

