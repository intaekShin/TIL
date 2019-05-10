# final D1 190510 金曜日 memo

###### C9 내용물 옮기기, cmd를 통해 django 작업하기.

우분투와 c9은 다르기 때문에 설명이 필요해요.

```
mkdir django
cd django
python -V
Python 3.5.3
mkdir api
cd api
```

파이썬 탈출을 못하니 고칠게요.

```
$ cd ~

student@DESKTOP MINGW64 ~
$ code .bash_profile
key 값은 삭제.
```

```
# .bash_profile
alias python='winpty python' // 단축을 만들어준것.
저장 후 git bash 끄고 다시켜기
///
$ python
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>	// 제대로 작동하는 것.

```

python 에 내장되어있는 가상환경을 이용해서 설치를 해야 되요.

```bash
다시 api폴더로 돌아가서 
$ python -m venv api-venv // 가상환경 설치
$ ls				// 확인이 된것.
api-venv/
$ source api-venv/Scripts/activate
/// 수업시간엔 파이썬 버전 문제로 ㅠㅠ 오류났어요.
그래서 git bash는 포기하고 cmd로 갈아탈게요.
```

CMD에서 프로젝트 진행할 때!

```cmd
dir
cd api 까지 이동 하신 후
api-venv\Scripts\activate.bat
pip install django
django-admin startproject api .
python manage.py runserver
웹 브라우저에 http://127.0.0.1:8000 은 자기자신을 지칭. 
또는 localhost:8000 을 입력하면 서버에 입장해요.
```



## Vue SPA -11 Project

##### 프로젝트 환경 설정(준비)

10project인 API 서버 구축 편을 그대로 가져와 사용해도 무방합니다. 

제출기한 : 화요일 넘어가는 월요일 자정까지.

매체를 사용하려면 git clone한 후 가상환경 설정해야한다.

studio code에서 cmd 사용하는 법.

ctrl + shift + p

shell

command prompt

ctrl + shift + `

---

git clone https://lab.ssafy.com/itShin2121/project10.git [project10 repo(저장소) 주소]

cd project10		// 작업 위치 이동

python -m venv api-venv		// 이러면 api-venv 가 생김.

사실 가상환경 폴더는 git에 올라가면 안되므로 .gitignore 파일을 만들게요.

```.gitignore
# .gitignore
api-venv
```

api-venv\Scripts\activate			// 가상환경 활성화.

예전 프로젝트의 Django version 이 2.1.8 이기 때문에 pip 로 설치 버전도 동일해야 해요.

1. pip install django==2.1.8
2. pip install djangorestframework
3. pip install django-rest-swagger

python manage.py runserver       // 서버 작동.

서버위치는 다르지만 서버가 돌아가는 작동원리는 똑같기 때문에 개발하는데 무방해요.

---



하나는 CORS를 설치하는 것! 또는 장고 안에 넣는 것. 두 가지 방법 중 하나를 택한 후 진행하세요.

movies/views.py 

```python
def index(request):
    return render(request, 'index.html')
```

urls.py

```python
urlpatterns = [
    path('', views.index),
```

movies 에서 templates 폴더를 생성 후 index.html 생성

```html
# index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Vue!</h1>
</body>
</html>
```







----

###### Studio Code 에서 Tab size 변경

Tab size 4  , Indent Using Tabs,  `4` click.

###### Template.zip 활용법

압축 풀기 후 index.html 파일을 movies에 바꿔치기 합니다.

movies안에 새 폴더 static 만들기.

static 폴더에 ??

{% static '' %} 사용한.

load static

장고와 뷰는 {{ }} 중괄호 2개 표기가 겹친다.

delimiters: ['[[', '']]'], 를 쓰면 뷰는 대괄호 2개를 쓰면 됩니다.

app.js 에서

axios.get(`/api/v1/genres`) 수정 들어간다. 

[여기까지가 황준우쌤이 말씀해주신 환경설정방법]

---

[내가 프로젝트를 진행하면서 배우게 된 점]

`html과 js의 Vue instance를 연결하는 법`

```html
# index.html
<div id="app">		// app이란 이름의 id를 가진 문서와 연결한다.
</div>
```

```django
<script src="{% static './app.js' %}"></script>		// static folder의 app.js를 부른다. 
src는 뭐지?
```

```javascript
const app = new Vue({
    el: "#app",			// Vue el(ement) 이고 id가 app이라고 명명한다.??(확실치 않음)
});

// #은 id를 뜻하는 기호. .(dot)은 class를 뜻하는 기호.
```

`axios를 이용하여 movies를 받아오는 법`

```javascript
const app = new Vue({
    data: {
        movies: [],
    },
    
    created: function () {
        axios.get(`/api/v1/movies`)		// axios라이브러리를 이용하여 json파일을 받아와요.
        	.then(res => this.movies = res.data)	//그런다음 this.movies는 data.movies를 지칭하는 데, 여기에 res.data를 담는다.
    }
})

```



## 개인 공부

* Git: 분산 소스 버전 관리 시스템(Distributed VCS)으로서 서버를 분산시켜 구축할 수 있다.

  * [반대 개념] Subversion(SVN): 중앙 서버에서 모든 소스 코드를 보관 관리하는 시스템. 

  * Git은 개발자의 시스템에 있는 복사본 디렉터리를 하나의 저장소 서버로 삼을 수 있다.

  * 분기된 저장소를 로컬에 두었기 때문에 자연스럽게 중앙 서버의 속도에 영향을 덜 받게 된다.

  * <https://terms.naver.com/entry.nhn?docId=4125964&cid=59321&categoryId=59321>

  * Quick Start

    1. 기본 환경 설정(심호흡하고)

       ```linux
       $ git config --global user.name 'name'
       $ git config --global user.email 'id@domain'
       ```

       

    2. 소스 다운로드(내려받고)

    3. 저장소 생성(만들고)

    4. 저장소 이력보기(살펴보고)

    5. 저장소 공유(나눈다!)

    6. Git 호스팅 서비스(초대하면 더 많이 오겠지?)

* Linux: 유닉스라는 운영 체계를 개인용 컴퓨터에서도 작동할 수 있게 만든 운영 체계.
  인터넷을 통해 프로그램 소스 코드를 완전 무료로 공개하여 사용자는 원하는 대로 특정 기능을 추가할 수 있을 뿐만 아니라, 어느 플랫폼에도 포팅(??)이 가능하다.
* 소스 코드: 원시코드라고도 한다. 컴퓨터의 소프트웨어를 개발할 때 그 안에 들어가는 모든 동작의 코드를 총체적으로 일컫는 말.
  * <https://terms.naver.com/entry.nhn?docId=3597396&cid=58598&categoryId=59316>
* Diff: 두 개의 파일 간 차이에 대한 정보를 출력하는 파일 비교 유틸리티이다.
  일반적으로 하나의 파일 버전과 동일한 파일의 다른 버전 간의 변경 사항을 보여주는 데 쓰인다.
  * 유틸리티(utility): 컴퓨터 이용에 도움이 되는 각종 소프트웨어.
  * <https://ko.wikipedia.org/wiki/Diff>
* pip: Python Package Installer 의 약자
* 需要 : 어떤 재화나 용역을 일정한 가격으로 사려고 하는 욕구.
* 財貨: 사람이 바라는 바를 충족시켜 주는 모든 물건.
* 仕樣 : 설계 구조. (=specifications)
* REST: 웹 기반 아키텍처 로서 확장성 생성 언어(XML) 파일로 된 웹 페이지를 읽어 원하는 정보를 수집하는 기능.
* Notation : 표기법
* XML: 확장성 생성 언어.(extensible markup language)
  인간과 기계가 모두 이해할 수 있는 텍스트 형태로 마크업 포맷을 정의하기 위한 메타 언어.
  인터넷 환경에 적합하도록 간결성, 보편성, 활용성에 중점을 두고 설계되었다.
* HTTP: 하이퍼텍스트 전송 규약.
* SOAP: 단순 객체 접근 프로토콜
* 도메인(domain):  숫자로 이루어진 인터넷상의 컴퓨터 주소를 알기 쉬운 영문으로 표현한 것.
  시스템, 조직, 조직의 종류, 국가 이름 순으로 구분된다.
  도메인 이름은 최상위 도메인과 서브도메인, 호스트 이름 등으로 계층적으로 구성된다.
  최상위 도메인은 '국가'를 의미.
  DNS(Domain Name System)은 도메인 이름을 IP주소로 변환하는 역할을 한다.
* 포트(port): 모뎀과 컴퓨터 사이에 데이터를 주고받을 수 있는 통로.
* 모뎀(MODEM): 아날로그 신호의 통신 회선인 전화선을 이용하여 디지털 통신 장비와 통신할 때 디지털 신호를 아날로그 신호로 변화시켜 주는 것을 변조(modulation)라고 하고, 그 반대의 경우를 복조(demodulation)라고 한다. 모뎀을 변복조기라고도 한다.
* axios(악시오스): axios는 현재 가장 성공적인 HTTP 클라이언트 라이브러리 중 하나입니다.
* **Ajax**(**A**synchronous [**J**avaScript](https://ko.wikipedia.org/wiki/자바스크립트) **a**nd [**X**ML](https://ko.wikipedia.org/wiki/XML), 에이잭스): 비동기적인 [웹 애플리케이션](https://ko.wikipedia.org/wiki/웹_애플리케이션)의 제작을 위해 아래와 같은 **조합**을 이용하는 [웹](https://ko.wikipedia.org/wiki/월드_와이드_웹) 개발 기법이다.(이하 생략)
  * 함께 사용하는 기술의 묶음을 지칭함.
* DOM(Document Object Model) : 문서 객체 모델은 객체 지향 모델로써 구조화된 문서를 표현하는 형식이다.
  플랫폼/언어 중립적으로 구조화된 문서를 표현하는 W3C의 공식 문서이다. 
  W3C가 표준화한 여러 개의 API의 기반이 된다.
  동적으로 문서의 내용, 구조, 스타일에 접근하고 변경하는 수단이었다.
* RSS(RDF Site Summary)
* RDF: 자원 기술 개념
* CLI: (Common Language Infrastructure) 공통 언어 기반. 단지 규격일뿐이다. 
* CSS(Cascading Style Sheets): 마크업 언어가 실제 표시되는 방법을 기술하는 언어. 레이아웃과 스타일을 정의할 때의 자유도가 높다. 
* 마크업 언어: 태그 등을 이용하여 문서나 데이터의 구조를 명기하는 언어의 한 가지이다.
* 시맨틱 태그: 
  * <https://maro1992.blog.me/221279119149>