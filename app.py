from flask import Flask, render_template, url_for, flash, redirect
from forms import registrationform, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '84f16fba54764efa034bfceaf75b6046'
#whenever a function is called  after a route,..whatever is returned is just spit to the browser

posts = [
  {
    'author': 'The boy himself',
    'title' : 'Blog Post 1',
    'content':'first post content',
    'date_created':'september 21,2019'
  },
  {
     'author': 'spacious_2000',
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('.home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

##templtes are the front end of flask
