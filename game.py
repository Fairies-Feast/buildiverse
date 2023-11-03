from flask import Flask, request, render_template
app = Flask('app')
@app.route("/")
def home():
  return "Success!"
app.run(host="0.0.0.0",port="8080")
