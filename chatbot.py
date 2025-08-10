import streamlit as st

from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings.openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_core import documents

from langchain.chains.question_answering import load_qa_chain

from langchain_community.chat_models import ChatOpenAI




OPENAI_API_KEY = "xxxxx-your-api-key-here"
#the above generated unique api key is from -  https://platform.openai.com/api-keys

##upload pdf files
st.header("My fist Chatbot")
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF File and start asking questions", type='pdf')

#extract the text
if file is not None:
    pdf_Reader = PdfReader(file)
    # if there is any file ,go inside the file and read the pages
    text = ''
    for page in pdf_Reader.pages:
        # for each of the page that is present in pdf , go ahead and extract the text on that page & put it in text variable
        text += page.extract_text()
        # st.write(text)

    #break into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # generating embeddings - we wikll be using openAI services to generate embeddings from chunks
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # creating a vector store -  gonna use faiss-cpu
    vector_store = FAISS.from_texts(chunks, embeddings)

    #it looks the above line as so simple but its doing three steps over there -
    # embeddings (openAI)
    # initailising FAISS
    #store chunks and embeddings

    # get the question  from user
    user_question = st.text_input("Type your Question here")

    # do semantic/similarity search

    # A= question -> user_question
    # B= vector_data base -> vector_store

    if user_question:
        # match = vector_store.similarity(user_question)
        match = vector_store.similarity_search(user_question)

        # st.write(match)

        # define the llm
        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            temperature = 0,
            max_tokens =  1000,
            model_name = "gpt-3.5-turbo"
        )

        # generate output results
        # chain -> take the question -> get relevant documents -> pass it to LLM -> generate the output
        chain = load_qa_chain( llm, chain_type="stuff")
        response = chain.run( input_documents = match , question = user_question )
        st.write(response)





