from utils.db import db

class Contact(db.Model):
    
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String(50))

    def __init__(self, fullname):
        self.fullname=fullname


