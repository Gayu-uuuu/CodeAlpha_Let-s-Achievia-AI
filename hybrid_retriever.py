from langchain.vectorstores import Chroma
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.schema import Document

def get_retriever():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k":3}
    )

    return retriever