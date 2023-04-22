from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from dao.models import Measurement
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = DB_HOST
app.config['MYSQL_DB'] = DB_NAME
app.config['MYSQL_USER'] = DB_USER
app.config['MYSQL_PASSWORD'] = DB_PASSWORD

mysql = MySQL(app)

# API endpoint to get all measurements
@app.route('/measurements')
def get_measurements():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM measurements')
    measurements = cursor.fetchall()
    cursor.close()

    measurement_list = []
    for m in measurements:
        measurement = Measurement(m[0], m[1], m[2], m[3], m[4])
        measurement_list.append(measurement.to_dict())

    return jsonify(measurement_list)

# API endpoint to get filtered waist measurements
@app.route('/waist_measurements')
def get_waist_measurements():
    height = int(request.args.get('height'))
    weight = int(request.args.get('weight'))
    age = int(request.args.get('age'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT waist FROM measurements WHERE height>=%s AND weight>=%s AND age>=%s', (height, weight, age))
    measurements = cursor.fetchall()
    cursor.close()

    waist_measurements = [m[0] for m in measurements]

    return jsonify(waist_measurements)

# API endpoint to add new measurement
@app.route('/add_measurement', methods=['POST'])
def add_measurement():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    age = data['age']
    waist = data['waist']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO measurements (height, weight, age, waist) VALUES (%s, %s, %s, %s)', (height, weight, age, waist))
    mysql.connection.commit()
    cursor.close()

    return 'Measurement added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
