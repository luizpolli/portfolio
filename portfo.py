from flask import Flask, render_template, url_for, request, redirect
import csv

portfolio = Flask(__name__)

@portfolio.route("/")
def indexpage():
    return render_template("index.html")

@portfolio.route("/<string:page>")
def allpages(page):
    return render_template(page)

def write_to_file(data):
    with open("form.txt", mode="a") as fileform:
        file = fileform.write("\n" + data["name"] + "," + data["email"] + "," + data["message"])

def write_to_csv(data):
    with open("form.csv", mode="a", newline="") as csvfile:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csvwriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([name,email,message])


@portfolio.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "The informations did not save. Please go back and check again."
    else:
        return "Something went wrong try again."