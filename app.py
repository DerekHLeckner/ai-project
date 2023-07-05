import streamlit as st
from transformers import pipeline
from textblob import TextBlob

# Set the page title
st.title("Sentiment Analysis App")

# Create a textarea for user input
text = st.text_area("Enter text")

classifier = pipeline('sentiment-analysis')
# Create a button to perform sentiment analysis
if st.button("Analyze"):
    # Perform sentiment analysis
    blob = classifier(text)
    sentiment = blob[0]

    # Determine sentiment label
    # sentiment_label = sentiment.label
    # Display the sentiment analysis results
    st.write("Sentiment:", sentiment)
    # st.write("Sentiment Label:", sentiment_label)
