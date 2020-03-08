# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:41:55 2020

@author: Sayantan
"""

from flask import Flask, render_template, request
from db_model import *
from send_email import *

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        try:
            create_table()
            insert_data(email,height)
            avg_height=calc_avg()
            count=get_count()
            send_email(email,height,avg_height,count)
            return render_template("success.html")
        except:
            return render_template("index.html", text="Email address already present.!!")

if __name__ =='__main__':
    app.run()
