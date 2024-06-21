import streamlit as st
import random
import pandas as pd

# List of scams and their definitions

# Read the csv file
df = pd.read_csv('scams.csv')

# Convert the dataframe to a dictionary
scams = df.set_index('Scam').T.to_dict('records')[0]

# Function to simulate scam conversation
def scam_conversation(scam_type):
    # Add your conversation logic here
    pass

# Main function for the Streamlit app
def main():
    st.title("Scam Awareness Chatbot")

    option = st.selectbox("Choose an option", ("Learn about scams", "Practice identifying scams"))

    if option == "Learn about scams":
        scam_type = st.selectbox("Choose a scam to learn about", list(scams.keys()))
        st.write(scams[scam_type])

        # Loop to allow user to learn about other scams
        while st.button("Learn about another scam"):
            scam_type = st.selectbox("Choose another scam to learn about", list(scams.keys()))
            st.write(scams[scam_type])

    elif option == "Practice identifying scams":
        scam_type = random.choice(list(scams.keys()))
        scam_conversation(scam_type)

if __name__ == "__main__":
    main()


