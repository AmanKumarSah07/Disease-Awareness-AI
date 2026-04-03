import traceback
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

load_dotenv(override=True)
token = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
try:
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.3",
        huggingfacehub_api_token=token,
    )
    chat_model = ChatHuggingFace(llm=llm)
    print("Agent initialized.")
    response = chat_model.invoke([HumanMessage(content="Hello")])
    print("Response:", response.content)
except Exception as e:
    print("ERROR OCCURRED:")
    import traceback
    traceback.print_exc()
