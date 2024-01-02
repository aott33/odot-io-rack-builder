from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Andrew!</p>"

if __name__ == "__main__":
    print("I am inside the if statement")
    app.run("0.0.0.0", debug=True)