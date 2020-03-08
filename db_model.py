# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 11:35:28 2020

@author: Sayantan
"""

import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='d8ei8q673ja2lm' user='lafasqtwegplzu' password='396c2bf2cc7e85f934d5be3c278ee35f4814294b2a3f8674cc30210a7985c375' host='ec2-50-17-178-87.compute-1.amazonaws.com' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS height_details(id SERIAL PRIMARY KEY, email TEXT UNIQUE, height REAL)")
    conn.commit()
    conn.close()
    
def insert_data(e,h):
    conn=psycopg2.connect("dbname='d8ei8q673ja2lm' user='lafasqtwegplzu' password='396c2bf2cc7e85f934d5be3c278ee35f4814294b2a3f8674cc30210a7985c375' host='ec2-50-17-178-87.compute-1.amazonaws.com' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO height_details (email,height) VALUES(%s,%s)",(e,h))
    conn.commit()
    conn.close()

def calc_avg():
    conn=psycopg2.connect("dbname='d8ei8q673ja2lm' user='lafasqtwegplzu' password='396c2bf2cc7e85f934d5be3c278ee35f4814294b2a3f8674cc30210a7985c375' host='ec2-50-17-178-87.compute-1.amazonaws.com' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT avg(height) from height_details")
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return result[0][0]

def get_count():
    conn=psycopg2.connect("dbname='d8ei8q673ja2lm' user='lafasqtwegplzu' password='396c2bf2cc7e85f934d5be3c278ee35f4814294b2a3f8674cc30210a7985c375' host='ec2-50-17-178-87.compute-1.amazonaws.com' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT count(*) from height_details")
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return result[0][0]

