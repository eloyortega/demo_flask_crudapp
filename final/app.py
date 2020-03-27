# required flask modules
from flask import Flask, render_template, request, redirect

import os
import sys
import json

app = Flask(__name__)
application = app

def jsondata():
    a = open(os.path.join(sys.path[0], "data.json"), "r")
    a = a.read()
    a = json.loads(a)
    # print(a)
    return a

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/read")
def read():
    jd = jsondata()
    return render_template('read.html', data=jd, l=len(jd))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        jd = jsondata()
        req = request.form
        # print(req)
        jd.insert(0,req)
        jd = json.dumps(jd)
        save = open(os.path.join(sys.path[0], "data.json"), "w")
        save.write(jd)
        save.close()
        return redirect('read')
    return render_template('create.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    jd = jsondata()
    if request.query_string:
       id = int(request.query_string)
        # print(id)
    if request.method == "POST":
        req = {
          "nm": request.form['nm'],
          "genre": request.form['genre']
        }
        i = int( request.form['id'] )
        jd[i]=req
        jd = json.dumps(jd)
        save = open(os.path.join(sys.path[0], "data.json"), "w")
        save.write(jd)
        save.close()
        return redirect('read')
    return render_template('update.html', data=jd[id], id=id)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    jd = jsondata()
    id = int(request.query_string)
    jd.pop(id)
    jd = json.dumps(jd)
    save = open(os.path.join(sys.path[0], "data.json"), "w")
    save.write(jd)
    save.close()
    return redirect('read')

#if __name__ == "__main__":
#    app.run(debug=True)