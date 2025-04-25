import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    base_url = os.getenv('COHERE_BASE_URL'),
    api_key = os.getenv('COHERE_API_KEY')
)

#get completion her is more like a helper function
def get_completions(prompt,model="gpt-4o-mini"):
    messages=[{'role':'user',
               'content':prompt}]
    response = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=messages
    )
    return response.choices[0].message.content

get_completions("what is the capital of india ")

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""

prompt =f"""just translate the email that is delimited
by triple backticks inside text into a style that is {style}.
text:```{customer_email}```
"""
print(prompt)
print(get_completions(prompt))


################################################
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini",
                base_url = os.getenv('baseURL'),
                api_key = os.getenv('apiKEY'))
messages = [{
    "role":"user",
    "content":"what is the capital of france"
}]
print(llm.invoke(messages).content)
##################################################

from langchain_core.prompts import ChatPromptTemplate

system_template = "just translate the given email into a style that is {style}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{email}")
])

email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

prompt=prompt_template.invoke({"style":"In normal english","email":email})
prompt.to_messages() #shows in a formatted output
response=llm.invoke(prompt)
print(response.content)

'''you can also use the below way on formatted output directly'''
# output =prompt.to_messages()
# response=llm.invoke(output)
# print(response.content)

#or you can simply chain llm and prompt template so that both can be invoked(notice how in the above example you are invoking llm and prompt seperately)
#and enter the arguments while invoking the chain

chain = prompt_template | llm 
chain.invoke({
    "style":"Into normal english",
    "email":email
}).content

