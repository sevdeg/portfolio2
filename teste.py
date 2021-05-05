from flask import Flask, render_template
import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)
mycursor = db.cursor()

if __name__ == '__main__':
    app.run(debug=True)