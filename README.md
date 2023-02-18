SRE Challenge - LATAM Airlines

this repo consist files related to SRE challenge.

Objective:

The goal is to stress test the service. We will create a model and api service for the model to send request and get the prediction based on data.

At first we will deploy this application on local system to test the functionality and will do stress test.
With time, we can improve the infrastructure of the application (for eg. Running in kubernetes cluster or cloudrun service from google.)

 
Version 1

Performance: 
Here we can assume that application will get affected if the system goes down and to scale up the infrastructure, we need manual intervention.

Repository:
Git

Pikling file is created and provided in drive.
Need to create web service that interacts with api
Api request will be done using postman


Let’s create a model.

Pre-requisite-
Create python virtual environment and install dependencies.
python3 -m venv sre-challenge 
pip install flask
pip install flask-restful
pip install bumpy
pip install pandas
pip install scikit-learn

Will download a new dataset which consist flight related details.

Download flight data from https://raw.githubusercontent.com/plotly/datasets/master/flightdata.csv

Goal:
In a model.py file, we will develop and train our model.
Load the dataset.
Clean the dataset
Create model.pkl file based on the dataset.

Clean and prepare data
	Figure out “feature ” Columns that are relevant to the output we are predicting.
	Eliminate Missing values either by deleting rows or columns or adding meaningful values




Check for null value in the data set by creating new notebook-

(cleanandpreparedataset.ipynb notebook for test and validate results, added to repo)

Added file model.py.

Model.pkl file generated and stored in root directory



Uploaded changes to git https://github.com/tjtanmay/latam-sre/tree/feature/add_api_py


Execute python api.py to launch.




Load Testing.

Install wrk benchmark tool

After running load test for 30 seconds, using 12 threads, and keeping 400 HTTP connections open

tanmay@Tanmays-MacBook-Pro ~ % wrk -t12 -c400 -d30s http://127.0.0.1:5000/          
Running 30s test @ http://127.0.0.1:5000/
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    46.12ms   36.43ms 280.88ms   82.78%
    Req/Sec   158.69    100.23   595.00     66.61%
  10673 requests in 30.03s, 219.88MB read
  Socket errors: connect 0, read 10978, write 369, timeout 0
Requests/sec:    355.43
Transfer/sec:      7.32MB

tanmay@Tanmays-MacBook-Pro ~ % wrk -t12 -c50000 -d45s http://127.0.0.1:5000/
Running 45s test @ http://127.0.0.1:5000/
  12 threads and 50000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   104.15ms  162.43ms   1.61s    98.06%
    Req/Sec    25.00     46.66   424.00     92.23%
  4117 requests in 45.10s, 84.82MB read
  Socket errors: connect 47447, read 652563, write 3326, timeout 0
Requests/sec:     91.29
Transfer/sec:      1.88MB


Added post.lua script with body to request from API and triggered with script.




Conclusion:

Here we can see the performance of the service depends upon availability of resource of the local system. We have to manually bring up the service every time if service goes down. 
This kind of infrastructure is not good for production use rather, developer can follow the above steps to test their application locally quickly without depending upon infra.













