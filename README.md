# Disease Outbreaks Prediction

## Overview
The **Disease Outbreaks Prediction** project is a Machine Learning-based application that predicts the likelihood of **Diabetes, Heart Disease, and Parkinson's Disease** based on user inputs. The application is built using **Streamlit** for an interactive and user-friendly experience.

## Features
- **Diabetes Prediction**: Predicts diabetes risk based on user health parameters.
- **Heart Disease Prediction**: Assesses the probability of heart disease.
- **Parkinson's Disease Prediction**: Identifies potential signs of Parkinson's disease.
- **User-Friendly Interface**: Built using **Streamlit** for a seamless experience.
- **Deployed Online**: Accessible at [Disease Outbreaks Prediction App](https://diseaseoutbreaksprojectbythrisha.streamlit.app/).

## Tech Stack
- **Python**
- **Machine Learning (Scikit-Learn, Pandas, NumPy)**
- **Streamlit** (for UI)
- **Pickle** (for model serialization)

## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/disease-outbreaks-prediction.git](https://github.com/DatawhizThrisha/Prediction_of_Disease_Outbreaks.git
cd Prediction_of_Disease_Outbreaks
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

## Model Training
The models were trained using datasets from reliable medical sources. Each dataset was preprocessed, and various ML models were tested to select the best-performing ones.

### Steps:
1. **Data Preprocessing**: Handling missing values, scaling features.
2. **Model Selection**: Logistic Regression, Decision Trees, Random Forest, and SVM.
3. **Evaluation**: Models were evaluated using accuracy, precision, recall, and F1-score.
4. **Serialization**: The best models were saved using `pickle`.

## Deployment
The project is deployed on **Streamlit Cloud** and can be accessed at:
🔗 **[Disease Outbreaks Prediction App](https://diseaseoutbreaksprojectbythrisha.streamlit.app/)**

## Usage
1. Open the [app link](https://diseaseoutbreaksprojectbythrisha.streamlit.app/).
2. Select the disease you want to predict.
3. Enter the required health parameters.
4. Click "Predict" to see the results.

## Future Enhancements
- Addition of more diseases for prediction.
- Integration with a database for storing user inputs.
- Deploying a more scalable backend with Flask/Django.

## Author
👩‍💻 **Thrisha** - [GitHub Profile](https://github.com/DatawhizThrisha)

