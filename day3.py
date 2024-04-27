import streamlit as st

# Display the title and mission statement
st.title("Welcome to Treasure Island!")
st.write("Your mission is to find the treasure.")

# Create a key to track progress through the game
if "stage" not in st.session_state:
    st.session_state.stage = 0

# Step 1: Choose Left or Right
if st.session_state.stage == 0:
    with st.form("form1"):
        path1 = st.radio("Choose a path:", ["Left", "Right"])
        submit1 = st.form_submit_button("Submit")

    if submit1:
        if path1 == "Left":
            st.session_state.stage = 1  # Move to the next stage
        else:
            st.error("Fell into a hole. GAME OVER.")
            st.session_state.stage = -1  # End the game

# Step 2: Choose Swim or Wait (if the previous step was successful)
if st.session_state.stage == 1:
    with st.form("form2"):
        path2 = st.radio("Swim or Wait?", ["Swim", "Wait"])
        submit2 = st.form_submit_button("Submit")

    if submit2:
        if path2 == "Wait":
            st.session_state.stage = 2  # End the game with success
        else:
            st.error("Attacked by trout. GAME OVER.")
            st.session_state.stage = -1  # End the game with failure
if st.session_state.stage == 2:
    with st.form("form3"):
        path3 = st.radio("Which door?", ["Red", "Blue", "Yellow"])
        submit3 = st.form_submit_button("Submit")

    if submit3:
        if path3 == "Red":
            st.error("Burned by a fire. GAME OVER.")
            st.session_state.stage = -1  # End the game with success
        elif path3 == "Blue":
            st.error("Eaten by beasts. GAME OVER.")
            st.session_state.stage = -1  # End the game with success
        else:
            st.success("You found the treasure! Congratulations!")
            st.session_state.stage = 3  # End the game with failure
if st.session_state.stage == -1 or st.session_state.stage == 3:
    if st.button("Restart"):
        st.session_state.stage = 0
        st.experimental_rerun()
