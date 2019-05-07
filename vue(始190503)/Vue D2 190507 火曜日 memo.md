# Vue D2 190507 火曜日 memo

##### git 설정

git config --global --list

git config --global user.name

git config --global user.email

git credentail reject

protocol==https

host=github.com

제어판 -자격 증명 관리자.

---

view js



#### v-model

두 부분이 동기화가 되어 작성되는게 v-model이라는 directive

```javascript
<div>
    <input type="text" v-model="newTodo">
</div>
        ....
      data: {
                newTodo: '',  
```







```javascript
        <div>
            <input type="text" v-model="newTodo" v-on:keyup.enter="addTodo">	// enter키를 눌렀을 때 addTodo라는 메소드를 실행하라는 event.
                ....
        methods: {
                check: function(todo){
                    todo.completed = !todo.completed
                },
                addTodo: function(){
                    this.todos.push({
                        content: this.newTodo,
                        completed: false, 
                    })
                }
            },
```

##### newTodo 추가하면서 빈칸만들기

newTodo란 값에 빈 문자열을 넣는 논리 사용해요~.

```javascript
   methods: {
                addTodo: function(){
                    this.todos.push({
                        content: this.newTodo,
                        completed: false, 
                    })
                    this.newTodo = ""
```

##### newTodo 마우스 버튼 만들기

```javascript
        <div>
            <button v-on:click="addTodo">+</button>
        </div>
```



##### 삭제버튼 만들기

완료된 친구들만 삭제할 거에요.

핵심 자바스크립트 문법은 filter라는 친구에요.

완료되지 않은 Todo들을 모아서 새로 리턴하는 논리를 사용해요! :)



```javascript
<footer>
    <button v-on:click="clearCompleted">Clear Completed</button>
</footer>

......

// 핵심은 '.filter'의 사용!
                clearCompleted: function(){
                    const notCompletedTodos = this.todos.filter((todo)=>{
                        return !todo.completed
                    }) // [{...},{...}]
                    this.todos = notCompletedTodos
                },
```



##### 완료할 때 체크박스와 취소선 만들기

```javascript
1. 체크 박스
<!-- v-if="!todo.completed" v-on:click="check(todo)" -->            

<!-- <li v-else v-on:click="check(todo)">[완료!]{{ todo.content }}</li> --> // 이 친구 삭제, 주석 처리.
            ....
            
            <li v-for="todo in todos" >
                <input type="checkbox" v-model="todo.completed"> // model로 동기화 되었기 때문에 처음에 체크가 됨.
                <span>{{ todo.content }}</span>
            </li>  // 로 변경.
```

 취소선은 CSS 를 이용해요.

삼항 연산자가 들어가요!

```javascript
2. 취소선 head와 script사이.
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
	<style>
        .completed {
            text-decoration: line-through;
            opacity: 0.6;
        }
    </style>
</head>
....
                <span v-bind class="todo.completed ? 'completed':'''">{{ todo.content }}</span>
// 조건문 ? 참값:거짓값 : 삼항 연산자


다른 방법도 있다.
"{completed: todo.completed}" // javascipt object 형태
// 뒷 조건이 만족하면 앞 값이 올 수 있게 하는 명령어이고 , 를 통해 복수의 명령어를 입력할 수 있다.
```

##### 취소선 꾸미기 

```javascript
<div v-bind:style="{color: 'red', fontSize: '30px'}">
                <span>Red Text, 30px</span>
            </div>
```





##### 조건별 보여주기 

```javascript
<li v-for="todo in todosByStatus()" >
    ...
methods: {
    todosByStatus: function(){
                        if (this.status === 'active') {
                            return this.todos.filter((todo)=>{
                                return !todo.completed
                            })
                        }

                        if (this.status === 'completed') {
                            return this.todos.filter((todo)=>{
                                return todo.completed
                            })
                        }

                        return this.todos
                    },
}
```

##### selected 박스 만들기

```javascript
<select v-model="status">
    <option value="all" selected>All</option> // 첫 화면에 이게 선택된다는 뜻.
    <option value="active">Active</option>
    <option value="completed">Complete~d</option>
</select>

selected 는 v-model에 의해 무시됨.~!! models에 all이 내장되어있음.
```



##### key값 부여하기

각 항목별로 구별할 수 있는 key값을 부여해야 의도치 않은 오류를 면할 수 있어요~.

중복되지 않은 id값을 부여할 때 가장 좋은 것은 현재시간을 주는 것이에요.

* Date.now() : 현재 시간을 입력.

```javascript
<li v-for="todo in todosByStatus()" v-bind:key="todo.id" >
    ...
		data: {
                todos: [
                    {
                        id : 1,
                    } (이하 동문)
	...
addTodo: function(){
                    this.todos.push({
                        id: Date.now(),
```

v-for 를 쓸 때, v-bind를 함께 써달라는 권유가 있어유~.





##### $는 속성을 불러올 수 있다.

v-on = @

...(후략)....





----

#### 개인적 공부 

콜백 함수

API

* DOM (Document Object Model) : 문서 객체 모델
  * HTML, XML 문서의 프로그래밍 interface이다. 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 돕는다.
  * 





### 0502 workshop

* Vue.js 

* v-bind, v-on 디렉티브

* 이벤트 핸들링의 이해 및 활용 

* Computed와 Watch의 활용

*  v-on 디렉티브를 활용하여, 다음과 같이 ‘+1’ 버튼을 누르면 숫자가 하나씩 증가하는 Counter 앱을 만들어 봅시다.

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
          <button v-on:click="counter++">+1</button>
          <span>Counter: {{ counter }}</span>
      </div>
      <script>
          const app = new Vue({
              el: '#app',
              data: {
                  counter: 0,
              }
          })
      </script>
  </body>
  </html>
  ```

  

### 0503 workshop

* Vue.js 

* v-bind, v-model 디렉티브

* 양방향 데이터 바인딩의 이해 및 활용

* v-bind와 v-model 디렉티브를 활용하여, 다음와 같이 'Go!' 링크를 누르면 입력 창에 작성한 URL로 가도록 하는 '주소가 변하는 링크'를 만들어 봅시다.

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
          <input type="text" v-model="url">
          <a v-bind:href="url">Go!</a>
      </div>
      <script>
          const app = new Vue({
              el: '#app',
              data: {
                  url: '',
              }
          })
      </script>
  </body>
  </html>
  ```

  

### 0502 homework

* v-bind, v-on 디렉티브 
* Computed와 Watch 속성

1. 빈칸 (a) 들어갈 v-bind 디렉티브의 약어를 작성하시오.
   A. `:href`
2. 빈칸 (a)에 들어갈 v-on 디렉티브의 약어를 작성하시오.
   A. `@click`
3. computed 속성과 watch 속성에 대하여 간략하게 설명하고, 이 둘의 차이점에 대해 작성하시오.
   A. `computed속성은 계산해야 하는 목표 데이터를 정의하는 방식으로 선언형 프로그래밍 방식,
   watch속성은 감시할 데이터를 지정하고 그 데이터가 바뀌면 함수를 실행하라는 방식.`

### 0503 homework

* 양방향 데이터 바인딩 
* v-model 디렉티브

1. v-model 디렉티브는 input, textarea, select와 같은 엘리먼트들과 ____(a)____을 생성합니다. 빈칸 (a)에 들어 갈 말을 작성하시오.
   양방향 데이터 바인딩 : 위에께 수정해도 아랫게 적용되고 반대방향도 적용됨.
2. v-model 디렉티브는 엘리먼트의 종류에 따라 인스턴스의 속성을 업데이트하는 데이터의 타입이 다릅니다. 아래의 엘리먼트들이 기본적으로 어떠한 데이터 타입으로 인스턴스의 속성을 업데이트 하는지 https://kr.vuejs.org/v2/guide/forms.html를 참고하여 작성하시오.

- input - `문자열`
- textarea - `문자열`
- 단일 checkbox -  `boolean`
- 다중 checkbox -  `배열`
- radio - `문자열`
- 단일 select - `문자열`
- 다중 select - `배열`

```
- input: 문자열 
-  textarea: 문자열 
- 단일 checkbox : Boolean 
- 다중 checkbox : 선택된 요소들의 value값이 들어가있는 배열의 형태로 나타냄 
- radio: 선택된 값을 문자열의 형태로 나타냄 
- 단일 select: 선택된 하나의 값을 문자열의 형태로 나타냄 
- 다중 select: 선택된 여러개의 값을 배열의 형태로 나타냄
```

-----

```javascript
constcomics = {
    'DC': ['Aquaman', 'SHAZAM'],
    'Marvel': ['Captain Marvel','Avengers']};
constmagazines = null;
constbookShop = {
    comics,
    magazines,
};
```

키값이랑 변수명이랑 같으면 축약해서 쓸 수 있다.