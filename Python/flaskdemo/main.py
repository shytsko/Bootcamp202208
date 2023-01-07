from flask import Flask, render_template
from auth import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'world hello'


@app.route('/', methods = ['GET', 'POST']) 
def index():
    form = LoginForm()
    print(form.csrf_token())
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        print(name, surname, email)
        return render_template('index.html', title='Главная страница',
            message='Вы авторизовались!')
    return render_template('index.html', title='Вы авторизовались!', form=form)



@app.route('/<name>') 
def hello(name):
    title = 'BootCamp'
    return render_template('hello.html', name=name, title = title)

@app.errorhandler(Exception)
def error(e: Exception):
    return render_template('error.html', error = str(e))

if __name__ == '__main__':
    app.run()