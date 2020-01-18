from flask import render_template, url_for, flash, redirect
from brentsblog import app
from brentsblog.forms import RegistrationForm, LoginForm
from brentsblog.models import User, Post


posts = [
    {
        'author': "Brent Rainwater",
        'title': "How to train a cat",
        'content': "not at easy as it seems.....",
        'date_posted': 'January, 15, 2020'
    },
    {
        'author': "Dr Seuss",
        'title': "How to catch a bird",
        'content': "Salt on the birds tail.....",
        'date_posted': 'January, 14, 2020'
    },
    {
        'author': "Ricky Martin",
        'title': "How to dance in Latin",
        'content': "Just get shaking.....",
        'date_posted': 'January, 13, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful - Check user name and password', 'danger')
    return render_template('login.html', title="Log In", form=form)

