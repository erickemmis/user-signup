from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        #get form data as seperate variables
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        valid = True

        #set default values to errors
        name_error = ''
        pass_error = '' 
        verify_error = '' 
        email_error = ''
        
        #validate string
        if not val_string(username):
            name_error = "Username cannot have space and must be between 3 and 20 characters long"
            valid = False
        #be sure username was entered
        if not username:
            name_error = "Username required"

        #validate password
        if not val_string(password):
            pass_error = "Password cannot have space and must be between 3 and 20 characters long"
            valid = False
        #be sure password was entered
        if not password:
            pass_error = "Password required"

        #be sure passwords match
        if not verify == password:
            verify_error = "Passwords do not match"
            valid = False
        #validate email
        if email and not val_email(email):
            email_error = "Email is not valid"
            valid = False


        if valid:
            return render_template('welcome.html', name=username)
        else:
            #reset memory of password
            password = ''
            verify = ''
            return render_template("index.html", name = username, name_error = name_error,
                                                 pass_error = pass_error,
                                                 verify_error = verify_error,
                                                 email = email, email_error = email_error,
                                                 disp_errorImg = "inline")
    
    if request.method == 'GET':
        return render_template('index.html', disp_errorImg = "none")

#function to validate string for 3 and 20 chars and no spaces
def val_string(message):
    size = len(message)
    if size < 3 or size > 20 or ' ' in message:
        return False
    else:
        return True

#function to validate email includes one "@" and one "."
def val_email(email):
    if val_string(email) and email.count('@') == 1 and email.count('.') == 1:
        return True
    else:
        return False

app.run()
