import streamlit as st
import json

st.set_page_config(page_title="DAC-AI", layout="wide")

st.title("🧠 DAC-AI – Digital Adhyatma Constitution")

st.markdown("**संविधान बनाम धर्मदृष्टि – एक संवादात्मक विश्लेषण**")

query = st.text_input("आपका प्रश्न लिखें (संविधान या धर्म से संबंधित):")

if query:
    if "धर्म" in query:
        st.info("🔍 शास्त्र दृष्टिकोण: धर्म वह है जो धारणीय है, केवल मज़हब नहीं।")
    elif "संविधान" in query:
        st.info("📜 संविधान दृष्टिकोण: संविधान 1950 में लागू हुआ, परंतु सनातन व्यवस्था उससे पुरानी है।")
    else:
        st.warning("यह विषय अभी उपलब्ध नहीं है — कृपया धर्म या संविधान से संबंधित प्रश्न पूछें।")
