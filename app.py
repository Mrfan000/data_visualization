from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/time")
def get_time():
    t = time.gmtime()
    local_time = time.strftime("%Y年%m月%d日 %H:%M:%S",t)
    return local_time

if __name__ == "__main__":
    app.run()