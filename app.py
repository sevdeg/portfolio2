from flask import Flask, render_template
import mysql.connector
import time

time.sleep(30)

db = mysql.connector.connect(
    host="database",
    user="root",
    passwd="admin",
    database="testdatabase"
)

mycursor = db.cursor()

try:
    mycursor.execute("CREATE TABLE Person1 (name VARCHAR(50),age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

# mycursor.execute("SHOW DATABASES")
# l = mycursor.fetchall()
# print (l)

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("heihei",13))
db.commit()
# # for x in mycursor:
# #     print(x)
# # mycursor.execute("CREATE DATABASE testdatabase")
# # from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)

# #ADD DATABASE

@app.route('/')
def index():
    return render_template('index.html')
    #return ("hello world")

@app.route('/kontakt')
def kontaktOss():
    return render_template('kontaktOss.html')
    #return ("hello world")

@app.route('/test')
def test():
    return render_template('test.html')
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
    app.run(debug=True, host="0.0.0.0")