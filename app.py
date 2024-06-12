from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/euodeioacordarcedo")
def index():
  return render_template("euodeioacordarcedo.html")



if __name__ == '__main__':
    app.run(port=5000, debug=True)