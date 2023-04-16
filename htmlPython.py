from flask import  Flask,render_template

app=Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temp=45
    return {"station":station,"date":date,"temp":temp }

app.run(debug=True)
