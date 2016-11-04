from flask import Flask, render_template,request,redirect,url_for,jsonify
import pymysql
import json
conn=pymysql.connect(host="localhost",user="root",password="root",db="satya")
c=conn.cursor()

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/createForm')
def createform():
	return render_template('insert.html')

@app.route('/insert',methods=['POST','GET'])
def insert():
	if request.method=='POST':
		name1=request.form['t_name']
		c.execute("""INSERT into trip(name,latitude,longitude) VALUES (%s,%s,%s)""",(name1,request.form['t_latitude'],request.form['t_longitude']))
		conn.commit()
		return redirect(url_for('disp',name=name1))

		
@app.route('/disp/<name>')
def disp(name):
	return "<h1>Hello %s" %name+"</h1>"+"<html><body><h2><font color='green'>Values Inserted</font></h2></body></html>"
	
@app.route('/listForm')
def select():
	c.execute("SELECT * from trip")
	data=c.fetchall()
	return render_template('show.html', data = data)
		
@app.route('/updateForm')
def update():
	return render_template('update_id.html')

@app.route('/updateid',methods=['POST','GET'])
def update_details():
    if request.method=='POST':
        update_data=request.form['upid']
        query="SELECT id,name,latitude,longitude from trip WHERE id=%s"
        param=update_data
        c.execute(query,param)
        data1=c.fetchall()	
        return render_template('show_update.html',data1=data1)

@app.route('/update_det', methods=['POST','GET'])
def details_update():
	if request.method=='POST':
		id=request.form['id']
		name=request.form['name']
		latitude=request.form['lat']
		longitude=request.form['lon']
		query="UPDATE trip set name=name and latitude=latitude and longitude=longitude where id=id"
		c.execute(query)
		conn.commit()
		return "<html><body><h1>Values updated</h1></body></html>"
app.run()