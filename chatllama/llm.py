import os
os.environ['CUDA_VISIBLE_DEVICES']='3'
from llama_index import ComposableGraph, GPTListIndex, LLMPredictor, GPTVectorStoreIndex, ServiceContext, \
    SimpleDirectoryReader,LangchainEmbedding,StorageContext,load_index_from_storage
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from file import check_index_file_exists, get_index_filepath, get_name_with_json_extension
#from dotenv import load_dotenv
from Chatglm_model import ChatGLMService
#load_dotenv()

# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# openai.api_key = OPENAI_API_KEY
llm_service=ChatGLMService()
llm_service.load_model(model_name_or_path='THUDM/chatglm-6b')
llm_predictor = LLMPredictor(llm=llm_service)

model_name = "hfl/chinese-roberta-wwm-ext"

os.environ['CURL_CA_BUNDLE'] = ''
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name=model_name))

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor,embed_model=embed_model)


def create_index(filepath, index_name):

    index = get_index_by_index_name(index_name)
    if index is not None:
        return index
    index_name = get_name_with_json_extension(index_name)
    documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
    index = GPTVectorStoreIndex.from_documents(documents,service_context=service_context)

    index.storage_context.persist(get_index_filepath(index_name))
    return index


def get_index_by_index_name(index_name):
    index_name = get_name_with_json_extension(index_name)
    if check_index_file_exists(index_name) is False:
        return None
    index_filepath = get_index_filepath(index_name)
    storage_context = StorageContext.from_defaults(persist_dir=index_filepath)
    index = load_index_from_storage(storage_context=storage_context,service_context=service_context)

    return index


def create_graph(index_sets, graph_name):
    graph_name = get_name_with_json_extension(graph_name)
    graph = ComposableGraph.from_indices(GPTListIndex,
                                         [index for _, index in index_sets.items()],
                                         index_summaries=[f"This index contains {indexName}" for indexName, _ in index_sets.items()],
                                         service_context=service_context)
    graph.save_to_disk(get_index_filepath(graph_name))
    return graph


def get_graph_by_graph_name(graph_name):
    graph_name = get_name_with_json_extension(graph_name)
    graph_path = get_index_filepath(graph_name)
    graph = ComposableGraph.load_from_disk(graph_path, service_context=service_context)
    return graph
