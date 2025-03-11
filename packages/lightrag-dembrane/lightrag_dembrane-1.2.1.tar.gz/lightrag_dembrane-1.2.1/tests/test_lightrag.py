import os
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.utils import EmbeddingFunc
# from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.llm.ollama import ollama_embed, ollama_model_complete
import time

model_name = "phi4:latest"

sample_text = '''
Where Echo is used today
We are proud that even in its early stages, Echo is already making waves across different communities. In Brabant, it helped amplify the voices of more than seventy young people during their Jongerentop youth summit. In 's-Hertogenbosch, over 200 citizens council participants used Echo to share their stories with each other. Setup takes under 5 minutes, and insights appear within 2 minutes of conversations. Most importantly, participants consistently report feeling more heard and valued than they would with traditional methods (audio recording with no ECHO feedback, or with manually taken notes or post-its).
'''

# WorkingDir
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKING_DIR = os.path.join(ROOT_DIR, "myKG")
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)
print(f"WorkingDir: {WORKING_DIR}")

os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "admin@dembrane"
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_PORT"] = "5432"
os.environ["POSTGRES_USER"] = "dembrane"
os.environ["POSTGRES_PASSWORD"] =  "dembrane"
os.environ["POSTGRES_DATABASE"] = "dembrane"
os.environ["VERBOSE"] = "true"

# async def initialize_rag():
# async def init():
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name=model_name,
    llm_model_max_async=4,
    llm_model_max_token_size=8192,
    llm_model_kwargs={
        "host": "http://host.docker.internal:11434",  # Changed: include protocol and port in host URL
        "options": {"num_ctx": 8192},
    },
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embed(
            texts, 
            embed_model="nomic-embed-text", 
            host="http://host.docker.internal:11434"  # Changed: use host.docker.internal
        ),
    ),
    graph_storage="Neo4JStorage",
    kv_storage="PGKVStorage",
    doc_status_storage="PGDocStatusStorage",
    vector_storage="PGVectorStorage",
)

#     # Add initialization code
#     await rag.initialize_storages()
#     await initialize_pipeline_status()

#     return rag


# loop = asyncio.get_event_loop()
# rag = loop.run_until_complete(init())

# print('******Insert******')
# rag.insert(input = sample_text, 
#            ids=[f"{model_name}_{int(time.time())}"])
# print('******Insert******')


print('******Query******')
print(rag.query(query="What is Echo?", 
                param = QueryParam(mode = "mix", 
                                   ids = ["phi4:latest_1741438809"])))
print('******Query******')
