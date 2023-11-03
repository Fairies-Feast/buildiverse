import subprocess
subprocess.run(["pip","install","flask"])
subprocess.run(['clear'])
from flask import Flask, request, render_template
app = Flask('app')
@app.route("/")
def home():
  return render_template("game.html")
app.run(host="0.0.0.0",port="8080")
