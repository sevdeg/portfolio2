#FØRSTE ALTERNATIV MED SQL
from flask import Flask, render_template, request, jsonify ,make_response,json
# from flask_restful import Api, Resource, reqparse
import mysql.connector
import time
import logging

logging.basicConfig(format="%(levelname)s: %(message)s",level=logging.DEBUG)

time.sleep(30)

db=mysql.connector.connect(
    host="database",
    user="root",
    passwd="admin",
    database="testdatabase"
)

mycursor = db.cursor()
#myresult = mycursor.fetchall()


try:
    mycursor.execute("CREATE TABLE Person3 (fname VARCHAR(50), lname VARCHAR(50), email VARCHAR(50), password VARCHAR(50), personID int PRIMARY KEY AUTO_INCREMENT)")
    mycursor.execute("INSERT INTO Person3 (fname,lname,email,password) VALUES(%s,%s,%s,%s)",("Tim","DON","Suhail_0310@hotmail.com","hei"))
    
    #Does not work, why?
    # result = mycursor.execute("SELECT * FROM Person2")
    # logging.info(result)


    #mycursor.execute("INSERT INTO Person2 (name,age) VALUES(%s,%s)",("Suhail",20))
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))   


db.commit()



'''
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2000Oguz",
    database="webshop_database"
)

mycursor = db.cursor()
mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("INSERT INTO Person1 (name,age) VALUES(%s,%s)",("Tim",19))
db.commit()
mycursor.execute("SELECT * FROM Person")
myresult=mycursor.fetchall()

for x in mycursor:
    print(x)

'''

#ADD DATABASE

#THE APII

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

@app.route('/register')
def register():
    # GET request
    # if request.method == 'GET':
    #     print("Requested users")
    #     return {"mesg" : "inne i get"}
    #     mycursor = db.cursor()
    #     mycursor.execute("SELECT * FROM Person2")
    #     myresult = mycursor.fetchall()
    #     return jsonify(myresult)  # serialize and use JSON headers
    # # # POST request
    # if request.method == 'POST':
    #     print("Requested users")
    #     return {"mesg" : "inne i post"}
    #     print(request.get_json())  # parse as JSON
    #     return 'Sucesss', 
        
    # req = request.get_json()

    # print(req)
    return render_template('register.html')
    # return "hallo"





# class registerUser(Resource):
#     def post(self):
#         return


# class User(Resource):
#     def get(self):








@app.route('/register/create-entry', methods=["POST"])
def leggTil():
    #KODE FUNGERE FOR DEN UTEN FORM
    # #get JSON object
    # req = request.get_json()

    # #no needed, just for debugging
    # logging.info("fetch in progress")
    # logging.info(req)

    # #values
    # inpName = req['innNavn']
    # inpMessage = req['innMessage']

    # #no needed, just for debugging
    # logging.info(inpName)
    # logging.info(inpMessage)

    # #insert a new user
    # mycursor.execute("INSERT INTO Person2 (name,message) VALUES(%s,%s)",(inpName,inpMessage))
    
    # #no needed, just for debugging
    # db.commit()
    
    # res = make_response(jsonify(req)), 200
    # return res

    #DEL 2
    #KODE FUNGERE FOR DEN UTEN FORM
    # #get JSON object
    req = request.get_json()

    #no needed, just for debugging
    logging.info("fetch in progress")
    logging.info(req)

    #values
    inpFornavn = req['innFornavn']
    inpEtternavn = req['innEtternavn']
    inpEmail = req['innEmail']
    inpPassord = req['innPassord']

    #no needed, just for debugging
    logging.info(inpFornavn)
    logging.info(inpEtternavn)
    logging.info(inpEmail)
    logging.info(inpPassord)

    #insert a new user
    mycursor.execute("INSERT INTO Person3 (fname,lname,email,password) VALUES(%s,%s,%s,%s)",(inpFornavn,inpEtternavn,inpEmail,inpPassord))
    
    #no needed, just for debugging
    db.commit()

    msg = {"Message ": "User created succsessfully"}, 201
    res = make_response(jsonify(req)), 200
    return jsonify(msg)



    
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") 
#     #db.close()







# # ANDRE ALTERNVATIV MED SQL-ALCHEMA
# from flask import Flask, render_template
# import mysql.connector
# from flask_sqlalchemy import SQLAlchemy 
# import pymysql
# import cryptography
# pymysql.install_as_MySQLdb()
# import time

# time.sleep(30)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@db-mysql/testdatabase'

# db = SQLAlchemy(app)



# # #ADD DATABASE

# class example(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         name = db.Column(db.String(255))

#         def __repr__(self):
#             return "<User(name='%s'>" % (
#                 self.name
#             )


# db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/customer')
# def customer():
#     return render_template('customerservice.html')

# @app.route('/checkout')
# def checkout():
#     return render_template('checkout.html')

# @app.route('/shoppingCart')
# def shoppingcart():
#     return render_template('shoppingCart.html')

# @app.route('/login')
# def login():
#     return render_template('loggInn.html')
    
# @app.route('/register')
# def register():
#     return render_template('register.html')
  
# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")
