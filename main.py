import random

from flask import Flask, url_for, request

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

@app.get('/astronaut_selection')
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="lastname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="lastname">
                                    <input type="text" class="form-control" id="firstname" placeholder="Введите имя" name="firstname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Ваше образование</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="1" id="prof1">
                                        <label class="form-check-label" for="prof1">
                                              Инженер-исследователь
                                        </label>
                                      </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="2" id="prof2">
                                        <label class="form-check-label" for="prof2">
                                              Инженер-строитель
                                        </label>
                                      </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="2" id="prof2">
                                        <label class="form-check-label" for="prof2">
                                              Пилот
                                        </label>
                                      </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите учавствовать в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

@app.post('/astronaut_selection')
def astronaut_selection_post():
    if request.method == 'POST':
        print(request.form)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
