from flask import Flask, render_template

app = Flask(__name__)

SKILLS = [
    {
        "id": 1,
        "name": "Python", 
        "level": "Intermediate"
    },
    {
       "id": 2,
        "name": "CSS", 
        "level": "Basics" 
    },
    {
        "id": 3,
        "name": "Linux", 
        "level": "Advanced"
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', skills= SKILLS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)