from flask import Flask, render_template, url_for

app = Flask(__name__)

#whenever a function is called  after a route,..whatever is returned is just spit to the browser

posts = [
  {
    'author': 'corey shafer',
    'title' : 'Blog Post 1',
    'content':'first post content',
    'date_created':'september 21,2019'
  },
  {
     'author': 'corey shafer',
     'title' : 'Blog post 2',
     'content':'second post content',
     'date_created':'september 22,2019'
  }
]

@app.route('/')
def index():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title=about)


if __name__ == "__main__":
    app.run(debug=True)

##templtes are the front end of flask
