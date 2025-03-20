from transformers import pipeline

classifier = pipeline("text-classification", model="microsoft/layoutlmv3-base")

def classify_document(text):
    return classifier(text)[0]["label"]
