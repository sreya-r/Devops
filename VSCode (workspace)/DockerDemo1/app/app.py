from flask import Flask
app = Flask(__name__) #flask app instance

@app.route("/") 
def home():
    return "Hello, from container 1!"
if __name__ == "__main__":
    app.run()