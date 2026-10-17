from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "Islamabad, Pakistan",
        "salary": {
            "currency": "PKR",
            "amount": 3600000,
        },
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "location": "Seoul, Korea",
        "salary": {
            "currency": "KRW",
            "amount": 200267022,
        },
    },
    {
        "id": 3,
        "title": "Data Engineer",
        "location": "New York, America",
        "salary": {
            "currency": "USD",
            "amount": 149000,
        },
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "location": "San Francisco, America",
        "salary": {
            "currency": "USD",
            "amount": 180000,
        },
    },
]


@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
