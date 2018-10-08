# sadsasadsasadassadsa
from flask import Flask,request,jsonify
from functools import wraps
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["calculations"]
myrow = mydb["last_operation"]

app = Flask(__name__)

#def inverse(f):
#    @wraps(f)
#    def wrapper(*arg,**kwargs):
#        data = request.json   
#        op = data["op"]
#        if op == "+":
#            request.json["op"] = "-"
#        elif op == "-":
#            request.json["op"] = "+"
#        return f(*arg,**kwargs)
#    return wrapper

#lknfewrkf
@app.route("/calculations", methods=['POST'])
#@inverse
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
    if op == "*":
        answer = op1*op2
    if op == "/":
        answer = op1/op2

    resp["result"] = answer
    mydict = { "op1" : op1 , "op2" : op2 , "op" : op , "result" : answer }
    calc = mycol.insert_one(mydict)
    return jsonify(resp)

@app.route("/find",methods=['GET'])
def find():
    x = mycol.find_one()
    return 'result found' + str(x['op1'])+ '  ' + str(x['op2'])+ '  ' + str(x['op'])+ '  ' + str(x['result']) 

@app.route("/lastoperations", methods=['GET'])
def last():

    pluscursor = mycol.find({'op' : '+'},{}).sort('_id',-1).limit(4)
    minuscursor =  mycol.find({'op' : '-'}).sort('_id',-1).limit(4)
    multcursor = mycol.find({'op' : '*'}).sort('_id',-1).limit(4)
    divcursor =  mycol.find({'op' : '/'}).sort('_id',-1).limit(4)
    
    for b in pluscursor:
        myrow.insert_one(b)
    for c in minuscursor:
        myrow.insert_one(c)
    for d in multcursor:
        myrow.insert_one(d)
    for e in divcursor:
        myrow.insert_one(e)
    
    llist=  []
    lastops = myrow.find({},{"_id":0})
    for f in lastops:
        llist.append(f)

    return jsonify(llist)
     


if __name__ == '__main__':

    app.run(host='0.0.0.0')



