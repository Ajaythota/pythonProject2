from flask import  Flask,render_template
import pandas as pd
import os

app=Flask("Website")
path=os.getcwd()+"\data\dictionary.csv"
df=pd.read_csv(path)
print(df)
#defi = df[df['word'] == 'accumulator']
#print(str(defi['definition']))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def api(word):
    defi= df[df['word'] == word]
    defini=str(defi['definition'])
    return  { "word": word,"defintion":defini}

app.run(debug=True)
