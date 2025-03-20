# Document-Classifier


This project is an end-to-end document classification and information extraction system built using FastAPI, React, and Transformers. It allows users to upload or capture images of documents such as licenses, passports, and IDs, then classifies them and extracts key information like name, date of birth, and document number using OCR and deep learning models.
# Technologies Used
### Backend (FastAPI)
•	- **FastAPI**: A modern, fast web framework for building APIs with automatic documentation.
•	- **Pytesseract (OCR)**: Extracts text from images using Tesseract OCR.
•	- **Transformers (LayoutLMv3)**: A state-of-the-art model from Hugging Face for document classification and layout-aware text extraction.
•	- **OpenCV**: Provides image preprocessing capabilities for noise reduction and better OCR accuracy.
•	- **PDF2Image**: Converts PDF documents into images for processing.
•	- **SQLAlchemy + SQLite**: Handles database storage for extracted document details.
•	- **Uvicorn**: ASGI server for running the FastAPI application efficiently.

### Frontend (React + Tailwind CSS)
•	- **React.js**: A powerful JavaScript library for building interactive user interfaces.
•	- **Axios**: Facilitates seamless API calls to interact with the FastAPI backend.
•	- **Tailwind CSS**: Provides a clean, modern, and responsive UI.
•	- **WebRTC & HTML5 Camera API**: Enables live camera scanning for document capture.

### AI & Machine Learning Technologies
•	- **Hugging Face Transformers**: Uses pre-trained LayoutLMv3 for document classification.
•	- **PyTorch**: Powers the deep learning model for inference.
•	- **Named Entity Recognition (NER)**: Identifies key details such as name, date of birth, and document number from extracted text.

# Project Features
•	1. **Document Upload**: Users can upload images (JPG, PNG, PDF) of documents.
•	2. **Live Camera Capture**: Uses the webcam to scan documents in real-time.
3. **OCR-based Text Extraction**: Extracts textual information using Tesseract OCR.
4. **Document Classification**: Uses LayoutLMv3 to classify documents as passport, license, or ID.
5. **Information Extraction**: Identifies key details such as name, date of birth, and document number.
6. **Database Storage**: Saves extracted information in a SQLite database.
7. **Real-time Processing**: Processes and classifies documents instantly.
8. **API-Driven Architecture**: Provides RESTful API endpoints for easy integration with other applications.

# System Requirements
### Backend Setup
Command:
pip install fastapi uvicorn transformers torch pytesseract opencv-python-headless sqlalchemy sqlite3 pdf2image
Install **Tesseract OCR**:
•	- Ubuntu: `sudo apt install tesseract-ocr`
•	- Windows: Download from [here](https://github.com/tesseract-ocr/tesseract)
•	- Mac: `brew install tesseract`

Start the backend:
Command:
uvicorn main:app --host 0.0.0.0 --port 8000

### Frontend Setup
Command:
npm install axios tailwindcss
npm start
Deployment
•	- **Docker Support**: The application can be containerized using Docker.
•	- **Cloud Deployment**: Can be deployed on AWS, Azure, or Google Cloud.
•	- **CI/CD Integration**: Supports automated deployment using GitHub Actions.
Future Enhancements
•	- **Expand classification** to support additional document types.
•	- **Enhance OCR accuracy** with deep learning-based text recognition.
•	- **Cloud storage integration** for document archiving.
•	- **Mobile app support** for scanning documents on the go.
•	- **Multi-language OCR support** for extracting text in different languages.
Use Cases
•	- **Banking & Finance**: Automates KYC verification processes.
•	- **Government Agencies**: Streamlines document verification for passports, licenses, etc.
•	- **Healthcare**: Automates patient record verification.
•	- **Corporate HR**: Verifies employee identity documents efficiently.
