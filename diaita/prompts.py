from langchain import PromptTemplate

compliance_assistant_cot_template = """

Question: {question}

Documents: {documents}

You have recieved a question from a company about USDA Organic compliance. 

Answer the question with the following steps:

1. Identify the parts of the question and interpret them. Write out the parts and your interpretation.

2. Identify any facts that the company provides about its situation and interpret them. Write out the facts and your interpretation.

3. Brainstorm the reasons why the company might be asking this question. Write out your ideas.

4. Brainstorm which parts of the documents might be relevant to the question. Write out your ideas.

5. Brainstorm possible answers to the question, using the documents. Write out your ideas.

Then write out a response to the company's question.

1. The response should provide an answer to the question.

2. The response should consider important questions that the company might want to consider.

"""

compliance_assistant_cot_prompt = PromptTemplate(input_variables=['question', 'documents'], template=compliance_assistant_cot_template)

compliance_assistant_template = """

Question: {question}

Reasoning: {reasoning}

Write out a response to the company's question using the reasoning.

"""

compliance_assistant_prompt = PromptTemplate(input_variables=['question', 'reasoning'], template=compliance_assistant_template)
