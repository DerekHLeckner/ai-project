import streamlit as st
from textblob import TextBlob

# Set the page title
st.title("Sentiment Analysis App")

# Create a textarea for user input
text = st.text_area("Enter text")

# Create a button to perform sentiment analysis
if st.button("Analyze"):
    # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Determine sentiment label
    if sentiment > 0:
        sentiment_label = "Positive"
    elif sentiment < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    # Display the sentiment analysis results
    st.write("Sentiment:", sentiment)
    st.write("Sentiment Label:", sentiment_label)
