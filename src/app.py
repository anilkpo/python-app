from flask import Flask, jsonify 
import socket
app = Flask(__name__)

@app.route('/api/details')
def get_details():
    json_data = {
        'name': 'Anil',
        'age': 30,
        'email': 'anil.p@tecnotree.com'}
    return jsonify(json_data)

@app.route('/api/host_details')
def get_host_details():
    json_data = {
        'hostname': socket.gethostname(),
        'ip_address': '192.168.1.100',
        'os': 'Ubuntu 20.04'
    }
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
    