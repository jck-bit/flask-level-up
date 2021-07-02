from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class blogpost(db.Model):
    id = db.column(db.integer, primary_key=True)
    title = db.column(db.String(100), nullable=False)
    content = db.column(db.Text, nullable=False)
    author = db.column(db.String(20), nullable=False, default = 'N/A')
    date_posted = db.column(db.DateTime, nullable=False, default =datetime.utcnow)

    def __repr__(self):
        return 'blog post' + str(self.id)

all_posts = [
    {
        'title': 'post 1',
        'content' : 'this is the content of post 1',
        'author': '2000'
    },
    {
        'title': 'post 2',
        'content' : 'this is the content of post 2'
    }
]




#whenever a function is called  after a route,..whatever is returned is just spit to the browser

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<string:name>')
def hello(name):
    return 'hello, ' + name


@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)


#i only allow a get request to the webpage below

@app.route('/only get', methods=['GET'])
def get_req():
    return 'you can only get this webpage'

if __name__ == "__main__":
    app.run(debug=True)

##templtes are the front end of flask