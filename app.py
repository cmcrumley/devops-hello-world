import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return os.getenv("GREETING", "Hello, World from DevOps!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)