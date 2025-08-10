**Code Explanation – Line by Line** written by authour - @KhutijaTasneemHub


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

