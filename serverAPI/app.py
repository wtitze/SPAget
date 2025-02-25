from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to handle the sum calculation using GET
@app.route('/sum', methods=['GET'])
def calculate_sum():
    num1 = request.args.get('num1', 0)  # Retrieve num1 from query parameters, default to 0
    num2 = request.args.get('num2', 0)  # Retrieve num2 from query parameters, default to 0
    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
