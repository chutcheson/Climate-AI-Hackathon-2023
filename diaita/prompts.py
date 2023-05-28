from langchain import PromptTemplate

compliance_assistant_cot_template = """

Question: {question}

Documents: {documents}

You have recieved a question from a company about USDA Organic compliance. 

Identify the parts of the question and interpret them. Write out the parts and your interpretation.

Identify any facts that the company provides about its situation and interpret them. Write out the facts and your interpretation.

Brainstorm the reasons why the company might be asking this question. Write out your ideas.

Brainstorm which parts of the documents might be relevant to the question. Write out your ideas.

Brainstorm possible answers to the question, using the documents. Write out your ideas.

For each brainstormed topic, write at least 4 sentences about the topic.

Mark out your final response with "Response" and write out your response.

The response should provide an answer to the question.

The response should be comprehensive and address all parts of the question.

"""

compliance_assistant_cot_prompt = PromptTemplate(input_variables=['question', 'documents'], template=compliance_assistant_cot_template)

compliance_assistant_template = """

Question: {question}

Reasoning: {reasoning}

Write out a response to the company's question using the reasoning.

"""

compliance_assistant_prompt = PromptTemplate(input_variables=['question', 'reasoning'], template=compliance_assistant_template)
