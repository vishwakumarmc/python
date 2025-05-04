
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    name = request.args.get('name')
    city = request.args.get('city')
    return jsonify({"message": f"Hello {name} from {city}!"})

@app.route('/api', methods=['POST'])
def save():
    name = request.json.get('name')
    city = request.json.get('city')
    return jsonify({"message": f"Hello {name} from {city}!"})

if __name__ == '__main__':
    app.run(debug=True)
