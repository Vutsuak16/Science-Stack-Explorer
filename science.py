import os
import pandas as pd
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
import json
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
from pandas.io.json import json_normalize




app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('album.html')

@app.route('/submit', methods=['POST'])
def submit():
    query=request.form['text']
    print(query)
    sparql = SPARQLWrapper("http://localhost:3030/kaja/query")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)
    result_table=json_normalize(results["results"]["bindings"])
    result_table.to_html('templates/query.html')
    return render_template("query.html")

@app.route("/query1",methods=['GET', 'POST'])
def query1():

    
    return render_template("after_Jan.html")
    

@app.route("/query2")
def query2():
    
    return render_template("query2_journal.html")
    #return render_template('query1.html')

@app.route("/query2_journal",methods=["POST"])
def query2_journal():

    keyword=request.form['text']
    f=open("title_journal.txt")
    query=f.read().replace("geometry",keyword)
    print(query)
    sparql = SPARQLWrapper("http://localhost:3030/kaja/query")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    result_table=json_normalize(results["results"]["bindings"])
    result_table.to_html('templates/query.html')
    return render_template("query.html")
    

@app.route("/query3")
def query3():
    
    if request.method=="POST":
        return render_template("query.html")
    return render_template("input.html")
    #return render_template('query1.html')

@app.route("/query4")
def query4():
    
    
    return render_template("rating7.html")
    #return render_template('query1.html')

@app.route("/query5")
def query5():
    
    if request.method=="POST":
        return render_template("query.html")
    return render_template("input.html")
    #return render_template('query1.html')

@app.route("/query6")
def query6():
    
    
    return render_template("top_votes_SSE.html")
    #return render_template('query1.html')

@app.route("/query7")
def query7():
    
    if request.method=="POST":
        return render_template("query.html")
    return render_template("input.html")
    #return render_template('query1.html')

@app.route("/query8")
def query8():
    
    if request.method=="POST":
        return render_template("query.html")
    return render_template("input.html")
    #return render_template('query1.html')



@app.route("/query9")
def query9():
    
    return render_template("query9_hackernews_comment.html")
    #return render_template('query1.html')

@app.route("/query9_hackernews_comment",methods=["POST"])
def query9_hackernews_comment():

    keyword=request.form['text']
    f=open("query_hackernews_comment.txt")
    query=f.read().replace("Tell",keyword)
    print(query)
    sparql = SPARQLWrapper("http://localhost:3030/kaja/query")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    result_table=json_normalize(results["results"]["bindings"])
    result_table.to_html('templates/query.html')
    return render_template("query.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
