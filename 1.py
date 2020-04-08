from flask import Flask, render_template, redirect

app = Flask(__name__)

USERNAME = "Аб"

class Tasks:
    @app.route('/')
    def tasks_num():
        return render_template('index.html', title='Задания',
                               username=USERNAME)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')