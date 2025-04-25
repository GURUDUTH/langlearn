import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    base_url = os.getenv('baseURL'),
    api_key = os.getenv('apiKEY')
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