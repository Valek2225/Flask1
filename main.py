from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h3>Человечество вырастает из детства.</h3>
                        <h3>Человечеству мала одна планета.</h3>
                        <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                        <h3>И начнем с Марса!</h3>
                        <h3>Присоединяйся!</h3>
                      </body>
                    </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Yandex Flask</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}" alt="mars">
    <p>Вот она какая, красная планета.</p>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
