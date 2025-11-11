from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from typing import List
from flipkart.config import Config

class RAGChainBuilder:
    def __init__(self,vector_store):
        self.vector_store=vector_store
        self.model = ChatGroq(model=Config.RAG_MODEL , temperature=0.5)
        self.history_store={}

    def _get_history(self,session_id:str) -> BaseChatMessageHistory:
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory()
        return self.history_store[session_id]
    
    def build_chain(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k":3})

        # Prompt for rewriting question with history
        context_prompt = ChatPromptTemplate.from_messages([
            ("system", "Given the chat history and user question, rewrite it as a standalone question."),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}")  
        ])

        # Prompt for answering with context
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", """You're an e-commerce bot answering product-related queries using reviews and titles.
                          Stick to context. Be concise and helpful.\n\nCONTEXT:\n{context}"""),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}")  
        ])

        # Format documents for context
        def format_docs(docs: List[Document]) -> str:
            return "\n\n".join(doc.page_content for doc in docs)

        # Create history-aware retriever: rewrite question, then retrieve
        history_aware_retriever = (
            RunnablePassthrough.assign(
                standalone_question=context_prompt | self.model | StrOutputParser()
            )
            | RunnablePassthrough.assign(
                context=lambda x: format_docs(retriever.invoke(x["standalone_question"]))
            )
        )

        # Create QA chain that uses the context
        rag_chain = (
            history_aware_retriever
            | qa_prompt
            | self.model
            | StrOutputParser()
        )

        # Wrap to return dict with "answer" key for compatibility with app.py
        def wrap_answer(response):
            return {"answer": response}

        wrapped_chain = rag_chain | wrap_answer

        return RunnableWithMessageHistory(
            wrapped_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )



