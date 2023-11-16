from flask import Flask, render_template, request, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

# MySQL Configuration
db_config = {
    'host': 'x71wqc4m22j8e3ql.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'user': 'of0zxxndddv53clf',
    'password': 'rhyfmihnp62cmw1x',
    'database': 'e5wmoflyt8aawue7'
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
    select_query = "SELECT name FROM tbl_users"
    cursor.execute(select_query)
    result = cursor.fetchone()  # Fetches the first row

    if result:
        name = result[0]  # Extracting the name from the fetched row
        flash(f"Hi {name}, great to see you!")
    else:
        flash("No name found in the database.")

    conn.close()
    return render_template("index.html")