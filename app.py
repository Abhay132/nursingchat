import streamlit as st

st.title("Nursing College Admission Assistant")

# Step tracker
if 'step' not in st.session_state:
    st.session_state.step = 0

user_text = st.text_input("You: ")

def bot_reply():
    text = user_text.lower()
    step = st.session_state.step

    # Step 0: Wait for greeting
    if step == 0:
        if "hi" in text or "hello" in text:
            st.session_state.step = 1
            return "Hello! Are you interested in Nursing College admission? (Yes/No)"
        else:
            return "Please start by saying 'hi' or 'hello' to begin."

    # Step 1: Ask if interested
    elif step == 1:
        if text == "yes":
            st.session_state.step = 2
            return "Did you have Biology in 12th grade? (Yes/No)"
        else:
            st.session_state.step = -1
            return "Okay! Feel free to ask anytime in the future. Thank you!"

    # Step 2: Check biology eligibility
    elif step == 2:
        if text == "yes":
            st.session_state.step = 3
            return ("Great! Here are the details:\n"
                    "- Total annual fee: ₹70,000 (3 installments)\n"
                    "- Hostel: 24x7 water & electricity, CCTV, warden\n"
                    "- Location: Delhi, near markets and hospitals\n"
                    "- Scholarships: Govt Post-Matric (₹18k–₹23k), Labour Ministry (₹40k–₹48k)\n"
                    "- Clinical training: District Hospital, Regional Hospital, etc.\n"
                    "- Total seats: 60\n"
                    "- Approved by Indian Nursing Council (INC)\n"
                    "Would you like to know about eligibility criteria? (Yes/No)")
        else:
            st.session_state.step = -1
            return "Biology in 12th grade is required for B.Sc Nursing admission."

    # Step 3: Share eligibility
    elif step == 3:
        if text == "yes":
            st.session_state.step = -1
            return ("Eligibility:\n"
                    "- Biology in 12th grade\n"
                    "- Pass the PNT Exam\n"
                    "- Age between 17 and 35 years\n"
                    "Thank you! Let me know if you have any more questions.")
        else:
            st.session_state.step = -1
            return "Okay! Feel free to ask anytime for more details."

    else:
        return "Chat has ended. Refresh the page to start again."

if user_text:
    reply = bot_reply()
    st.text_area("Assistant:", value=reply, height=250)
