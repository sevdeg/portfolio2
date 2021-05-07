# #FØRSTE ALTERNATIV MED SQL
# from flask import Flask, render_template
# import mysql.connector
# import time

# time.sleep(30)

# db=mysql.connector.connect(
#     host="database",
#     user="root",
#     passwd="admin",
#     database="testdatabase"
# )

# mycursor = db.cursor()

# try:
#     mycursor.execute("CREATE TABLE Person1 (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# except mysql.connector.Error as err:
#     print("Something went wrong: {}".format(err))

# db.commit()
# '''
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="2000Oguz",
#     database="webshop_database"
#     )

# mycursor = db.cursor()
# #mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# #mycursor.execute("INSERT INTO Person (name,age) VALUES(%s,%s)",("Tim",19))
# #db.commit()
# mycursor.execute("SELECT * FROM Person")
# myresult=mycursor.fetchall()

# for x in mycursor:
#     print(x)

# '''
# #ADD DATABASE

# #THE APII

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')
#     #return ("hello world")

# @app.route('/customer')
# def customer():
#     return render_template('customerservice.html')
#     #return ("hello world")


# @app.route('/checkout')
# def checkout():
#     return render_template('checkout.html')
#     #return ("hello world")

# @app.route('/shoppingCart')
# def shoppingcart():
#     return render_template('shoppingCart.html')
#     #return ("hello world")


# @app.route('/login')
# def login():
#     return render_template('loggInn.html')
#     #return ("hello world")

# @app.route('/register')
# def register():
#     return render_template('register.html')
    
# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")
# #     #db.close()







# ANDRE ALTERNVATIV MED SQL-ALCHEMA
from flask import Flask, render_template
import mysql.connector
from flask_sqlalchemy import SQLAlchemy 
import pymysql
import cryptography
pymysql.install_as_MySQLdb()
import time

time.sleep(30)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@db-mysql/testdatabase'

db = SQLAlchemy(app)



# #ADD DATABASE

class example(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255))

        def __repr__(self):
            return "<User(name='%s'>" % (
                self.name
            )


db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/kontakt')
def kontaktOss():
    return render_template('kontaktOss.html')
    #return ("hello world")

@app.route('/test')
def test():
    return render_template('test.html')
    #return ("hello world")
=======
@app.route('/customer')
def customer():
    return render_template('customerservice.html')
>>>>>>> 75444da392492a6f02990eb36bcfc2d2e9a4b370

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shoppingCart')
def shoppingcart():
    return render_template('shoppingCart.html')

@app.route('/login')
def login():
    return render_template('loggInn.html')
<<<<<<< HEAD
    #return ("hello world")


=======
>>>>>>> 75444da392492a6f02990eb36bcfc2d2e9a4b370
    
@app.route('/register')
def register():
    return render_template('register.html')
  
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
<<<<<<< HEAD
    #db.close()
=======
>>>>>>> 75444da392492a6f02990eb36bcfc2d2e9a4b370
