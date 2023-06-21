# LLM Summarizer

* txt, pdf 문서를 요약할 수 있고 pdf 문서에 대해 질문을 할 수 있다.
* python code가 하는 작업을 요약하여 주석으로 출력해준다.

## 필요성???

* 문서를 ctrl+c ctrl+v로 힘들게 요약할 필요 없이 로컬 디스크에 존재하는 문서 형태 그대로 불러와 요약 가능.
* 문서의 내용이 너무 많아 읽기 힘들 때, 읽기 전 내용의 핵심을 상기하고 싶을 때 사용.
* 문서를 읽어도 내용 파악이 잘 되지 않을 때, 질문을 할 수 있음.

## 어떻게 만들었나

* [LangChain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
* 해당 링크를 참조하여 만들었다.
    - map_template : 주어진 파이썬 코드를 요약하기 위한 프롬프트 엔지니어링 탬플릿
    - reduce_template: map_template대로 만들어진 요약을 출력하는 서식을 정하기 위한 프롬프트 엔지니어링 탬플릿
    - MAP_PROMPT, REDUCE_PROMPT : 탬플릿을 적용한 프롬프트
    - map_llm_chain, reduce_llm_chain : 모델과 프롬프트를 적용한 체인
    - generative_result_reduce_chain : 코드가 하는 작업을 설명한 code_description을 생성해 내는 체인
    - combine_documents : 위 작업들을 하나로 합친 체인
    - map_reduce : 완성된 맵 리듀스 체인

## 어떻게 사용하나??

<img src = "assets/0tab.png" width = "200" height="200">
<img src = "assets/0tab done.png" width = "200" height="200">