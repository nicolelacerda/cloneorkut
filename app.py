from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, <b>tudo bem<b>?"



if __name__ == '__main__':
    app.run(port=5000, debug=True)