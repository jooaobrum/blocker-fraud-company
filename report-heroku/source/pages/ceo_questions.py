import streamlit as st

def write():

	st.title("CEO Questions")

	st.write(
		"""

	**1. What is the Precision and Accuracy of the model?**

	The Precision of the model (Random Forest) after cross-validation is between 99.96% and 100%. Also, the accuracy achieved is 100%.

	**2. How Reliable is the model in classifying transactions as legitimate or fraudulent?**
	
	The model has performed very well to classify new transactions. Using the test dataset, we could classify correctly 99.6% of the fraudulent transactions.

	**3. What is the Company's Expected Revenue if we classify 100% of transactions with the model?**
	
	Using the model, the company receives an estimated revenue of $950,509,043.18 from 2655 transactions detect as a fraud and $135.88 from 3 transactions classified as possible frauds.

	**4. What is the expected loss by the company in case of model failure?**

	The client's expected loss in case of model failure is about $946,963,857.77.

	**5. What is the expected profit for the client and for the Blocker Fraud Company when using the model?**

	The profit of Blocker Fraud Company when using the model is $946,963,857.77 and  the client has a profit of $2,858,617,636.23.

	   """ )


	