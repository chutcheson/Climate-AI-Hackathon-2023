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

6. Brainstorm possible ways that the answer might differ depending on the company's situation and write them down. 2-3 sentences.

7. Brainstorm possible answers to the question, using the documents and write them down. 4-5 sentences.

8. Write a response to the question.

Check to ensure that you have written out all of the information above.

"""

compliance_assistant_cot_prompt = PromptTemplate(input_variables=['question', 'documents'], template=compliance_assistant_cot_template)

compliance_assistant_template = """

Question: {question}

Reasoning: {reasoning}

Provide an answer to the company's question using the reasoning.

The answer should be comprehensive and include all relevant information.

The answer should be written in a way that is easy to understand.

"""

compliance_assistant_prompt = PromptTemplate(input_variables=['question', 'reasoning'], template=compliance_assistant_template)
