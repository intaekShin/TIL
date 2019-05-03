# Vue D1 190503 金曜日 memo



## 싱글 페이지 어플리케이션

```
싱글 페이지 애플리케이션(single-page application, SPA, 스파)은 서버로부터 완전한 새로운 페이지를 불러오지 않고 현재의 페이지를 ``동적으로 다시 작성함``으로써 사용자와 소통하는 웹 애플리케이션이나 웹사이트를 말한다. 이러한 접근은 연속되는 페이지들 간의 사용자 경험의 간섭을 막아주고 애플리케이션이 더 데스크톱 애플리케이션처럼 동작하도록 만들어준다. SPA에서 HTML, 자바스크립트, CSS 등 필요한 모든 코드는 하나의 페이지로 불러오거나,[1] 적절한 자원들을 동적으로 불러들여서 필요하면 문서에 추가하는데, 보통 사용자의 동작에 응답하게 되는 방식이다. 문서는 프로세스 중 어떠한 지점에서도 다시 불러들이지 않으며 다른 문서로 제어권을 넘기지 않으나, 위치 해시나 HTML5 히스토리 API를 사용하여 애플리케이션 안에서 개개의 논리 문서의 인식 및 탐색을 제공할 수 있다.[2] 싱글 페이지 애플리케이션과의 소통은 뒷편에 있는 웹 서버와의 동적인 통신을 수반하기도 한다.
```

* 목적 : 자연스러운 유저 경험을 위해 만들어짐.
* [빈도수 低] 코드 양이 너무 많아져서 항상 쓰이는 건 아니다.
  - 유지 보수가 복잡해진다.

##### SPA framework - 검색

그중에 vue.js 를 배운다.

## Vue

angular 개발자 출신이 Vue를 만들었다.

react의 장점을 착안해서 만들었다.

##### 시작하기

```html
<head>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>

```

* CDN : 콘첸츠 전송 네트워크 - 설치를 한 적이 없는데 사용할 수 있다. 인터넷을 통해서 불러온 다음 사용하기 때문이다.
* 어글리파이 : 가독성을 의도적으로 낮춰서 다른사람이 알아보기 어렵게 하고 용량을 줄여 최적화 하는데에도 도움을 준다.

##### 맨 첫장 : 동기화, 연결하기

```html
<body>
    <div id = "app">
        {{ message }}
    </div>

    <script>
        const app = new Vue({
            el: '#app', // el = element 의 약자 , 이 코드는 동기화가 된다는 뜻. 
            data : {
                message: 'Hello, Vue!',
            },
        })
    </script>
</body>
```

![vue시작하기](C:\Users\student\TIL\vue\vue시작하기.PNG)

Vue의 장점: javascript를 통해서 script부분만 바꾸면 실제 페이지 내용이 바뀐다.

https://github.com/vuejs/vue-devtools

##### 확장프로그램: devtools

개발자 도구를 켜면 나온다.
인스턴스의 내용을 확인할 수 있다.

설치 후 확장 프로그램 관리 - 파일URL에 대한 액세스 허용 활성화 - 개발자 도구 맨 끝 Vue 활성화됨.

#### MVC(MTV)

[중간 배경지식 설명]

M - Model(models.py) : 데이터가 저장 되는 곳

V - View(Template.html) : 사용자가 보는 화면 구성

C - Controller(views.py) : 위 두 구성요소를 제어

### MVVM

Vue의 구성요소

M - Model : 현재 수업 중 아직 없음(추후 django를 쓸 수도 있고 여러가지 방법이 있다.)

V - View(HTML) : 사용자가 보는 화면 구성

VM - View-Model(Vue) : 데이터가 오고 가는 것을 중간에 제어. (Data Binding)



뷰 인스턴스 속성에 접근하고 싶으면 $를 앞에 붙여요.

원래라면 app.$data.message 가 맞는데 app.message 로 축약해서 쓸 수 있도록 마련했어요.

this : 자기 자신을 지칭. 내부 를 호출할 때 사용해요.





```javascript
<div id = "app">    <!-- app으로 지정된 곳 안에 작성.-->
    {{ message }} - {{ count }}
</div>


<script>
        const app = new Vue({
            el: '#app', // el = element 의 약자 , 어디에를 뜻함.
            data : { // 무엇을
                message: 'Hello, Vue!',
                count: 0, 
            },
            methods: { // 어떻게
                // this.message 
                plus: function(){   // function은 익명 함수.
                    this.count++
                }
            }
        })
</script>
```



```
# console in 0503.html
> app.plus()
undefined
1이 증가.
filter components - Root에서 확인 가능하다.
```





#### django

```python
# 조건
{% if post.is_public %}
	{{ post }}
{% endif %}

# 반복
{% for post in posts %}
	{{ post }}
{% endfor %}
```



#### Vue Directive(디렉티브)
```html
<!-- 조건 -->
<p v-if="post.isPublic">
    {{ post }}
</p>

<!-- 반복 -->
<ul>
    <li v-for="post in posts">
        {{ post }}
    </li>
</ul>
```

디렉티브는 지시자라는 뜻.

##### 조건문

```python
 <p v-if="checked">이건 보임.</p>
    
 console in 0503.html
> app.checked = false
false	// checked 문장이 안보이게 돼요. 숨기는 게 아니라 코드에서 사라지게 하는 거에요.
> app.checked = true
true
```



##### 반복문

````html
<body>
    <div id = "app">    <!-- app으로 지정된 곳 안에 작성.-->
        {{ message }} - {{ count }}
        <p v-if="checked">이건 보임.</p>
        <li v-for="post in posts">
            {{ post }}
        </li>
        <li v-for="info in Object.keys(student)">
            {{ info }}
        </li>
    </div>


    <script>
        const app = new Vue({
            el: '#app', // el = element 의 약자 , 어디에를 뜻함.
            data : { // 무엇을
                message: 'Hello, Vue!',
                count: 0, 
                checked: true,
                posts: ['첫 게시물', '두번째 게시물', '세번째!']
                student: {
                    name: 'nwith',
                    univ: 'KNU',
                }
            },
            methods: { // 어떻게
                // this.message 
                plus: function(){   // function은 익명 함수.
                    this.count++
                }
            }
        })
    </script>
</body>

# key값을 부르고 싶다면?
		<li v-for="info in Object.keys(student)">
            {{ info }} -{{ student[info] }}
        </li>
# key와 value 다 부르고 싶다면?
		<li v-for="info in Object.keys(student)">
            {{ info }}
        </li>
````



javascript에서는 반복문을 돌리면 value값이 나와요.(key값이 아니에요.)



##### todo.html



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        <ul>
            <li v-for="todo in todos" v-if="!todo.completed">
                {{ todo.content }}
            </li>
            <li v-else>[완료!]</li>
        </ul>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                todos: [
                    {
                        content: '점심 메뉴 고민하기',
                        completed: true,
                    },
                    {
                        content: '사다리 타기',
                        completed: false,
                    },   
                    {
                        content: '약속의 2시, 낮잠자기',
                        completed: false,
                    },   
                    {
                        content: '야자하기',
                        completed: false,
                    },
                ]
            }
        })
    </script>
</body>
</html>
```

문자열 말고 todo들이 추가적인 정보를 가질 수 있도록, 문자열이 아니라 오브젝트로 만들겠어요.

완료된 투두는 보이지 않도록 수정을 해볼게요.

```
 <li v-for="todo in todos" v-if="!todo.completed"> // 한 번 돌 때 마다 조건을 검사한다.
 // for 가 if 보다 우선순위가 높습니다.
```



##### v-on

```html
<li v-for="todo in todos" v-if="!todo.completed" v-on:click="todo.completed = true">
```

```html
2번째 방법.
<div id="app">
        <ul>
            <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
        </ul>
    </div>

<script>
        const app = new Vue({           
            methods: {
                check: function(todo){
                    todo.completed = true
                }
            },
        })
    </script>
```

###### 서로 전환되는 버튼 만들기

```html
<div id="app">
<li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
                {{ todo.content }}
            </li>
            <li v-else v-on:click="check(todo)">[완료!]{{ todo.content }}</li>
 </div>
    
<script>
methods: {
                check: function(todo){
                    todo.completed = !todo.completed
                }
            },
</script>
```







##### 이미지 올리기

api를 이용하여

v-bind: src가 붙은 태그에는 중괄호 문법을 못쓰기 때문에 v-bind를 쓴다.

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <style>
        img {
            width: 400px;
        }
    </style>
</head>
<body>
    <div id="app">
        <button v-on:click="getCatImage">MeUMeU</button>
        <div>
            <img v-bind:src="imageURL" alt="cat image">
        </div>
    </div>
    
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                imageURL: '',
            },
            methods: {
                getCatImage: function(){
                    axios.get('https://api.thecatapi.com/v1/images/search')
                        .then((response) => { // arrow function 기존 익명 함수와 미묘하게 다르다.만 여기서는 같다고 취급해봐요.
                            this.imageURL = response.data[0].url    // 실제 고양이 사진이 들어간 주소. this를 사용하기 위해 arrow function을 사용한다.
                        })
                }
            }
        })
    </script>

</body>
```





---

### 0430 workshop

* Single Page Application 
* Vue.js

---

*  Single Page Application에 대한 이해 
*  Vue 인스턴스에 대한 이해

*  다음은 Vue 인스턴스를 사용하여 렌더링한 DOM의 결과물이다.
  위와 같이 렌더링 하기 위하여 필요한 (a), (b)를 작성하여 Vue 인스턴스를 완성하시오

(a) : `{{ message }}`, (b) : `#app`

### 0501workshop

* Vue.js 
* v-bind, v-for, v-if 디렉티브

---

* 인터폴레이션과 디렉티브의 활용
* 다음과 같은 Vue 인스턴스가 있을 때, v-for와 v-if 디렉티브를 활용하여 짝수만 나타나 도록 하는 리스트를 만들어 봅시다.

```html
<div>
    <li v-for="number in numbers" v-if="number % 2 == 0">
     // or<li v-for="number in numbers" v-if="!(number % 2)">  
    	{{ number }}
    </li>
</div>
```



### 0430homework

*  Single Page Application 
*  Vue.js

1. SPA가 무엇의 약자인지 작성하고, 어떤 것을 의미하는지 간략하게 작성하시오.

   ```
   single-page application의 약자. 단 하나의 페이지로서만 작성된 것.
   
   서버로부터 완전한 새로운 페이지를 불러오지 않고 현재의 페이지를 ``동적으로 다시 작성함``으로써 사용자와 소통하는 웹 애플리케이션이나 웹사이트를 말한다.
   ```

   

   

2. 'MVVM 패턴'에서 MVVM은 무엇의 약자인지 작성하고, 그 중에서 Vuejs가 담당하는 부분은 무엇인지 간략 하게 작성하시오.

   ```
   Model-View-View-Model 의 약자.
   View-Model을 담당해서 데이터가 오고 가는 것을 중간에 제어한다.
   ```

   

   



### 0501homework

* Vue.js 
* v-bind, v-for, v-if 디렉티브

1. html 속성(attributes)에는 인터폴레이션(Interpolation)으로 값을 직접 넣지 못하기 때문에 디렉티브 ____(a)____를 사용해야 한다. 빈칸 (a)에 들어갈 디렉티브를 작성하시오.
   * 인터폴레이션(Interpolation) : 보간법
     * f string 처럼 중간 중간 에 뭐 갖다 넣는 거에요.
   * Answer : `v-bind`
2. 동일한 노드에 ____(a)____와 ____(b)____ 두 디렉티브가 함께 있다면 ____(a)____가 ____(b)____보다 높은 우선 순위를 가지며, ____(b)____는 루프가 반복될 때마다 실행됩니다. 빈칸 (a), (b)에 들어갈 디렉티브를 작성 하시오.
   (a) : `v-for` , (b): `v-if`

