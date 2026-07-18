# AI-Powered Image Caption Generator

## Project Overview

The AI-Powered Image Caption Generator is a web application that automatically generates captions for uploaded images using Artificial Intelligence. The project uses the BLIP (Bootstrapping Language-Image Pre-training) model from Hugging Face and is built with Python and Flask.

## Features

- Upload an image
- Generate AI-based captions
- User-friendly web interface
- Supports JPG, PNG and JPEG images
- Fast caption generation using BLIP

## Technologies Used

- Python
- Flask
- PyTorch
- Hugging Face Transformers
- HTML
- CSS

## Project Structure

AI-Image-Caption-Generator/
│
├── dataset/
├── model/
│   ├── encoder.py
│   └── decoder.py
├── static/
│   ├── uploads/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── predict.py
├── train.py
├── requirements.txt
└── README.md

## Installation

1. Install Python
2. Create Virtual Environment
3. Install Requirements

pip install -r requirements.txt

4. Run the application

python app.py

5. Open Browser

http://127.0.0.1:5000

## Future Improvements

- Voice Caption
- Multi-language Translation
- Caption History
- Dark Mode
- Drag and Drop Upload

## Author

Durgesh Shukla