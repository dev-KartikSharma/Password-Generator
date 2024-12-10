from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # Correct way to get JSON data
    length = int(data.get('length', 12))
    use_uppercase = data.get('use_uppercase', True)
    use_numbers = data.get('use_numbers', True)
    use_special = data.get('use_special', True)

    password = generate_password(length, use_uppercase, use_numbers, use_special)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
