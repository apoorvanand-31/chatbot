import streamlit as st

st.set_page_config(page_title="Health & Hygiene Chatbot", page_icon="🧼")

# Title
st.title("🤖 SwasthyaBot - Your Health & Hygiene Assistant")

# Introduction
st.markdown("Hello! I'm **SwasthyaBot**, here to help you with health and hygiene tips. Choose an option below to get started.")

# Menu options
options = [
    "Personal Hygiene",
    "Healthy Eating",
    "Preventing Common Illnesses",
    "Ask a Health Question"
]

choice = st.selectbox("What would you like to learn about?", options)

# Logic for each menu
if choice == "Personal Hygiene":
    st.subheader("🧼 Personal Hygiene Tips")
    st.markdown("""
    - Wash your hands regularly with soap for at least 20 seconds.  
    - Bathe daily and keep your clothes clean.  
    - Trim your nails weekly.  
    - Cover your mouth while sneezing or coughing.  
    - Use deodorant to avoid body odor.
    """)

elif choice == "Healthy Eating":
    st.subheader("🍎 Healthy Eating Tips")
    st.markdown("""
    - Eat a balanced diet with fruits, vegetables, grains, and proteins.  
    - Drink 8 glasses of water daily.  
    - Avoid junk food and excess sugar.  
    - Do not skip breakfast.  
    - Eat in moderation and at regular intervals.
    """)

elif choice == "Preventing Common Illnesses":
    st.subheader("🤒 Illness Prevention Tips")
    st.markdown("""
    - Get vaccinated as per medical advice.  
    - Maintain personal and environmental cleanliness.  
    - Use mosquito repellents and sleep under nets.  
    - Avoid close contact with sick individuals.  
    - Get enough sleep and manage stress.
    """)

elif choice == "Ask a Health Question":
    st.subheader("❓ Ask Me Anything")
    user_question = st.text_input("Type your health or hygiene question here:")
    
    if user_question:
        # Basic keyword matching for demonstration
        if "hand" in user_question.lower():
            st.info("You should wash your hands frequently, especially before meals and after using the toilet.")
        elif "food" in user_question.lower() or "eat" in user_question.lower():
            st.info("A healthy diet includes vegetables, fruits, whole grains, and lean proteins.")
        elif "flu" in user_question.lower() or "cold" in user_question.lower():
            st.info("To avoid flu, wash hands often, avoid close contact with sick people, and get vaccinated.")
        else:
            st.warning("I'm still learning. Please consult a health expert for detailed advice.")

# Optional Footer
st.markdown("---")
st.caption("Made by Team AAT 💡 | For Educational Purposes Only")
