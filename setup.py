from setuptools import setup

setup(
    name='diaita',
    version='0.1',
    author='Campbell Hutcheson',
    author_email='nchutcheson@gmail.com',
    description='climate hackathon 2023',
    packages=['diaita'],
    install_requires=[
        'langchain',
        'marvin',
        'openai',
        'pandas',
        'chromadb',
        'streamlit',
        'streamlit-chat'
    ],
)

