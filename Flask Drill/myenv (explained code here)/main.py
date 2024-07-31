from flask import Flask, make_response, jsonify, request, abort
from flask_mysqldb import MySQL
from flask_httpauth import HTTPBasicAuth
import dicttoxml 
from xml.dom.minidom import parseString

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "checklist_system"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@auth.verify_password
def verify_password(username, password):
    return username == "yappy" and password == "7891"

def convert_to_xml(data):
    xml = dicttoxml.dicttoxml(data, custom_root='response', attr_type=False)
    dom = parseString(xml)
    return dom.toprettyxml()

def format_response(data):
    response_format = request.args.get('format', 'json').lower()
    if response_format == 'xml':
        xml_data = convert_to_xml(data)
        return make_response(xml_data, 200, {'Content-Type': 'application/xml'})
    else:
        return make_response(jsonify(data), 200)
    
@app.route("/protected")
@auth.login_required
def protected_resource():
    data = {"message": "You are authorized to access this resource."}
    return format_response(data)

@app.route("/customer", methods=["GET"])
@auth.login_required
def get_customer():
    data = data_fetch("SELECT * FROM customer")
    return format_response(data)

@app.route("/customer/<int:id>", methods=["GET"])
@auth.login_required
def get_customers_by_id(id):
    data = data_fetch(f"SELECT * FROM customer WHERE customer_id = {id}")
    return format_response(data)

@app.route("/customer/<int:id>/orders", methods=["GET"])
@auth.login_required
def get_customer_by_customer_id(id):
    data = data_fetch(f"""
       SELECT customer.customer_id, orders.order_id
        FROM customer
        INNER JOIN orders
        ON customer.customer_id = orders.order_id
        WHERE customer.customer_id = {id}""")
    
    response_data = {"customer_id": id, "count": len(data), "rate": data}
    return format_response(response_data)

@app.route("/customer", methods=["POST"])
@auth.login_required
def add_customer():
    if not request.is_json:
        abort(400, description="Request must be in JSON format.")
    cur = mysql.connection.cursor()
    info = request.get_json()
    customer_id = info["customer_id"]
    first_name = info["first_name"]
    last_name = info["last_name"]
    city = info["city"]
    amount = info["amount"]
    
    if not all([customer_id, first_name, last_name, city, amount]):
        abort(400, description="Missing required fields in JSON data.")
        
    cur.execute(
        """ INSERT INTO customer (customer_id, first_name, last_name, city, amount) 
        VALUES (%s, %s, %s, %s, %s)""",
        (customer_id, first_name, last_name, city, amount))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    data = {"message": "customer added successfully", "rows_affected": rows_affected}
    return format_response(data)

@app.route("/customer/<int:id>", methods=["PUT"])
@auth.login_required
def update_customer(id):
    if not request.is_json:
        abort(400, description="Request must be in JSON format.")
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    city = info["city"]
    amount = info["amount"]

    if not all([first_name, last_name, city, amount]):
        abort(400, description="No data provided for update.")
        
    cur.execute(
        """ UPDATE customer SET first_name = %s, last_name = %s, city = %s, amount = %s WHERE customer_id = %s """,
        (first_name, last_name, city, amount, id))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    data = {"message": "customer updated successfully", "rows_affected": rows_affected}
    return format_response(data)

@app.route("/customer/<int:id>", methods=["DELETE"])
@auth.login_required
def delete_customers(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customer WHERE customer_id = %s", (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    data = {"message": "customer deleted successfully", "rows_affected": rows_affected}
    return format_response(data)

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

if __name__ == "__main__":
    app.run(debug=True)
