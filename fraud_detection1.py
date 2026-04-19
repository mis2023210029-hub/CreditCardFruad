import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title('Fraud Detection Prediction App!')
st.markdown('Please enter the transaction details and use the predict button')
st.divider()

# 2. Input Fields
transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT', 'CASH_IN'])
amount = st.number_input('Amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input('New Balance (Sender)', min_value=50.0, value=9000.0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value=50.0, value=10000.0)
newbalanceDest = st.number_input('New Balance (Receiver)', min_value=50.0, value=1000.0)

# 3. Prediction Logic
if st.button('Predict'):
    # Create the DataFrame with exact column names used during training
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    }])

    # Add the Feature Engineering columns that the model expects
    input_data['balanceDiffOrig'] = input_data['oldbalanceOrg'] - input_data['newbalanceOrig']
    input_data['balanceDiffDest'] = input_data['newbalanceDest'] - input_data['oldbalanceDest']

    # Manual Logic Check: Does (Old - New) equal the Amount?
    # This catches cases where the model says '0' but the math is suspicious.
    actual_deduction = oldbalanceOrg - newbalanceOrig
    is_math_wrong = abs(actual_deduction - amount) > 0.01  # Allow for small float errors
    
    # Get model prediction
    prediction = model.predict(input_data)[0]
    
    st.divider()
    
    # 4. Display Results
    if prediction == 1 or is_math_wrong:
        st.subheader("Prediction Result: '1'")
        st.error('⚠️ This transaction is flagged as suspicious!')
        
        if is_math_wrong:
            st.warning(f"Reason: Balance mismatch. Sender lost ${actual_deduction:.2f} but only sent ${amount:.2f}.")
        if prediction == 1 and not is_math_wrong:
            st.warning("Reason: Model identified a known fraud pattern (e.g., high-risk TRANSFER).")
            
    else:
        st.subheader("Prediction Result: '0'")
        st.success('✅ This transaction looks legitimate.')