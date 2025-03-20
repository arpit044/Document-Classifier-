from fastapi import FastAPI, UploadFile, File
import pytesseract
import cv2
import numpy as np
from transformers import pipeline

app = FastAPI()

# Load model for document classification
classifier = pipeline("text-classification", model="microsoft/layoutlmv3-base")

def read_text_from_image(image_bytes):
    # Convert image bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Convert image to grayscale for better OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

@app.post("/process-document/")
async def process_document(file: UploadFile = File(...)):
    contents = await file.read()
    text = read_text_from_image(contents)
    classification = classifier(text)[0]["label"]
    return {"text": text, "classification": classification}
