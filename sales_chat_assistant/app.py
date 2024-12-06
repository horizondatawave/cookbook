import chainlit as cl
from dotenv import load_dotenv
import os
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from hdw_tools.tools.llama_linkedin import LinkedInToolSpec
from llama_index.tools.google import GmailToolSpec, GoogleCalendarToolSpec

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'

llm = OpenAI(model="gpt-4o", temperature=0.2)

@cl.on_chat_start
async def start():
    system_message = (
        "You are an AI assistant that can help the user with LinkedIn searches, "
        "manage their Gmail inbox, and assist with Google Calendar tasks. "
        "You have access to three sets of tools: "
        "1) LinkedIn tools for searching profiles, companies, jobs; "
        "2) Gmail tools for reading, sending, and organizing emails; "
        "3) Google Calendar tools for creating, reading, updating, and deleting calendar events. "
        "From the user's messages, infer which toolset to use. "
        "If the user asks something related to LinkedIn, use the LinkedIn tools. "
        "If the user wants to send or read emails, use the Gmail tools. "
        "If the user mentions scheduling, events, meetings, or calendar-related tasks, use the Google Calendar tools. "
        "If unsure, ask a clarifying question. "
        "If you need to find a LinkedIn profile by email, try to infer the name or company name of the addressee and use it for the search. "
        "Make a few attempts with different variations of parameters to find the profile. "
        "When working with the calendar, ensure to confirm the details with the user (such as time, date, and participants) before performing actions."
    )

    # Создаем "суперагента" с двумя наборами инструментов
    agent = OpenAIAgent.from_tools(
        [tool for sublist in [LinkedInToolSpec().to_tool_list(), GmailToolSpec().to_tool_list(), GoogleCalendarToolSpec().to_tool_list()] for tool in sublist],
        llm=llm,
        verbose=True,
        system_prompt=system_message
    )

    cl.user_session.set("agent", agent)
    await cl.Message(content="Hello! How can I help you today?").send()


@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    response = agent.chat(message.content)
    await cl.Message(content=str(response)).send()