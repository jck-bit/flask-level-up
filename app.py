from flask import Flask, render_template

app = Flask(__name__)
#whenever a function is called in front of a route,..whatever is returned is just spit to the browser

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<string:name>')
def hello(name):
    return 'hello, ' + name

#i only allow a get request to the webpage below

@app.route('/only get', methods=['GET'])
def get_req():
    return 'you can only get this webpage'

if __name__ == "__main__":
    app.run(debug=True)

##templtes are the front end of flask