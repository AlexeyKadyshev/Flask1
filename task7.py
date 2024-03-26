# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)

news = [
    {"title": 'Вести с полей', "date": '25.03.2024',
     "text": 'В совхозе "Красный луч" во время подготовки к посевной, обнаружены яйца неизвестных рептилий. '
             'Ученые проводят исследования.'},
    {"title": 'Новости зарубежья', "date": '14.01.2024',
     "text": 'На Мадакаскаре обнаружен новый вид неизвестного науке животного.'},
    {"title": 'Погода', "date": '20.03.2024', "text": 'Завтра ожидается снегопад, местами дожди.'},
]


@app.route('/')
def news_page():
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()
