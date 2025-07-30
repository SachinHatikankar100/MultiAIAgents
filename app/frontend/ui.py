import streamlit as st
from app.config.config import Config
import requests
from app.common.custom_exception import CustomException
from app.common.logger import get_logger

logger = get_logger(__name__)


st.set_page_config("Multi Provider and models AI Agent",layout="centered")


st.title("Multi Provider and models AI Agent")


system_prompt= st.text_area("Input for AI Agent",height=70,)
providers = st.selectbox("Select Provider",options=Config.ALLOWED_PROVIDERS)
if providers=="Gemini":
    model = st.selectbox("Select Model",options=Config.GEMINI_MODELS,key=Config.GEMINI_MODELS)
else:
    model = st.selectbox("Select Model",options=Config.GROQ_MODELS,key=Config.GROQ_MODELS)
allow_search = st.checkbox("Allow web search")
user_input=st.text_area("Input for User",height=70)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Send") and user_input.strip():

    payload ={
        "provider":providers,
        "model":model,
        "user_input":user_input,
        "allow_search":allow_search,
        "system_prompt":system_prompt

    }

    try:

        response = requests.post(API_URL,json=payload)

        if response.status_code==200:
            logger.info("Request sent to backend successfully")
            agent_response = response.json().get("response","")
            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n","<br>"), unsafe_allow_html=True)
        else:
            logger.error("Error in backend")

    except CustomException as e:
        logger.error("Error while sending request to backend")
        raise Exception(str(CustomException("Error while sending request to backend",error_detail=e)))


