from langchain_community.llms.tongyi import Tongyi

from aisql.settings import settings


ty = Tongyi(model='qwen-max', api_key=settings.api_key)


if __name__ == '__main__':
    # res = ty.invoke('你是谁，能做什么？')
    # print(res)

    # 流式输出
    res = ty.stream('你是谁，能做什么？')
    for r in res:
        print(r, end='', flush=True)
