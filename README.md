```markdown
# Project Overview

This repository contains three distinct projects, each demonstrating different aspects of web development, machine learning, and data processing.

## 1. **To-Do List Web Application**

This project is a simple **To-Do List web application** built using **Flask** and **SQLAlchemy**. It uses an **SQLite** database to store tasks, which consist of a title, description, and creation date. The application includes three routes:

- `/`: Adds a new task to the database.
- `/show`: Displays the list of tasks.
- `/bye`: Returns a basic farewell message.

Technologies used:
- **Flask**: For web routing.
- **SQLAlchemy**: For database management.
- **SQLite**: For data storage.

## 2. **MELDDataset for Multimodal Machine Learning**

The **MELDDataset** class is a custom **PyTorch Dataset** designed to handle multimodal data, including text, video, and audio, for machine learning tasks. It processes data using the following methods:
- Tokenizes text using **Hugging Face's AutoTokenizer**.
- Extracts and processes video frames using **OpenCV**.
- Extracts audio from video using **FFmpeg** and converts it to a **Mel-spectrogram** with **Torchaudio**.
- Maps emotion and sentiment labels to integer values.

The dataset returns tokenized text, video frames, audio features, and labels in tensor format, making it ideal for training multimodal models.

Technologies used:
- **PyTorch**: For creating custom datasets.
- **Hugging Face Transformers**: For text tokenization.
- **OpenCV**: For video frame extraction.
- **FFmpeg**: For audio extraction.
- **Torchaudio**: For audio processing and Mel-spectrogram generation.

## 3. **Employee Sign-In System**

This project implements a simple employee sign-in system using **Streamlit** for the frontend and **Flask** for the backend. Users input their name and employee ID on the frontend, which sends the data to the backend via an HTTP POST request. The backend validates the input and returns either a personalized welcome message or an error response.

Technologies used:
- **Streamlit**: For frontend user interface.
- **Flask**: For backend API and validation.

---

### How to Run

1. **To-Do List Web Application**:
   - Install dependencies: `pip install -r requirements.txt`
   - Run the Flask app: `python app.py`

2. **MELDDataset for Machine Learning**:
   - Ensure you have the required dependencies installed, including `torch`, `transformers`, `opencv-python`, `torchaudio`, and `ffmpeg`.
   - Load and process the dataset as part of your ML pipeline.

3. **Employee Sign-In System**:
   - Install dependencies: `pip install -r requirements.txt`
   - Run the Flask backend: `python app.py`
   - Run the Streamlit frontend: `streamlit run frontend.py`
-


```---------------------------------------------------------------------------------------------------------
