from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
]

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the username and password match a user in the database
    for user in users:
        if user['username'] == username and user['password'] == password:
            # Return a success message or token
            return jsonify({'message': 'Login successful'})

    # Return an error message if the login credentials are invalid
    return jsonify({'message': 'Invalid username or password'}), 401

# Protected route that requires authentication
@app.route('/protected', methods=['GET'])
def protected():
    # Check if the request contains a valid authentication token
    token = request.headers.get('Authorization')

    if token == 'your_token_here':
        # Return the protected resource
        return jsonify({'message': 'Protected resource'})

    # Return an error message if the token is invalid
    return jsonify({'message': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run()
