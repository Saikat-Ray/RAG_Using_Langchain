import os
from dotenv import load_dotenv
load_dotenv()

import os
from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types

from IPython.display import display
from IPython.display import Markdown
import textwrap

from pathlib import Path
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import  GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA

client = genai.Client()
model="gemini-3.6-flash"

chat = client.chats.create(
    model=model
)

# 3. Send the message via the chat session (instead of client.models)
response = chat.send_message("Explain Generative AI with 3 bullet points")

print(response.text)
Markdown(response.text)