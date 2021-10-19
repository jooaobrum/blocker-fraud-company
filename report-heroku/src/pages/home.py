import streamlit as st


def write():

	st.title("Home")

	st.write(
		"""

	## About the Blocker Fraud Company:

	Blocker Fraud Company is a company specialized in the detection of fraud in financial \
	transactions made through mobile devices. The company has a service called “Blocker Fraud” \
	which guarantees the blocking of fraudulent transactions. And the company's business model is \
	of the Service type, with monetization made by the performance of the service provided, that is, \
	the user pays a fixed fee on the success in detecting fraud in the client's transactions.

	### Business Model Strategy:
	- The company will receive 25% of the value of each transaction that is truly detected as fraud.
	- The company will receive 5% of the value of each transaction detected as fraud, however the transaction is truly legitimate.
	- The company will return 100% of the value to the customer for each transaction detected as legitimate, however the transaction is truly a fraud. With this aggressive strategy, the company assumes the risks of failing to detect fraud and is compensated for assertively detecting fraud.
	   
	### The Challenge: 

	- Creating an highly accurate model for detecting fraud in transactions made through mobile devices;
	- Provide an API hosted in some cloud to classify them as fraudulent or legitimate;
	- Provide a report for the solution.


	   """ )