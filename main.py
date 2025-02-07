import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]

# Sidebar Content
st.sidebar.title("📌 About This App")
st.sidebar.write("""
🚀 **Abijeeth's LinkedIn Post Generator** helps you generate engaging LinkedIn posts with ease.  
💡 Select a **topic** and **length**, then click **Generate** to get an AI-crafted post.
""")

st.sidebar.markdown("---")
st.sidebar.write("🔗 **How to Use:**")
st.sidebar.write("""
1️⃣ Select a **Topic** from the dropdown.  
2️⃣ Choose the **Length** of the post.  
3️⃣ Click **Generate** to get a unique post.  
4️⃣ Copy and share it on LinkedIn! 🚀  
""")

st.sidebar.markdown("---")
st.sidebar.write("🎯 **Why Use This?**")
st.sidebar.write("""
✅ Saves time creating engaging posts  
✅ AI-powered for **creativity & engagement**  
✅ Tailored content for LinkedIn  
""")

# Main UI
st.title("📝 Abijeeth's LinkedIn Post Generator!")
st.write("👋 Welcome! Select a **topic & length**, and let AI craft an engaging LinkedIn post for you.")

# Create columns for dropdowns
col1, col2 = st.columns(2)

fs = FewShotPosts()
tags = fs.get_tags()

with col1:
    selected_tag = st.selectbox("📌 Select a Topic", options=tags)

with col2:
    selected_length = st.selectbox("📏 Select Length", options=length_options)

st.markdown("---")  # Separator for cleaner UI

# Generate Button
if st.button("🚀 Generate Post"):
    post = generate_post(selected_length, "English", selected_tag)
    st.markdown("### ✍️ Your AI-Generated LinkedIn Post:")
    st.success(post)  # Display post in a highlighted success box
