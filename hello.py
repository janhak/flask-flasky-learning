from flask import Flask, request ,make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "Hello world, your browser is {}".format(user_agent)


@app.route('/user/<name>')
def user(name):
    return "Hello {}!".format(name)

@app.route('/cookie')
def response_cookie():
    response = make_response('This doc carries cookie')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)
