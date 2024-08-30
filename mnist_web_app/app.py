import logging
from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the model
model = tf.keras.models.load_model('mnist_model.keras')

@app.route('/')
def home():
    return render_template('index.html')

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        # Open the image file
        img = Image.open(io.BytesIO(file.read()))
        logging.info("Image opened successfully")

        # Convert the image to grayscale if it isn't already
        if img.mode != 'L':
            img = img.convert('L')
        logging.info("Image converted to grayscale")

        # Resize the image to 28x28
        img = img.resize((28, 28))
        logging.info("Image resized to 28x28")

        # Normalize the image array
        img_array = np.array(img) / 255.0
        logging.info("Image array normalized")

        # Reshape the array to match the model input
        img_array = img_array.reshape(1, 28, 28, 1)  # Ensure the correct shape for grayscale images
        logging.info("Image array reshaped")

        # Make prediction
        predictions = model.predict(img_array)
        logging.info("Prediction made")

        # Process the prediction
        predicted_class = np.argmax(predictions, axis=1)
        logging.info("Prediction processed")

        return jsonify({'predicted_class': int(predicted_class[0])})

    except Exception as e:
        logging.error(f"Error processing the image: {e}")
        return jsonify({'error': 'Error processing the image'}), 500

if __name__ == '__main__':
    app.run(debug=True)