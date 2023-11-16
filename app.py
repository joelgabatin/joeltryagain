from flask import Flask, render_template, request, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# MySQL Configuration
db_config = {
    'host': 'y5svr1t2r5xudqeq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'user': ''xkwo0puwn8wpp11p',
    'password': 'iacxea8i0tdesdgg',
    'database': 'lxm14898h1ry2khd'
}

# Function to Connect to MySQL
def connect_to_mysql():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route("/hello")
@app.route("/")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Fetching name from tbl_users
    select_query = "SELECT full_name FROM tbl_farmer_users"
    cursor.execute(select_query)
    result = cursor.fetchone()  # Fetches the first row

    if result:
        name = result[0]  # Extracting the name from the fetched row
        flash(f"Hi {name}, great to see you!")
    else:
        flash("No name found in the database.")

    conn.close()
    return render_template("index.html")
