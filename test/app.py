from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

@app.route('/data')
def get_data():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM yourtable")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


#for sql
#4. MySQL (Database)
#Ensure you have a MySQL database set up with the necessary tables and data. Here's an example of creating a table and inserting data:
"""
CREATE DATABASE yourdatabase;

USE yourdatabase;

CREATE TABLE yourtable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    value INT
);

INSERT INTO yourtable (name, value) VALUES ('Sample', 123);
"""

"""
5. Running the Application
Start your Flask server by running the Python script:

python app.py

Open your HTML file in a web browser.
Your web page should now be able to fetch data from the 
MySQL database through the Flask server and display it 
using JavaScript. If you encounter any issues, 
feel free to reach out for further assistance!
"""