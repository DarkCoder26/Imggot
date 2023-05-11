from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        return "it worked"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)