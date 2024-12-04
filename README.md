# MSc Project: Predicting Petroleum Presence with Regression  



https://github.com/user-attachments/assets/356299b0-587d-4a9e-b807-17f9b85e969a


## Overview  
This project, completed as part of my MSc in Nuclear Engineering, focuses on building an end-to-end solution to predict the **drad column**, which indicates the presence of petroleum in a given area. The solution combines:  
- **Data preprocessing**  
- **Exploratory Data Analysis (EDA)**  
- **Linear Regression Modeling**  
- **Deployment** via Flask and Docker  

The model achieved an exceptional **Mean Squared Error (MSE)** of **7.47e-31** on the test dataset.  

---

## Links  
- **GitHub Repository**: [GitHub](https://github.com/Mouradadel1919/DRAD_Prediction)  
- **Docker Image**: [Docker Hub](https://hub.docker.com/r/mouradadel313/drad_flask)

---

## Key Features  
1. **Data Preprocessing**: Cleaned and transformed raw data for analysis.  
2. **Exploratory Data Analysis (EDA)**: Visualized and analyzed patterns in the dataset.  
3. **Regression Model**: Built and evaluated a linear regression model.  
4. **Deployment**: Exposed the model through a Flask API and containerized it using Docker for broader accessibility.  

---

### Run with Docker  
Pull the Docker image and start the container:  
```bash  
docker pull mouradadel313/drad_flask:latest
docker run -p 5000:5000 mouradadel313/drad_flask:latest  
```  
The API will be available at `http://127.0.0.1:5000/`.  

---

## Run with Flask 

### Clone the Repository  
```bash  
git clone https://github.com/Mouradadel1919/DRAD_Prediction.git
cd DRAD_Prediction
```  

### Install Requirements  
```bash  
pip install -r requirements.txt  
```  

### Run Flask API  
Start the Flask API locally:  
```bash  
python app.py  
```  
Access the API at `http://127.0.0.1:5000/`.  



## API Usage  

### Predict Endpoint  
- **URL**: `/predict`  
- **Method**: `POST`  
- **Input**: A JSON object with required features.  
- **Output**: Predicted `drad` value.  


## Results  
- **Mean Squared Error (MSE)**: `7.47e-31`  
This demonstrates high model accuracy and its potential for practical use in petroleum exploration.  

---

