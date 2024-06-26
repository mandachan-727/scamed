import streamlit as st
import random
import pandas as pd

# Read the csv file
df = pd.read_csv('data/scams.csv')

# Convert the dataframe to a dictionary
scams = df.set_index('Scam').T.to_dict('records')[0]

# Function to simulate scam conversation
def scam_conversation(scam_type):
    # Add your conversation logic here
    pass

# Function to learn about scams
def learn_about_scams(scams, columns=3, initial_lines=3):
    st.write("Choose a scam to learn about:")

    # Initialize the session state if not already done
    if 'expanded' not in st.session_state:
        st.session_state.expanded = False

    # Function to toggle the expanded state
    def toggle_expand():
        st.session_state.expanded = not st.session_state.expanded

    # Determine the number of scams to display based on the expanded state
    scam_keys = list(scams.keys())
    total_scams = len(scam_keys)
    lines_to_display = total_scams if st.session_state.expanded else initial_lines
    lines_to_display = min(lines_to_display, total_scams)

    # Display the scam buttons in columns inside a container
    with st.container(height = 150, border= False):
        for i in range(0, lines_to_display * columns, columns):
            cols = st.columns(columns)
            for j, col in enumerate(cols):
                if i + j < total_scams:
                    scam = scam_keys[i + j]
                    if col.button(scam):
                        st.session_state.selected_scam = scam

    # Display the description of the selected scam outside of the container
    if 'selected_scam' in st.session_state and st.session_state.selected_scam in scams:
        st.write(scams[st.session_state.selected_scam])

    # Button to show more or less scams
    if st.session_state.expanded:
        if st.button("_Less_", on_click=toggle_expand):
            pass
    else:
        if st.button("_More_", on_click=toggle_expand):
            pass


# Main function for the Streamlit app
def main():
    st.title("Scam Awareness Chatbot")

    option = st.selectbox("Choose an option", ("Learn about scams", "Practice identifying scams"))

    if option == "Learn about scams":
        learn_about_scams(scams)
    elif option == "Practice identifying scams":
        scam_type = random.choice(list(scams.keys()))
        scam_conversation(scam_type)

if __name__ == "__main__":
    main()
