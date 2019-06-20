from flask import Flask,render_template,make_response
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import numpy as np
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

@app.route('/')
def assign4():
    return render_template("assign4.html")

@app.route('/plot')
def plot():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
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
    fig=plt.plot(lat,long)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    #plt.show()
    plt.savefig("static/graph3.png")
    return render_template("display.html")

def convert_fig_to_html(fig):

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    # rewind to beginning of file
    #figdata_png = base64.b64encode(figfile.read())
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png

@app.route('/pie')
def pie():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
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
    plt.show()
    return render_template('display.html')


@app.route('/scatter')
def scatter():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
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
    plt.show()
    return render_template('display.html')

@app.route('/histogram')
def histo():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection....")
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
    plt.plot(lat,long)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
    return render_template('display.html')



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


