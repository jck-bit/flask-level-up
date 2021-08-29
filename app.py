from flask import Flask

app = Flask(__name__)

#whenever a function is called  after a route,..whatever is returned is just spit to the browser

@app.route('/')
def index():
    return "<h1>home page</h1>"

@app.route('/about')
def about():
    return "my about page"


if __name__ == "__main__":
    app.run(debug=True)

##templtes are the front end of flask
