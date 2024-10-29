from flask import Flask, jsonify, request
import requests
import sqlite3

app = Flask(__name__)


database_path = "/app/data/guests.db"

def get_db_connection():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    return conn



# GET A LIST OF ALL USERS
@app.route('/guests', methods=['GET'])
def get_guests():
    conn = get_db_connection()
    guests = conn.execute("SELECT * FROM guests").fetchall()
    conn.close()
    return jsonify([dict(guest) for guest in guests])


# GET GUEST BY LAST NAME
@app.route('/guests/search', methods=['GET'])
def search_guest_by_last_name():
    last_name = request.args.get('last_name')
    conn = get_db_connection()
    guests = conn.execute("SELECT * FROM guests WHERE last_name = ?", (last_name,)).fetchall()
    conn.close()
    return jsonify([dict(guest) for guest in guests])



# ADD A GUEST
@app.route('/guests', methods=['POST'])
def create_guest():
    new_guest = request.get_json()

    first_name = new_guest.get('first_name')
    last_name = new_guest.get('last_name')
    country = new_guest.get('country')

    conn = get_db_connection()
    conn.execute("INSERT INTO guests (first_name, last_name, country) VALUES(?,?,?)", (first_name, last_name, country))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Guest added succesfully'})



# CHANGE GUEST INFORMATION
@app.route('/guests/<int:id>', methods=['PUT'])
def change_guest_information(id):
    update_guest = request.get_json()

    conn = get_db_connection()
    conn.execute("UPDATE guests SET first_name = ?, last_name = ?, country = ? WHERE id = ?", 
                 (update_guest.get('first_name'), update_guest.get('last_name'), update_guest.get('country'), id))
    
    conn.commit()
    conn.close()

    return jsonify({'message': 'Guest information updated successfully'})
   
    

# GET A GUEST BY ID
@app.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    conn = get_db_connection()
    guest = conn.execute("SELECT * FROM guests WHERE id = ?", (id,)).fetchone()
    conn.close()

    return jsonify(dict(guest))                     



# DELETE A GUEST BY ID
@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM guests WHERE id = ?", (id,))
    guest = cursor.fetchone()

    conn.execute("DELETE FROM guests WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Guest is deleted succesfully'})



    



app.run(debug=True, host='0.0.0.0', port=5000)


# docker build -t kong_arthur_guest .    -> Først skrives den her nede i terminalen
# docker run -it -p 5000:5000 -v miniprojekt:/app/data kong_arthur_guest    -> Derefter køres denne i terminalen
