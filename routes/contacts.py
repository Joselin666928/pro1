from flask import Blueprint, render_template

contacts= Blueprint('contacts', __name__)

@contacts.route('/')
def add_contact():
    return render_template('index.html')