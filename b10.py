from flask import Flask, render_template, request
import time
import re

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def indexJS():
    if request.method == "GET":
        return render_template("indexJS.html")

    if request.method == "POST":
        if request.form["usn"] == "" or request.form["dob"] == "" or request.form["mark1"] == "" or request.form["mark2"] == "" or request.form["mark3"] == "":
            msg = "All form fields are required"
            return render_template("indexJS.html", msg=msg)
        try:
            time.strptime(request.form["dob"], "%d/%m/%Y")
        except ValueError:
            msg = "***Date is invalid***"
            return render_template("indexJS.html", msg=msg)

        usn_pattern = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

        if not re.match(usn_pattern, request.form["usn"]):
            msg = "***USN format invalid***"
            return render_template("indexJS.html", msg=msg)

        x = int(request.form["mark1"])
        y = int(request.form["mark2"])
        z = int(request.form["mark3"])
        msg = int((x+y+z)/3)
        return render_template("success.html", msg=msg)

if __name__ == '__main__':
    app.run()
