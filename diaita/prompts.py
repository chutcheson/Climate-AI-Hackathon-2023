from langchain import PromptTemplate

compliance_assistant_cot_template = """

Question: {question}

Documents: {documents}

You have recieved a question from a company about USDA Organic compliance. 

1. Write out the parts of the question.

2. Write out an interpretation of each part of the question.

3. Write out the facts that the company provides about its situation and interpret them.

4. Brainstorm the reasons why the company might be asking this question and write them down. 2-3 sentences.

5. Brainstorm which parts of the documents might be relevant to the question and write them down. 2-3 sentences.

6. Brainstorm possible answers to the question, using the documents and write them down. 4-5 sentences.

7. Write a response to the question.

"""

compliance_assistant_cot_prompt = PromptTemplate(input_variables=['question', 'documents'], template=compliance_assistant_cot_template)

compliance_assistant_template = """

Question: {question}

Reasoning: {reasoning}

Write out an answer to the company's question using the reasoning.

The answer should be addressed the company. 

The answer should be comprehensive and include all relevant information.

The answer should be easy to read.

"""

compliance_assistant_prompt = PromptTemplate(input_variables=['question', 'reasoning'], template=compliance_assistant_template)
