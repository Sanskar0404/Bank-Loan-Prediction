import numpy as np
import pickle 
import math
from Flask import flask, request, jsonify,render_template

app = Flask(__name__,template_folder="template",static_folder = "staticfiles")##assign Flask
model= pickle.load(open('build.pkl','rb')) ## import model

@app.route('/')
def home():
    return render_template('index.html')##read index.html file

@app.route('/predict',methods=['POST']) ## transfer data from html to python/server

def predict():
    int_features =[int(x) for x in request.form.values()] #request for data values
final_features= [np.array(int_features)] #convert into array
predict = model.predict(final_features)##predict
if prediction ==0:
    return render_template('index.html', prediction_text ="Loan is Rejected").format(prediction)
else:
    return render_template('indedx.html',prediction_text="Loan is Apporoved").format(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)




