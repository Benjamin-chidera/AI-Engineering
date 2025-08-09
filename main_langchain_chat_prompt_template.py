from dotenv import load_dotenv
import os
load_dotenv()

# OPENAI_API_KEY_LANGCHAIN = os.getenv("OPENAI_API_KEY_LANGCHAIN")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, model_kwargs= {'seed': 365})

TEMPLATE_SYSTEM = '{description}'
TEMPLATE_HUMAN = "I've recently adopted a {pet}. Could you suggest some {pet} name?"

message_template_system = SystemMessagePromptTemplate.from_template(template=TEMPLATE_SYSTEM)
message_template_human = HumanMessagePromptTemplate.from_template(template=TEMPLATE_HUMAN)

chat_template = ChatPromptTemplate.from_messages([message_template_system, message_template_human])

chat_value = chat_template.invoke({
    'description': "I'm a chatbot that reluctantly answers questions with sarcastic responses.",
    'pet':"dog"
})

response = chat.invoke(chat_value)
print(response)