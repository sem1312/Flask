from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/brol")
def brol():
    return render_template("brol.html")

@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

if __name__ == "__main__":
    app.run(debug=True, port=3500)

