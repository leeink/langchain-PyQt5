import os
import glob

os.environ['OPENAI_API_KEY']='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' # 동근
#os.environ['OPENAI_API_KEY']='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'
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

"""
llm = OpenAI(temperature=0)

text_splitter = CharacterTextSplitter()

with open("memo.txt", encoding='UTF8') as f:
    state_of_the_union = f.read()
texts = text_splitter.split_text(state_of_the_union)

docs = [Document(page_content=t) for t in texts[:3]]

chain = load_summarize_chain(llm, chain_type="map_reduce")
res=chain.run(docs)
print(res)
"""

class summarizer:
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.text_splitter = CharacterTextSplitter()
        self.chain_type = "map_reduce"
        self.chain = load_summarize_chain(self.llm, chain_type=self.chain_type)
    
    def summary(self, doc):
        texts = self.text_splitter.split_text(doc)
        docs = [Document(page_content=t) for t in texts[:3]]
        return self.chain.run(docs)
    
    def summaryPdf(self, path, custom_prompt=""):
        loder = PyPDFLoader(path)
        docs = loder.load_and_split()
        chain = load_summarize_chain(self.llm, chain_type=self.chain_type)
        summary = chain.run(docs)
        if custom_prompt !="":
            prompt_template = custom_prompt +"""

            {text}
                
            SUMMARY:"""
            PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
            chain = load_summarize_chain(self.llm, chain_type=self.chain_type,
                                                  map_prompt=PROMPT, combine_prompt=PROMPT)
            custom_summary = chain({"input_documents": docs}, return_only_outputs=True)["output_text"]

        else:
            custom_summary = ""

        return summary, custom_summary
    
    def custom_summary(self,path,custom_prompt):
        loader = PyPDFLoader(path)
        docs = loader.load_and_split()
        prompt_template = custom_prompt +"""
        {text}
        SUMMARY:"""
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(self.llm, chain_type=self.chain_type,
                                                    map_prompt=PROMPT, combine_prompt=PROMPT)
        summary_output = chain({"input_documents": docs}, return_only_outputs=True)["output_text"]

        return summary_output
    
    def summarize_pdfs_from_folder(self,pdfs_folder):
        summarize =[]
        for pdf in glob.glob(pdfs_folder + "/*.pdf"):
            loader = PyPDFLoader(pdf)
            docs = loader.load_and_split()
            chain = load_summarize_chain(self.llm, chain_type=self.chain_type)
            summary = chain.run(docs)
            summarize.append(summary)

        return summarize
    
    def QueryPdfs_fromFolder(self,pdfs_folder,query):
        loader = PyPDFDirectoryLoader(pdfs_folder)
        #docs = loader.load()
        index = VectorstoreIndexCreator().from_loaders([loader])
        res = index.query(query)
        return res