from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import streamlit as st

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    return tokenizer, model

tokenizer, model = load_model()

def analyze_sentiment(text):
    """Returns sentiment label: positive / negative / neutral"""
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probs).item()
    label_map = {0: "negative", 1: "neutral", 2: "positive"}
    return label_map[predicted_class]
