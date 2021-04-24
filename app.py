from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return ("hello world")

@app.route('/kontakt')
def kontaktOss():
    return render_template('kontaktOss.html')
    #return ("hello world")

if __name__ == '__main__':
    app.run(debug=True)