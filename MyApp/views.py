from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

def renderData(req):
	return render(req,"insert.html")

def insertData(req):
	nm=req.GET['nm']
	add=req.GET['add']
	sal=req.GET['sal']
	mb=req.GET['mb']
	conn=MySQLdb.connect("localhost","root","","employee")
	cur=conn.cursor()
	query="insert into eployee(ename,eadd,esal,emob)value('{}','{}','{}','{}')".format(nm,add,sal,mb)
	cur.execute(query)
	conn.commit()
	return HttpResponse("Data Saved In DataBase")