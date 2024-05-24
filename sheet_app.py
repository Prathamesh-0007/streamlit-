import streamlit as st
import pandas as pd
import os

# Function to insert data into CSV
def insert_into_csv(data, csv_file='user_data.csv'):
    # Check if the CSV file exists
    if os.path.exists(csv_file):
        # If it exists, load the existing data
        df = pd.read_csv(csv_file)
    else:
        # If it does not exist, create an empty DataFrame with the correct columns
        df = pd.DataFrame(columns=['User Name', 'Phone Number', 'Email ID', 'Designation'])
    
    # Append the new data as a new row
    new_row = pd.DataFrame([data], columns=['User Name', 'Phone Number', 'Email ID', 'Designation'])
    df = pd.concat([df, new_row], ignore_index=True)
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

# Streamlit form
st.title("User Information Form")

with st.form("user_info_form"):
    user_name = st.text_input("User Name")
    phone_number = st.text_input("Phone Number")
    email_id = st.text_input("Email ID")
    designation = st.selectbox("Designation", ["Software Engineer", "Senior Software Engineer", "Data Scientist", "Implementation", "DevOps"])
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if user_name and phone_number and email_id and designation:
            data = [user_name, phone_number, email_id, designation]
            insert_into_csv(data)
            st.success("Data has been successfully submitted!")
        else:
            st.error("Please fill all the fields.")
