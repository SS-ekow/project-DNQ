from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/getstarted')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('landingpage.html')

if __name__ == '__main__':
    app.run(debug=True)