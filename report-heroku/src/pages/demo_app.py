import streamlit as st
import pandas as pd
import time
import requests
import json


def write():

	st.title("Demo Web App")

	st.write(
		"""

	## Demonstration of Blocker Fraud API:

	In order to provide a simple solution, we developed an API on Heroku which can be used to classify wheter a transaction is fraudulent or legitimate.
	The customer has transaction information based on activities on the page. With that in mind, we developed this demonstration via web app so that new transactions can be uploaded in CSV format and so our model generates a classification according to the information contained. 


	   """ )

	st.subheader("Upload File:")

	uploaded_file = st.file_uploader("Choose a file")
	if uploaded_file is not None:
		df = pd.read_csv(uploaded_file)
		st.write(df)


		with st.spinner('The model is classifying...'):
			time.sleep(2)

		# Convert dataframe to json
		data = json.dumps(df.to_dict(orient = 'records'))

		# API CALL
		url = 'https://blocker-fraud-api.herokuapp.com/blocker/predict'
		header = {'Content-type': 'application/json'}

		# Make the request
		r = requests.post(url, data = data, headers=header)
		
		st.write(f"Status code: {r.status_code}")

		df_results = pd.DataFrame(r.json(), columns = r.json()[0].keys())
		
		st.write(df_results)

		st.subheader("API Result:")

		for row in df_results.index:
			if df_results.loc[row]['pred'] == 0:
				st.write(f"Transaction from {df_results.loc[row]['name_orig']} to {df_results.loc[row]['name_dest']} is legitimate.")
			else:
				st.write(f"Transaction from {df_results.loc[row]['name_orig']} to {df_results.loc[row]['name_dest']} is fraudulent.")

		