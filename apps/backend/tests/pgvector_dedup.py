from langchain_postgres import PGVector
from langchain_community.indexes._sql_record_manager import SQLRecordManager
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.indexing import index

from aisql.settings import settings

def main():
    # 1. 初始化向量库 (存储向量)
    collection_name = settings.vector_collection_name
    connection_string = settings.pg_conn_str
    embeddings = DashScopeEmbeddings(dashscope_api_key=settings.api_key)

    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=collection_name,
        connection=connection_string,
    )

    # 2. 初始化 Record Manager (存储索引记录)
    # 注意：它会创建一个名为 'record_manager_cache' 的表
    namespace = f"pgvector/{collection_name}"
    record_manager = SQLRecordManager(namespace, db_url=connection_string)

    # 3. 创建 Schema
    record_manager.create_schema()

    # 4. 执行索引操作
    docs = [doc1, doc2, doc3]  # 你的文档对象列表

    indexing_stats = index(
        docs,
        record_manager,
        vector_store,
        cleanup="incremental",  # 关键参数：incremental, full, 或 None
        source_id_key="source",  # 文档元数据中标识来源的字段
    )
