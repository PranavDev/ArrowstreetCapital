# **********************************************************************************************************************
# Author: Pranav H. Deo { phd24@umd.edu }
# Date: 11/13/2021
# Version: v1.0
# Code Description:
# Website and API (Beta Version) for ArrowStreetCapital.

# **********************************************************************************************************************

##############################################################
import yaml
from flask import *
from modules.apiReader import pull_data
from modules.analyzer import transaction_analysis

##############################################################
# ------------------- FLASK-APP CONFIG --------------------- #
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev')
app.secret_key = 'PrjDev'

##############################################################

# ------------------- VARIABLE CONFIGS --------------------- #
user = ""
data_file_path = 'config/asc_trx_data.txt'
styvio_company_list = yaml.safe_load(open('config/company_tracker.yaml'))

##############################################################


# [Routing] Login Routine
@app.route('/')
@app.route('/Login', methods=['GET', 'POST'])
def Login():
    global user
    session.pop('user_email', None)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        '''
        Usually we have a DB connection established here
        to authenticate the user credentials. Since I do
        not have an Amazon RDS for connection, I cannot
        authenticate the user.
        '''
        session['user_email'] = email
        user = email.split("@")[0]
        flash("Login Success!", "success")
        return render_template('HomePage.html', user=user)
    return render_template('Login.html')


# [Routing] Register Routine
@app.route('/Register', methods=['GET', 'POST'])
def Register():
    session.pop('user_email', None)
    if request.method == 'POST':
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        '''
        Usually we have a DB connection established here
        after which we record a new user's registration.
        Since I do not have an Amazon RDS, I cannot pass
        down a new account.
        '''
        return render_template('Login.html')
    return render_template('Register.html')


# [Routing] HomePage
@app.route('/HomePage')
def HomePage():
    global user
    if 'user_email' in session:
        return render_template('HomePage.html', user=user)
    else:
        session.pop('user_email', None)
        return render_template('Login.html')


# [Routing] Logout Routine
@app.route('/Logout')
def Logout():
    session.pop('user_email', None)
    flash("Logged Out!", "success")
    return render_template('Login.html')


# [Routing] Investments Routine
@app.route('/Investments')
def Investments():
    global user
    if 'user_email' in session:
        pull_data(styvio_company_list)
        analysed_data = transaction_analysis(data_file_path)
        flash("STYVIO Data Analysis Complete", "info")
        return render_template('Investments.html', user=user, data=analysed_data)
    else:
        session.pop('user_email', None)
        return render_template('Login.html')


# [MAIN] Runner Call
if __name__ == '__main__':
    app.run()

# **********************************************************************************************************************

