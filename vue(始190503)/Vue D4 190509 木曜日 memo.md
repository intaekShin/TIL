# Vue D4 190509 木曜日 memo

## Django와 Vue의 연결

###### 기본 틀 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- Vue CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
    <div id="app">

    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                
            },
        })
    </script>
</body>
</html>
```

Axios를 이용할 예정입니다.

Axios로 요청을 보낸다??

주소로 요청을 보내고 응답을 받을 수 있습니다.

```html
<body>
    <div id="app">

    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                
            },
            methods: {
                getMusics: function(){
                    axios.get('https://playground-itshin.c9users.io/api/v1/musics') // axios를 통하여 해당 주소로 요청 보내기.
                            .then((response)=>{
                                console.log(response.data)
                            })
                },
            },
        })
    </script>
</body>
----
여기서 개발자도구를 켜서 app.getMusics()를 입력하면 오류가 뜬다.
```

![chat-vue](C:\Users\student\TIL\vue(始190503)\with-django\chat-vue.PNG)

###### 오류나는 이유.

* XMLHttpRequest 으로 접근이 되지 않았다.
* CORS정책때문에 블락됐다. Cross Origin Resource Sharing 의 약자.
* 그리고 이 헤더가 없으면 요청이 안보내져요. 정확하게 말하면 요청은 보내지는 데, 응답을 못 받는 거에요.

(나중에 정리하자...)

 이미지태그로 이미지 파일 받아오거나 링크 태그로 부트스트랩이나 뷰같은 것도 주소를 통하여 사용을 하죠
그런 태그 안에 있는 것들은 사용 가능한데 , 

* 자바스크립트 코드 내에서는 바로 웹으로 요청이 기본 설정이 막혀 있어요.
  그에 대한 응답으로 요청을 주고 받을 수 없게 되어잇거든요.
  왜? 범죄가 가능하기 때문에

* 요청이라는 게 크로스 오리진이잔하요. 정확하게 도메인이랑 매칭되느 건 아닌데 이 소스안에서 컴퓨터에서 c9에서 접근 햇잖아요. 도메인의 파일 명이 두 개 가 다르게 위치한다면 아무런 제약없이 주고 받는 게 불가해요. 
* 가능한 건, 이 허락을 해줬기 때문인거든요. 웹 자체는 자기자신이 보낸 요청이 아니라면 차단이 되는게 기본이에요.

* 그럼 궁금하신 점은 ??? ㅇ이 axios는 외부요청인데? 이건 자바스크립트안에 코드로 들어있는 요청은 불러오는 것이 가능해요. 정책이 다른 도메인간의 주고 받는 것은 스크립트안에서 불가능하다. 라고 알고 있으면 됩니다.

-

해결책 : 설정 변경. 
장고만으로는 번거롭기 때문에 
추가적인 라이브러리를 설치합니다.

`pip install django-cors-headers`

> pip 를 설치 했으므로 settings.py  에 INSTALLED_APPS 사항을 추가해유. `'corsheaders'`
>
> MIDDLEWARE 중 3번째 순서('django.middleware.common.CommonMiddleware',바로 위). `'corsheaders.middleware.CorsMiddleware',` ` 삽입.
>
> 순서가 중요한 이유는 어떠한 요청이 들어왔을 때, 거치게 되는 요청을 정하기 때문이에요.
>
> 서버가 외부에서 요청을 보내도 허락해줄꺼야 라는 내용이 'Access-Control-Allow-Origin'에 해당되요.

이제 허락 범위를 정할 수 있어요.

모든 도메인에 대해서 허락을 하려면	`CORS_ORIGIN_ALLOW_ALL = True`  을 입력해요.

반면에, 선택적으로 허락을 하려면 

```python
CORS_ORIGIN_WHITELIST = [
    'example.com',
]
```

그 후에 개발자도구 Network 탭에 가보시면

우리가 여태껏 한 요청과 응답에 대한 기록이 담겨있어요.

정상 작동시

![chat-vue2](C:\Users\student\TIL\vue(始190503)\with-django\chat-vue2.PNG)-

##### 음악 목록 나오기

```html
<div id="app">
    <ul>
        <li v-for="music in musics">
            {{ music.artist }} - {{ music.title }}
        </li>
    </ul>
</div>
```

##### 에러 나올 경우 대비

```html
<script>
methods: {
    getMusics: function(){
        axios.get('https://playground-itshin.c9users.io/api/v1/musics/') // axios를 통하여 해당 주소로 요청 보내기.
            .then((response)=>{
            this.musics = response.data
        })
            .catch((error)=>{   // error 가 났을 때
            console.log(error)
        })
    },
},
    mounted: function(){
        this.getMusics()
    },
</script>
```



id 값 대신 아티스트 이름이 나오면 좋겠죠?? 데이터 내용을 변경하는 것.
이건 Django의 몫입니다.

MusicSerializer 의 역할이 기존 데이터의 형식을 가능하게 햇어요.

```python
#serializers.py
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist',]
    변경 전    
//////////
	변경 후
class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name') //
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_name',] //
```

이러면 아티스트 네임이 뜨진 않을거에요.

```html
<li v-for="music in musics">
    {{ music.artist_name }} - {{ music.title }} // 이러면 바뀌어요.
</li>
...	아래는 나중을 위해서 미리 정리한 코드에요.
	return response.data
})
.then((musics)=>{
	this.musics = musics
})
```



in serializers.py
MusicSerializer에서

`'comment_set',]` 음악에 대한 모든 댓글들. 추가합니다.

```python
#serializers.py
// 실행순서를 고려해야해서 CommentSerializer 를 위에 올렸어요.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content',]
        

class MusicSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_name', 'comment_set',]
```



```html
<div id="app">
    <ul>
        <li v-for="music in musics">
            <div>
                {{ music.artist_name }} - {{ music.title }}
            </div>
            <ul>
                <li v-for="comment in music.comment_set">
                    {{ comment.content }}
                </li>
            </ul>
        </li>
    </ul>
</div>
```

이렇게 하면 댓글들도 잘 표시돼요.

##### 댓글 입력 설정

```html
div tag 안 comment 밑에 입력
<div>
    <input type="text" v-model="newComment">
</div>
이러면 모든 칸이 똑같이 적용 되어 제대로 된 댓글 작성이 어렵게 돼요.
지금은 각 musics object별로 꼽사리를 끼지 못했어요.
[변경 전]
//////
[변경 후]
<div>
    <input type="text" v-model="music.newComment">
</div>
....
<script>
    .then((musics)=>{
        this.musics = musics.map((music)=>{ // musics가 반복을 하고 map이 music하나를 꺼내와요.
            return { ...music, newComment: '' } // copy 용법.
        })
    })
    
   
INPUT이 따로 동작해요.
```

##### 댓글 생성

```html
<button @click="addComment(music)">+</button>
```



##### 댓글 삭제 



```javascript
{{ comment.content }}  <button @click="deleteComment(music,comment)">X</button>
....
deleteComment: function(music, comment){  // parameter에 댓글과 음악에 대한 정보를 넘겨받아요. 
    axios.delete(`https://playground-itshin.c9users.io/api/v1/musics/${music.id}/comments/${comment.id}/`)
    // 보내는 방법도, 도메인도 변경. 따로 data를 넘길 필요 없어서 추가 인자가 없어요.
        .then((response)=>{
            music.comment_set = music.comment_set.filter((c)=>{
                return c.id != comment.id
        	})
    	})
        .catch((error)=>{   // error 가 났을 때
        	console.log(error)
    	})
},
```



## 팀 프로젝트 회의





## 개인 공부

###### 미라콤 자소서 질문 목록

1. 간단한 본인 소개 및 성장과정 중 본인에게 영향을 끼친 사건 혹은 인물을 서술하시오. 
2. 미라콤의 인재상을 고려하여 당사에 지원한 사유 및 입사 후 포부를 기술하시오. 
3. 소프트웨어 직군과 관련한 경험 및 활동에 대하여 작성하시오. 

* NoSQL 데이터베이스는 전통적인 관계형 데이터베이스 보다 덜 제한적인 일관성 모델을 이용하는 데이터의 저장 및 검색을 위한 메커니즘을 제공한다. 이러한 접근에 대한 동기에는 디자인의 단순화, 수평적 확장성, 세세한 통제를 포함한다. NoSQL 데이터베이스는 단순 검색 및 추가 작업을 위한 매우 최적화된 키 값 저장 공간으로, 레이턴시와 스루풋과 관련하여 상당한 성능 이익을 내는 것이 목적이다. NoSQL 데이터베이스는 빅데이터와 실시간 웹 애플리케이션의 상업적 이용에 널리 쓰인다.

* CORS (Cross Origin Resource Sharing) 
  개요 - HTTP 요청은 기본적으로 Cross-Site HTTP Requests가 가능하다.
   다시 말하면, <img> 태그로 다른 도메인의 이미지 파일을 가져오거나, <link> 태그로 다른 도메인의 CSS를 가져오거나, <script> 태그로 다른 도메인의 JavaScript 라이브러리를 가져오는 것이 모두 가능하다.
   하지만 <script></script>로 둘러싸여 있는 `스크립트`에서 생성된 Cross-Site HTTP Requests는 `Same Origin Policy`를 적용 받기 때문에 Cross-Site HTTP Requests가 불가능하다.
   AJAX가 널리 사용되면서 <script></script>로 둘러싸여 있는 스크립트에서 생성되는 `XMLHttpRequest`에 대해서도 Cross-Site HTTP Requests가 가능해야 한다는 요구가 늘어나자 W3C에서 CORS라는 이름의 권고안이 나오게 되었다. 
* AJAX(Asynchronous JavaScript and XML,  에이잭스) : 비동기적인 웹 애플리케이션의 제작을 위해 아래와 같은 조합을 이용하는 웹 개발 기법이다.
  * 표현 정보를 위한 HTML (또는 XHTML) 과 CSS.
  * 동적인 화면 출력 및 표시 정보와의 상호작용을 위한 DOM, 자바스크립트.
  * 웹 서버와 비동기적으로 데이터를 교환하고 조작하기 위한 XML, XSLT, XMLHttpRequest.
  * 기존 기술과의 차이점: 기존의 웹 애플리케이션은 브라우저에서 폼을 채우고 이를 웹 서버로 제출(submit)을 하면 //하나의 요청으로 웹 서버는 요청된 내용에 따라서 데이터를 가공하여 //새로운 웹 페이지를 작성하고 응답으로 되돌려준다.// 이 때, 최초에 폼을 가지고 있던 페이지와 사용자가 이 폼을 채워 //결과물로서 되돌려 받은 페이지는// 일반적으로 유사한 내용을 가지고 있는 경우가 많다. 
  * 반면에 Ajax 애플리케이션은 필요한 데이터만을 웹서버에 요청해서 받은 후 클라이언트에서 데이터에 대한 처리를 할 수 있다.  
* SQL (Structured Query Language, 구조화 질의어) : `관계형 데이터베이스 관리 시스템(RDBMS)`의 `데이터를 관리하기 위해` 설계된 특수 목적의 프로그래밍 언어이다. 
* SOAP(Simple Object Access Protocol) :  일반적으로 HTTP, HTTPS, SMTP 등을 통해 XML 기반의 메시지를 컴퓨터 네트워크 상에서 교환하는 프로토콜이다. 