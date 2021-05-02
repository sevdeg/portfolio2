from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return ("hello world")

@app.route('/customer')
def customer():
    return render_template('customerservice.html')
    #return ("hello world")


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')
    #return ("hello world")

@app.route('/shoppingCart')
def shoppingcart():
    return render_template('shoppingCart.html')
    #return ("hello world")


@app.route('/login')
def login():
    return render_template('loggInn.html')
    #return ("hello world")
    
if __name__ == '__main__':
    app.run(debug=True)