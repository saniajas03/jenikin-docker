from flask import Flask

app = Flask(__name__)

@app.route('/') # ❌ you wrote router instead of route
def hello_world():
    return 'Hello from Flask Dockerized!' # fixed spelling too :)

if __name__ == '__main__': # ❌ use == not =
    app.run(debug=True, host='0.0.0.0') # ❌ use host='0.0.0.0'