
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_get():
    name = request.args.get('name')
    city = request.args.get('city')
    return jsonify({"message": f"Hello {name} from {city}!"})

@app.route('/api', methods=['POST'])
def api_post():
    name = request.json.get('name')
    city = request.json.get('city')
    #city = request.get_json('city')
    return jsonify({"message": f"Hello {name} from {city}!"})

if __name__ == '__main__':
    app.run(debug=True)
