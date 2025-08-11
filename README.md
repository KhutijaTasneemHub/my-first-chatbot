**Code Explanation – Line by Line** written by author - @KhutijaTasneemHub


Importing libraries (tools that python program needs) 
**import streamlit as st**
**What it does**: Loads the Streamlit library, which lets you create web apps using Python.
**In simple terms:** Think of Streamlit as the “website builder” for your chatbot. Instead of writing HTML and CSS, you just write Python code, and Streamlit turns it into a webpage automatically.
**Example:** If you want a text box on your web page, Streamlit can create it with one line of code.

**from PyPDF2 import PdfReader**
**What it does:** Imports the PdfReader tool from the PyPDF2 library, which allows your code to read PDF files and extract text from them.
**Example: **If you upload a 10-page PDF, PdfReader can read every page and give you the words inside it, just like reading a book and copying text.

**from langchain.text_splitter import RecursiveCharacterTextSplitter**
**What it does:** Imports the RecursiveCharacterTextSplitter tool from LangChain, which splits big chunks of text into smaller, manageable pieces.
Why: Large documents are too big for AI to process at once. This breaks them into smaller “paragraph” chunks so the AI can search through them faster.
**Example:** If your PDF text has 10,000 characters, it might split it into 1,000-character pieces with some overlap so no important sentence is cut in half.

**from langchain_community.embeddings.openai import OpenAIEmbeddings**
**What it does:** Lets your program create embeddings using OpenAI’s service.
What are embeddings? They are like “mathematical fingerprints” of text. Instead of storing text as words, the computer converts it into numbers so it can compare and search them quickly.
**Example:** “Apple” and “Banana” have embeddings close to each other (both are fruits), but “Apple” and “Car” are far apart.

**from langchain_community.vectorstores import FAISS**
**What it does:** Imports FAISS, a tool for storing and searching embeddings very fast (developed by Facebook AI).
**In simple terms:** FAISS is like a Google Search for your document, but instead of searching for exact words, it searches for meaning.
**Example:** If your PDF says “car”, and you search “vehicle”, FAISS can still find the right place.

**from langchain_core import documents**
**What it does:** Brings in LangChain’s documents system for handling structured text.
**In this code:** It’s imported but not directly used — possibly unnecessary here.

**from langchain.chains.question_answering import load_qa_chain**
**What it does:** Loads a Question-Answering Chain from LangChain.
**In simple terms:** A chain is a pipeline. This one:
Takes your question. Looks for matching text in your document. Passes it to the AI model.Gets the answer and gives it back to you.

**from langchain_community.chat_models import ChatOpenAI**
**What it does:** Lets you use OpenAI’s ChatGPT-like models inside your Python code.
**Example:** You can ask it questions and it replies just like ChatGPT.

**Setting the API key**-
OPENAI_API_KEY = "xxxxx-your-api-key-here"
**What it does:** Stores your secret OpenAI API Key in a variable.
Why: This is like your personal password that lets your program use OpenAI’s AI models.
Security: You should never put your real API key here when uploading to GitHub. Use st.secrets or environment variables instead.


**Building the web page**
st.header("My fist Chatbot")
**What it does:**
Creates a big heading at the top of your web app saying “My first Chatbot”.


with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF File and start asking questions", type='pdf')
**What it does:**
with st.sidebar: — Creates a sidebar panel on the left side of the app.
st.title("Your Documents") — Adds a title in the sidebar.
file = st.file_uploader(...) — Creates a file upload box where you can upload PDFs.
**Example:** This is like when a website lets you “Choose File” to upload something.

**Reading the PDF**
if file is not None:
    pdf_Reader = PdfReader(file)
**What it does:**
Checks if the user has uploaded a file.
If yes, it uses PdfReader to open it.
**Example:** It’s like saying “If a book is given to me, I will open it.”

text = ''
for page in pdf_Reader.pages:
    text += page.extract_text()

**What it does:**
Starts with an empty text variable.
Loops through every page in the PDF.
Extracts text from each page and adds it to text.

**Example:** Imagine copying text from each page of a book and pasting it into one giant document.

**Breaking the text into smaller pieces** 
text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    
**What it does:**
Creates a tool to split text:
chunk_size=1000 → Each piece will be at most 1000 characters long.
chunk_overlap=150 → The last 150 characters of the previous chunk will be repeated in the next one to keep context.
separators="\n" → Splits at new lines when possible.

chunks = text_splitter.split_text(text)
**What it does:** Actually splits the extracted PDF text into small pieces (chunks).

**Turning chunks into embeddings**
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
**What it does:**
Connects to OpenAI and gets ready to create embeddings for your text chunks.

vector_store = FAISS.from_texts(chunks, embeddings)
**What it does:**
Takes each chunk.
Creates an embedding for it.
Stores it inside a FAISS database for fast searching.

user_question = st.text_input("Type your Question here")
What it does: Shows a text box where the user can type a question.

**Searching for relevant chunks**
    if user_question:
        match = vector_store.similarity_search(user_question)
**What it does:**
Looks for chunks in your FAISS database that match the meaning of the user’s question.
Returns the most relevant pieces.

**Getting AI to answer**
llm = ChatOpenAI(
openai_api_key = OPENAI_API_KEY,
temperature = 0,
max_tokens =  1000,
model_name = "gpt-3.5-turbo"
)

**What it does:**
Sets up an AI model (gpt-3.5-turbo) from OpenAI.
temperature=0 → Makes the answer more factual and less creative.
max_tokens=1000 → The maximum length of the answer.

chain = load_qa_chain(llm, chain_type="stuff")
**What it does:** Loads a Question-Answer chain that:
Takes the question.
Passes relevant text from your PDF to the AI.
Returns the answer.


response = chain.run(input_documents=match, question=user_question)
st.write(response)
**What it does:**
Runs the chain. Gets the AI’s answer. Displays it in your web app.
