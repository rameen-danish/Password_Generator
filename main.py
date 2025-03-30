import re
import random
import string
import streamlit as st

# Common weak passwords
COMMON_PASSWORDS = {"password", "123456", "12345678", "qwerty", "abc123", "password1"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a unique one."]

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Set page configr
st.set_page_config(page_title=" Password Generator")
# Streamlit UI
st.title("🔒 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    for msg in feedback:
        st.write(msg)

st.subheader("Need a strong password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.code(strong_password, language="text")

# Footer
st.markdown("<br><hr><center>Made with ❤️ by Rameen Rashid</center>", unsafe_allow_html=True)