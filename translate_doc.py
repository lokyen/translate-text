import streamlit as st

from langchain.schema import Document
from langchain_community.document_transformers import DoctranTextTranslator
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

load_dotenv()

st.title(''':red[Translate] :orange[Any] :green[Foreign] :blue[Text] :violet[to] :red[English]''')

st.write("Press ctrl + enter or cmd + enter to submit")
sample_text = st.text_area('Enter text', '', height=300)

#Translating text
documents = [Document(page_content=sample_text)]
qa_translator = DoctranTextTranslator(language="english", openai_api_model="gpt-3.5-turbo")

translated_document = qa_translator.transform_documents(documents)

st.write(translated_document[0].page_content)

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

#Summarizing text
summarized_text = []
text_splitter = CharacterTextSplitter() 
texts = text_splitter.split_text(translated_document[0].page_content)
docs = [Document(page_content=t) for t in texts]

chain = load_summarize_chain(llm, chain_type='map_reduce')
summary = chain.invoke(docs)
summarized_text.append(summary)

st.header("Short Summary of Text") 
st.write(summarized_text) 