from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__, static_folder='web')

@app.route("/")
def index_page():
    return send_from_directory('web', 'index.html')

@app.route('/calc', methods=['POST'])
def calc():
    input = request.get_json()
    result = 0
    if 'number1' in input and 'number2' in input and 'operation' in input:
        number1 = float(input['number1'])
        number2 = float(input['number2'])
        operation = input['operation']
        
        if operation == 'add':
            result = number1+number2
        elif operation == 'sub':
            result = number1-number2
        else:
            return jsonify({'error': 'You can only add or subtract'}), 400
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Input two numbers and an operation'}), 400