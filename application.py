from flask import Flask,render_template,request
import matplotlib.pyplot as plt

import mysql.connector
from io import BytesIO
import base64
import numpy as np
app = Flask(__name__,static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.after_request
def after_request(response):

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = -1
    response.headers["Pragma"] = "no-cache"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

config = {
  'host':'demoquakes.mysql.database.azure.com',
  'user':'quakes@demoquakes',
  'password':'Earth_quake',
  'database':'equakes'
}


@app.route('/',methods=['POST','GET'])
def assign4():
    return render_template("assign4.html")

@app.route('/plot',methods=['POST','GET'])
def plot():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection.....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)

        #query="select time,latitude,longitude,depthError from earthquake where (depthError between "+d1+" and "+d2+") and longitude> "+long1
        #query="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"



        #query1='select latitude from earthquake where mag>'+str(r1)+'ORDER BY latitude ASC'
        query1="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"
        cursor.execute(query1)

        result_set1 = cursor.fetchall()
        count=[]

        for i in range(0,len(result_set1),1):
            count.append(result_set1[i][0])

        print(count)
        lat=[]
        #long=[]
        for i in range(len(result_set1)):
            lat.append(result_set1[i][0])
            #long.append(result_set[i][2])

        print(lat)
        print("----------------------")
        #print(long)
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.plot(count,lat,label='line1',color='k')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.legend()
        #plt.show()
        plt.savefig("static/b1.png")
    return render_template("display_plot.html")


@app.route('/hbar',methods=['POST','GET'])
def hbar():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)

        #query="select count(*) from earthquake where mag>8"'


        query='select * from earthquake where mag between '+str(r1)+' and '+str(r2)+''
        cursor.execute(query)

        result_set = cursor.fetchall()
        mag=[]
        rms=[]
        for i in range(len(result_set)):
            mag.append(result_set[i][4])
            rms.append(result_set[i][9])

        print(mag)
        print("----------------------")

        x=[5,4,3,2,7]

        bars = ('A', 'B', 'C', 'D', 'E')
        y_pos = np.arange(len(rms))             #y-axis
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.barh(y_pos,mag,label="Bar1",color='c')
        plt.yticks(y_pos, bars)
        plt.legend()
        plt.savefig("static/h2.png")



    return render_template("display_hbar.html",value=result_set)

@app.route('/vbar',methods=['POST','GET'])
def vbar():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)

        #query="select count(*) from earthquake where mag>8"'
        query="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"
        cursor.execute(query)

        result_set = cursor.fetchall()
        mag=[]
        depth=[]
        for i in range(len(result_set)):
            mag.append(result_set[i][0])
            depth.append(result_set[i][1])

        print(mag)
        print("----------------------")
        #ids=[5,5.5,6,6.5,7,7.5]
        plt.rcParams['figure.figsize']=(10,6)
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.bar(depth,mag,label="Bar1",color='c')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.yticks([0,2,4,6,8],['0','2','4','6','8'])
        plt.legend()
        #plt.show()
        plt.savefig("static/v2.png")
    return render_template("display_vbar.html")


@app.route('/pie',methods=['POST','GET'])
def pie():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)

        #query="select count(*) from earthquake where mag>8"
        #query="select latitude,longitude from earthquake where mag>6"
        query="select count(*) from earthquake where mag<2"
        #query="select time,latitude,longitude,depthError from earthquake where (depthError between "+d1+" and "+d2+") and longitude> "+long1
        cursor.execute(query)
        result=cursor.fetchall()

        query1="select count(*) from earthquake where mag between 3 and 4"
        cursor.execute(query1)
        result1=cursor.fetchall()

        query2="select count(*) from earthquake where mag between 4 and 5"
        cursor.execute(query2)
        result2=cursor.fetchall()

        query3="select count(*) from earthquake where mag>5"
        cursor.execute(query3)
        result3=cursor.fetchall()

        count=[]
        count.append(result[0][0])
        count.append(result1[0][0])
        count.append(result2[0][0])
        count.append(result3[0][0])
        print(count)
        explode = (0, 0, 0, 0.1)
        activities=['<2','3-4','4-5','>5']
        cols=['yellowgreen','lightcoral','white','blue']
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.pie(count,labels=activities,colors=cols,explode=explode, autopct='%1.1f%%')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.legend()
        #plt.show()
        plt.savefig("static/p1.png")
    return render_template('display_pie.html')


@app.route('/scatter',methods=['POST','GET'])
def scatter():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)
        #query="select count(*) from earthquake where mag>8"
        query="select latitude,longitude from earthquake where mag>6.7"
        cursor.execute(query)

        result_set = cursor.fetchall()
        lat=[]
        long=[]
        for i in range(len(result_set)):
            lat.append(result_set[i][0])
            long.append(result_set[i][1])

        print(lat)
        print("----------------------")
        print(long)
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.scatter(lat,long,label='skitscat',color='k',marker='*',s=2)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.show()
        plt.savefig("static/s1.png")
    return render_template('display_scatter.html')

@app.route('/histogram',methods=['POST','GET'])
def histogram():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        r1=request.form['r1']
        print(r1)
        r2=request.form['r2']
        print(r2)
        #query="select count(*) from earthquake where mag>8"
        query="select mag,depth from earthquake where mag>6"
        cursor.execute(query)

        result_set = cursor.fetchall()
        mag=[]
        depth=[]
        for i in range(len(result_set)):
            mag.append(result_set[i][0])
            depth.append(result_set[i][1])

        print(mag)
        print("----------------------")
        print(depth)
        y=5
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.hist(mag,y,histtype='bar',rwidth=1)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.savefig("static/his1.png")

    return render_template('display_histogram.html')



if __name__ == '__main__':
  app.run(debug='true')


#colors = ["b.", "r.", "g.", "w.", "y.", "c.", "m.", "k."]
'''

        #query="select count(*) from earthquake where mag>8"'
        query="select mag,depth from earthquake where mag>5"
        cursor.execute(query)

        result_set = cursor.fetchall()
        mag=[]
        depth=[]
        for i in range(len(result_set)):
            mag.append(result_set[i][0])
            depth.append(result_set[i][1])

        print(mag)
        print("----------------------")
        plt.rcParams['figure.figsize']=(10,6)
        fig=plt.bar(depth,mag,label="Bar1",color='r')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.show()
        plt.savefig("static/graph_plot.png")
'''
