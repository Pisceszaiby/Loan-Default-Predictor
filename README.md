## Loan-Default-Predictor

To select the most suitable and optimal machine learning model that can accurately predict loan default based on loan information, borrower information, financial indicators, collateral information, etc. 
Loan default prediction is commonly treated as a binary classification problem where the objective is to predict whether a loan will default or not. This problem involves assigning one of two classes to each loan: default (indicating non-payment) or non-default (representing successful repayment). It is represented as a binary outcome. By analyzing historical data and utilizing various features, machine learning models can be trained to estimate the likelihood of default for future loans.

### Group Members:
- [Zainab Anwaar](https://github.com/Pisceszaiby)
- [Sadia Rehman](https://github.com/sadiarehman)
- [Hafsa Tariq](https://github.com/h-afsatariq)

### Dataset Description:
The Loan Default Prediction dataset typically uses various features such as Loan Amount, Funded Amount, Interest Rate, Loan Title, Debit to Income, etc. to predict whether a person is a loan defaulter. It uses machine learning models to predict the likelihood of loan defaulting. 

Total Entries: 67463
Columns: 35
Target Column (‘Loan Status’) values: 0, 1

![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/57f7d2f8-0305-4a1f-b0f7-57ea50a7bab6)


### Data Exploration and Preprocessing
Firstly, the number of unique values in each column has been observed. Certain attributes which give only a single value (Loan Title, Payment Plan, Accounts Delinquent) are removed from the dataset. 
Secondly, categorical data is converted to numerical data: For ’Loan Status’ (target column), LabelEncoder has been used. For x inputs, mappings have been performed on ‘Employment Duration’, ‘Verification Status’, ‘Initial List Status’, and ‘Application Type’. Mapping Encoding has been used instead of One-hot encoding since the categorical variables have a greater number of categories and represent an ordinal relationship (for example: 'Not Verified':0,'Source Verified':1,'Verified':2)
After the removal of unnecessary features, the dataset now holds 28 columns. In the next step, the dataset is analyzed for missing values (which have not been found in any of the entries). 
To drop more features in the dataset, the correlation matrix has been plotted to find the correlation of the features with the target feature. The matrix did not indicate a high correlation with the target feature for any specific features. So, the features were not dropped based on the correlation matrix.

### Detection of Outliers In Data:
Through the use of Box Plots, the attributes containing outliers have been identified visually i.e. "Funded Amount Investor","Interest Rate", "Home Ownership", "Debit to Income", "Open Account", "Revolving Balance","Total Accounts", "Total Received Interest", "Total Current Balance", "Total Revolving Credit Limit","Recoveries","Collection Recovery Fee","Total Received Late Fee", "Last week Pay","Total Collection Amount". 
The skewness of these features is reduced through Interquartile Range (IQR) method. The IQR methods detects outliers which are present above the specified Upper Limit and specified Lower Limit. It caps the outliers present above the Upper Limit to the Upper Limit and caps the outliers present below the lower limit to the Lower Limit of the feature. Hence the skewness in each specified feature was reduced.

### Dealing With Imbalance
The dataset was found to be quite imbalanced. When the values of the target column are calculated, the count of 0 and 1 occurrences turn out to be 61222 and 6241 respectively. This imbalance has been addressed through 2 common techniques:
##### ●	Oversampling
##### ●	Undersampling
The results are observed after applying both approaches. When the majority class was undersampled, the accuracies of the machine learning models decreased noticeably. Furthermore, it decreased the size of the dataset which led to inefficient training of the model. 
On the other hand, oversampling (duplicating examples of the minority class i.e. ‘1’) gives better outcomes. After oversampling the dataset contains 122444 examples. 


### Model Selection And Training:
##### •	Data Splitting: 
Test data: 30 %
Training data: 70%
##### •	Models Considered for this Dataset: (KNN, Gaussian NB, LR)
1.	XGBoost
2.	Decision Tree Classifier
3.	Random Forest Classifier


### Results After Hypertuning:
Hypertuning improves the performance of the models, as indicated by their accuracies. In case of Random Forest, accuracy is 1 while for decision tree model, the metric values at 0.96. It is evident that Random Forest performs better than Decision tree model so the final model used for this loan default prediction dataset is Random forest.

### Model Deployment:
The final trained model has been deployed as a web application using Flask. A Flask application has been created and Jinja- for the HTML template has been used. The machine learning model is persisted as a serialized Python object in a .sav file. It is loaded in the Flask application’s app.py file using joblib.load(). Flask's request module has been used to handle incoming requests, preprocess the data, and pass it to the model for prediction. The 'predict' method of the pre-trained model is called to predict the possibility of loan default. The results are displayed by rendering the result_Yes.html and result_No.html template and passing the predicted value as a parameter accordingly. 

### Visualization:
![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/12152fb6-b882-4f6d-a463-1a59e1cec221)
![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/4628ad8b-b7aa-46ea-a049-99a48695db5f)
![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/dfdc083b-7253-4e89-be93-65f6826bb122)
![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/6cd73225-8d44-4b47-b025-b81a64c5ca6c)

### Summary of ResultsS:
![image](https://github.com/Pisceszaiby/Loan-Default-Predictor/assets/52016745/56c45644-5ab7-4e95-a442-7565ce2e463a)

### Conclusion:
The project has helped in the understanding of data and models and the application of techniques for dataset analysis, data cleaning, feature engineering, model selection, and deployment. It has greatly aided in gaining insight into the process of solving problems through the knowledge of machine learning. Furthermore, it has improved the analysis of different machine-learning models and how they apply to our given problems in addition to their comparison against one another. 
In summary, the combination of Random Forest's versatility, ability to capture complex relationships, robustness against overfitting, handling of imbalanced data, and feature importance estimation makes it a suitable choice for loan default prediction datasets.
