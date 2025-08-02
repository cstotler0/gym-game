from myapp import app
from flask import render_template, flash, redirect, url_for
from myapp.forms import LoginForm


@app.route('/')

@app.route('/home')
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.email.data, form.remember_me.data
        ))
        return redirect(url_for('home'))
    
    return render_template('login.html', title='Log In', form=form)
