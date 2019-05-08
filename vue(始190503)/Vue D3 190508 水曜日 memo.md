# Vue D3 190508 水曜日 memo

##### Vue 과목평가 리뷰

1. block 안에 let을 선언했기 때문에 block을 벗어나면 존재하지 않는 변수가 되어 오류가 발생한다.
2. o.= 2개는 값만 비교해요. = 3개는 값뿐만 아니라 타입도 비교해요. 답은 0 == []
3. array, help 를 묻는 문제였어요(?)
4. o.shift()는 제일 왼쪽에 있는 것을 빼는 거에요.
   pop()은 무슨 수가 들어가든 마지막 값을 빼는 거에요.
5. JS는 get이란 명령어가 없어요.
6. o. speed를 묻는 문제에요. 답은 [{speed :10}, {speed :25} ,speed:5}] 에요.
7. o. keypress는 누르고있는 동안 발생하는거에요.
8. 쪼갠 함수 속 callback, filter를 묻는 문제에요. --- 공부할 부분!!
   [4, 5, 4] 가 답이에요. 
9. 답은 addEvenetListener 두번째 인자로 들어가는 함수를 arrow function....(후략)
10. 답은 axios를 이용하여 여러코드를 동시에 실행할 수 있는 이유는 javascript가 비동기로 동작하기 때문이다.(로 수정해야 합니다.)
11. o.에러가 발생한 이유는 배열이나 문자열은 값이 변경해도 괜찮지만(다른 것을 참조하기 때문), const는 재선언, 재할당이 불가능하다. 하지만, 숫자의 경우 재할당될 수 없기에 오류가 난다.
12. 답은 typeof null === 'null'. object type입니다. 그래서 틀린 문항이다.
13. 답은 18. string 3개짜리이기 때문에 6*3으로 계산한다.
14. o.답은 7.  파라미터로 함수를 넘겨줄 수 있는 개념이 들어간 것.
15. 답은 a() === typeof c. 이 문제는 type 비교하는 문제입니다.
16. o. v-for, v-if 를 묻는 문제에요. 답은 124578.
17. o. 답은 post.content. data로 시작하지 않아요.
18. 답은 V-HTML. 안에 H1태그가 있기 때문에 적용하려면 이 명령어를 쓴다.
19. 답은< img v-bind:src ="imageUrl"> 중간에 인터폴레이션  쓸 수 없어요.
20. o.답은 {{ const number =1 }}. 인터폴레이션 안에 쓸 수 있는 것은 딱 결과가 찍히는 것만 입력이 가능한거에요.
    선언문은 사용할 수 없어요.
21. o.답은 v-on:click 혹은 @click. 
22. 답은 app.$el. 엘리먼트 가져올려면 달라만 되요~!
23. o. 답은 v-model
24. o. 답은 watch.
25. o. 답은 v-if 는 조건문을 만족할 경우에만 렌더링되고, 디렉티브 v-show는 조건과 관계없이 항상 렌더링된다.







## firebase

도구 중 하나. 구글 계정을 이용.

#### firebase settings

새 프로젝트 생성 후 개발-Database 메뉴에 들어가요.

우리는 Realtime Database 가 가벼우니까 사용할게요.

테스트 모드로 개발할게요.

![realtimedatabase1](C:\Users\student\TIL\vue(始190503)\realtimedatabase1.PNG)

밑에 주소가 나중에 유용하게 쓰일 거에요.

파이어 베이스를 사용하기 위해서 스크립트 몇 개를 추가를 해야 된대요.

<https://firebase.google.com/docs/web/setup/?hl=ko>

위 링크에 들어간후 웹 가이드에서 앱에 Firebase추가 항목을 찾아 참고하세요.

```html
<script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
<script>
  // Initialize Firebase
  // TODO: Replace with your project's customized code snippet
  var config = {
    apiKey: "<API_KEY>",
    authDomain: "<PROJECT_ID>.firebaseapp.com",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    projectId: "<PROJECT_ID>",
    storageBucket: "<BUCKET>.appspot.com",
    messagingSenderId: "<SENDER_ID>",
  };
  firebase.initializeApp(config);
</script>

storageBucket: "<BUCKET>.appspot.com",
messagingSenderId: "<SENDER_ID>", 
    // 이 중 위 2개는 필요없어요. 삭제합니다.
    
    
<DATABASE_NAME>, <PROJECT_ID> 에 프로젝트 ID인 vue-todo-c6852 를 입력해요.
<API_KEY> 에 웹 API키인 AIzaSyDpDsBIaBGezsleOkiecXEGymfXXv53ick를 입력해요.
[  웹 API 키 받는 링크  ]      
https://console.firebase.google.com/project/vue-todo-c6852/settings/general/
```

<https://github.com/vuejs/vuefire>

* Vue fire
  *  좀 더 쉽게 사용하게끔 만드는 도구.
  * Table에서 Vuefire 클릭 - Firebase Realtime database에서 v1 instead 클릭 - Installation 항목에서 아래 코드 복사!

<https://github.com/vuejs/vuefire/tree/v1>

```html
<!-- VueFire -->
    <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
```



우리가 불러왔었던 firebase의 객체를 생성해야 돼요.

```javascript
<script>
const database = firebase.database()
						.....


firebase: {
                todos: database.ref('messages'),
            },
                
                
						.....

addTodo: function(){
                    this.$firebaseRefs.todos.push({
                        
                        .....
                        

```

실제로는 하나의 JSON파일입니다.

이러한 형식을 NoSQL이라고 불러요~.

현재까지는 체크된 게 저장되지 않아요~.

뷰 인스턴스내에서만 적용이 되지만 데이터베이스에 바로바로 적용되지 않았기 때문이에요.

###### 체크박스 데이터베이스에 저장.

```javascript
<input type="checkbox" v-model="todo.completed" v-on:change="updateTodo(todo)"> // 바뀔때마다 업데이트 투두 기능 실현하고 파라미터로 (todo) 를 사용.
							.....

methods: {
    updateTodo: function(todo){
        // todo = {'content': 'hi', completed: true}
        // {'content': 'hi', completed: true} 괄호 버리기
        const newTodo = { ...todo } // todo가 오게 될텐데 이 ... 은 스프레드오버레이터, spread operator. 복사본을 만들기 위해서(deepcopy의 역할)
        delete newTodo['.key']  // 알맹이?? 이해 안됨.
        this.$firebaseRefs.todos.child(todo['.key']).set(newTodo) // firebase vuefire 의 사용법 중 하나. 업데이트 하겠다. 앞의 것을 뒤의 것으로.
    },
        
       // 이 세줄로는 실행이 안 되겠죠? 체크박스 표시가 바뀔때마다 업데이트 시키면 되겠죠??
```

##### clearcompleted 수정

완료한 것들을 따로 데이터 베이스에 보내야 합니다.

```javascript
clearCompleted: function(){
    const completedTodos = this.todos.filter((todo)=>{
        return todo.completed
    }) // [{...},{...}]

    completedTodos.forEach((todo)=>{
        this.$firebaseRefs.todos.child(todo['.key']).remove()
    })
},
```



###### create chat folder and create index.html

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- Vue CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- firebase -->
    <script src="https://www.gstatic.com/firebasejs/5.9.1/firebase.js"></script>
    <!-- VueFire -->
    <script src="https://unpkg.com/vuefire/dist/vuefire.js"></script>
</head>
<body>
    <div id="app">
        <ul>
            <li v-for="message in messages">
                {{ message.content }}
            </li>
        </ul>
        <input type="text" v-model="newMessage" v-on:keyup.enter="addMessage">
        <button v-on:click="addMessage">></button>
    </div>

    <script>
        const app = new Vue({
            el: '#app',
            data: {
                messages: [],
                newMessage: '',
            },
            methods: {
                addMessage: function(){
                    this.messages.push({
                        content: this.newMessage
                    })
                    this.newMessage = ''
                }
            }
        })
    </script>
    
</body>
</html>
```



##### 빈칸 입력 안되게 끔 하는 거.

```javascript
입력 예정..
```



* trim - 양 옆에 공백을 날려준다.



Authentication - 로그인 방법- 이메일/비밀번호: 사용설정. 

```javascript
const auth = firebase.auth()
const ui = new firebaseui.auth.AuthUI(auth)


```

가이드 - 인증 - 웹 - 기본UI로 로그인

이메일 주소 및 비밀번호 2번

+로그인 callbacks:{}





##### 채팅창과 로그인창 중 하나만 띄우기

##### 로그인 성공시 명령어 작성

authResult.user에 대해 담겨있다.

```javascript
callbacks: {
    signInSuccessWithAuthResult: (authResult, redirectUrl) => {
        // User successfully signed in.
        // Return type determines whether we continue the redirect automatically
        // or whether we leave that to developer to handle.
            this.currentUser.uid = authResult.user.uid
            this.currentUser.email = authResult.user.email
            this.currentUser.name = authResult.user.displayName
            return false;
                                
// arrowfunction 으로 바꿔서 this가 app을 가리키게 됨.
// false로 바꾸면 다른 페이지로 이동시키는 대신에 로그인 창을 숨기게 됨.
```

로그인된 유저의 정보는 지금 날아가게끔 설정되어 있어서 새로고침하면 다시 로그인 해야 되요.



##### 로그인 유지시키기

```javascript
mounted: function(){ // mounted 는 연결이 되고 난 직후,
    // 로그인 된 상태인지 검사하는 코드를 작성.
    auth.onAuthStateChanged((user)=>{
        if (user) {
            this.currentUser.uid = user.uid
            this.currentUser.email = user.email
            this.currentUser.name = user.displayName
        } else {
            this.initUi()
        }
    })
}    
```



##### 로그아웃

```javascript
<body>
    <div id="app">
        <div v-if="currentUser.uid">
            <div>
                <span>Hi, {{ currnetUser.name }}</span>
                <button @click="logout">로그아웃</button>
            </div>

....
logout: function(){
    // 1. currentUser 초기화
    this.currentUser = {
        uid: '',
        email: '',
        name: '',
    }
    // 2. firebase auth한테 로그아웃 알리기
    auth.signOut().then(()=>{

    }).catch((error)=>{

    })
},
    

```

```javascript
 <b>{{ message.username }}</b> {{ message.content }}

...

 username: this.currnetUser.name,
```

현재는 다른사람과 채팅하기 어렵습니다.

##### 호스팅 서비스

누구든지 채팅창에 올 수 있도록 할게요.

create chat folder and move index.html in chat folder

cmd 명령 프롬프트 실행후

move chat folder

npm 확인( node)

npm install -g firebase-tools

firebase login

firebase init

yes, database, hosting 

vue-chat

? Configure as a single-page app (rewrite all urls to /index.html)? Yes





```json
{
  "rules": {
    "message": {
      ".read": "auth != null",
      ".write": "auth != null",
    }
  }
}
login을 한 상태에만 메세지를 읽고 쓸 수 있다. 오타 한치 허용치 않는다.
```

firebase deploy : 변경사항 반영

추후 html 에 변경하면 chat 폴더에 가서 다시 firebase deploy 명령하면 적용된다. 

## 개인적 공부

* API
  * application programming interface의 약자에요.
  * 운영체제(시스템 프로그램)와 응용프로그램 사이의 통신에 사용되는 언어나 메세지 형식을 말해요.
  * 프로그래머를 위한 (운영체제나 프로그램의) 인터페이스에요.
  * 좋은 API는 모든 building block을 제공함으로써 프로그램 개발을 쉽게 해줘요.
  * 사용자 입장에서도 같은 API를 사용한 프로그램은 비슷한 인터페이스를 가지기 때문에 새로운 프로그램의 사용법을 배우기가 쉬워져요.
  * <https://terms.naver.com/entry.nhn?docId=1179553&cid=40942&categoryId=32837>
* 기계학습(Machine Learning)
  * 인공지능의 한 분야에요.
  * 1959년 아서사무엘이 "컴퓨터에 명시적인 프로그램 없이 배울 수 있는 능력을 부여하는 연구 분야"라고 정의했어요.
  * ?? Supervised/Unsupervised Learning
  * 사물인터넷이 활성화되면 가장 두드러지는 현상은 엄청난 데이터가 발생하게 되요.
  * 딥러닝이 비약적인 발전을 이루게 된 것은 학습을 위한 데이터들을 비지도 학습(Unsupervised Learning)을 통해 전처리하면 신경망이 깊어져도 학습이 잘 된다는 것을 발견하였기 때문이죠.
  * 이미지 인식, 음성 인식, 번역 드으이 분야에서 현저한 성과가 이루어지고 있어요.
* 踏步
* 約款
* 誘發
* 