from flask import Flask,render_template,request
import matplotlib.pyplot as plt

import mysql.connector
from io import BytesIO
import base64

app = Flask(__name__)

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
    print("Connection....")
    if request.method=="POST":

        #query="select count(*) from earthquake where mag>8"'
        query="select latitude,longitude from earthquake where mag>6"
        cursor.execute(query)

        result_set = cursor.fetchall()
        lat=[]
        long=[]
        for i in range(len(result_set)):
            lat.append(result_set[i][0])
            long.append(result_set[i][1])

        print(lat)
        print("----------------------")
        fig=plt.plot(lat,long)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.show()
        plt.savefig("static/graph_plot.png")
    return render_template("display_plot.html")


@app.route('/pie',methods=['POST','GET'])
def pie():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":

        #query="select count(*) from earthquake where mag>8"
        query="select latitude,longitude from earthquake where mag>6"
        cursor.execute(query)

        result_set = cursor.fetchall()
        lat=[]
        long=[]
        for i in range(len(result_set)):
            lat.append(result_set[i][0])
            long.append(result_set[i][1])

        print(lat)
        print("----------------------")
        plt.pie(lat,long)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.show()
        plt.savefig("static/graph_pie.png")
    return render_template('display_pie.html')


@app.route('/scatter',methods=['POST','GET'])
def scatter():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    if request.method=="POST":
        #query="select count(*) from earthquake where mag>8"
        query="select latitude,longitude from earthquake where mag>6"
        cursor.execute(query)

        result_set = cursor.fetchall()
        lat=[]
        long=[]
        for i in range(len(result_set)):
            lat.append(result_set[i][0])
            long.append(result_set[i][1])

        print(lat)
        print("----------------------")
        plt.scatter(lat,long)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        #plt.show()
        plt.savefig("static/graph_scatter.png")
    return render_template('display_scatter.html')

@app.route('/histogram')
def histogram():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")

        #query="select count(*) from earthquake where mag>8"
    query="select latitude,longitude from earthquake where mag>8"
    cursor.execute(query)

    result_set = cursor.fetchall()
    lat=[2,4,6,8,10]
    long=[6,7,8,2,4]


    print(lat)
    print("--------------------")
    print(long)
    plt.bar(lat,long,label="Bars1")
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    #plt.show()
    plt.savefig("static/graph_histogram.png")
    return render_template('display_histogram.html')



if __name__ == '__main__':
  app.run(debug='true')
'''
def plot():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
   
    row=[]
    #query='select count(*) from earthquake where "depthError" between 0 and 1'
    #query="select time,latitude,longitude,depthError from earthquake where depthError between 0 and 3"
    #query="select count(*) from earthquake where depthError between 0 and 0.5"
    query="select latitude,longitude from earthquake where depthError between 0 and 0.2"
    cursor.execute(query)
    row = cursor.fetchall()

    lat=[]
    long=[]
    for i in row:
        lat.append(row[0])
        long.append(row[1])

    print(type(list(lat)))
    print("----------------------")


    plt.plot(lat,long)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()




    return render_template('display_plot.html')







def barchart():

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    query="select latitude,longitude from earthquake where depthError between 0 and 0.2"

    cursor.execute(query)
    result_set = cursor.fetchall()
    lat =[]
    lon=[]
    for row in result_set:
        lat.append(row[0])
        lon.append(row[1])


    objects = ('1', '2')
    y_pos = np.arange(len(objects))
    performance = [lat[0]]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Count')
    plt.title('numbers of male survivors')
    plt.show()

    return render_template('display_plot.html')
'''


