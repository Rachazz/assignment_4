from flask import Flask,render_template,request

import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello():
    plt.plot([1,2,3],[5,6,4])
    plt.show()

    return "Success..."

if __name__ == '__main__':
  app.run()

