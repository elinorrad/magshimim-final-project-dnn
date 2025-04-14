from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow.lite as tflite

app = Flask(__name__)

# Load TFLite model and allocate tensors
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@app.route('/')
def home():
    # Render the main page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form and preprocess
        input_data = [float(x) for x in request.form.values()]
        input_array = np.array(input_data, dtype=np.float32).reshape(1, -1)

        # Set input tensor and run inference
        interpreter.set_tensor(input_details[0]['index'], input_array)
        interpreter.invoke()

        # Get prediction result
        output_data = interpreter.get_tensor(output_details[0]['index'])
        prediction = output_data[0][0]  # Assuming single float output

        return render_template('index.html', prediction_text=f'Result: {prediction:.2f}')

    except Exception as e:
        # Return error as JSON
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
