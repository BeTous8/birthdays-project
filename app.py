import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

# PASSCODE = "1234"

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        action = request.form.get("action")
        # passcode = request.form.get("passcode")
        print(f"This is {action}")


        # if action in ["edit", "delete"] and passcode != PASSCODE:
        #     print(f"This is {passcode}")
        #     return "Incorrect passcode", 403

        # TODO: Add the user's entry into the database
        if name and month and day and action=="add":
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)" , name, month, day)
        elif name and action=="delete":
            db.execute("DELETE FROM birthdays where name=?", name)
        elif name and month and day and action=="edit":
            db.execute("UPDATE birthdays SET month=?, day=? where name=?", month, day, name)
            # or
            # db.execute("UPDATE birthdays SET name=? where name=? and day=?", name, month, day)



        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays order by month asc")
        print(rows)
        return render_template("index.html", birthdays=rows)


if __name__ =="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)