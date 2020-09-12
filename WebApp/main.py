from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def say_hello():
    if request.form:
        name = request.form.get("user")
    else:
        name = "John Doe"

    return render_template('hello.html', user=name)


if __name__ == '__main__':
    app.run()