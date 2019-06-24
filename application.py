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

@app.route('/display',methods=['POST','GET'])
def display():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection...")
    row=[]
    row1=[]

        #query='select count(*) from earthquake where "depthError">1'
    query='select StateName from voting3 where (TotalPop between 2000 and 8000)  '

        #query="SELECT longitude, depth, mag, place FROM earthquaketable WHERE latitude BETWEEN " + range1 + " and " + range2
    print("query...")
    cursor.execute(query)
    row = cursor.fetchall()
    query1='select StateName from voting3 where (TotalPop between 8000 and 40000)  '
    cursor.execute(query1)
    row1 = cursor.fetchall()
    print(row)
    print("fetching")
    return render_template('display_values.html',value=row,value1=row1)

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

        ##query="select time,latitude,longitude,depthError from earthquake where (depthError between "+d1+" and "+d2+") and longitude> "+long1
        #query="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"
        #query1='select latitude from earthquake where mag>'+str(r1)+'ORDER BY latitude ASC'

        query='select mag,depth from earthquake where mag between '+str(r1)+' and '+str(r2)+''
        query1="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"
        cursor.execute(query)

        result_set = cursor.fetchall()
        mag=[]
        depth=[]

        for i in range(0,len(result_set)):
            mag.append(result_set[i][0])
            depth.append(result_set[i][1])




        print(mag)
        print("----------------------")
        #print(long)
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.plot(mag,depth,label='line1',color='y')
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
        print("---------------------")

        x=[5,4,3,2,7]

        bars = ('A', 'B', 'C', 'D', 'E')
        y_pos = np.arange(len(rms))             #y-axis
        plt.clf()
        plt.rcParams['figure.figsize']=(10,6)
        plt.barh(y_pos,mag,label="Bar1",color='green')
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
        #query="select mag,depth from earthquake where mag>5 ORDER BY mag ASC"
        query='select mag,depth from earthquake where mag>'+str(r1)+''
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
        r1=int(request.form['r1'])
        print(r1)
        r2=int(request.form['r2'])
        print(r2)
        '''
        #query="select count(*) from earthquake where mag>8"
        #query="select latitude,longitude from earthquake where mag>6"
        #query="select count(*) from voting3 where mag<2"
        query='select count(*) from voting3 where StateName between '+str(r1)+' and '+str(r2)+''
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
        '''
        count=[]
        for i in range(r1,r2,5000):
            temp=i+5000
            #query='select count(*) from earthquake where mag between'+str(i)+' and '+str(temp)+''
            #query='select count(*) from earthquake where "mag" between '+str(i)+' and '+ str(temp) +''
            query='select count(*) from voting3 where TotalPop between '+str(i)+' and '+str(temp)+''      ## correct version
            cursor.execute(query)
            result=cursor.fetchall()
            count.append(result[0][0])

        print(count)
        explode = (0.1, 0, 0)
        activities=['0-5million','5-10million','10-15million']
        cols=['yellowgreen','lightcoral','blue']
        plt.clf()
        plt.rcParams['figure.figsize']=(10,10)
        plt.pie(count,labels=activities,colors=cols,explode=explode, autopct='%1.1f%%')
        #plt.xlabel('x-axis')
        #plt.ylabel('y-axis')
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
        #query="select latitude,longitude from earthquake where mag>6"
        #'select * from earthquake where "depthError" between '+str(mag1)+' and '+str(mag2)+''
        query='SELECT "TotalPop","Registered" from voting3 where TotalPop betweeen \''+r1+'\' and\''+r2+'\''
        query='select TotalPop,Registered from voting3 where TotalPop between '+str(r1)+' and '+str(r2)+''
        cursor.execute(query)

        result_set = cursor.fetchall()
        lat=[]##Totalpop
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
        plt.xlabel('Total population')
        plt.ylabel('Registered')
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

