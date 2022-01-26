from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/zamestnanci", methods=["GET"])
def main():
    x = open("EmployeeData.json")
    t = json.load(x)
    x.close()
    return jsonify(t),200



if __name__ == "__main__":
    app.run()
