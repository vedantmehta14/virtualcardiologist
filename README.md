# Virtual Cardiologist

The Virtual Cardiologist project is an innovative solution designed to assist in the early detection and diagnosis of cardiovascular diseases using machine learning. The system leverages predictive models trained on medical data to identify potential heart-related conditions, providing support to healthcare professionals and patients for timely decision-making.

## Project Overview

This project aims to build a machine learning-based tool that can analyze patient data and predict the risk of heart disease. The Virtual Cardiologist is intended to complement the expertise of medical professionals by providing data-driven insights and increasing the accuracy of preliminary diagnoses.

## Features

- **Data Preprocessing**: Cleans and prepares medical datasets for training.
- **Machine Learning Model**: Uses algorithms such as logistic regression, random forest, and support vector machines to build a robust predictive model.
- **Performance Evaluation**: Evaluates model accuracy using metrics like precision, recall, F1-score, and ROC-AUC.
- **User Interface**: A simple interface for inputting patient data and displaying results.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Scikit-learn for model development and evaluation
  - Pandas and NumPy for data manipulation
  - Matplotlib and Seaborn for data visualization
  - Streamlit for creating a web-based interface

## Dataset

The project uses publicly available medical datasets that include features such as age, cholesterol levels, blood pressure, and other health indicators. These datasets are preprocessed to ensure data quality and reliability.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/vedantmehta14/virtualcardiologist.git
    ```
2. Navigate to the project directory:
    ```bash
    cd virtualcardiologist
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Jupyter Notebook (`Virtual Cardiologist.ipynb`) to explore data preprocessing, model training, and evaluation.
2. Modify parameters or experiment with different algorithms as needed.
3. To launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. Access the web application at `http://localhost:8501`.

## Model Performance

The project's notebook includes detailed performance evaluations for the models used, including metrics and plots for better analysis. Fine-tuning and cross-validation are applied to ensure optimal performance.

## Future Enhancements

- Expanding the feature set to include more complex health indicators.
- Integration with electronic health record (EHR) systems.

## Contact

For questions, feedback, or collaboration inquiries:
- **Author**: Vedant Mehta
- **Email**: mehtavedant8@gmail.com

