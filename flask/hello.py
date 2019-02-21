from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'Python is fun!'

@app.route('/dictionary/<string:word>') #variable routing <>사용. string부분에 int, float이 올 수 있다.
def dictionary(word):
    dictionary = {
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
    result = dictionary.get(word,'나만의 단어장에 없는 단어입니다!')
    return f'{word}는(은) {result}!'