from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS threats (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/phishing")
def phishing():
    return render_template("phishing.html")

@app.route("/password")
def password():
    return render_template("password.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/threats")
def threats():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM threats")

    threats_data = cursor.fetchall()

    conn.close()

    return render_template(
        "threats.html",
        threats=threats_data
    )

@app.route("/add", methods=["GET", "POST"])
def add_threat():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO threats (title, description) VALUES (?, ?)",
            (title, description)
        )

        conn.commit()
        conn.close()

        return redirect("/threats")

    return render_template("add_threat.html")

if __name__ == "__main__":
    app.run(debug=True)