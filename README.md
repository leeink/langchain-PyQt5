# PyQt5 - LangChain
## Documents summary

**PyQt5와 LangChain의 요약 모델을 활용하여 만든 문서 요약 프로그램** <br/>
**Python >= 3.10.8** <br/>
**라이브러리는 requirements.txt 참조**<br/>
`pip install -r requiremetns.txt`

<hr/>

* PyQt: PyQt 클라이언트 프로그램 존재하는 프로그램.
  - llms.py: LangChain을 사용하여 모델 객체를 담고 있는 파일
  - main.py: 클라이언트 프로그램
  - pj.ui: QtDesigner프로그램을 사용하여 만든 UI파일
* memo.txt : 샘플 txt문서
* PdfFolders: 샘플 Pdf파일들이 존재하는 폴더
* quickSort : 샘픔 python 파일

- 다음과 같은 섹션으로 나뉨
* txt
  - txt 문서를 요약할 수 있는 섹션이다.
  - Raw File 필드에 txt 문서 원본이 표시된다.
  - summary 버튼을 누르면 요약이 실행된다.
  - Summarized 필드에 txt 문서가 요약된 내용이 표시된다.

* pdf
  - pdf 문서를 요약할 수 있는 섹션이다.
  - summary 버튼을 누르면 요약이 실행된다.
  - Summarized 필드에 txt 문서가 요약된 내용이 표시된다.

* pdfs
  - pdf문서 여러 개를 한 번에 요약할 수 있는 섹션이다.
  - pdf문서가 있는 폴더를 선택하면 모든 문서를 요약하여 표시해준다.

* pdfs query
  - pdf문서에 담겨있는 내용에 대하여 궁금한 것이 있으면 질문할 수 있는 섹션이다.
  - Query 필드에 질문할 내용을 입력하고 Query Enter를 누르면 좌측 필드에 답변이 나온다.

* code summary
  - code 입력란에 코드를 작성하면 해당 코드의 작업을 설명하는 주석을 생성한다.
  - 요약 필드에 주석과 코드가 함께 출력된다.


[설명은 여기서](INFORMATION.md)