from flask import Flask,render_template,make_response
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import numpy as np
import mysql.connector

app = Flask(__name__)

config = {
  'host':'demoquakes.mysql.database.azure.com',
  'user':'quakes@demoquakes',
  'password':'Earth_quake',
  'database':'equakes'
}

@app.route('/')
def piechart():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
    ##query="select count(*) from earthquake where mag>8"
    ##cursor.execute(query)

    ##result_set = cursor.fetchall()
    ##age =[]
    #for row in result_set:
       #age.append(row[0])

    age1=[1,2,3]
    p_labels=[1,2,3]




    plt.pie(age1,labels=p_labels)

    plt.show()

    return render_template('display.html')


if __name__ == '__main__':
  app.run()
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




    return render_template('display.html')







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

    return render_template('display.html')
'''


