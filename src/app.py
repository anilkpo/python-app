from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/details')
def get_details():
    return {'message': 'Hello, this is the details endpoint!'}

if __name__ == '__main__':
    app.run(debug=True)
    