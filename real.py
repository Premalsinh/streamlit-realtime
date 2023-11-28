import streamlit as st
import time
import pandas as pd
import numpy as np

# Function to simulate streaming data
def generate_data():
    while True:
        # Simulate streaming data (replace this with your actual data source)
        data = pd.DataFrame({
            'Timestamp': [pd.Timestamp.now()],
            'Value': [np.random.rand()]
        })

        # Display the streaming data in the Streamlit app
        st.add_rows(data)

        # Sleep to simulate real-time updates
        time.sleep(10)

# Main Streamlit app
def main():
    st.title("Real-Time Streaming in Streamlit")

    # Start streaming data
    st.table()
    generate_data()
   

if __name__ == "__main__":
    main()
