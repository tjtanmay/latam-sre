from flask import Flask, request
from flask import render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['POST','GET'])
def get_delay():
    if request.method=='POST':
        result=request.form
        print(result)
#Prepare the feature vector for prediction
        pkl_file = open('x_data', 'rb')
        index_dict = pickle.load(pkl_file)
        new_vector = np.zeros(len(index_dict))
  
        try:
               new_vector[index_dict['Terminal_'+str(result['Terminal'])]] = 1            
        except:
                 pass
        try:
                new_vector[index_dict['Weekday_'+str(result['Weekday'])]] = 1
        except:
                pass
        try:
               new_vector[index_dict['Airline_'+str(result['Airline'])]] = 1
        except:
                pass
        try:
                new_vector[index_dict['Origin_'+str(result['Origin'])]] = 1
        except:
                pass
        try:
                new_vector[index_dict['Destination_'+str(result['Destination'])]] = 1
        except:
                pass
        try:
                new_vector[index_dict['ScheduledTime_'+str(result['ScheduledTime'])]] = 1
        except:
                pass
            
        pkl_file = open('model_v1.pkl', 'rb')
        adamodel = pickle.load(pkl_file)
        new_vector = new_vector.reshape(1, -1)
        Prediction = adamodel.predict(new_vector)
        for i in Prediction:
               if i == 1:
                      Prediction ="will be"
               if i == 0:
                      Prediction ="won't get"
            
    return render_template('results.html',prediction=Prediction)       


    
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
