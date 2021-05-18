#FØRSTE ALTERNATIV MED SQL
from flask import Flask, render_template, request, jsonify ,make_response,json, url_for
import flask
# from flask_restful import Api, Resource, reqparse
import mysql.connector
import time
import logging
import os
import sqlite3
import hashlib
from passlib.hash import sha256_crypt
#from oauthlib.oauth2 import WebApplicationClient
from google.oauth2 import id_token as goog_token
from google.auth.transport import requests as goog_req
#from flask_login import (LoginManager, current_user, login_required, login_user, logout_user,)
#from db import init_db_command
#from user import User

#GOOGLE_CLIENT_ID = os.environ.get("202265633567-a7p3rejn0cpau3r242ar8074bhhu8gpv.apps.googleusercontent.com", None)
#GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
#GOOGLE_DISCOVERY_URL = (

#)


time.sleep(30)

oauth_id = '202265633567-a7p3rejn0cpau3r242ar8074bhhu8gpv.apps.googleusercontent.com'

db=mysql.connector.connect(
    host="database",
    user="root",
    passwd="admin",
    database="testdatabase"
)

mycursor = db.cursor()
mycursor.execute("SELECT * FROM Person3")
myresult = mycursor.fetchall()


try:
    mycursor.execute("CREATE TABLE Person3 (fname VARCHAR(50), lname VARCHAR(50), email VARCHAR(50), password Text, personID int PRIMARY KEY AUTO_INCREMENT)")
    mycursor.execute("INSERT INTO Person3 (fname,lname,email,password) VALUES(%s,%s,%s,%s)",("Tim","DON","Suhail_0310@hotmail.com","hei"))
    
    #Does not work, why?
    # result = mycursor.execute("SELECT * FROM Person2")
    # logging.info(result)


    #mycursor.execute("INSERT INTO Person2 (name,age) VALUES(%s,%s)",("Suhail",20))
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))   


db.commit()



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    #return ("hello world")

@app.route('/users')
def users():
    auth_token = flask.request.headers.get("Authorization")
    if(auth_token):
        print("AUTHENTICATION ATTEMPT. Token: {}".format(auth_token))
        valid_user = validate_token(auth_token)

        if not valid_user:
            return flask.jsonify([])

        print("{} is a valid Google user".format(valid_user['given_name']))
        auth_email = valid_user['email']
        #smith_img = 

    return flask.jsonify(myresult)
   #return render_template('logginn.html')

def validate_token(token):
    some_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5ZWQ1N2Y0MjQ0OTEyODJhMTgwMjBmZDU4NTk1NGI3MGJiNDVhZTAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTk5MTgxNjM0NTkyLW04YmVuaTUzM2Y5ZThhYWJmZWRwZ2ZlZzc3dWhraTk1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiMTk5MTgxNjM0NTkyLW04YmVuaTUzM2Y5ZThhYWJmZWRwZ2ZlZzc3dWhraTk1LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA2MDA0Mzg5OTc5NzEzNjc5ODc1IiwiZW1haWwiOiJkZXJlay5iaXBhcnRpc2FuQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiejN6dW5vUUtDcGlDS2xrUHdmVjhrUSIsIm5hbWUiOiJEZXJlayBCaXBhcnRpc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBVFhBSnlvdGZfSy01S0c2cFg4emZDX05JblI4OGpBbUE0V3ZSYXRUR1c3PXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkRlcmVrIiwiZmFtaWx5X25hbWUiOiJCaXBhcnRpc2FuIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2MjAyOTUzNzQsImV4cCI6MTYyMDI5ODk3NCwianRpIjoiYmNlYmE0M2FkM2RlZTFhNjlmYjgwOTIxZGI4ZWJjNGY0ZGU3YzQxMCJ9.EyOWk8Sph7mawEy5HTSvCgQNWObVp6DmJEMp1fWgmcH6m4q6YNf2Ubge7M_dwP2zp39XoWPrgRQXs2hceFKVlhKnhvGVeVaxS4e-0C9hnQFfKUDTOFMjY-hgBd0UoP9N8cUIcK1MiLgatkRiajX9Rykdf2QSAxXQd0LkD1AAueoCyrwJsDyLnogzlBnvtCc_hN8r9_TLC7v-XBrZPeW3pOrsrmGzQkCnDCtTYg7TtFv-1r5p6OK74DB3x-BqRFVyp7u_9d-zxoG__8sq2WnocutwieXUSf7q1NNWGSzcba0SmOHpg35u5dqWFhGirZRRhTvHlI5D2lqGl1ctR7XWOA"
    if (token == some_token):
        print("Token is re-used. OK.")
        return True
    else:
        print("Never seen this token before...")

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = goog_token.verify_oauth2_token(token, goog_req.Request(), oauth_id)
        print("\nTOKEN VALID. User: {}\nUser data: \n{}\n"
            .format(idinfo['given_name'],idinfo))
        return idinfo

    except ValueError as err:
        # Invalid token
        print(f"Token validation failed: {err}")

    return False

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
    inpPassord = sha256_crypt.encrypt(req['innPassord'])
    #inpPassord2 = sha256_crypt.encrypt(req['innPaard'])


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
