import sys
from flask import Flask, jsonify, request

a = 0
b = 0
result = 0
op = ''

app = Flask(__name__)
@app.route('/')
def index():
	return "Hello"

@app.route('/postNumbers', methods=['POST'])
def postNumere():
    
    #nu inteleg de ce e cu print aici
    print(request.json)

    global a
    global b
    global op
    a = request.json['a']
    b = request.json['b']
    op = request.json['op']
    
    return "got it"


@app.route('/getResult', methods=['GET'])
def getRezultat():

    error='unknown operation'
    result=0
    if op=='+':
        result=a+b
        error='all ok'
    if op=='-':
        result=a-b
        error='all ok'
    if op=='*':
        result=a*b
        error='all ok'
    if op=='/':
        if b==0:
            error='divide by 0 impossible'
        else:  
            result=a/b
            error='all ok'
    
    return jsonify({'result': result, 'error': error})





#nu prea inteleg care e treaba cu asta:
if __name__ == '__main__':
		app.run(debug=True)