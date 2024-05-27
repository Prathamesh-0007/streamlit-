import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Surprise for Anushri", page_icon=":heart:")

# Custom CSS to center content and style the button
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .heart {
        font-size: 100px;
        color: red;
    }
    .surprise-button {
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center content
st.markdown('<div class="center">', unsafe_allow_html=True)

# Display heart emoji
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

# Main message
st.title("Love You, Anushri!")
st.subheader("Click the button below for a surprise!")

# Button to reveal the surprise
if st.button("Click Me!", key="surprise-button"):
    surprise_messages = [
        "You are the sunshine in my life!",
        "Every moment with you is a treasure!",
        "You make my heart skip a beat!",
        "I love you more than words can say!",
        "You are my one and only, Anushri!"
    ]
    surprise_message = random.choice(surprise_messages)
    st.balloons()
    st.success(surprise_message)

# End centered content
st.markdown('</div>', unsafe_allow_html=True)
