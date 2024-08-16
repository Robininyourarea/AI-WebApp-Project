# NeuralTech (AI Model Web Application)

Welcome to the AI Model Web Application! This project provides a platform where users can try out various types of AI models through a web interface. The application is designed to be user-friendly and accessible, making it easy for anyone to experiment with different AI technologies.

## Features

- **Multiple AI Models**: Access a variety of AI models, including image recognition, natural language processing, and more.
- **User-Friendly Interface**: An intuitive web interface that allows users to interact with the AI models effortlessly.
- **Real-Time Results**: Get instant feedback and results from the AI models.

## Project Screenshots

In this project I have seperatef into 2 part

- **AI application part**: The AI applications that user can interact with including select the model and make the prediction
- **Web pages part**: Web pages for customer who need to see the details of the AI company

### 1.AI application part
![Demo Image](assets/scrn15.png)

### 1.1 Classification Inference feature
model available below
- **EfficientNet B0**
- **EfficientNet B1**
- **EfficientNet B2**
- **EfficientNet B3**

![Demo Image](assets/scrn20.png)

### 1.2 Object Detection Inference feature
model available below
- **YOLOv8n**
- **YOLOv8s**

![Demo Image](assets/scrn22.png)

### 1.3 Segmentation Inference feature
model available below
- **YOLOv8n**
- **YOLOv8s**

![Demo Image](assets/scrn21.png)

### 2.Web pages part

#### 2.1 Login page
![Demo Image](assets/scrn.33.png)

#### 2.2 Home page
![Demo Image](assets/scrn.23.png)
![Demo Image](assets/scrn.24.png)
![Demo Image](assets/scrn.25.png)
![Demo Image](assets/scrn.26.png)
![Demo Image](assets/scrn.27.png)

#### 2.3 About page
![Demo Image](assets/scrn.28.png)
![Demo Image](assets/scrn.29.png)
![Demo Image](assets/scrn.30.png)
![Demo Image](assets/scrn.31.png)

#### 2.4 Contact Us page
![Demo Image](assets/scrn.32.png)

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)

### Installation

1. Clone the repository:
  ```bash
   git clone https://github.com/Robininyourarea/AI-WebApp-Project.git
   cd your-repo-name
   ```

2. Set up the AI Server:
  ```bash
  cd .\AI-server\
  py -3.10 -m venv venv
  cd .\venv\
  cd .\Scripts\
  .\activate
  cd ..
  cd ..
  pip install -r requirements.txt
  pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
  python aiservermaster.py
  ```

3. Set up the Web Server:
  ```bash
  cd ./client
  npm install
  npm run dev
  ```

4. Set up the frontend (client):
  ```bash
  cd .\web-server\
  npm install
  npm run dev
  ```

5. Access the application at http://localhost:5173.

### Usage
Select an AI Model: Choose from a list of available AI models on the homepage.
Input Data: Provide the necessary input data for the selected model.
Run the Model: Click the "Run" button to execute the model.
View Results: The results will be displayed in real-time on the screen.
Contributing
We welcome contributions from the community! To contribute:

### Acknowledgements
- PyTorch
- React
