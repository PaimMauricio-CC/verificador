import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded key-city mapping for demonstration purposes
# In a real scenario this could be loaded from a database or environment variable
ALLOWED_KEYS = {
    "12345": "Sao Paulo",
    "67890": "Rio de Janeiro",
    "abcde": "Curitiba"
}

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json(force=True)
    key = data.get('key')
    city = data.get('city')

    if key is None or city is None:
        return jsonify({"verified": False, "error": "Missing key or city"}), 400

    expected_city = ALLOWED_KEYS.get(key)
    verified = expected_city == city

    return jsonify({"verified": verified})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
