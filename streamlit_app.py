import streamlit as st 

st.title("AI For ASL")

sidebar = st.sidebar.selectbox("Index",["About"])

if sidebar == "About":
    with st.container():
        st.paragraph("There are thousands of people in Canada who use sign languages as their primary form of communication. Although there are various resources to learn sign languages such as with courses or videos, these methods take extensive amounts of time to learn and become conversational in the language. Spoken languages have electronic translators which are easily accessible, simple to use, and allow for quick and immediate translations between numerous languages. This technology, however, does not accommodate users of sign languages and those wishing to communicate with someone using sign language.Our team would like to bridge this gap by creating a sign language translator, specifically for American Sign Language (ASL). The translator would allow for instant communication between a user of ASL and a non-user, removing the need to spend considerable amounts of time to become conversational in ASL. As an added benefit, the translator would also be a valuable resource for those learning ASL.")
        st.subheader("Contributors")
        st.text("Avnish Jadhav")
        st.text("Belton He")
        st.text("Urvi Patel")



