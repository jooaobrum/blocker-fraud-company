import streamlit as st


def write():

	st.title("Results")

	st.write(
		"""

	### Model Results:

	The dataset provided has **0.13%** of fraudulent data.
	Our model achieved **99%** of Precision to detect a fraudulent transaction, which means 2655 frauds detected correcly in one month (dataset provided).

	### Blocker Fraud Company Financial Results:

	The company receives an estimated revenue of **$950,509,043.18** from 2655 transactions detect as a fraud.
	
	The company receives an estimated revenue of **$135.88** from 3 transactions classified as possible frauds.
	
	The company has to pay as charge back an estimated amount of **$3,545,321.29** from 11 transactions that the model lost.
	
	Estimated profit: **$946,963,857.77**

	### Client Benefits:

	The client could lost **$3,805,581,494.00** due to the fraudulent transactions.
	
	Using the blocker fraud model, the client actually lost **$946,963,857.77** (payment to the Blocker Fraud Company).
	
	Finally, the client saved **$2,858,617,636.23**.

	   """ )