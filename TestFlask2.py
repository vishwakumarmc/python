# app.py

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Set a secret key for encrypting session data
#app.secret_key = 'my_secret_key'

# dictionary to store user and password
users = {
	'username': 'vishwa',
	'password': 'kumar'
}

# To render a login form
@app.route('/')
def view_form():
	return render_template('Login.html')

# For handling get request form
@app.route('/handle_get', methods=['GET'])
def handle_get():
	if request.method == 'GET':
		username = request.args['username']
		password = request.args['password']
		print(username, password)
		if username in users.values() and password in users.values():
			return '<h1>Welcome!!! {username}</h1>'
		else:
			return '<h1>invalid credentials!</h1>'
	else:
		return render_template('Login.html')


@app.route('/handle_post', methods=['POST'])
def handle_post():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print(username, password)
		if username in users.values() and password in users.values():
			return f'<h1>Welcome!!! {username}</h1>'
		else:
			return '<h1>invalid credentials!</h1>'
	else:
		return render_template('Login.html')

if __name__ == '__main__':
	#app.run(debug=True, port=5001)  The default port is 5000 for flask is 5000, but it can be changed here
	app.run(debug=True)
