# Credit Risk Prediction with Random Forest

This project predicts credit risk using a **Random Forest model**. It includes:
1. A **Flask API** to serve predictions.
2. A **web-based front-end** for user interaction.
3. Scripts and notebooks for **data preparation** and **model training**.

---

## **Overview**

The project consists of:
- **Back-End**: A Flask API that uses a pre-trained Random Forest model to predict credit risk.
- **Front-End**: A simple web-based interface where users input feature values to get predictions.
- **Data Preparation**: Jupyter notebooks and Python scripts for cleaning the data and training the model.

---

## **Project Structure**

```
CREDIT_RISK_PROJECT/
├── app/                    # Flask back-end
│   └── app.py              # API code
├── data/                   # Data files
│   ├── german_credit_data.csv
│   ├── preprocessed_german_credit_data.csv
│   └── renamed_german_credit_data.csv
├── frontend/               # Front-end code
│   ├── images/
│   │   └── background.png  # Background image for the front-end
│   ├── index.html          # Front-end HTML file
│   └── Dockerfile          # Dockerfile for front-end container
├── notebooks/              # Jupyter notebooks
│   └── data_cleaning.ipynb # Notebook for data cleaning and exploration
├── outputs/                # Saved model and feature files
│   ├── feature_names.pkl   # Encoded feature names
│   └── random_forest_model.pkl # Trained Random Forest model
├── scripts/                # Scripts for data processing
│   └── load_data.py        # Script to preprocess the dataset
├── .dockerignore           # Docker ignore file
├── Dockerfile              # Back-end Dockerfile
├── requirements.txt        # Python dependencies for Flask API
└── README.md               # Project documentation
```

---

## **Getting Started**

### **Requirements**
- Docker
- Python 3.9+ (for local development)

---

## **Steps to Run the Project**

### **Step 1: Run the Back-End**

1. Navigate to the root directory of the project:
   ```bash
   cd CREDIT_RISK_PROJECT
   ```
2. Build the Docker image for the Flask API:
   ```bash
   docker build -t credit-risk-api .
   ```
3. Run the Flask container:
   ```bash
   docker run -p 5000:5000 credit-risk-api
   ```
4. The API will be available at `http://127.0.0.1:5000`.
   If the API runs, you may see a 404 error (this is normal since / is not defined). The endpoint /predict will process requests.

---

### **Step 2: Run the Front-End**

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Build the Docker image for the front-end:
   ```bash
   docker build -t credit-risk-frontend .
   ```
3. Run the front-end container:
   ```bash
   docker run -p 8080:80 credit-risk-frontend
   ```
4. The front-end will be available at `http://127.0.0.1:8080`.

---

### **Step 3: Test the Application**

#### **Using the Front-End**
1. Open your browser and go to `http://127.0.0.1:8080`.
2. Enter feature values in the form and click **Predict**.
3. View the prediction results displayed on the page.

#### **Using `curl`**
Test the API directly by sending a POST request:
```bash
curl -X POST -H "Content-Type: application/json" -d \
"{\"features\": [0.0, 1.0, 25.0, 5000.0, 2.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0]}" \
http://127.0.0.1:5000/predict
```
Expected output (example):
```json
{
  "prediction": "Good",
  "probability": 0.85
}
```

---

### **Optional: Run Both Containers with Docker Compose**

1. Create a `docker-compose.yml` file in the root directory:
   ```yaml
   version: '3.8'
   services:
     backend:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - "5000:5000"
     frontend:
       build:
         context: ./frontend
         dockerfile: Dockerfile
       ports:
         - "8080:80"
   ```
2. Run both containers:
   ```bash
   docker-compose up
   ```
3. Access the front-end at `http://127.0.0.1:8080` and the back-end at `http://127.0.0.1:5000`.

---

## **Environment Requirements**

### **Python Dependencies (Back-End)**
The Flask API requires the following Python packages. These are listed in `requirements.txt`:
```plaintext
flask
flask-cors
pandas
scikit-learn
```

### **Conda Environment (Optional)**
If using Conda, create the environment using `environment.yml`:
```yaml
name: credit-risk
channels:
  - defaults
dependencies:
  - python=3.9
  - flask
  - flask-cors
  - pandas
  - scikit-learn
```
To create the environment:
```bash
conda env create -f environment.yml
conda activate credit-risk
```

---

## **Testing and Debugging**

### **Logs**
- To debug issues, check the logs of each container:
  - For the back-end:
    ```bash
    docker logs <container_id>
    ```
  - For the front-end:
    ```bash
    docker logs <container_id>
    ```

### **Updating the Model**
1. Train a new model using `data_cleaning.ipynb` or `load_data.py`.
2. Save the updated `random_forest_model.pkl` and `feature_names.pkl` in the `outputs/` folder.
3. Rebuild and restart the back-end container.

---

## **Acknowledgments**
- Flask for the back-end framework.
- Scikit-learn for machine learning.
- Docker for containerization.
- Nginx for serving the front-end.
```
