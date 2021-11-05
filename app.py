'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Code Author:- Kartik Deshmukh a.k.a MelloB~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
from flask import Flask, request, render_template, send_file
import os
import mysql.connector

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_patient():

    #Fetching request form data
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    address = request.form['address']
    disease = request.form['disease']
    doctor_id = request.form['doctor_id']

    #Connecting to mysql database
    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hms"
)

    #Executing the query
    mycursor = mydb.cursor()
    sql = "INSERT INTO apollo (patient_id, name, age, gender, address, disease, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (0, name, age, gender, address, disease, doctor_id)
    mycursor.execute(sql, val)
    mydb.commit()

    #Return message to user.
    return 'Patient has been registered!'

if __name__ == '__main__':
    app.run(debug=True)