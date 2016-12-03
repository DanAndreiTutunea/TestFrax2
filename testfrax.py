import sys
from flask import Flask, jsonify, request

a = 0
b = 0	
sum = 0

app = Flask(__name__)
@app.route('/')
def index():
	return "Hello"

@app.route('/getName', methods=['GET'])
def func():
	names = [
		{
			"id": 1,
			"firstName": "Vlad",
			"age": 19
		},
		{
			"id": 2,
			"firstName": "Dan",
			"age": 30
		}
	]
	return jsonify({'names': names})


@app.route('/postNumbers', methods=['POST'])
def getNumere():
	print(request.json)
	global a
	global b
	a = request.json['a']
	b = request.json['b']

	return "got it"


@app.route('/Suma', methods=['GET'])
def sum():
	
	global sum
	sum = a + b

	return jsonify({'sum': sum})


#def main():
#
#	a=1
#	b=2
#
#	c=a+b
#	print c

if __name__ == '__main__':
		app.run(debug=True)

#main()
