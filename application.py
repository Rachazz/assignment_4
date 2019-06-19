from flask import Flask,render_template,make_response
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random


app = Flask(__name__)
@app.route('/')
def plot():
    plt.plot([1,2,3],[5,6,7])
    plt.show()

    return "Success"


if __name__ == '__main__':
  app.run()





