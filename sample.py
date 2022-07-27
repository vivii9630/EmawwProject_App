from flask import Flask, jsonify, render_template, redirect, url_for, request
import xml.etree.ElementTree as ET
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

tree = ET.parse('config.xml')
root = tree.getroot()

sub = root[0]
cookies = root[1]



@app.route("/")
def home():
    return render_template('user_template.html')

database={'nachi':'123','james':'aac','karthik':'asdsf'}




@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('user_template.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('user_template.html',info='Invalid Password')
        else:
	         return render_template('export.html',name=name1)


@app.route('/export',methods=['POST','GET'])
def export():
    k,v = [], []

    for s,c in zip(sub, cookies):
        k.append(s.text)
        v.append(c.text)

    result = {
        "subdomains" : k,
        "cookies" : v
    }
    return jsonify(result)


if __name__ == '__main__':
   app.run(debug = True)