# Potato Disease Detection

This project is a Convolutional Neural Network (CNN) that can detect whether a potato leaf is healthy, has early blight disease, or late blight disease.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install Docker](#install-docker)
  - [Start the TensorFlow Serving Container](#start-the-tensorflow-serving-container)
  - [Set up the Python Virtual Environment](#set-up-the-python-virtual-environment)
  - [Start the FastAPI Server](#start-the-fastapi-server)
  - [Start the Frontend](#start-the-frontend)
- [Usage](#usage)
- [Credits](#credits)
- [Follow Me on Twitter](#follow-me-on-twitter)

## Introduction
Potato blight is a major problem in the agricultural industry, causing significant crop losses. This project aims to provide a solution to this problem by using a Convolutional Neural Network (CNN) to detect early and late blight diseases in potato leaves. The application is built using FastAPI for the backend, React for the frontend, and TensorFlow Serving for the machine learning model deployment.

## Requirements
To run this application, you will need the following:
- Docker
- Python 3.7 or later
- Node.js 16 or later
- NVM (Node Version Manager)

## Setup

### Install Docker
1. Visit the official Docker website ([https://www.docker.com/](https://www.docker.com/)) and download the appropriate Docker installation for your operating system.
2. Follow the installation instructions provided by Docker to install and set up Docker on your machine.

### Start the TensorFlow Serving Container
1. Open a terminal or command prompt.
2. Run the following command to start the TensorFlow Serving container:
   ```bash
   docker run -t --rm -p 8501:8501 -v C:/Users/arnol/Desktop/Potato_Disease:/Potato_Disease tensorflow/serving --rest_api_port=8501 --model_config_file=/Potato_Disease/models.config

Replace `C:/Users/arnol/Desktop/Potato_Disease` with the path to your local Potato_Disease directory.

### Set up the Python Virtual Environment
1. Open a new terminal or command prompt.
2. Navigate to the Potato_Disease directory.
3. Create a new Python virtual environment by running the following command:
   ```bash
   python -m venv potatoenv
4. Activate the virtual environment with this command
    source potatoenv/Scripts/activate


### Start the FastAPI Server
1. Ensure you have activated the Python virtual environment (see the previous step).
2. Navigate to the /api directory.
3. Start the FastAPI server by executing:
 
    python main.py
### Start the Frontend
1. Open a new terminal or command prompt.
2. Ensure you have installed NVM and Node.js 16.
3. Navigate to the /frontend directory.
4. Install the dependencies by running:
bash
Copy code
npm install
Start the frontend application with the command:
bash
Copy code
npm start
Usage
Open a web browser and navigate to http://localhost:3000.
You should see the Potato Disease Detection application.
Upload an image of a potato leaf, and the application will detect whether the leaf is healthy, has early blight disease, or late blight disease.
Credits
This project was developed by [Your Name] as a demonstration of a Convolutional Neural Network for potato disease detection.

Follow Me on Twitter
For more updates and projects, follow me on Twitter: @arnold0duor

scss
Copy code

This Markdown text now includes both the instructions and the corresponding code blocks, formatted for your `README.md` file.








