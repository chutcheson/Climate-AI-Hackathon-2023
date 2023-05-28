from langchain import PromptTemplate

compliance_system_template = """
You are an expert in USDA Organic complaince and you are helping a company to understand the requirements.
"""

compliance_assistant_cot_template = """

Question: {question}

Documents: {documents}

You have recieved a question from a company about USDA Organic compliance. 

1. Break the question up into parts.

2. Identify any facts that the company provides about its situation.

3. Brainstorm the reasons why the company might be asking this question.

4. Brainstorm which parts of the documents might be relevant to the question.

5. Brainstorm possible answers to the question, using the documents.

Write out your ideas on each of these steps.

Then write out a response to the company's question.

1. The response should include the context that you assumed for the question.

2. The response should provide an answer to the question.

"""

compliance_assistant_cot_prompt = PromptTemplate(input_variables=['question', 'documents'], template=compliance_assistant_cot_template)

compliance_assistant_template = """

Question: {question}

Reasoning: {reasoning}

Write out a response to the company's question using the reasoning.

"""

compliance_assistant_prompt = PromptTemplate(input_variables=['query', 'reasoning'], template=compliance_assistant_template)
