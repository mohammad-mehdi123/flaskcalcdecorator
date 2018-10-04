# sadsasadsasadassadsa
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.before_request
def inverse():
    data = request.json
    resp = {}
    answer = None
    op = data["op"]
    op1 = data["op1"]
    op2 = data["op2"]
    if op == "+":
        answer = op1-op2
    elif op == "-":
        answer = op1+op2
   
    resp["result"] = answer
    return jsonify(resp)


@app.route("/calc", methods=['POST'])
def calculator():
    data=request.json
    op1 = data["op1"]
    op2 = data["op2"]
    op = data["op"]
    resp = {}
    answer = None
    
    if op == "+":
        answer = op1+op2

    resp["result"] = answer

    return jsonify(resp)

if __name__ == '__main__':

    app.run(host='0.0.0.0')



