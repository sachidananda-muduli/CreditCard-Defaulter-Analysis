# CreditCard-Defaulter-Analysis

## 🎯 **Project Overview**
This project is a **web application** designed to predict the likelihood of a credit card default based on various financial and personal factors. Utilizing a machine learning model, the application offers real-time predictions through an intuitive and user-friendly web interface, ensuring secure handling of sensitive financial data.

## ✨ **Features**
- 🌐 **Web-Based Interface**: Easily input customer data through a simple form.
- ⚡ **Real-Time Prediction**: Instantly receive predictions based on a pre-trained machine learning model.
- 🔒 **Secure Data Handling**: Sensitive information is securely processed and managed.
- 📱 **Responsive Design**: Optimized for use across a wide range of devices.
- 📊 **Prediction Results**: Clear indication of whether a credit default is likely or unlikely based on the provided data.

## 🛠️ **Technology Stack**
- **Backend**: ![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- **Frontend**: ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- **Machine Learning**: ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
- **Data Preprocessing**: StandardScaler



## 🚀 **Installation**

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/credit-card-default-prediction.git
    cd credit-card-default-prediction
    ```

2. **Install Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

## 🧑‍💻 **Usage**

1. **Ensure Model Files are in Place**:
   - Place the trained model (`clf2.pkl`) and scaler (`train_scaler.pkl`) in the `models/` directory.

2. **Run the Flask Application**:
    ```sh
    python main.py
    ```

3. **Access the Web Interface**:
   - Open a web browser and navigate to `http://localhost:5000`.

4. **Input Data & Predict**:
   - Fill out the form with the necessary details and submit to receive the prediction.
   - The application will return a result indicating whether a **"Default is likely"** or **"Default is unlikely"**.

## 🧠 **Model Information**
The prediction model implemented in this project is a **[e.g., Random Forest Classifier]** trained on historical credit card data. It analyzes various features such as credit limit, payment history, bill amounts, and personal demographics to predict the likelihood of default.

## 🌟 **Project Highlights**
- **Form Handling**: The application accepts various financial inputs from the user, including credit limit, payment history, bill amounts, and payment amounts.
- **AJAX Integration**: Supports real-time prediction updates without needing to refresh the page.
- **Scalability**: The application is designed to be easily extended with more complex models or additional input features.

## 📸 **Screenshots**
Include screenshots of your web interface here to showcase the UI and prediction results.

## 🤝 **Contributing**
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 📧 **Contact**
For any questions or suggestions, feel free to reach out.

- **GitHub**: [yourusername](https://github.com/sachidananda-muduli)
- **Email**: bapsmuduli69@gmail.com
