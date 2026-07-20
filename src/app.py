from flask import Flask

app = Flask(__name__)

@app.route('/api/details')
def get_details():
    return {'message': 'Hello, this is the details endpoint!'}

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
    