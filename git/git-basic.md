# Git & GitHub 

## Git에 내 정보 설정



* `git config --global user.name 'intaek Shin'` : 이름 설정.

* `git config --global user.email 'sit921212@gmail.com'` : 이메일 설정.

* `git config --global --list` : 정보설정 확인

# Git repo를 처음 생성한 경우



* `git init` : git 초기화. 지금 폴더를 git으로 관리하겠다!

* `rm -rf .git` : 잘못된 위치에 `git init`을 한 경우, 삭제하는 법.

* `git remote add origin` 주소 : 원격 저장소(remote repository) 주소 등록
  * `git remote set-url origin` 주소 : 원격 저장소 수정

# Git Repo clone한 경우

* `git clone` 주소  [폴더 이름] : 이 주소로 부터 내용 내려받기
  * 이 경우에는 git init, git remote add origin 주소를 하지 않아도 이미 다 되어있다.

## Git Commit & Push

* `git status` : 현재 폴더의 git의 상태 확인
* `git add .` : 현재 폴더의 변경사항들을 commit하기 위하여 준비. ‘’.‘’대신에 특정 파일 이름도 가능.
* `git commit -m ‘D04 | 190107 AM | Git & CLI’` :  commit, 변경 사항 저장. 메세지는  자유롭게 작성 가능.
* `git push -u origin master` : remote로 등록된 원격저장소에 commit한 것들 올리기
  * 이 후에는 `git push`만 입력해도 동작합니다. `git clone`을 한 경우에도 해당합니다.
  * 이 컴퓨터에서 최초 push인 경우, 로그인 창이 뜨며 로그인을 해줍니다.

## Git Pull

* `git pull` : GitHub에 올라가 있는 내용들, 즉 commit들을 내려받는 것.
* 아침에 오자마자 `git pull` 한번 하고 시작합시다!



## Git & GitHub 재설정

```bash
# Git 이름, 이메일 재설정
git config --global user.name 'Intaek Shin'
git config --global user.email 'sit921212@gmail.com'

#GitHub 로그인 정보 초기화
git credential reject
protocol=https
host=github.com


```



# CLI

- CLI : Command Line Interface
- GUI : Graphic User Interface 
- prompt /command/ -붙어서 오는 것들. 
- shell $를 지칭하는 말.

## Exercises
1. 터미널에 `Hello, world`를 출력해보자.
2. `echo 'Hello 라고 입력하고 이 문제상황에서 빠져나와 보자.
3. echo 메뉴얼을 참고하여 줄 바꿈(개행, new line)을 하지 않고 'hello, World'를 출력해보자.
4. `sleep`이라고 하는 명령어의 메뉴얼 페이지를 읽고, 우리의 터미널을 5초간 재워 보자.
5. 이번에는 터미널을 100초간 재워 보고, 중간에 깨워 보도록 하자.

## Summary
- `echo <string>` : 화면에 문자열 출력. ex) echo hello
- `man <command>` : 특정 커맨드 매뉴얼 페이지. ex) man echo
- `^c` : 현재 입력중인 작업 취소(Cancel) 이후 새 줄 실행.
- `^a` : 현재 입력중이 줄 맨 앞으로 커서 이동.
- `^e` : 현재 입력중이 줄 맨 뒤로 커서 이동
- `^u` : 현재 커서 기준, 앞쪽 전체 삭제.
- `^k` : 현재 커서 기준, 뒷쪽 전체 삭제. (c9에서 동작하지 않음)
- `^w` : 현재 커서 기준, 앞쪽 단어 단위로 삭제. (c9에서는 사용 불가)
- `alt + click` : 클릭하는 곳으로 커서 이동.
- `방향키 위, 아래` : 명령어 히스토리 탐색
- `clear` or `^l` : 화면 정리(clear screen)
- `exit` or `^d` : bash 종료
