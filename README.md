# Compressive_strength
This is compressive strength predictor app that can predict compressive strength of a material using given four parameters 
-Grade
-UPV
-Rebound
-Age

First a random forest regressor model has been trained of google collab using given dataset, the data has been visualised and tested with accuracy scores of r2 error upto 0.63 to 0.83. 
The model predicts two values "STRENGTH TO" and "STRENGTH FROM" ,the pickel file then for the trained model has been generated using pickle libray , The code for training the model on google collab has been provided in comp_strength.ipynb file
A flask api is then used to pass the parametes to pickle file and predict the two values , POST method is used and the api is tested using postman.
The flask api is then deployed on an AWS EC2 linux instance and the server is made live on http://13.232.91.214 , This server is then used to send POST predict request to api which then predicts using the pickle file and sends response back to the endpoint
A simple android application which uses volley libraries has been used as a GUI to take parameters from user and send api request to flask server on the EC2 instance, the response from the api call i.e the predicted values is then shown on the application
