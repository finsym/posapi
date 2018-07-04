from flask import Flask, request, jsonify
from nltk import pos_tag, word_tokenize

app = Flask(__name__)

@app.route("/")
def index() :
    resp = error_resp()
    return jsonify(resp)

@app.route("/pos",methods={'POST'})
def pos() :
    data = request.form['q']
    tokens = word_tokenize(data)
    tags = pos_tag(tokens)
    return jsonify(build_pos_resp(tags))
        

def error_resp(msg = None) :
    if msg == None :
        msg = "invalid request"
    resp = { 'status' : 400, 'message' : msg }
    return resp

def build_pos_resp(tags) :
    resp = {}
    resp['status'] = 200
    resp['pos'] = tags
    return resp
