from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.output_parsers import DatetimeOutputParser

load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Initialize the DatetimeOutputParser
parser = DatetimeOutputParser()

# Construct the message with proper format instructions
message = [
    HumanMessage(
        content=f"When was the University of Dundee founded?\n\n{parser.get_format_instructions()}"
    )
]

# Invoke the LLM
prompt_response = llm.invoke(message)

# Parse the response using the DatetimeOutputParser
parsed_response = parser.parse(prompt_response.content)

# Print the parsed datetime
print(parsed_response)