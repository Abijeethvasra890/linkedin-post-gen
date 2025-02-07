import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post


# Options for length and language
length_options = ["Short", "Medium", "Long"]


# Main app layout
def main():
    st.subheader("Abijeeth's LinkedIn Post Generator!")

    # Create three columns for the dropdowns
    col1, col2 = st.columns(2)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)


    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, "English", selected_tag)
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()
