import random

from flask import Flask, url_for

app = Flask(__name__)

promo = ["Человечество вырастает из детства.",
         "Человечеству мала одна планета.",
         "Мы сделаем обитаемыми безжизненные пока планеты.",
         "И начнем с Марса!",
         "Присоединяйся!"]


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promo = ["Человечество вырастает из детства.",
             "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             "И начнем с Марса!",
             "Присоединяйся!"]
    return "</br>".join(promo)


@app.route('/image_mars')
def image_mars():
    return '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img width="100%" src="https://yandex.ru/images/search?img_url=https%3A%2F%2Fw.wallhaven.cc%2Ffull%2Fzm%2Fwallhaven-zm387v.jpg&lr=11212&pos=0&rpt=simage&serp_list_type=all&source=serp&text=mars%20jpg">
    <p>Вот она какая, красная планета!</p>
</body>
</html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css"/>
    <title>Марс промо!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img width="100%" src="{url_for("static", filename="/img/mars.jpg")}" alt="">
    <p>Вот она какая, красная планета!</p>
    <div class="alert alert-primary" role="alert">
        A simple primary alert—check it out!
    </div>
    {'\n'.join(promo_alert(p) for p in promo)}
</body>
</html>'''


def promo_alert(text):
    color = "primary", "secondary", "success", "danger", "warning", "info "
    return f"""<div class="alert alert-{random.choice(color)}" role="alert">
        {text}
    </div>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
