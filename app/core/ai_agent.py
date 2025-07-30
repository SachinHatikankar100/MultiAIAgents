from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
#This imports the TavilySearchResults tool used for web search (requires Tavily API key).
from langgraph.prebuilt import create_react_agent
#This imports a prebuilt ReAct (Reasoning + Action) agent that can use tools like Tavily.
from langchain_core.messages import AIMessage
#gets only messages from agent
from dotenv import load_dotenv

load_dotenv()

def ai_agent_response(provider_id,llm_id,query,system_promt,allow_search):


    if provider_id == "Gemini":
        llm = ChatGoogleGenerativeAI(model=llm_id)
    else:
        llm = ChatGroq(model=llm_id)
    tools = [TavilySearchResults(max=2)] if  allow_search else []

    agent = create_react_agent(
        model = llm,
        tools=tools,
        state_modifier=system_promt
    )

    state = {"messages":[query]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]