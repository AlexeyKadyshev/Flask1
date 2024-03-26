# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)

category = [
    {"title": 'Одежда', "func_name": 'dress'},
    {"title": 'Обувь', "func_name": 'shoes'},
    {"title": 'Куртки', "func_name": 'jackets'}
]


@app.route('/')
def index():
    return render_template('index.html', category=category)


@app.route('/info/')
def info():
    return render_template('info.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/dress/')
def dress():
    return render_template('dress.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jackets/')
def toys():
    return render_template('jackets.html')


if __name__ == '__main__':
    app.run(debug=True)
