import streamlit as st

# पेज सेटअप
st.set_page_config(page_title="DAC-AI", layout="wide")

# शीर्षक
st.title("🧠 DAC-AI – Digital Adhyatma Constitution")

# साइडबार से विषय चुनें
option = st.sidebar.selectbox("📚 विषय चुनें:", ["मुख्य संवाद", "📜 संचार-संहिता देखें"])

# संचार-संहिता दिखाने वाला विकल्प
if option == "📜 संचार-संहिता देखें":
    try:
        with open("dharm_sanchar_sanhita.md", "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("❌ संचार-संहिता फाइल नहीं मिली। कृपया 'dharm_sanchar_sanhita.md' अपलोड करें।")

# मुख्य संवाद – प्रश्न पूछने का भाग
else:
    query = st.text_input("✍️ अपना प्रश्न लिखें (जैसे 'धर्म क्या है?' या 'संविधान का दृष्टिकोण')")
    if query:
        if "धर्म" in query:
            st.info("🔍 शास्त्र दृष्टिकोण: धर्म वह है जो धारणीय है, जो समाज, आत्मा और विश्व की गति को संतुलित करे।")
        elif "संविधान" in query:
            st.info("📜 संविधान दृष्टिकोण: भारतीय संविधान 1950 में लागू हुआ, जो व्यक्तिगत स्वतंत्रता, पंथ-स्वतंत्रता तथा समानता को मान्यता देता है।")
        else:
            st.warning("⚠️ यह विषय अभी उपलब्ध नहीं है – कृपया धर्म या संविधान से संबंधित प्रश्न पूछें।")