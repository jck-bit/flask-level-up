from flask import Flask

app = Flask(__name__)

@app.route('/home/<string:name>')
def hello(name):
    return 'hello, ' + name

#i only allow a get request to the webpage below

@app.route('/only get', methods=['GET'])
def get_req():
    return 'you can only get this webpage'

if __name__ == "__main__":
    app.run(debug=True)