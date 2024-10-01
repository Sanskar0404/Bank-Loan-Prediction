# **Bank Loan Prediction**

This project focuses on predicting whether a customer will be granted a loan based on certain financial and personal attributes. The model is built using the **Decision Tree algorithm** in Python, making use of various libraries for data processing, model building, and evaluation.


## **Overview**
The goal of this project is to predict loan approval based on features such as customer income, credit history, and other demographic attributes. The decision tree algorithm helps in identifying patterns and making predictions that are easy to interpret.

## **Dataset**
The dataset contains the following features:

- **Loan_ID**: Unique identifier for each loan application.
- **Age**: Age of the applicant.
- **Gender**: Gender of the applicant (Male/Female).
- **Married**: Marital status of the applicant (Yes/No).
- **Dependents**: Number of dependents.
- **Education**: Educational qualification (Graduate/Not Graduate).
- **Self_Employed**: Whether the applicant is self-employed (Yes/No).
- **ApplicantIncome**: The income of the applicant.
- **LoanAmount**: The loan amount applied for.
- **Previous_Loan_Taken**: Whether the applicant has taken a loan before (Yes/No).
- **Cibil_Score**: The applicant's CIBIL score.
- **Property_Area**: The type of area in which the property is located (Urban/Semiurban/Rural).
- **Customer_Bandwith**: Customer bandwidth.
- **Tenure**: The tenure of the loan.
- **Loan_Status**: The target variable, indicating whether the loan was approved (Y/N).

## **Tools and Libraries**
This project was implemented using Python, with the following libraries:
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **Scikit-learn**: Model building and evaluation
- **Matplotlib/Seaborn**: Data visualization

## **Methodology**
1. **Data Preprocessing**:
   - Handle missing values.
   - Convert categorical features into numerical ones.
   - Perform feature scaling.

2. **Model Selection**:
   - A Decision Tree classifier was chosen due to its interpretability and ability to handle both categorical and numerical data.

3. **Model Evaluation**:
   - Metrics such as accuracy, precision, recall, and F1-score were used to evaluate model performance.

## **Modeling**
The Decision Tree algorithm was applied to the preprocessed data, where the model split the dataset based on the most important features to make predictions. The model was tuned to avoid overfitting by setting a maximum depth for the tree.

## **Conclusion and Solution**
The Decision Tree algorithm was able to successfully predict loan approvals with a satisfactory level of accuracy. The model identified key factors like **Cibil_Score**, **ApplicantIncome**, and **LoanAmount** as critical in predicting whether a customer is likely to be approved for a loan.

The solution can be used by banks to automate and streamline their loan approval process, allowing for faster decision-making based on historical data. Additionally, this model can serve as a foundation for future enhancements, such as incorporating more advanced algorithms or additional features for better accuracy.
