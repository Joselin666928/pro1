from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)

app.register_blueprint(contacts)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://joselo:96Bh@localhost:8080/contactsdb"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)