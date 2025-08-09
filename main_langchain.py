from dotenv import load_dotenv
import os
load_dotenv()

# OPENAI_API_KEY_LANGCHAIN = os.getenv("OPENAI_API_KEY_LANGCHAIN")

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# this is for the prompt template
from langchain_core.prompts import PromptTemplate

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, model_kwargs= {'seed': 365})


# system_message = "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
# human_message = "I've recently adopted a dog, what should i name it?"
# ai_message = "Oh, absolutely, because nothing screams i'm a responsible pet owner like naming your dog after a food item. How about 'Biscuit' or 'Nacho'? That way, every time you call your dog, you'll be reminded of your poor life choices. Genius!"
# # response = chat.invoke(human_message)


# # message_s = SystemMessage(content=system_message)
# message_h = HumanMessage(content=human_message)
# message_a = AIMessage(content=ai_message)
# # response = chat.invoke([message_s, message_h])
# response = chat.invoke([message_h, message_a])

# print(response.content)


# ADDING A PROMPT TEMPLATE
TEMPLATE = """
System: 
{description}

Human:
I've recently adopted a {pet}.
Could you suggest some {pet} name?
"""

prompt_template = PromptTemplate.from_template(template=TEMPLATE)

prompt_value = prompt_template.invoke({
    'description': "I'm a chatbot that reluctantly answers questions with sarcastic responses.",
    'pet':"dog"
})

print(prompt_value)