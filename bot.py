import requests
import os
from langchain_chroma import Chroma
from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


class ContextRetriever:
    def __init__(self, embeddings_model, persist_directory, threshold):
        self.context = None
        self.persist_directory = persist_directory
        self.threshold = threshold
        self.vectorstore = Chroma(persist_directory=self.persist_directory,
                                  embedding_function=embeddings_model)
        # self.retriever = self.vectorstore.as_retriever(search_kwargs={'k': self.num_results})
        self.retriever = self.vectorstore.as_retriever(search_type="similarity_score_threshold",
                                                       search_kwargs={"score_threshold": self.threshold})

    def get_context(self, question):
        self.context = self.retriever.invoke(question)
        return self.context


class ChatHistoryFormatter:
    @staticmethod
    def format_chat_history(chat_history, len_history=50):
        formatted_history = []
        if len(chat_history) > 0:
            for human, ai in chat_history[-len_history:]:
                formatted_history.append(HumanMessage(content=human))
                formatted_history.append(AIMessage(content=ai))
            return formatted_history
        else:
            return chat_history


class QuestionContextualizer:
    def __init__(self, chat_model):
        self.contextualized_question = None
        self.formatted_chat_history = None
        self.question = None
        self.chat_model = chat_model
        self.contextualize_q_system_prompt = """Given the following conversation between a user and an AI assistant (yourself) and a follow up question from user,
                                                rephrase the follow up question in order to be consistent with the chat history (only the user history). 
                                                Rephrase it in a way suitable to query a search engine and, if necessary create new questions and make explicit every aspect of the question."""
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{question}")
        ])
        self.contextualize_chain = self.prompt_template | chat_model | StrOutputParser()

    def contextualize_question(self, formatted_chat_history, question):
        self.question = question
        self.formatted_chat_history = formatted_chat_history
        self.contextualized_question = self.contextualize_chain.invoke({'chat_history': formatted_chat_history, 'question': question})
        return self.contextualized_question


class AnswerGenerator:
    def __init__(self, chat_model):
        self.answer = None
        self.question = None
        self.context = None
        self.chat_model = chat_model
        # Create the prompt template
        self.prompt_template = """You are a Q&A assistant expert on the FAIRiCUBE project (refer to this in generic questions where it is not specified) and your name is 'FAIRiCUBE-KB-chatbot'.
                                The assistant is talkative and provides lots of specific details from its context.
                                Your goal is to answer questions regarding FAIRiCUBE as accurately as possible based on the instructions and the knowledge base context provided but do not introduce FAIRiCUBE in every answer.
                                Reply to greetings and be complete in your answer and address all points raised in the provided questions. 
                                Do not write path of file, filenames, images and my instructions but you can use external links.
                                If the information in the provided context does not help in answering the questions clearly state it but you can use your knowledge. 
                                If do not have an answer do not write 'Empty Response' but try to use your knowledge or write a detailed reason.
                                Write your answer in 500 words or less.

                                Context: {context}

                                Question: {contextualized_question}

                                Answer: 
                                """
        self.prompt_template = ChatPromptTemplate.from_template(self.prompt_template)
        # Question and answer chain that takes in the context and contextualized question and spits out the answer
        self.qa_chain = self.prompt_template | self.chat_model | StrOutputParser()

    def generate_answer(self, context, question):
        self.context = context
        self.question = question
        # Invoke the question and answer chain
        self.answer = self.qa_chain.invoke({'context': self.context, 'contextualized_question': self.question})
        return self.answer


class ResultFormatter:
    @staticmethod
    def format_result(answer, context):
        bases = ['https://fairicube.readthedocs.io/en/latest/',
                 'https://fairicube.readthedocs.io/en/latest/overview/',
                 'https://fairicube.readthedocs.io/en/latest/use_cases/',
                 'https://fairicube.readthedocs.io/en/latest/user_guide/',
                 'https://fairicube.readthedocs.io/en/latest/self_training/',
                 'https://fairicube.readthedocs.io/en/latest/ai_toolkit/',
                 'https://fairicube.readthedocs.io/en/latest/gdc_toolkit/',
                 'https://fairicube.readthedocs.io/en/latest/lessons_learnt_tips_tricks/',
                 'https://fairicube.readthedocs.io/en/latest/external_resource/'
                 ]
        def url_ok(url):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            }
            r = requests.get(url, headers=headers)
            return r.status_code == 200
        def build_link(name):
            if name == 'index':
                return bases[0]
            for i in bases:
                u = i + name + '/'
                if url_ok(u):
                    return u

        files = set((doc.metadata['source']) for doc in context)
        files = list(files)
        links = []

        for i in files:
            i = i.replace("\\","/")
            title = i.split('/')[1].split('.')[0]
            l = build_link(title)
            links.append(l)

        if len(links) == 0:
            return answer

        titles_string = '\n'.join(links)
        titles_formatted = f"Relevant documents in the FAIRiCUBE Knowledge Base:\n{titles_string}"
        response = f"{answer}\n\n{titles_formatted}"
        return response


class KnowledgeBaseBot:
    def __init__(self, temp=0.1,
                       chat_model_name='gpt-4o',
                       embeddings_model_name='text-embedding-3-large',
                       threshold=0.5,
                       persist_directory='./kb_chroma_db',
                       ):
        # Load environment and API keys
        load_dotenv()
        api_key = os.getenv('MISTRAL_API_KEY')
        OPENAI_APIKEY = os.environ['OPENAI_APIKEY']

        self.embeddings_model_name = embeddings_model_name
        self.temp = temp
        self.chat_model_name = chat_model_name
        self.threshold = threshold
        self.persist_directory = persist_directory

        # Embeddings Model
        self.embeddings_model = OpenAIEmbeddings(api_key=OPENAI_APIKEY,
                                                model=self.embeddings_model_name,
                                                max_retries=100,
                                                chunk_size=700,
                                                show_progress_bar=False,
                                                )

        # Initialize Chat Model
        self.chat_model = ChatOpenAI(api_key=OPENAI_APIKEY,
                                     temperature=self.temp,
                                     model=self.chat_model_name,
                                     max_tokens=700
                                     )

        # Set up vector store and other components
        self.context_retriever = ContextRetriever(embeddings_model=self.embeddings_model,
                                                  persist_directory=self.persist_directory,
                                                  threshold=self.threshold)
        self.chat_history_formatter = ChatHistoryFormatter()
        self.question_contextualizer = QuestionContextualizer(self.chat_model)
        self.answer_generator = AnswerGenerator(self.chat_model)
        self.result_formatter = ResultFormatter()

    def process_chat(self, new_question, chat_history):
        formatted_chat_history = self.chat_history_formatter.format_chat_history(chat_history)
        contextualized_question = self.question_contextualizer.contextualize_question(formatted_chat_history, new_question)
        context = self.context_retriever.get_context(contextualized_question)
        answer = self.answer_generator.generate_answer(context=context, question=contextualized_question)
        final_result = self.result_formatter.format_result(answer, context)
        return final_result
