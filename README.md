# MNIST Digit Recognition Web App

Welcome to the MNIST Digit Recognition Web App! This project demonstrates how to deploy a machine learning model that can recognize handwritten digits using a Flask web application. The app allows users to upload an image of a handwritten digit, and it will return the predicted digit.

## Features

- **Upload Image**: Upload an image of a handwritten digit.
- **Instant Prediction**: Get the digit prediction in real-time.
- **User-Friendly Interface**: Simple and intuitive web interface.

## Tech Stack

- **Backend**: Flask
- **Machine Learning**: TensorFlow
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: PIL (Pillow)
- **Deployment**: Local environment

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/SumitPaul22/MNIST-Digit-Recognition-model.git
   cd mnist_web_app
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

4. **Download or Train the MNIST Model**

   Ensure that you have the model file `mnist_model.keras` in the project directory. If you don't have it, you can train a model using TensorFlow or download my pre-trained model.

5. **Run the Flask Application**

   ```sh
   python app.py
   ```

### Usage

1. Open the web application in your browser.
2. Click the "Choose File" button to upload an image of a handwritten digit.
3. Click "Submit" to get the prediction.

### File Structure

```
mnist_web_app/
├── app.py                # Flask application
├── mnist_model.keras      # Pre-trained TensorFlow model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main HTML page
└── static/
    └── styles.css         # Custom CSS styles
```

### Contributing

Feel free to contribute by submitting issues or pull requests. Ensure that your changes are well-tested and documented.

### Acknowledgements

- **TensorFlow**: For providing the tools to build and train the digit recognition model.
- **Flask**: For the web framework used to deploy the application.
- **Pillow**: For image processing tasks.
