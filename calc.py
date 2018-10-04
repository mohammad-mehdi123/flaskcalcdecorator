# sadsasadsasadassadsa
from flask import Flask,request,jsonify
from functools import wraps

app = Flask(__name__)

def inverse(f):
    @wraps(f)
    def wrapper(*arg,**kwargs):
        data = request.json   
        op = data["op"]
        if op == "+":
            request.json["op"] = "-"
        elif op == "-":
            request.json["op"] = "+"
        return f(*arg,**kwargs)
    return wrapper

#lknfewrkf
@app.route("/calc", methods=['POST'])
@inverse
def calculator():
    data=request.json
    op1 = data["op1"]
    op2 = data["op2"]
    op = data["op"]
    resp = {}
    answer = None
    
    if op == "+":
        answer = op1+op2
    if op == "-":
        answer = op1-op2

    resp["result"] = answer
    return jsonify(resp)

if __name__ == '__main__':

    app.run(host='0.0.0.0')



