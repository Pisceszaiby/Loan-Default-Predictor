import flask
import pandas as pd
from joblib import load

with open('DeploymentModel.joblib', 'rb') as f:
    model = load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))
    if flask.request.method == 'POST':
        Loan_Amount = flask.request.form['LoanAmount']
        Funded_Amount = flask.request.form['FundedAmount']
        Funded_Amount_Investor = flask.request.form['FundedAmountInvestor']
        Term = flask.request.form['Term']
        Interest_Rate = flask.request.form['InterestRate']
        Employment_Duration = flask.request.form['EmpDuration']
        Home_Ownership = flask.request.form['HomeOwnership']
        Verification_Status = flask.request.form['VerificationStatus']
        Debit_to_Income = flask.request.form['DebtToIncomeRatio']
        Delinquency = flask.request.form['DelinquenciesInLast2Years']
        Inquires_six_months = flask.request.form['InquiriesInLast6Months']
        Open_Account = flask.request.form['OpenAccounts']
        Public_Record = flask.request.form['PublicRecords']
        Revolving_Balance = flask.request.form['RevolvingBalance']
        Revolving_Utilities = flask.request.form['RevolvingUtilities']
        Total_Accounts = flask.request.form['TotalAccounts']
        Initial_List_Status = flask.request.form['w']
        Total_Received_Interest = flask.request.form['TotalReceivedInterest']
        Total_Received_Late_Fee = flask.request.form['TotalReceivedLateFee']
        Recoveries = flask.request.form['Recoveries']
        Collection_Recovery_Fee = flask.request.form['CollectionRecoveryFee']
        Collection_12_months_Medical = flask.request.form['med']
        Application_Type = flask.request.form['ApplicationType']
        Last_week_Pay = flask.request.form['LastWeekPay']
        Total_Collection_Amount = flask.request.form['TotalCollectionAmount']
        Total_Current_Balance = flask.request.form['TotalCurrentBalance']
        Total_Revolving_Credit_Limit = flask.request.form[
            'TotalRevolvingCreditLimit']

        incoming_vector = pd.DataFrame(
            [[
                Loan_Amount, Funded_Amount, Funded_Amount_Investor, Term,
                Interest_Rate, Employment_Duration, Home_Ownership,
                Verification_Status, Debit_to_Income, Delinquency,
                Inquires_six_months, Open_Account, Public_Record,
                Revolving_Balance, Revolving_Utilities, Total_Accounts,
                Initial_List_Status, Total_Received_Interest,
                Total_Received_Late_Fee, Recoveries, Collection_Recovery_Fee,
                Collection_12_months_Medical, Application_Type, Last_week_Pay,
                Total_Collection_Amount, Total_Current_Balance,
                Total_Revolving_Credit_Limit
            ]],
            columns=[
                'Loan Amount', 'Funded Amount', 'Funded Amount Investor',
                'Term', 'Interest Rate', 'Employment Duration',
                'Home Ownership', 'Verification Status', 'Debit to Income',
                'Delinquency - two years', 'Inquires - six months',
                'Open Account', 'Public Record', 'Revolving Balance',
                'Revolving Utilities', 'Total Accounts', 'Initial List Status',
                'Total Received Interest', 'Total Received Late Fee',
                'Recoveries', 'Collection Recovery Fee',
                'Collection 12 months Medical', 'Application Type',
                'Last week Pay', 'Total Collection Amount',
                'Total Current Balance', 'Total Revolving Credit Limit'
            ],
            dtype=float,
            index=['input'])
        prediction = model.predict(incoming_vector)[0]
        print('prediction is :', prediction)
        for i in incoming_vector:
            print(i)
        print('incoming vector is :', incoming_vector)
        if prediction == 1:
            return flask.render_template('result_Yes.html')
        elif prediction == 0:
            return flask.render_template('result_No.html')


if __name__ == '__main__':
    app.run(debug=True)