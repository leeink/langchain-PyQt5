import os

from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.chains.mapreduce import MapReduceChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain

os.environ['OPENAI_API_KEY']='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'

agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(),
    verbose=True
)

res=agent_executor.run("피보나치 수열을 동적 계획법으로 구현한 함수를 작성하시오")

llm = OpenAI(temperature=0)
chain = load_summarize_chain(llm, chain_type="map_reduce")

prompt_template = """Write a concise summary of the following:


{text}


CONCISE SUMMARY IN ITALIAN:"""

map_template_string = """Give the following python code information, generate a description that explains what the code does and also mention the time complexity.
Code:
{code}

Return the the description in the following format:
name of the function: description of the function
"""


reduce_template_string = """Give the following following python fuctions name and their descritpion, answer the following question
{code_description}
Question: {question}
Answer:
"""

MAP_PROMPT = PromptTemplate(input_variables=["code"], template=map_template_string)
REDUCE_PROMPT = PromptTemplate(input_variables=["code_description", "question"], template=reduce_template_string)

map_llm_chain = LLMChain(llm=llm, prompt=MAP_PROMPT)
reduce_llm_chain = LLMChain(llm=llm, prompt=REDUCE_PROMPT)

generative_result_reduce_chain = StuffDocumentsChain(
    llm_chain=reduce_llm_chain,
    document_variable_name="code_description",
)

combine_documents = MapReduceDocumentsChain(
    llm_chain=map_llm_chain,
    combine_document_chain=generative_result_reduce_chain,
    document_variable_name="code",
)

map_reduce = MapReduceChain(
    combine_documents_chain=combine_documents,
    text_splitter=CharacterTextSplitter(separator="\n##\n", chunk_size=100, chunk_overlap=0),
)

code = """
def bubblesort(list):
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
    return list
##
def insertion_sort(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
   while (InputList[j] > nxt_element) and (j >= 0):
      InputList[j+1] = InputList[j]
      j=j-1
   InputList[j+1] = nxt_element
   return InputList
##
def shellSort(input_list):
   gap = len(input_list) // 2
   while gap > 0:
      for i in range(gap, len(input_list)):
         temp = input_list[i]
         j = i
   while j >= gap and input_list[j - gap] > temp:
      input_list[j] = input_list[j - gap]
      j = j-gap
      input_list[j] = temp
   gap = gap//2
   return input_list

"""

map_reduce.run(input_text=code, question="어느 함수가 실행속도가 가장 빠른가요?")