from langchain_postgres.vectorstores import PGVector
from langchain_community.embeddings import DashScopeEmbeddings

from aisql.settings import settings

def main():
    vector_store = PGVector(
        embeddings=DashScopeEmbeddings(dashscope_api_key=settings.api_key),
        collection_name=settings.vector_collection_name,
        connection=settings.pg_conn_str,
    )

    vector_store.add_texts([
        "这是一个测试文档。", 
        "我想去上海旅游", 
        "今天天气不错",])


    print(vector_store.similarity_search('我想去上海', k=2))


if __name__ == '__main__':
    main()
