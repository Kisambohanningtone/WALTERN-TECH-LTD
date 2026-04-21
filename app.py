from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mpesa/stkpush', methods=['POST'])
def stkpush():
    data = request.get_json()
    # For demo: just echo back the payload
    return jsonify({
        "status": "success",
        "message": "STK Push request received",
        "data": data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
