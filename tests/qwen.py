import os

from openai import OpenAI
from aisql.settings import settings

# 注意: 不同地域的base_url不通用（下方示例使用北京地域的 base_url）
# - 华北2（北京）: https://dashscope.aliyuncs.com/compatible-mode/v1
# - 新加坡: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
client = OpenAI(
    api_key=settings.api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {'role': 'system', 'content': '你是一个 Python 编程专家，并且不说废话，简单回答'},
        {'role': 'assistant', 'content': '好的，我是编程专家，并且话不多，你要问什么？'},
        {'role': 'user', 'content': '输入 1-10 的数字，使用 Python 代码'}
    ],
    stream=True
)

# print(completion.choices[0].message.content)

# 流式输出
for chunk in completion:
    print(chunk.choices[0].delta.content, end='')

