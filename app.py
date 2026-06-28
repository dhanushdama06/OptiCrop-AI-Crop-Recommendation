from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("notebooks/model.pkl", "rb"))
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

    return render_template("predict.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)