from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ''' Hello from team 1 
              \n Abbas
              \n demo 
              \n test

    '''

app.run(host="0.0.0.0", port=5001)
