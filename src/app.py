from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/api/details')
def get_details():
    json_data = {
        'name': 'Anil',
        'age': 30,
        'email': 'anil.p@tecnotree.com'}
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
    