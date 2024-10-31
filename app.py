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
    
    if guests:
        return jsonify([dict(guest) for guest in guests]), 200
    else:
        return jsonify({"error": "Not found"}), 404


# GET GUEST BY LAST NAME
@app.route('/guests/search', methods=['GET'])
def search_guest_by_last_name():
    last_name = request.args.get('last_name')
    conn = get_db_connection()
    guests = conn.execute("SELECT * FROM guests WHERE last_name = ?", (last_name,)).fetchall()
    conn.close()

    if guests:
        return jsonify([dict(guest) for guest in guests]), 200
    else:
        return jsonify({"error": "Not found"}), 404    



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
    
    if new_guest:
        return jsonify({'message': 'Guest added succesfully'}), 201
    else:
        return jsonify({"error": "Bad request"}), 400




# CHANGE GUEST INFORMATION
@app.route('/guests/<int:id>', methods=['PUT'])
def change_guest_information(id):
    update_guest = request.get_json()

    conn = get_db_connection()
    conn.execute("UPDATE guests SET first_name = ?, last_name = ?, country = ? WHERE id = ?", 
                 (update_guest.get('first_name'), update_guest.get('last_name'), update_guest.get('country'), id))
    
    conn.commit()
    conn.close()

    if update_guest:
        return jsonify({'message': 'Guest information updated successfully'}), 200
    else:
        return jsonify({"error": "Not found"}), 404    
   
    

# GET A GUEST BY ID
@app.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    conn = get_db_connection()
    guest = conn.execute("SELECT * FROM guests WHERE id = ?", (id,)).fetchone()
    conn.close()

    if guest:
        return jsonify(dict(guest)), 200
    else:
        return jsonify({"error": "Not found"}), 404




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

    if delete_guest:
        return jsonify({'message': 'Guest is deleted succesfully'}), 200
    else:
        return jsonify({"error": "Not found"}), 404    


#Send all data
@app.route('/guests/data', methods=["GET"])
def get_bookings_data():
    with sqlite3.connect('/app/data/guests.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM guests")
        data = cur.fetchall()

        #Check the response
        if not data:
            #response is empty
            return "There was an error trying to retrieve all guests!", 400
        return data

    



app.run(debug=True, host='0.0.0.0')


# docker build -t kong_arthur_guest .    -> Først skrives den her nede i terminalen
# docker run -it -p 5001:5001 -v miniprojekt:/app/data kong_arthur_guest    -> Derefter køres denne i terminalen
