import json

from openai import OpenAI
from config import ai_key

### 摘抄自一个学弟的第二课堂仓库AI部分
## https://github.com/tinyvan/SecondClass

system_prompt = """
You are highly skilled in analyzing Chinese text and are proficient in answering questions based on the information provided in the text. Your responses should follow the structure of the JSON format, providing clear and concise answers based on the analysis of the text.
Usually the answer can be easily found in the text.
You should provide your thinking process in the "thinking" field of the JSON response.
Your responses should be the following format and answer letter must be in uppercase.:
{
"thinking":"Your thinking process should be put here",
"answer":["A","B","C"]
}
"""

client = None


def LLM_init(api_key: str):
    global client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.chatanywhere.tech/v1",
    )


def get_ans(text):
    if client is None:
        raise Exception("LLM is not initialized")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': text}],
    )
    return completion.choices[0].message.content


def request_ai(type, problem, options):
    LLM_init(ai_key)
    response = get_ans(str({
        "type": type,
        "question": problem,
        "options": options
    }))
    print(response)
    return json.loads(response)["answer"]
