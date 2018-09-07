import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os.exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port='5000')
=======
    app.run(host='0.0.0.0')
>>>>>>> 753e080d3ec779da19e82c1ea64b899fb13d416b
