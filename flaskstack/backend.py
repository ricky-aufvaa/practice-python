
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signin', methods=['POST'])
def signin():
    # Get the JSON data sent from the frontend
    data = request.json
    name = data.get('name')
    employee_id = data.get('employee_id')

    # Create a welcome message
    if name and employee_id:
        message = f"Welcome {name} - {employee_id}"
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "Name and Employee ID are required"}), 400

if __name__ == '__main__':
    app.run(debug=True)
