from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html', x=x)

if __name__ == '__main__':
    app.run(debug=True)