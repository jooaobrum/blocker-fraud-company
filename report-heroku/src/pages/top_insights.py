import streamlit as st
#import 

def write():

    st.title("Top Insights")

    option = st.selectbox(
                        'Select an hypothesis',
                        ('Select...',

                         'Transactions classified as transfer is more likely to be fraud.',    
                         'When the origin new balance is equal zero and the old balance is greater than zero, it is more likely to be fraud.',    
                         'When the error before and after a transaction in the destination side is different than zero, a fraud occurs.'))

    if option == 'Select...':
        pass
    
    elif option == 'Transactions classified as transfer is more likely to be fraud.':

        st.write(
            """
                ### FALSE 

                - Cash-Out and Transfer have almost the same number of fraud transactions, then it is not possible to affirm it. However, when compared with regular transactions, transfer type is significantly greater than the regular ones (49.9% x 8.3%).
            """

            )

        st.image('src/images/hypothesis_1.PNG')


    elif option == 'When the origin new balance is equal zero and the old balance is greater than zero, it is more likely to be fraud.':
        st.write(
            """
                ### TRUE 

                - Almost always when a fraudulent transaction happen, the newbalance_orig is zero (98%). The percentage of transactions that have newbalance_orig equal zero when is a regular transaction is 35.6%, quite different than the fraudulent ones.
            """

            )

        
        st.image('src/images/hypothesis_9.PNG')

    else:
        st.write(
            """
                ### TRUE 

                - There is a strong pattern that shows fraudulent transactions with error different than zero. 

                - Fraudulent transactions have both patterns, when the error is equal 0 and equal to the amount of money;
            
                - The scatterplot of fraudulent transactions shows when the error in destination account before and after a transaction is equal to the amount of money, a fraud occurs more likely (45º slope);
            
                
            """

            )

        st.image('src/images/hypothesis_12.PNG')

        st.write(
            """
                - Related to fraudulent transactions, only 35.2% have the error equal to zero, while the regular transactions have 66.8%.
                
            """
                )

        st.image('src/images/hypothesis_12_2.PNG') 

         



    