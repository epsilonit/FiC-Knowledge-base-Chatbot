import gradio as gr
import bot
import os
import vector_store_builder

# if not os.path.isdir('./kb_chroma_db'):
#    print('Vector store building...')
#    vector_store_builder.build_vector_store()

kb_bot = bot.KnowledgeBaseBot()

# Set up chatbot interface
answer_bot = gr.ChatInterface(kb_bot.process_chat,
                              chatbot=gr.Chatbot(type="tuples"),
                              textbox=gr.Textbox(placeholder="Type your question about the FAIRiCUBE project or "
                                                             "knowledge base here...", container=False,
                                                 scale=7),
                              title="FAIRiCUBE Knowledge Base ChatBot",
                              description="The FAIRiCUBE Knowledge Base ChatBot is an intelligent assistant designed "
                                          "to help understand the FAIRiCUBE project. This chatbot acts as a guide to "
                                          "FAIRiCUBE’s resources, answering questions about its objectives, "
                                          "methodologies, and knowledge base. Whether you’re a researcher, "
                                          "policymaker, or developer, the ChatBot provides insights into FAIRiCUBE’s "
                                          "tools, use cases, analysis and processing resources, datasets, "
                                          "and applications in environmental and spatial data science. With an "
                                          "intuitive interface, it efficiently retrieves project information, "
                                          "clarifies technical aspects, and directs users to relevant documents and "
                                          "data sources within the FAIRiCUBE knowledge base. "
                                          "Use the text box at the bottom of the page to ask your question about the FAIRiCUBE project and the Knowledge Base.",
                              theme="soft",
                              stop_btn="Interrupt",
                              submit_btn="Ask",
                              type="tuples"
                              )

answer_bot.queue(default_concurrency_limit=None)
answer_bot.launch(share=True)
