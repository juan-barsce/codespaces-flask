from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = 'supersecret key'


def predict(x):
    return 'it\'s a dog'


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template("index.html", title="Hello fellows")
    if request.method == 'POST':
        value_to_predict = request.form['value_to_predict']
        predicted_class = predict(value_to_predict)

        return render_template("index.html", title="Hello fellows", predicted=predicted_class)
